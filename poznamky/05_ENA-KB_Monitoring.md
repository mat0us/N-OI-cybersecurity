# P5 - ENA-KB: Monitoring a správa služeb a sítí

**Zdroj:** `05_ENA-KB_monitoring.pdf`  
**Autor materiálu:** Tomáš Sochor, březen 2026

---

## 1. Smysl monitoringu

Cílem provozu IT je, aby služby byly dostupné ve chvíli, kdy jsou potřeba. Výpadek systému se typicky nestane bez příčiny:

- každé selhání má nějakou příčinu,
- před selháním se často objevují symptomy,
- pokud symptomy sledujeme, můžeme problém odhalit dřív, než nastane skutečný výpadek.

### Dopady výpadku

| Dopad | Vysvětlení |
|---|---|
| **Ztráta reputace** | Organizace působí nespolehlivě. |
| **Finanční ztráta** | Zákazníci nemohou využít službu nebo dokončit objednávku. |
| **Ztráta produktivity** | Zaměstnanci nemohou pracovat s informačním systémem. |

Monitoring proto není jen "graf CPU". Je to systematické sledování toho, jak se chovají jednotlivé komponenty a služby.

---

## 2. Cíle monitoringu služeb

Většina dnešních služeb má požadavek dostupnosti **24/7**. Platí to i v organizacích s jednosměnným provozem, protože uživatelé často přistupují ke službám večer, v noci nebo o víkendu.

### Parametry služby

| Typ parametru | Co sledujeme | Příklad |
|---|---|---|
| **Lokální dostupnost** | Jestli služba nebo proces běží. | Systémová služba je `running`. |
| **Lokální využití zdrojů** | CPU, paměť, disk, fyzické nebo virtuální zdroje. | Disk je zaplněný na 92 %. |
| **Vzdálená dostupnost** | Jestli je služba dostupná z jiného místa. | Port odpovídá z internetu/VPN. |
| **Latence** | Doba odezvy. | HTTP odpověď trvá 250 ms. |
| **Propustnost** | Přenos dat za čas. | Stahování obsahu v MB/s. |
| **QoS parametry** | Jitter, maximální zpoždění apod. | Důležité u hlasu/videa. |

### Latence vs. propustnost

PDF výslovně upozorňuje, že **latence** a **transmission rate/throughput** se nemají zaměňovat:

- latence = jak rychle přijde odpověď,
- propustnost = kolik dat proteče za jednotku času.

Služba může mít nízkou latenci, ale špatnou propustnost, nebo naopak.

---

## 3. Problém: proces běží, ale služba nemusí fungovat

To, že proces existuje v systému, ještě neznamená, že je služba opravdu dostupná.

Je potřeba ověřovat:

- zda je server vzdáleně "živý" např. přes ping,
- zda je port otevřený a naslouchá,
- zda aplikace odpovídá v rozumném čase,
- zda je služba dostupná z pohledu uživatele.

Příklad: webový server může mít běžící proces, ale aplikace může vracet chybu, databáze nemusí odpovídat nebo firewall může blokovat přístup.

---

## 4. Metriky monitoringu služeb

### Lokální metriky

U virtualizované infrastruktury se sleduje hlavně:

- dostupnost hypervizoru,
- stav virtuálního stroje:
  - running,
  - suspended,
  - stopped,
- běh procesu,
- využití hardwarových zdrojů:
  - CPU,
  - RAM,
  - disk,
  - další fyzické nebo virtuální zdroje.

### Vzdálené metriky

Z pohledu dostupnosti služby se sleduje:

- IPv4/IPv6 ping,
- otevřený a odpovídající port,
- aplikační odezva,
- přenosová rychlost při stahování obsahu,
- další QoS parametry podle typu služby.

---

## 5. Nástroje pro monitoring serveru

Existuje mnoho komerčních i open-source nástrojů. PDF uvádí jako příklady:

- **Prometheus**,
- **Nagios**,
- **Zabbix**.

### Požadavky na monitorovací nástroj

| Požadavek | Proč je důležitý |
|---|---|
| **Široký výběr metrik** | Bez metrik není co vyhodnocovat. |
| **Standardní i vlastní metriky** | Obecné metriky nestačí pro všechny aplikace. |
| **Alerting při překročení prahu** | Např. příliš dlouhá latence nebo vysoké CPU. |
| **Detekce anomálií** | Sleduje odchylku od baseline, tedy normálního stavu. |
| **Korelace metrik** | Pomáhá při hledání příčiny problému napříč systémy. |
| **Podpora cloudu** | Cloudové služby mají jinou měřitelnost než vlastní servery. |

### Korelace metrik

Při ladění incidentu je často nutné spojit data z více zdrojů:

- servery,
- switche,
- firewally,
- aplikace,
- cloudové služby.

Proto je zásadní **časová synchronizace**. Bez ní se špatně určuje, co se stalo dříve a co bylo následkem.

---

## 6. Logování

Monitoring sám o sobě nemusí stačit. Metrika řekne, že se něco změnilo; log často řekne, co přesně se stalo.

### Vlastnosti logu

Logy se mohou lišit:

- velikostí,
- tím, co se loguje a co se vynechá,
- závažností události,
- dobou uchování,
- formátem,
- možností centrálního sběru.

Stejně jako u metrik je důležitá **časová synchronizace**.

### Typy logování

| Typ logu | Typický obsah |
|---|---|
| **Security** | Přihlášení, změny oprávnění, bezpečnostní události. |
| **Server** | Systémové služby, jádro, stav systému. |
| **Application** | Chyby aplikace, transakce, business události. |

Každý typ logu může mít jinou dobu uchování a jinou úroveň detailu.

---

## 7. Protokoly a nástroje pro logování

### Syslog

Syslog je obecný protokol pro uchovávání textových log záznamů.

Charakteristika:

- častý v unixových systémech,
- logy se často posílají do vzdáleného umístění,
- standard IETF, aktuální RFC 5424 z roku 2009,
- existují protokoly inspirované syslogem, např. RELP.

### Windows Event Log

Windows Event Log je nástroj pro Windows servery.

Výhody:

- dobře integrovaný do Windows,
- lepší nástroje pro vyhledávání v prostředí Windows.

Nevýhoda:

- horší interoperabilita s jinými operačními systémy, zejména při centralizovaném logování.

---

## 8. SNMP

**SNMP** (Simple Network Management Protocol) je IETF standard pro monitoring síťových zařízení.

### Základní vlastnosti

- Verze: **1, 2c, 3**.
- Architektura klient-server, označovaná jako **agent/manager**.
- Agent = monitorované zařízení.
- Manager = řídicí systém, který sbírá data.
- Aplikační protokol nad UDP.
- Port agenta: **161**.
- Port managera pro trapy: **162**.

### Typy SNMP zpráv

| Zpráva | Směr | Význam |
|---|---|---|
| **GetRequest** | Manager -> Agent | Dotaz na hodnotu. |
| **SetRequest** | Manager -> Agent | Nastavení hodnoty. |
| **Response** | Agent -> Manager | Odpověď na dotaz. |
| **Trap** | Agent -> Manager | Nevyžádaná zpráva vyvolaná událostí. |

### Bezpečnost SNMP

| Verze | Bezpečnost |
|---|---|
| **SNMP v1/v2c** | Plaintext community string, z bezpečnostního pohledu slabé. |
| **SNMP v3** | Podporuje autentizaci a šifrování zpráv. |

---

## 9. MIB a OID

**MIB** (Management Information Base) je databáze proměnných, které SNMP agent poskytuje managerovi.

Objekty jsou zapisované v notaci **ASN.1**. Každá proměnná má identifikátor **OID**.

### Příklad OID

`1.3.6.1.4.1.14988.1.1.1.2`

| Část | Význam |
|---|---|
| `1` | ISO |
| `1.3` | identified-organization |
| `1.3.6` | DoD |
| `1.3.6.1` | internet |
| `1.3.6.1.4` | private |
| `1.3.6.1.4.1` | IANA enterprise numbers |
| `1.3.6.1.4.1.14988` | Mikrotik |
| další část | proprietární struktura konkrétního zařízení |

U Mikrotiku materiál zmiňuje příkaz:

```text
interface print oid
```

---

## 10. SNMP Manager a Agent

### SNMP Manager

Manager je software běžící typicky na jednom počítači v síti.

Sbírá data:

- od všech agentů identifikovaných stejným community stringem,
- z odpovědí na GetRequest/SetRequest,
- z trapů posílaných agentem při události.

Příklad trapu: CPU usage přesáhne 80 %.

### SNMP Agent

Agent je softwarový modul dostupný na mnoha spravovatelných zařízeních:

- router,
- switch,
- IDS/IPS,
- firewall,
- některé servery.

SNMP je v materiálu označen jako **legacy protokol**. Postupně je nahrazován novějšími alternativami, ale stále se drží kvůli široké podpoře napříč vendory.

---

## 11. Monitoring síťových toků

### NetFlow

NetFlow je proprietární protokol Cisco z roku 1996. Používá třívrstvou architekturu:

- **Flow exporter** - zařízení, které exportuje informace o tocích,
- **Flow collector** - systém, který toky sbírá,
- **Analyzer app** - aplikace pro analýzu.

Místo ukládání jednotlivých paketů NetFlow sumarizuje informace do **flows**. To je:

- snazší na pochopení,
- méně náročné na uložení,
- vhodné pro přehled o provozu.

### Co je flow

Flow je skupina IP paketů se shodnými:

- zdrojovou a cílovou IP adresou,
- zdrojovým a cílovým portem,
- číslem protokolu:
  - TCP = 6,
  - ICMP = 1.

### Verze NetFlow

| Verze | Poznámka |
|---|---|
| **v5** | Jedna z nejpoužívanějších verzí. |
| **v9** | Flexibilnější, podpora IPv6, MPLS a dalších technologií. |

---

## 12. Alternativy k NetFlow

| Protokol | Charakteristika |
|---|---|
| **IPFIX** | IP Flow Information Export, IETF standard RFC 7011-7015 a RFC 5103. |
| **sFlow** | Sampled Flow, náhodné vzorkování každého n-tého paketu. Méně přesné, ale méně náročné. Popsáno v RFC 3176. |
| **J-Flow** | Proprietární protokol Juniper. |

Rozdíl mezi agregací a samplingem:

- NetFlow/IPFIX typicky agreguje informace do toku.
- sFlow vzorkuje provoz, a proto může být méně přesný, ale levnější na výkon a úložiště.

---

## 13. RMON a SMON

### RMON

**Remote Monitoring of Network** slouží pro monitoring fyzické a linkové vrstvy.

Vlastnosti:

- rozšiřuje MIB o nové položky,
- sondy na zařízeních posílají MIB data SNMP managerovi,
- IETF standard RFC 4502,
- v1 je popsána v RFC 2819.

### SMON

**SMON** je rozšíření RMON pro přepínané sítě.

- standard RFC 2613,
- řeší monitoring v prostředí switchů.

---

## 14. Network Discovery

Discovery slouží k identifikaci zařízení v blízkém okolí síťového prvku.

Typicky běží na:

- routeru,
- switchi,
- firewallu,
- jiném prvku síťové infrastruktury.

Umí zjistit např.:

- sousední routery a switche,
- schopnosti zařízení:
  - L3 routing,
  - L2 switching,
- rozhraní a jejich typy:
  - GigabitEthernet,
  - Serial,
  - FastEthernet,
- další informace o zařízení.

Správná funkce discovery vyžaduje, aby na obou propojených zařízeních běžel stejný nebo kompatibilní discovery protokol.

### CDP vs. LLDP

| Protokol | Typ | Význam |
|---|---|---|
| **CDP** | Cisco proprietary | Funguje pro Cisco zařízení, chybí interoperabilita v heterogenním prostředí. |
| **LLDP** | IEEE 802.1AB | Multivendor přístup, podporuje Cisco, HP, Dell, Juniper a další; dá se propojit se SNMP a MIB. |

LLDP je obecně vhodnější tam, kde je infrastruktura složená z více vendorů.

---

## 15. Zkouškové shrnutí

- Monitoring slouží k odhalení problémů před reálným výpadkem.
- Proces může běžet, ale služba přesto nemusí být dostupná.
- Rozlišuj lokální a vzdálené metriky.
- Nezaměňuj latenci a propustnost.
- Monitoring potřebuje alerting, baseline, detekci anomálií a korelaci metrik.
- Logy doplňují metriky a pomáhají vysvětlit, co se stalo.
- Syslog je obecný a interoperabilní, Windows Event Log je silný ve Windows prostředí.
- SNMP používá model manager/agent a porty UDP 161/162.
- SNMP v1/v2c je bezpečnostně slabé kvůli plaintext community stringu; v3 podporuje autentizaci a šifrování.
- MIB obsahuje proměnné, OID jednoznačně identifikuje objekt.
- NetFlow sumarizuje provoz do toků; alternativy jsou IPFIX, sFlow a J-Flow.
- Discovery protokoly pomáhají zjistit sousední zařízení; CDP je Cisco-only, LLDP je standardizované a multivendor.

---

## Otázky k opakování

1. Proč samotný běh procesu nestačí jako důkaz dostupnosti služby?
2. Jak se liší lokální a vzdálené metriky?
3. Jaký je rozdíl mezi latencí a propustností?
4. Proč je důležitá časová synchronizace při korelaci metrik a logů?
5. Jaké jsou výhody a nevýhody Syslogu a Windows Event Logu?
6. Popište architekturu SNMP manager/agent.
7. Jaké porty SNMP používá?
8. Co je MIB a co je OID?
9. Co je flow v NetFlow?
10. Jak se liší NetFlow, IPFIX, sFlow a J-Flow?
11. K čemu slouží RMON a SMON?
12. Proč je LLDP vhodnější než CDP v heterogenních sítích?
