# 00 - Co umět ke zkoušce

Tento soubor je rychlá mapa přes hlavní výstupy učení. Slouží jako kontrolní seznam: pokud umíš každou položku vysvětlit vlastními slovy a uvést příklad, máš pokryté jádro předmětu.

---

## 1. Hrozba, zranitelnost, riziko a mitigace

### Co umět říct

- **Hrozba** je potenciální příčina incidentu, např. malware, výpadek elektřiny, útočník nebo chyba uživatele.
- **Zranitelnost** je slabé místo, které může hrozba využít, např. neaktualizovaný systém, slabé heslo nebo otevřený port.
- **Riziko** je kombinace hrozby, zranitelnosti a dopadu na aktivum.
- **Mitigace** je opatření, které riziko snižuje.

### Krátký příklad

Server má neaktualizovanou webovou aplikaci.

- Hrozba: útočník z internetu.
- Zranitelnost: známá chyba v aplikaci.
- Riziko: kompromitace serveru a únik dat.
- Mitigace: aktualizace aplikace, WAF, omezení přístupu, monitoring logů, zálohy.

### Kde v poznámkách

- [01_Obecne_principy_bezpecnosti.md](01_Obecne_principy_bezpecnosti.md)
- [11_ENA-KB_Infrastructure_protection.md](11_ENA-KB_Infrastructure_protection.md)

---

## 2. Symetrické vs. asymetrické šifrování a hash

### Co umět říct

- **Symetrické šifrování** používá stejný klíč pro šifrování i dešifrování.
- Je rychlé, hodí se pro větší objemy dat.
- Problém je bezpečná distribuce klíče.

- **Asymetrické šifrování** používá dvojici veřejný/soukromý klíč.
- Hodí se pro výměnu klíčů, certifikáty, digitální podpisy a ověřování identity.
- Je pomalejší než symetrické šifrování.

- **Hash** vytváří otisk dat.
- Slouží pro kontrolu integrity, ukládání hesel a digitální podpisy.
- Hash není šifrování, protože nejde běžně "dešifrovat" zpět.

### Kde v poznámkách

- [03_Kryptografie.md](03_Kryptografie.md)
- [04a_Symetricka_kryptografie.md](04a_Symetricka_kryptografie.md)
- [04b_Asymetricka_kryptografie_a_hashing.md](04b_Asymetricka_kryptografie_a_hashing.md)
- [07_ENA-KB_PKI.md](07_ENA-KB_PKI.md)

---

## 3. AAA, MFA a SSO

### Co umět říct

- **AAA** znamená:
  - **Authentication** - ověření identity.
  - **Authorization** - určení, co smí subjekt dělat.
  - **Accounting/Auditing** - evidence aktivit, dohledatelnost a audit.

- **MFA** zvyšuje jistotu ověření identity, protože kombinuje více faktorů:
  - něco, co znám,
  - něco, co mám,
  - něco, čím jsem.

- **SSO** umožňuje přihlásit se jednou a používat více služeb.
- Přínos SSO je pohodlí a centrální správa identit.
- Riziko SSO je vysoký dopad kompromitace centrální identity.

### Kde v poznámkách

- [01_Obecne_principy_bezpecnosti.md](01_Obecne_principy_bezpecnosti.md)
- [02_ENA-KB_Data_a_server_protection.md](02_ENA-KB_Data_a_server_protection.md)
- [12_ENA-KB_Wireless.md](12_ENA-KB_Wireless.md)

---

## 4. Minimální ochrana serveru a dat

### Co umět vyjmenovat

Minimální kroky:

1. Nastavit uživatelské role a oprávnění.
2. Nepoužívat běžně administrátorský účet.
3. Vynucovat silná hesla, ideálně MFA.
4. Aktualizovat operační systém a aplikace.
5. Zapnout auditování bezpečnostních událostí.
6. Centralizovat a uchovávat logy.
7. Pravidelně zálohovat.
8. Testovat obnovu ze záloh.
9. Šifrovat citlivá data nebo disk.
10. Omezit síťovou dostupnost jen na nutné služby.

### Kde v poznámkách

- [02_ENA-KB_Data_a_server_protection.md](02_ENA-KB_Data_a_server_protection.md)
- [05_ENA-KB_Monitoring.md](05_ENA-KB_Monitoring.md)
- [11_ENA-KB_Infrastructure_protection.md](11_ENA-KB_Infrastructure_protection.md)

---

## 5. Logování, monitoring a syslog

### Co umět říct

- **Monitoring** sleduje stav systému a metriky, např. dostupnost, CPU, RAM, disk, latenci nebo otevřené porty.
- Pomáhá odhalit problém dříve, než způsobí výpadek.
- **Logování** uchovává záznamy o událostech.
- Logy pomáhají vysvětlit, co se stalo, kdy se to stalo a kdo nebo co to způsobilo.
- **Syslog** je běžný protokol/formát pro posílání a ukládání textových logů, typicky v unixových systémech a síťových zařízeních.

### Kde v poznámkách

- [05_ENA-KB_Monitoring.md](05_ENA-KB_Monitoring.md)
- [02_ENA-KB_Data_a_server_protection.md](02_ENA-KB_Data_a_server_protection.md)

---

## 6. Endpoint a síťová opatření

### Endpoint opatření

- antivirus/antimalware,
- osobní firewall,
- pravidelné aktualizace,
- správa zařízení přes UEM/MDM,
- omezení oprávnění uživatele,
- kontrola přístupu do sítě přes NAC,
- ochrana proti škodlivým přílohám a aplikacím.

### Síťová opatření

- síťový firewall,
- IDS/IPS,
- VLAN segmentace,
- VPN,
- DHCP Snooping,
- Dynamic ARP Inspection,
- RA Guard,
- IP Source Guard,
- Web Proxy,
- WAF.

### Kde v poznámkách

- [10_ENA-KB_Endpoint_protection.md](10_ENA-KB_Endpoint_protection.md)
- [11_ENA-KB_Infrastructure_protection.md](11_ENA-KB_Infrastructure_protection.md)
- [12_ENA-KB_Wireless.md](12_ENA-KB_Wireless.md)

---

## 7. CSIRT, CERT a SOC

### Co umět říct

- **CSIRT** je tým pro řešení bezpečnostních incidentů.
- **CERT** je podobný pojem, historicky často používaný pro týmy koordinující reakci na incidenty a zranitelnosti.
- **SOC** je bezpečnostní dohledové centrum, které průběžně monitoruje události, logy, alerty a podezřelé chování.

### Rozdíl v jedné větě

SOC typicky incidenty detekuje a monitoruje, CSIRT/CERT je řeší, koordinuje a pomáhá s reakcí.

### Kde v poznámkách

- [05_Legislativa.md](05_Legislativa.md)
- [05_ENA-KB_Monitoring.md](05_ENA-KB_Monitoring.md)
- [11_ENA-KB_Infrastructure_protection.md](11_ENA-KB_Infrastructure_protection.md)

---

## 8. Legislativní povinnosti: ZKB, GDPR, NIS2

### Co umět říct

- **ZKB** řeší kybernetickou bezpečnost v českém právním prostředí.
- **GDPR** řeší ochranu osobních údajů.
- **NIS2** rozšiřuje evropskou regulaci kybernetické bezpečnosti na více subjektů a zdůrazňuje řízení rizik, odpovědnost vedení, incidenty, dodavatelský řetězec a bezpečnostní opatření.

### Praktický význam

Kybernetická bezpečnost není jen technické téma. Organizace musí řešit také:

- odpovědnost vedení,
- dokumentaci,
- řízení rizik,
- hlášení incidentů,
- ochranu osobních údajů,
- audit a prokazování souladu.

### Kde v poznámkách

- [05_Legislativa.md](05_Legislativa.md)
- [01_Obecne_principy_bezpecnosti.md](01_Obecne_principy_bezpecnosti.md)

---

## Rychlý test

Zkus si bez poznámek odpovědět:

1. Jaký je rozdíl mezi hrozbou, zranitelností a rizikem?
2. Proč se v TLS používá kombinace asymetrické a symetrické kryptografie?
3. Proč hash není šifrování?
4. Co znamená AAA?
5. Proč MFA snižuje riziko kompromitace účtu?
6. Jaký je rozdíl mezi monitoringem a logováním?
7. Co je syslog?
8. Jaká je minimální sada opatření pro server?
9. Jaký je rozdíl mezi firewallem, IDS a IPS?
10. Kdy použít VPN?
11. Co dělá SOC a co CSIRT/CERT?
12. Proč se v kyberbezpečnosti řeší legislativa?
