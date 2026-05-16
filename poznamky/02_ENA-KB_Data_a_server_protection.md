# P2 – ENA-KB: Ochrana dat a serverů (Data and Server Protection)

**Zdroj:** `02_ENA-KB_Data-and-server_protection.pdf`  
**Autor:** Tomáš Sochor  
**Poslední aktualizace:** 2026-05-15

---

## 0. Lecture agenda

Materiál pokrývá ochranu služeb a dat v pěti hlavních blocích:

1. Úvod do ochrany dat a služeb na úrovni operačního systému
2. Uživatelské role a oprávnění v operačních systémech
3. Auditování událostí
4. Zálohování dat
5. Šifrování disku

---

## 1. Úvod – Operační systémy: základní pojmy a principy

### 1.1 Hlavní rizika pro OS

- **Uživatelé s nežádoucím nebo škodlivým chováním** – a jejich procesy (aplikace)
- **Škodlivý software (malware)** – oba typy mohou mít dopad na data

### 1.2 Protiopatření

- **Autentizace** – ověření identity uživatele
- **Řízení přístupu (Access Control):**
  - Řízení přístupu k souborům (uživatelé/procesy)
  - Řízení přístupu do paměti (procesy)
- **Firewally** (na úrovni OS)
- **IDS/IPS** (na úrovni OS)
- **Prevence:** zálohování dat, …

### 1.3 Hardening (zpevnění) operačního systému

Hardening znamená snížení útočné plochy OS prostřednictvím správné konfigurace:

- **Pravidelné záplatování (patching)** OS
- **Správná konfigurace OS:**
  - Odstranění nepoužívaných služeb (potenciální zranitelnost)
  - Kontrola zdrojů (resource controls)
  - Správa uživatelů, skupin a oprávnění
- **Bezpečnostní politiky pro uživatele:**
  - Politiky hesel:
    - Minimální délka a složitost hesla
    - Vynucování sady znaků (velká/malá písmena, číslice, speciální znaky)
    - Maximální počet neúspěšných pokusů o přihlášení (dočasné zablokování účtu)
- **Pomocná opatření:**
  - Logování a auditing
  - Zálohy a archivace dat

---

## 2. Uživatelské role a oprávnění

### 2.1 Víceuživatelské OS

Téměř každý moderní OS je **víceuživatelský** – platí pro serverové i desktopové systémy (Windows, Linux/Unix, macOS, Android, …).

- **Klíčový bezpečnostní princip:** Jakýkoli uživatel může ohrozit celkovou bezpečnost OS.
- I zdánlivě jedno-uživatelské systémy často podporují více uživatelských účtů. Příkladem z materiálu je **Android**, který podporuje multi-user režim.

### 2.2 Typy omezení uživatelských účtů

Dvě hlavní kategorie:

1. **Přístup k souborům** – přístupová práva k souborovému systému
2. **Přístup k uživatelskému účtu (modifikace)** – spolu s dalšími objekty v databázi přístupu, např. Active Directory (Windows)

### 2.3 Typy uživatelských účtů

| Typ | Popis |
|-----|-------|
| **Administrátor** | Obvykle žádná nebo malá omezení (např. root v Unixu). Na jednom stroji může existovat více admin účtů. |
| **Běžný uživatel** | Libovolné jméno (unikátní v rámci stroje), sadu oprávnění definuje administrátor – individuálně nebo přes skupiny. |

### 2.4 Uživatelské účty v konkrétních OS

**Unix/Linux:**
- 2 typy účtů:
  - **Běžný uživatel** – respektuje atributy souborů
  - **Root** – neomezený přístup k souborům
- Přepínání uživatelů: příkaz `su`
- Zvýšení oprávnění: `sudo` (pouze pro uživatele uvedené v `/etc/sudoers`)
- Granulárnější oprávnění jsou dostupná v konkrétních distribucích

| Příkaz / účet | Význam | Bezpečnostní poznámka |
|---------------|--------|-----------------------|
| `root` | Superuživatel s prakticky neomezeným přístupem | Používat jen tam, kde je to nutné; chyba může poškodit celý systém |
| `su` | Přepnutí na jiného uživatele, typicky na `root` | Vyžaduje znalost hesla cílového účtu |
| `sudo` | Spuštění konkrétního příkazu se zvýšeným oprávněním | Lepší auditovatelnost a jemnější řízení přes `/etc/sudoers` |

**Windows:**
- Větší granularita uživatelských oprávnění
- Více přednastavených typů účtů: admin, power user, user, guest, …

**Cisco IOS** (routery a switche):
- Hierarchické módy:
  - **User mode** – téměř žádná oprávnění, pouze zobrazení konfigurace (prompt `>`)
  - **Privileged mode** – zobrazení všeho, volitelná ochrana heslem
  - Možnost definovat vlastní úrovně oprávnění (sady povolených akcí)
- Volitelná autentizace uživatele: username + heslo (lokálně nebo RADIUS)
- Pro vzdálený přístup (SSH/Telnet): lze omezit na konkrétní IP adresy pomocí ACL
- Pro konzolový přístup: přímý sériový kabel (rollover cable)

**Další síťové OS / vendori:**
- Materiál zmiňuje, že podobné možnosti mají i jiní výrobci.
- Příklad **MikroTik**: username + heslo, filtrování podle IP adres, změna čísla portu služby, vypnutí nepotřebných funkcí.

### 2.5 Bezpečnost uživatelských účtů

Spoléhání se pouze na heslo **nestačí**:

- **Omezení vzdáleného přihlášení** – seznam povolených IP adres
- **Omezení počtu neúspěšných pokusů o přihlášení** – komplikuje slovníkové i brute-force útoky
- **Nahrazení hesla veřejným klíčem:**
  - Uživatel vygeneruje pár klíčů na svém PC
  - Nahraje veřejný klíč na server
  - Při přihlášení obdrží „náhodný" řetězec, zašifruje ho privátním klíčem a odešle serveru
- **Vícefaktorová autentizace (MFA)** – např. mobilní autentizační aplikace

---

## 3. Řízení přístupu k souborům (File Access Control)

### 3.1 Základní principy

Přístup k souborům je uživatelům/procesům přidělován prostřednictvím sady oprávnění:

1. Čtení (Read)
2. Zápis (Write – obvykle přepsání)
3. Spuštění (Execute)
4. Procházení (Navigate)
5. Úprava obsahu (Modify contents)
6. Změna oprávnění uživatele (User permission modification)

**Dva převládající přístupy:**
- **POSIX** – oprávnění 1–3 (r, w, x)
- **Access Control Lists (ACL)** – uloženy v souborovém systému (NTFS, inody v ext) nebo samostatně

### 3.2 Implementace v konkrétních OS

**Unix:**
- Standardní atributy přístupu: `-rwxr-xr-- 200 file1`
  - Tři trojice: vlastník | skupina | ostatní
- **SELinux** – rozšíření pomocí ACL:
  - Příkazy `getfacl`, `setfacl`
  - Umožňuje přidat kombinaci `rwx` atributů pro libovolného uživatele/skupinu

**Windows:**
- ACL je přiřazena k souboru/adresáři
- ACL je složena z více **ACE (Access Control Entry):**
  - Každý ACE identifikuje uživatele/skupinu/počítač pomocí **SID**
  - Definuje `{Allow|Deny} Read/Write/List Contents`
- U složitějších kombinací pravidel `Allow` a `Deny` může být vyhodnocení oprávnění nepřehledné, proto je potřeba ACL pravidelně kontrolovat a zjednodušovat.

| Model | Typická oprávnění | Typické použití | Poznámka |
|-------|-------------------|-----------------|----------|
| **POSIX** | `r`, `w`, `x` pro vlastníka, skupinu a ostatní | Unix/Linux souborové systémy | Jednoduchý a přehledný model |
| **ACL** | Individuální záznamy pro uživatele/skupiny/počítače | NTFS, SELinux/ext ACL | Větší granularita, ale vyšší riziko nepřehledné konfigurace |

---

## 4. Auditování událostí (Event Auditing)

### 4.1 Co je auditování?

**Auditování** = proces ověření shody (compliance) se zákonem, pravidly, standardy apod.

### 4.2 Audit logy

Audit logy jsou podobné běžným logům, ale:
- **Obohaceny o více dat**
- **Lépe zabezpečeny:**
  - Proces auditování běží s privilegovanými oprávněními (nelze jej zastavit uživateli)
  - Soubory audit logů nesmí být přístupné uživatelům
  - Software pro auditování je „uzavřený systém" (closed system)
- Převládající přístup je, že auditovací mechanismus tvoří oddělený a řízený systém, který běžný uživatel nemůže obejít ani upravit.

### 4.3 Obsah audit logů (audit trail)

| Položka | Otázka |
|---------|--------|
| **Název a popis události** | Co se stalo? |
| **Časové razítko** (synchronizovaný čas) | Kdy se to stalo? |
| **Aktér** (ID uživatele nebo procesu) | Kdo to udělal? |
| **Dotčené objekty** (Device ID, IP adresa, …) | Čeho se to týkalo? |
| **Další informace** (dle typu události) | Kontextové údaje, např. procesy běžící na zařízení v době události |

### 4.4 Audit logy vs. běžné logy

| Vlastnost | Audit logy | Běžné logy |
|-----------|-----------|------------|
| **Účel** | Trvalý (neměnný) záznam důležitých událostí | Provozní informace pro adminy/vývojáře |
| **Doba uchovávání** | Dlouhodobá (roky) | Krátkodobá (max. měsíce) |
| **Důvod** | Legislativní, byznysová compliance | Ladění, monitoring |
| **Neměnnost** | Ano – omezený a řízený přístup | Ne nutně |
| **Centralizace** | Ano | Nemusí být centralizovány |

**Důležitý rozdíl:** Audit log má sloužit jako důkazní stopa. Běžný log slouží hlavně k provozní diagnostice.

---

## 5. Zálohy dat (Data Backup)

### 5.1 Základní pojmy

- Různé nástroje se liší dle platformy/OS
- **Cíle zálohy:**
  - Externí zařízení (lokální/sdílená)
  - Sdílený/serverový HDD/SSD
  - Cloud (privátní/veřejný)

### 5.2 Cíle obnovy

| Zkratka | Název | Popis |
|---------|-------|-------|
| **RPO** | Recovery Point Objective | K jakému bodu v čase musí být možné data obnovit po selhání. Ovlivňuje, jak **často** se zálohy provádí. |
| **RTO** | Recovery Time Objective | Jak rychle musí být obnovený systém připraven k použití. Ovlivňuje, zda je potřeba např. standby server, připravený hardware nebo předinstalovaný OS. |

**Příklad interpretace:**
- RPO „včera večer" znamená, že organizace akceptuje ztrátu dat vytvořených od poslední večerní zálohy.
- RTO „2 hodiny" znamená, že samotná záloha nestačí; musí existovat i připravený postup a infrastruktura pro rychlou obnovu.

### 5.3 Ověřování záloh

Každá záloha MUSÍ být ověřena z hlediska:
1. **Integrity souborů** – zda nejsou poškozeny
2. **Schopnosti obnovy** – aby byl znám postup obnovy a ověřeno, že jsou zahrnuty všechny soubory

Obnova dat se testuje:
- Periodicky (např. dvakrát ročně)
- Kdykoli dojde ke změně zálohovací procedury

### 5.4 Možné problémy se zálohami

- **Správné nastavení RPO/RTO** – kontinuita provozu vs. ekonomická efektivita
- **Ochrana zálohy:**
  - **Integrita** – zamezení pozdější modifikaci (ransomware, pochybení uživatele)
  - Ochrana před cíleným útokem, ransomwarem i uživatelskou nedbalostí
  - **Vyhýbat se trvale připojeným úložištím!** – snadná infekce při útoku
  - Dodržovat pravidlo **3-2-1-0**

#### Pravidlo 3-2-1-0

| Číslo | Pravidlo |
|-------|----------|
| **3** | 3 kopie dat |
| **2** | na 2 různých typech médií |
| **1** | 1 kopie uložena offsite (mimo lokalitu) |
| **0** | 0 chyb při ověřování zálohy |

**Smysl pravidla:** Nestačí mít jednu technicky správnou kopii. Záloha má přežít poruchu média, lokální incident, ransomware i chybu při obnově.

---

## 6. Šifrování disku (Disk Encryption)

### 6.1 Proč šifrovat disk?

Datové zálohy jsou zranitelné – zejména na externích zařízeních:
- Chybí ochrana při fyzické ztrátě/odcizení
- Nejde jen o zálohy: snadno odcizitelná jsou obecně všechna data na externích nebo výměnných médiích
- Celé mobilní zařízení může být ztraceno

**Šifrování celého disku se doporučuje pro:**
- Externí úložná zařízení (přenosná média)
- Úložiště mobilních zařízení
- Jakékoli jiné zařízení s daty, které může být fyzicky ztraceno

Na serverech se šifrování celého disku podle materiálu nepoužívá tak široce, protože riziko fyzické ztráty serverového hardwaru nebo disku bývá nižší než u notebooků, telefonů a externích médií.

### 6.2 Jak funguje šifrování disku?

- Převládající přístup: **vytvoření nové šifrované partition**
  - Často zabere většinu dostupného prostoru na disku
  - Všechna data na nové partition jsou šifrována
- Obvykle se používá **symetrické (rychlé) šifrování** se silným heslem
- K šifrované partition se přistupuje přes specializovaného klienta, který při prvním přístupu vyžádá heslo
- Data jsou dešifrována při čtení a šifrována při zápisu **průběžně (on-the-fly)**

### 6.3 Dostupné nástroje

| OS/Platforma | Nástroj |
|-------------|---------|
| **Windows** | BitLocker |
| **macOS** | FileVault |
| **Třetí strany** | Různý software s integrací do OS |
| **Externí disk** | Šifrování jako funkce disku (od výrobce), možnost biometrického faktoru |

---

## Otázky k opakování

1. Jaká jsou hlavní rizika pro operační systém a jaká protiopatření se používají k jejich zmírnění?
2. Co znamená OS hardening a jaké konkrétní kroky zahrnuje?
3. Jaký je rozdíl mezi účtem administrátora a běžného uživatele? Jak funguje `sudo` v Unixu?
4. Proč nestačí spoléhat se pouze na heslo pro zabezpečení účtu a jaké alternativy existují?
5. Vysvětlete rozdíl mezi POSIX oprávněními a Access Control Lists (ACL). Jak se liší implementace v Unixu a Windows?
6. Co je auditování a čím se audit logy liší od běžných logů? Jaké informace musí audit log obsahovat?
7. Co znamenají zkratky RPO a RTO a jak ovlivňují zálohovací strategii?
8. Jaké je pravidlo 3-2-1-0 pro zálohy a proč je důležité nevyužívat trvale připojená úložiště?
9. Proč jsou zálohy zranitelné a pro jaká zařízení se doporučuje šifrování celého disku?
10. Jak funguje šifrování disku „on-the-fly" a jaké nástroje se používají v různých OS?
11. Proč se šifrování celého disku používá častěji u mobilních zařízení a externích médií než u serverů?
