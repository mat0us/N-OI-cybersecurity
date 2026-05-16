# 05 - Legislativni ukotveni KB, NIS2, novy zakon o KB

**Zdroj:** `05_Legislativni_ukotveni_KB,_NIS2,_Novy_zakon_o_KB.pdf`  
**Stav poznamek:** zpracovano podle prednaskoveho PDF; u pravnich tvrzeni je potreba pocitat s tim, ze realny stav legislativy se muze menit.

---

## 1. Zakladni kontext

Prednaska navazuje na evropskou regulaci kyberneticke bezpecnosti:

- **NIS** byla prijata Evropskou unii v roce 2016.
- Jejim cilem bylo zajistit vysokou spolecnou uroven bezpecnosti siti a informacnich systemu v EU.
- **NIS2** je nova smernice EU o kyberneticke bezpecnosti, jejiz oficialni zneni bylo publikovano v urednim vestniku EU 16. 1. 2023.
- Podle materialu byl novy cesky zakon o kyberneticke bezpecnosti schvalen a ma byt ucinny od roku 2025.

Hlavni myslenka: kyberneticka bezpecnost uz nema byt jen internim IT problemem vybranych velkych organizaci. Regulace se rozsiruje na tisice subjektu, jejichz sluzby jsou dulezite pro fungovani statu, ekonomiky a spolecnosti.

---

## 2. Proc NIS2 vznikla

Puvodni regulace dopadala jen na uzkou skupinu nejvyznamnejsich organizaci. NIS2 rozsah vyrazne zvetsuje:

- zahrnuje vice odvetvi,
- sjednocuje dohled a spolupraci mezi staty EU,
- posiluje roli dozorovych organu,
- zavadi vyssi sankce,
- klade vetsi odpovednost na vedeni organizaci,
- zduraznuje rizika dodavatelskeho retezce, zranitelnosti, kontinuitu provozu a incident response.

### Nejvyznamnejsi povinnosti podle materialu

- Stat urci jeden ze svych tymu CSIRT/CERT jako koordinatora pro koordinovane zverejnovani zranitelnosti.
- Dozorove organy si maji poskytovat vzajemnou pomoc a kontrolu.
- Evropska komise ma mit vetsi zapojeni do sjednocovani regulace.
- Pokuty se vyrazne zvysuji; u **essential entities** material uvadi horni hranici nejmene 10 milionu EUR nebo alespon 2 % celkoveho celosvetoveho rocniho obratu.

---

## 3. Strezni zmena v ceske regulaci

Navrh nove ceske regulace podle materialu sdruzuje drive roztristenou upravu nekolika typu povinnych osob do jedne kategorie:

> **poskytovatel regulovane sluzby**

Takovy poskytovatel musi naplnovat kriteria stanovena vyhlaskou o regulovanych sluzbach.

### Co z toho prakticky plyne

Organizace se nema ptat jen "jsme kriticka infrastruktura?", ale hlavne:

1. Poskytujeme sluzbu uvedenou v priloze/ve vyhlasce?
2. Splnujeme velikostni nebo specialni kriteria?
3. Spadame do nizsiho, nebo vyssiho rezimu?
4. Jake povinnosti z toho pro nas konkretne vyplyvaji?

![Stanoveni rezimu poskytovatele regulovane sluzby](assets/05_legislativa/slide-16.png)

---

## 4. Koho se nove povinnosti tykaji

Dosavadni regulace se tykala jen nekolika stovek nejvyznamnejsich organizaci. NIS2 a navazujici ceska uprava mirila na mnohem sirsi okruh poskytovatelu sluzeb dulezitych pro fungovani spolecnosti.

### Obecne podminky

Aby soukroma nebo verejna organizace spadala pod regulaci, material uvadi dve zakladni podminky:

1. Organizace poskytuje alespon jednu sluzbu uvedenou v priloze smernice nebo ve vyhlasce.
2. Je strednim nebo velkym podnikem:
   - alespon 50 zamestnancu,
   - nebo rocni obrat ci bilancni suma rocni rozvahy alespon 10 milionu EUR.

Pozor na partnerske a propojene podniky, protoze velikost se nemusi posuzovat izolovane jen podle jedne pravni osoby.

### Subjekty bez ohledu na velikost

Nektere organizace spadaji pod regulaci bez ohledu na velikost, napr.:

- poskytovatele sluzeb elektronickych komunikaci,
- poskytovatele sluzeb vytvarejicich duveru,
- poskytovatele DNS sluzeb.

![Urceni organizace podle kriterii](assets/05_legislativa/slide-09.png)

![Prahove hodnoty](assets/05_legislativa/slide-10.png)

---

## 5. Zakladni a dulezite subjekty

NIS2 meni cleneni subjektu. Drive se mluvilo o provozovatelich zakladnich sluzeb a poskytovatelich digitalnich sluzeb. Nove se subjekty deli na:

- **zakladni subjekty**,
- **dulezite subjekty**.

Rozdil je v kriticnosti odvetvi/sluzby a v zavislosti ostatnich odvetvi na dane sluzbe.

| Typ subjektu | Prakticky vyznam |
|---|---|
| **Zakladni subjekt** | Prisnejsi kyberneticka opatreni, ex-ante kontrola ze strany NUKIB. |
| **Dulezity subjekt** | Mene prisne povinnosti, typicky ex-post kontrola. |

![Zakladni deleni subjektu](assets/05_legislativa/slide-12.png)

---

## 6. Odvetvi a typy subjektu

### Zakladni entity

Material mezi zakladni entity radi zejmena:

- zdravotnictvi,
- vyrobu farmaceutickych vyrobku,
- energetiku,
- dopravu,
- bankovnictvi,
- infrastruktury financnich trhu,
- digitalni infrastrukturu,
- pitnou vodu,
- odpadni vody,
- verejnou spravu,
- vesmir.

### Dulezite entity

Mezi dulezite entity material uvadi zejmena:

- postovni a kuryrni sluzby,
- nakladani s odpady,
- vyrobu zdravotnickych prostredku,
- vyrobu pocitacu, elektronickych a optickych zarizeni,
- vyrobu elektrozarizeni, stroju, motorovych vozidel a dopravnich prostredku,
- vyrobu, zpracovani a distribuci potravin,
- vyrobu a distribuci chemikalii,
- digitalni poskytovatele.

![Prehled zakladnich a dulezitych entit](assets/05_legislativa/slide-13.png)

---

## 7. Povinnosti poskytovatele regulovane sluzby

Prednaska shrnuje povinnosti prakticky: poskytovatel regulovane sluzby musi mit bezpecnost rizene, dokumentovane, kontrolovatelne a provozne vymahatelne.

### Hlavni povinnosti

- Nastavit system rizeni rizik ve vlastnich sitich a informacnich systemech.
- Zavest minimalni standard kyberbezpecnostnich opatreni.
- Resit bezpecnost dodavatelskeho retezce.
- Ridit zranitelnosti.
- Hodnotit rizika kyberneticke bezpecnosti.
- Vytvorit tym, ktery schvaluje opatreni a dohlizi na jejich dodrzovani.
- Klasifikovat pouzivane aplikace a systemy.
- Mit plan obnovy.
- Provadet penetracni testy.
- Pouzivat silna hesla, dvoufaktorove overovani nebo certifikaty pro prihlasovani do kriticky dulezitych systemu.
- Aplikovat bezpecnostni aktualizace vydavane vyrobci softwaru.
- Resit lokalizaci dat podle pozadavku materialu.
- Hlasit kyberbezpecnostni incidenty NUKIB.
- Pravidelne aktualizovat a revidovat procesy kyberneticke bezpecnosti.

---

## 8. Opatreni k rizeni rizik

Opatreni k rizeni rizik maji podle materialu zahrnovat alespon:

- analyzu rizik,
- politiku bezpecnosti informacnich systemu,
- reseni incidentu:
  - prevence,
  - odhalovani,
  - reakce,
- rizeni kontinuity provozu,
- krizove rizeni,
- zabezpeceni dodavatelskeho retezce,
- zabezpeceni porizovani, vyvoje a udrzby siti a informacnich systemu,
- testovani a audit v oblasti kyberneticke bezpecnosti,
- pouzivani kryptografie a sifrovani.

### Dulezity princip

Regulace neni jen o technickem zabezpeceni. Je to kombinace:

- rizeni,
- dokumentace,
- technickych opatreni,
- odpovednosti vedeni,
- kontinualni kontroly,
- schopnosti reagovat na incidenty.

---

## 9. Incidenty a hrozby

Material uvadi povinnost neprodlene oznamovat:

- kazdy incident, ktery ma zavazny dopad na poskytovani sluzeb dotceneho subjektu,
- kazdou vyznamnou kybernetickou hrozbu, kterou subjekt zjisti a ktera by mohla vest k vyznamnemu incidentu.

V praxi je dulezite mit predem pripravene:

- kdo incident vyhodnocuje,
- kdo komunikuje s NUKIB,
- jake informace se sbiraji,
- jak se doklada casova osa incidentu,
- jak se po incidentu aktualizuji procesy a opatreni.

---

## 10. Prima odpovednost vedeni

Jedna z nejdulezitejsich zmen je odpovednost statutarnich organu.

Podle materialu se problematika kyberneticke bezpecnosti neda jednoduse delegovat na IT oddeleni. Vedeni organizace musi:

- zajimat se o kybernetickou bezpecnost,
- schvalovat nebo vynucovat opatreni,
- zajistit jejich dodrzovani,
- nest odpovednost za nedostatecne rizeni.

To je zasadni prakticky posun: kyberneticka bezpecnost se stava soucasti corporate governance.

---

## 11. Nizsi a vyssi rezim povinnosti

Material rozlisuje dve sady pravidel:

- **nizsi povinnosti** pro mene kriticke regulovane sluzby,
- **vyssi povinnosti** pro kritictejsi regulovane sluzby.

![Prizpusobeni kategorii](assets/05_legislativa/slide-17.png)

### Nizsi povinnosti

Nizsi rezim zahrnuje zejmena:

- zajistovani minimalni urovne kyberneticke bezpecnosti,
- povinnosti vrcholneho vedeni,
- rizeni rizik,
- bezpecnost lidskych zdroju,
- rizeni kontinuity cinnosti,
- rizeni pristupu,
- rizeni identit a opravneni,
- detekci a zaznamenavani kybernetickych bezpecnostnich udalosti,
- reseni kybernetickych bezpecnostnich incidentu,
- bezpecnost komunikacnich siti,
- aplikacni bezpecnost,
- kryptograficke algoritmy.

### Vyssi povinnosti

Vyssi rezim jde vic do hloubky a material ho deli na organizacni a technicka opatreni.

| Organizacni opatreni | Technicka opatreni |
|---|---|
| System rizeni bezpecnosti informaci | Fyzicka bezpecnost |
| Povinnosti vrcholneho vedeni | Bezpecnost komunikacnich siti |
| Bezpecnostni role | Sprava a overovani identit |
| Rizeni bezpecnostni politiky a dokumentace | Rizeni pristupovych opravneni |
| Rizeni aktiv | Detekce bezpecnostnich udalosti |
| Rizeni rizik | Zaznamenavani bezpecnostnich a provoznich udalosti |
| Rizeni dodavatelu | Vyhodnocovani udalosti |
| Bezpecnost lidskych zdroju | Aplikacni bezpecnost |
| Rizeni zmen | Kryptograficke algoritmy |
| Akvizice, vyvoj a udrzba | Zajistovani dostupnosti regulovane sluzby |
| Zvadani udalosti a incidentu | Zabezpeceni prumyslovych a ridicich systemu |
| Rizeni kontinuity cinnosti |  |
| Audit kyberneticke bezpecnosti |  |

---

## 12. Regulovane sluzby s vyssim rezimem

Material mezi sluzby s vyssim rezimem radi:

- verejnou spravu,
- energetiku:
  - elektrina,
  - dalkove vytapeni a chlazeni,
  - ropa,
  - plyn,
  - vodik,
- dopravu:
  - letecka,
  - zeleznicni,
  - vodni,
  - silnicni,
- bankovnictvi a infrastruktury financnich trhu,
- zdravotnictvi,
- vyrobu farmaceutickych a zdravotnickych prostredku,
- pitnou vodu a odpadni vody,
- digitalni infrastrukturu,
- vymenne uzly internetu,
- poskytovatele DNS,
- registry TLD,
- poskytovatele cloud computingu,
- poskytovatele datovych center,
- site pro dorucovani obsahu,
- poskytovatele sluzeb vytvarejicich duveru,
- verejne site a sluzby elektronickych komunikaci,
- vesmir.

---

## 13. Organizace s nizsim rezimem

Do nizsiho rezimu material radi napr.:

- vyrobu strojniho zarizeni,
- vyrobu pocitacu a elektroniky,
- vyrobu motorovych vozidel,
- vyrobu jinych zdravotnickych prostredku,
- vyrobu potravin,
- digitalni poskytovatele:
  - internetova trziste,
  - internetove vyhledavace,
  - platformy socialnich siti,
- postovni a kuryrni sluzby,
- nakladani s odpady,
- chemicke latky.

---

## 14. Jak organizace zjisti, zda spada pod regulaci

Material doporucuje test zarazeni organizace a pripomina velikostni kategorie podniku:

| Kategorie | Orientacni kriteria podle materialu |
|---|---|
| **Mikropodnik** | Méně než 10 osob a obrat/bilancni suma do 2 milionu EUR. |
| **Maly podnik** | Méně než 50 osob a obrat/bilancni suma do 10 milionu EUR. |
| **Stredni podnik** | Vice nez 50 a mene nez 250 osob, obrat do 50 milionu EUR nebo bilancni suma do 43 milionu EUR. |

Pokud organizace nevi, do jakeho oddilu CZ-NACE patri, lze vyuzit Registr ekonomickych subjektu. Oddil urcuje prvni dvojcisli klasifikace.

---

## 15. Co znamena zavest smernice informacni bezpecnosti

Organizace ma mit zakladni bezpecnostni dokumentaci, napr.:

- bezpecnostni politiku,
- politiku hesel,
- pravidla pridelovani opravneni,
- dokumentaci pro prokazani shody s NIS2,
- navazujici procesy a odpovednosti.

Dokumentace nema byt formalita. Ma dolozit, ze organizace vi:

- co chrani,
- proc to chrani,
- kdo za ochranu odpovida,
- jaka opatreni plati,
- jak se opatreni kontroluji.

---

## 16. Co znamena rizeni bezpecnosti v praxi

Rizeni bezpecnosti podle materialu znamena mit pod kontrolou:

- komu a proc davame opravneni k aplikaci,
- kdo zna jaka hesla,
- kdo ma kam fyzicky pristup:
  - klice,
  - vstupni karty,
- kdo kam uklada jake informace,
- odebirani pristupu pri odchodu zamestnance,
- pridelovani pristupu pri nastupu zamestnance.

Tohle je velmi prakticka cast: NIS2 neni jen o firewallech a sifrovani, ale i o tom, jestli organizace umi ridit identity, pristupy, odpovednosti a zmeny v zivotnim cyklu zamestnance.

---

## 17. Zkouskove shrnuti

- NIS2 rozsiruje regulaci kyberneticke bezpecnosti na mnohem vice subjektu.
- Zakladni pojem ceske upravy je **poskytovatel regulovane sluzby**.
- Organizace se zaradi podle poskytovane sluzby, velikosti a pripadne specialnich kriterii.
- Subjekty se deli na **zakladni** a **dulezite**.
- Zakladni subjekty maji prisnejsi povinnosti a ex-ante kontrolu.
- Dulezite subjekty maji mirnejsi rezim a typicky ex-post kontrolu.
- Klicove oblasti jsou rizeni rizik, incidenty, kontinuita, dodavatelsky retezec, pristupy, kryptografie, audit a dokumentace.
- Statutarni organy nesou primou odpovednost; kyberbezpecnost nelze jen "hodit na IT".

---

## Otazky k opakovani

1. Proc byla prijata smernice NIS2 a co meni oproti puvodni NIS?
2. Co znamena pojem poskytovatel regulovane sluzby?
3. Jake dve zakladni podminky musi organizace typicky splnit, aby spadala pod regulaci?
4. Ktere subjekty mohou spadat pod regulaci bez ohledu na velikost?
5. Jak se lisi zakladni a dulezite subjekty?
6. Co je ex-ante a ex-post kontrola v kontextu NIS2?
7. Jake oblasti musi pokryvat opatreni k rizeni rizik?
8. Proc je dulezita prima odpovednost statutarnich organu?
9. Co patri mezi nizsi povinnosti?
10. Co patri mezi vyssi organizacni a technicka opatreni?
