#!/usr/bin/env python3
from __future__ import annotations

import csv
import html
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "poznamky"
OUT_DIR = ROOT / "anki"
OUT_FILE = OUT_DIR / "kyberneticka_bezpecnost.tsv"
README_FILE = OUT_DIR / "README.md"

SKIP_HEADINGS = {
    "obsah",
    "obsah prednasky",
    "obsah přednášky",
    "otazky k opakovani",
    "otázky k opakování",
    "literatura a zdroje",
}


@dataclass
class Section:
    level: int
    title: str
    lines: list[str]
    parent: str | None


def strip_numbering(title: str) -> str:
    title = re.sub(r"^\s*\d+(\.\d+)*\.?\s*", "", title)
    return title.strip()


def normalize_key(text: str) -> str:
    text = text.lower().strip()
    replacements = {
        "á": "a",
        "č": "c",
        "ď": "d",
        "é": "e",
        "ě": "e",
        "í": "i",
        "ň": "n",
        "ó": "o",
        "ř": "r",
        "š": "s",
        "ť": "t",
        "ú": "u",
        "ů": "u",
        "ý": "y",
        "ž": "z",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return text


def tagify(value: str) -> str:
    value = normalize_key(value)
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def clean_line(line: str) -> str:
    line = line.rstrip()
    line = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"[obrázek: \1]", line)
    return line


def parse_sections(path: Path) -> tuple[str, list[Section]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    title = path.stem
    sections: list[Section] = []
    current: Section | None = None
    current_h2: str | None = None

    for raw in lines:
        heading = re.match(r"^(#{1,4})\s+(.+?)\s*$", raw)
        if heading:
            level = len(heading.group(1))
            heading_title = strip_numbering(heading.group(2).strip())
            if level == 1:
                title = heading_title
                current = None
                continue
            if current is not None:
                sections.append(current)
            if level == 2:
                current_h2 = heading_title
            current = Section(level=level, title=heading_title, lines=[], parent=current_h2 if level > 2 else None)
            continue

        if current is not None:
            current.lines.append(clean_line(raw))

    if current is not None:
        sections.append(current)

    return title, sections


def markdown_to_html(lines: list[str]) -> str:
    lines = [line for line in lines if line.strip() != "---"]
    text = "\n".join(lines).strip()
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    escaped = html.escape(text, quote=False)
    escaped = escaped.replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>")
    escaped = escaped.replace("&lt;code&gt;", "<code>").replace("&lt;/code&gt;", "</code>")
    return escaped.replace("\n", "<br>")


def plain_text(lines: list[str]) -> str:
    text = "\n".join(lines)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    return text.strip()


def extract_tables(lines: list[str]) -> list[list[list[str]]]:
    tables: list[list[list[str]]] = []
    i = 0
    while i < len(lines):
        if "|" not in lines[i]:
            i += 1
            continue
        block: list[str] = []
        while i < len(lines) and "|" in lines[i]:
            block.append(lines[i].strip())
            i += 1
        rows = []
        for row in block:
            cells = [cell.strip() for cell in row.strip("|").split("|")]
            if cells and all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells):
                continue
            if len(cells) >= 2:
                rows.append(cells)
        if len(rows) >= 2:
            tables.append(rows)
    return tables


def split_bullets(lines: list[str]) -> list[str]:
    bullets = []
    for line in lines:
        match = re.match(r"^\s*[-*]\s+(.+)$", line)
        if match:
            item = match.group(1).strip()
            if 35 <= len(item) <= 220:
                bullets.append(item)
    return bullets


def add_card(cards: list[tuple[str, str, str]], front: str, back: str, tags: list[str]) -> None:
    front = re.sub(r"\s+", " ", front).strip()
    back = back.strip()
    if not front or not back:
        return
    tags_clean = " ".join(sorted({tag for tag in tags if tag}))
    cards.append((front, back, tags_clean))


def build_cards() -> list[tuple[str, str, str]]:
    cards: list[tuple[str, str, str]] = []
    for path in sorted(NOTES_DIR.glob("*.md")):
        chapter_title, sections = parse_sections(path)
        chapter_tag = tagify(path.stem)
        chapter_short = path.stem.split("_")[0]

        for section in sections:
            key = normalize_key(section.title)
            if key in SKIP_HEADINGS:
                continue

            body = plain_text(section.lines)
            if len(body) < 80:
                continue

            tags = ["kyber", chapter_tag, tagify(chapter_short)]
            parent = f"{section.parent} / " if section.parent else ""
            front = f"{chapter_short}: Vysvětli pojem nebo část: {parent}{section.title}"
            back = f"<b>{html.escape(chapter_title)}</b><br><br>{markdown_to_html(section.lines)}"
            add_card(cards, front, back, tags)

            for table in extract_tables(section.lines):
                header = table[0]
                for row in table[1:]:
                    if len(row) < 2:
                        continue
                    subject = re.sub(r"\*\*(.+?)\*\*", r"\1", row[0]).strip()
                    if not subject or len(subject) > 90:
                        continue
                    answer_bits = []
                    for idx, value in enumerate(row[1:], start=1):
                        label = header[idx] if idx < len(header) else f"Pole {idx + 1}"
                        answer_bits.append(f"<b>{html.escape(label)}</b>: {markdown_to_html([value])}")
                    add_card(
                        cards,
                        f"{chapter_short}: Co znamená / jakou roli má „{subject}“ v části {section.title}?",
                        "<br>".join(answer_bits),
                        tags + ["tabulka"],
                    )

            if "shrnuti" in key or "shrnutí" in section.title.lower():
                for bullet in split_bullets(section.lines):
                    add_card(
                        cards,
                        f"{chapter_short}: Doplň/vysvětli shrnutí: {re.sub(r'<[^>]+>', '', bullet)[:90]}",
                        markdown_to_html([bullet]),
                        tags + ["shrnuti"],
                    )

    unique: dict[str, tuple[str, str, str]] = {}
    for front, back, tags in cards:
        unique[f"{front}\t{back}"] = (front, back, tags)
    return list(unique.values())


def write_output(cards: list[tuple[str, str, str]]) -> None:
    OUT_DIR.mkdir(exist_ok=True)
    with OUT_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerows(cards)

    README_FILE.write_text(
        "\n".join(
            [
                "# Anki import",
                "",
                f"Soubor: `{OUT_FILE.name}`",
                "",
                "Import v Anki:",
                "",
                "1. `File` -> `Import`.",
                "2. Vyber `kyberneticka_bezpecnost.tsv`.",
                "3. Separator nastav na `Tab`.",
                "4. Typ poznámky použij `Basic`.",
                "5. Pole mapuj jako: `Front`, `Back`, `Tags`.",
                "6. Povol HTML v polích, pokud se Anki zeptá.",
                "",
                f"Počet vygenerovaných kartiček: {len(cards)}.",
                "",
                "Import je generovaný z Markdown poznámek v `poznamky/`. Obrázky nejsou v kartičkách vkládané jako Anki media; textové kartičky ale zachovávají informaci, že v dané části byl obrázek.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def main() -> None:
    cards = build_cards()
    write_output(cards)
    print(f"Generated {len(cards)} cards -> {OUT_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
