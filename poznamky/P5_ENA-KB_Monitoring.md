# P5 - ENA-KB: Monitoring a sprava sluzeb a siti

**Zdroj:** `05_ENA-KB_monitoring.pdf`  
**Autor materialu:** Tomas Sochor, brezen 2026

---

## 1. Smysl monitoringu

Cilem provozu IT je, aby sluzby byly dostupne ve chvili, kdy jsou potreba. Vypadek systemu se typicky nestane bez priciny:

- kazde selhani ma nejakou pricinu,
- pred selhanim se casto objevuji symptomy,
- pokud symptomy sledujeme, muzeme problem odhalit driv, nez nastane skutecny vypadek.

### Dopady vypadku

| Dopad | Vysvetleni |
|---|---|
| **Ztrata reputace** | Organizace pusobi nespolehlive. |
| **Financni ztrata** | Zakaznici nemohou vyuzit sluzbu nebo dokoncit objednavku. |
| **Ztrata produktivity** | Zamestnanci nemohou pracovat s informacnim systemem. |

Monitoring proto neni jen "graf CPU". Je to systematicke sledovani toho, jak se chovaji jednotlive komponenty a sluzby.

---

## 2. Cile monitoringu sluzeb

Vetsina dnesnich sluzeb ma pozadavek dostupnosti **24/7**. Plati to i v organizacich s jednosmennym provozem, protoze uzivatele casto pristupuji ke sluzbam vecer, v noci nebo o vikendu.

### Parametry sluzby

| Typ parametru | Co sledujeme | Priklad |
|---|---|---|
| **Lokalni dostupnost** | Jestli sluzba nebo proces bezi. | Systemova sluzba je `running`. |
| **Lokalni vyuziti zdroju** | CPU, pamet, disk, fyzicke nebo virtualni zdroje. | Disk je zaplneny na 92 %. |
| **Vzdalena dostupnost** | Jestli je sluzba dostupna z jineho mista. | Port odpovida z internetu/VPN. |
| **Latence** | Doba odezvy. | HTTP odpoved trva 250 ms. |
| **Propustnost** | Prenos dat za cas. | Stahovani obsahu v MB/s. |
| **QoS parametry** | Jitter, maximalni zpozdeni apod. | Dulezite u hlasu/videa. |

### Latence vs. propustnost

PDF vyslovne upozornuje, ze **latence** a **transmission rate/throughput** se nemaji zamenovat:

- latence = jak rychle prijde odpoved,
- propustnost = kolik dat protece za jednotku casu.

Sluzba muze mit nizkou latenci, ale spatnou propustnost, nebo naopak.

---

## 3. Problem: proces bezi, ale sluzba nemusi fungovat

To, ze proces existuje v systemu, jeste neznamena, ze je sluzba opravdu dostupna.

Je potreba overovat:

- zda je server vzdaleně "zivy" napr. pres ping,
- zda je port otevreny a nasloucha,
- zda aplikace odpovida v rozumnem case,
- zda je sluzba dostupna z pohledu uzivatele.

Priklad: webovy server muze mit bezici proces, ale aplikace muze vracet chybu, databaze nemusi odpovidat nebo firewall muze blokovat pristup.

---

## 4. Metriky monitoringu sluzeb

### Lokalni metriky

U virtualizovane infrastruktury se sleduje hlavne:

- dostupnost hypervizoru,
- stav virtualniho stroje:
  - running,
  - suspended,
  - stopped,
- beh procesu,
- vyuziti hardwarovych zdroju:
  - CPU,
  - RAM,
  - disk,
  - dalsi fyzicke nebo virtualni zdroje.

### Vzdalene metriky

Z pohledu dostupnosti sluzby se sleduje:

- IPv4/IPv6 ping,
- otevreny a odpovidajici port,
- aplikacni odezva,
- prenosova rychlost pri stahovani obsahu,
- dalsi QoS parametry podle typu sluzby.

---

## 5. Nastroje pro monitoring serveru

Existuje mnoho komercnich i open-source nastroju. PDF uvadi jako priklady:

- **Prometheus**,
- **Nagios**,
- **Zabbix**.

### Pozadavky na monitorovaci nastroj

| Pozadavek | Proc je dulezity |
|---|---|
| **Siroky vyber metrik** | Bez metrik neni co vyhodnocovat. |
| **Standardni i vlastni metriky** | Obecne metriky nestaci pro vsechny aplikace. |
| **Alerting pri prekroceni prahu** | Napr. prilis dlouha latence nebo vysoke CPU. |
| **Detekce anomalii** | Sleduje odchylku od baseline, tedy normalniho stavu. |
| **Korelace metrik** | Pomaha pri hledani priciny problemu napric systemy. |
| **Podpora cloudu** | Cloudove sluzby maji jinou meritelnost nez vlastni servery. |

### Korelace metrik

Pri ladeni incidentu je casto nutne spojit data z vice zdroju:

- servery,
- switche,
- firewally,
- aplikace,
- cloudove sluzby.

Proto je zasadni **casova synchronizace**. Bez ni se spatne urcuje, co se stalo drive a co bylo nasledkem.

---

## 6. Logovani

Monitoring sam o sobe nemusi stacit. Metrika rekne, ze se neco zmenilo; log casto rekne, co presne se stalo.

### Vlastnosti logu

Logy se mohou lisit:

- velikosti,
- tim, co se loguje a co se vynecha,
- zavaznosti udalosti,
- dobou uchovani,
- formatem,
- moznosti centralniho sberu.

Stejne jako u metrik je dulezita **casova synchronizace**.

### Typy logovani

| Typ logu | Typicky obsah |
|---|---|
| **Security** | Prihlaseni, zmeny opravneni, bezpecnostni udalosti. |
| **Server** | Systemove sluzby, jadro, stav systemu. |
| **Application** | Chyby aplikace, transakce, business udalosti. |

Kazdy typ logu muze mit jinou dobu uchovani a jinou uroven detailu.

---

## 7. Protokoly a nastroje pro logovani

### Syslog

Syslog je obecny protokol pro uchovavani textovych log zaznamu.

Charakteristika:

- casty v unixovych systemech,
- logy se casto posilaji do vzdaleneho umisteni,
- standard IETF, aktualni RFC 5424 z roku 2009,
- existuji protokoly inspirovane syslogem, napr. RELP.

### Windows Event Log

Windows Event Log je nastroj pro Windows servery.

Vyhody:

- dobre integrovany do Windows,
- lepsi nastroje pro vyhledavani v prostredi Windows.

Nevyhoda:

- horsi interoperabilita s jinymi operacnimi systemy, zejmena pri centralizovanem logovani.

---

## 8. SNMP

**SNMP** (Simple Network Management Protocol) je IETF standard pro monitoring sitovych zarizeni.

### Zakladni vlastnosti

- Verze: **1, 2c, 3**.
- Architektura klient-server, oznacovana jako **agent/manager**.
- Agent = monitorovane zarizeni.
- Manager = ridici system, ktery sbira data.
- Aplikacni protokol nad UDP.
- Port agenta: **161**.
- Port managera pro trapy: **162**.

### Typy SNMP zprav

| Zprava | Smer | Vyznam |
|---|---|---|
| **GetRequest** | Manager -> Agent | Dotaz na hodnotu. |
| **SetRequest** | Manager -> Agent | Nastaveni hodnoty. |
| **Response** | Agent -> Manager | Odpoved na dotaz. |
| **Trap** | Agent -> Manager | Nevyzadana zprava vyvolana udalosti. |

### Bezpecnost SNMP

| Verze | Bezpecnost |
|---|---|
| **SNMP v1/v2c** | Plaintext community string, z bezpecnostniho pohledu slabe. |
| **SNMP v3** | Podporuje autentizaci a sifrovani zprav. |

---

## 9. MIB a OID

**MIB** (Management Information Base) je databaze promennych, ktere SNMP agent poskytuje managerovi.

Objekty jsou zapisovane v notaci **ASN.1**. Kazda promenna ma identifikator **OID**.

### Priklad OID

`1.3.6.1.4.1.14988.1.1.1.2`

| Cast | Vyznam |
|---|---|
| `1` | ISO |
| `1.3` | identified-organization |
| `1.3.6` | DoD |
| `1.3.6.1` | internet |
| `1.3.6.1.4` | private |
| `1.3.6.1.4.1` | IANA enterprise numbers |
| `1.3.6.1.4.1.14988` | Mikrotik |
| dalsi cast | proprietarni struktura konkretniho zarizeni |

U Mikrotiku material zminuje prikaz:

```text
interface print oid
```

---

## 10. SNMP Manager a Agent

### SNMP Manager

Manager je software bezici typicky na jednom pocitaci v siti.

Sbira data:

- od vsech agentu identifikovanych stejnym community stringem,
- z odpovedi na GetRequest/SetRequest,
- z trapu posilanych agentem pri udalosti.

Priklad trapu: CPU usage presahne 80 %.

### SNMP Agent

Agent je softwarovy modul dostupny na mnoha spravovatelných zarizenich:

- router,
- switch,
- IDS/IPS,
- firewall,
- nektere servery.

SNMP je v materialu oznacen jako **legacy protokol**. Postupne je nahrazovan novejsimi alternativami, ale stale se drzi kvuli siroke podpore napric vendory.

---

## 11. Monitoring sitovych toku

### NetFlow

NetFlow je proprietarni protokol Cisco z roku 1996. Pouziva trivrsvou architekturu:

- **Flow exporter** - zarizeni, ktere exportuje informace o tocich,
- **Flow collector** - system, ktery toky sbira,
- **Analyzer app** - aplikace pro analyzu.

Misto ukladani jednotlivych paketu NetFlow sumarizuje informace do **flows**. To je:

- snazsi na pochopeni,
- mene narocne na ulozeni,
- vhodne pro prehled o provozu.

### Co je flow

Flow je skupina IP paketu se shodnymi:

- zdrojovou a cilovou IP adresou,
- zdrojovym a cilovym portem,
- cislem protokolu:
  - TCP = 6,
  - ICMP = 1.

### Verze NetFlow

| Verze | Poznamka |
|---|---|
| **v5** | Jedna z nejpouzivanejsich verzi. |
| **v9** | Flexibilnejsi, podpora IPv6, MPLS a dalsich technologii. |

---

## 12. Alternativy k NetFlow

| Protokol | Charakteristika |
|---|---|
| **IPFIX** | IP Flow Information Export, IETF standard RFC 7011-7015 a RFC 5103. |
| **sFlow** | Sampled Flow, nahodne vzorkovani kazdeho n-teho paketu. Mene presne, ale mene narocne. Popsano v RFC 3176. |
| **J-Flow** | Proprietarni protokol Juniper. |

Rozdil mezi agregaci a samplingem:

- NetFlow/IPFIX typicky agreguje informace do toku.
- sFlow vzorkuje provoz, a proto muze byt mene presny, ale levnejsi na vykon a uloziste.

---

## 13. RMON a SMON

### RMON

**Remote Monitoring of Network** slouzi pro monitoring fyzicke a linkove vrstvy.

Vlastnosti:

- rozsiruje MIB o nove polozky,
- sondy na zarizenich posilaji MIB data SNMP managerovi,
- IETF standard RFC 4502,
- v1 je popsana v RFC 2819.

### SMON

**SMON** je rozsireni RMON pro prepinane site.

- standard RFC 2613,
- resi monitoring v prostredi switchu.

---

## 14. Network Discovery

Discovery slouzi k identifikaci zarizeni v blizkem okoli sitoveho prvku.

Typicky bezi na:

- routeru,
- switchi,
- firewallu,
- jinem prvku sitove infrastruktury.

Umi zjistit napr.:

- sousedni routery a switche,
- schopnosti zarizeni:
  - L3 routing,
  - L2 switching,
- rozhrani a jejich typy:
  - GigabitEthernet,
  - Serial,
  - FastEthernet,
- dalsi informace o zarizeni.

Spravna funkce discovery vyzaduje, aby na obou propojenych zarizenich bezel stejny nebo kompatibilni discovery protokol.

### CDP vs. LLDP

| Protokol | Typ | Vyznam |
|---|---|---|
| **CDP** | Cisco proprietary | Funguje pro Cisco zarizeni, chybi interoperabilita v heterogennim prostredi. |
| **LLDP** | IEEE 802.1AB | Multivendor pristup, podporuje Cisco, HP, Dell, Juniper a dalsi; da se propojit se SNMP a MIB. |

LLDP je obecne vhodnejsi tam, kde je infrastruktura slozena z vice vendoru.

---

## 15. Zkouskove shrnuti

- Monitoring slouzi k odhaleni problemu pred realnym vypadkem.
- Proces muze bezet, ale sluzba presto nemusi byt dostupna.
- Rozlisuj lokalni a vzdalene metriky.
- Nezamenuj latenci a propustnost.
- Monitoring potrebuje alerting, baseline, detekci anomalii a korelaci metrik.
- Logy doplnuji metriky a pomahaji vysvetlit, co se stalo.
- Syslog je obecny a interoperabilni, Windows Event Log je silny ve Windows prostredi.
- SNMP pouziva model manager/agent a porty UDP 161/162.
- SNMP v1/v2c je bezpecnostne slabe kvuli plaintext community stringu; v3 podporuje autentizaci a sifrovani.
- MIB obsahuje promenne, OID jednoznacne identifikuje objekt.
- NetFlow sumarizuje provoz do toku; alternativy jsou IPFIX, sFlow a J-Flow.
- Discovery protokoly pomahaji zjistit sousedni zarizeni; CDP je Cisco-only, LLDP je standardizovane a multivendor.

---

## Otazky k opakovani

1. Proc samotny beh procesu nestaci jako dukaz dostupnosti sluzby?
2. Jak se lisi lokalni a vzdalene metriky?
3. Jaky je rozdil mezi latenci a propustnosti?
4. Proc je dulezita casova synchronizace pri korelaci metrik a logu?
5. Jake jsou vyhody a nevyhody Syslogu a Windows Event Logu?
6. Popiste architekturu SNMP manager/agent.
7. Jake porty SNMP pouziva?
8. Co je MIB a co je OID?
9. Co je flow v NetFlow?
10. Jak se lisi NetFlow, IPFIX, sFlow a J-Flow?
11. K cemu slouzi RMON a SMON?
12. Proc je LLDP vhodnejsi nez CDP v heterogennich sitich?
