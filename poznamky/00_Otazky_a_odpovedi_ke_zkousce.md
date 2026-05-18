# 00 - Otázky a odpovědi ke zkoušce

Souhrn otázek z konců jednotlivých poznámek a z hlavního checklistu. Odpovědi jsou psané stručně tak, aby se daly použít jako základ pro test nebo ústní vysvětlení.

---

## Kontrola podle 00_reading-week-enc-kb-ls-2026.html

Tato část převádí osnovu z hlavního HTML souboru na otázky. Slouží jako kontrola, že souhrn nepokrývá jen jednotlivá PDF, ale i celé požadované tematické minimum předmětu.

### 1. Co zahrnují obecné principy zajišťování bezpečnosti digitálních aktiv?

<details>
<summary>Odpověď</summary>

Patří sem identifikace a hodnocení digitálních aktiv, určení jejich důvěrnosti, integrity a dostupnosti, vyhodnocení hrozeb, zranitelností a rizik, návrh opatření, bezpečnostní politika a také fyzická a organizační ochrana infrastruktury.

</details>

### 2. Jak se hodnotí digitální aktiva a proč se to dělá?

<details>
<summary>Odpověď</summary>

U aktiva se určuje vlastník, hodnota, umístění, závislosti, dopad ztráty důvěrnosti, integrity nebo dostupnosti a vazba na procesy organizace. Cílem je vědět, co je opravdu důležité a kam má směřovat nejsilnější ochrana.

</details>

### 3. Co znamená eliminace nebo mitigace rizika?

<details>
<summary>Odpověď</summary>

Riziko lze snížit bezpečnostním opatřením, přenést například pojištěním nebo smlouvou, akceptovat, pokud je přijatelné, případně se mu vyhnout změnou procesu. V praxi se často nemluví o úplné eliminaci, ale o snížení rizika na přijatelnou úroveň.

</details>

### 4. Co je bezpečnostní politika?

<details>
<summary>Odpověď</summary>

Bezpečnostní politika je soubor pravidel, odpovědností a postupů, které určují, jak organizace chrání aktiva. Popisuje například práci s účty, hesly, oprávněními, incidenty, zálohami, zařízeními, vzdáleným přístupem a dodavateli.

</details>

### 5. Co patří do fyzické a organizační ochrany infrastruktury?

<details>
<summary>Odpověď</summary>

Fyzická ochrana zahrnuje zabezpečení prostor, serveroven, rozvaděčů, napájení, chlazení, požární ochranu a kontrolu vstupu. Organizační ochrana řeší role, odpovědnosti, procesy, školení, změnové řízení, pravidla pro zaměstnance a kontrolu dodavatelů.

</details>

### 6. Jaký je rozdíl mezi kryptografií a kryptoanalýzou?

<details>
<summary>Odpověď</summary>

Kryptografie navrhuje metody pro ochranu důvěrnosti, integrity, autenticity a nepopiratelnosti. Kryptoanalýza zkoumá, jak kryptografické systémy prolomit nebo oslabit, například hledáním slabých klíčů, chyb v algoritmu nebo špatné implementace.

</details>

### 7. Kdy použít symetrické a kdy asymetrické šifrování?

<details>
<summary>Odpověď</summary>

Symetrické šifrování se hodí pro rychlé šifrování většího objemu dat, protože používá stejný tajný klíč pro šifrování i dešifrování. Asymetrické šifrování používá pár veřejného a soukromého klíče a hodí se pro výměnu klíčů, ověření identity, certifikáty a elektronické podpisy.

</details>

### 8. K čemu slouží hashovací algoritmus?

<details>
<summary>Odpověď</summary>

Hash vytváří krátký otisk dat s pevnou délkou. Používá se pro kontrolu integrity, ukládání hesel ve formě salted hashe, digitální podpisy, kontrolu souborů a detekci změny dat. Není to šifrování, protože z hashe se nemá dát získat původní zpráva.

</details>

### 9. Co jsou bezpečnostní techniky založené na kryptografických systémech?

<details>
<summary>Odpověď</summary>

Jde například o TLS, VPN, elektronický podpis, certifikáty, PKI, šifrování disků, šifrování záloh, bezpečné ukládání hesel, kontrolní součty, HMAC a mechanismy pro ověření identity nebo integrity dat.

</details>

### 10. Co znamená AAA?

<details>
<summary>Odpověď</summary>

AAA znamená Authentication, Authorization, Accounting/Auditing. Authentication ověřuje, kdo uživatel je. Authorization určuje, co smí dělat. Accounting nebo Auditing zaznamenává, co uživatel nebo systém provedl.

</details>

### 11. Co má řešit heslová politika?

<details>
<summary>Odpověď</summary>

Heslová politika má řešit délku a kvalitu hesel, zákaz opakovaného používání hesel, bezpečné ukládání hesel, ochranu proti hádání, použití správců hesel, reset hesel, zákaz sdílení účtů a doplnění hesel o MFA tam, kde je to důležité.

</details>

### 12. Proč se řeší MFA?

<details>
<summary>Odpověď</summary>

MFA snižuje riziko, že kompromitované heslo automaticky znamená kompromitovaný účet. Kombinuje více faktorů, typicky něco, co uživatel zná, má nebo čím je. Příkladem je heslo plus mobilní aplikace, hardwarový token nebo biometrie.

</details>

### 13. Co jsou uživatelské účty, skupiny a oprávnění?

<details>
<summary>Odpověď</summary>

Účet reprezentuje identitu uživatele nebo služby. Skupiny usnadňují správu více účtů najednou. Oprávnění určují přístup ke konkrétním systémům, souborům, službám nebo akcím. Správný návrh oprávnění má vycházet z principu nejmenších oprávnění.

</details>

### 14. Co je centralizovaná AAA a SSO?

<details>
<summary>Odpověď</summary>

Centralizovaná AAA znamená, že ověřování, oprávnění a audit se spravují na jednom nebo několika centrálních systémech místo samostatně na každé službě. SSO umožňuje uživateli přihlásit se jednou a používat více služeb bez opakovaného zadávání hesla.

</details>

### 15. Jaké jsou minimální kroky ochrany serveru a dat?

<details>
<summary>Odpověď</summary>

Nastavit role a oprávnění, omezit služby jen na nutné minimum, pravidelně aktualizovat, zapnout audit a logování, používat silnou autentizaci, chránit data šifrováním, dělat zálohy, testovat obnovu, oddělovat prostředí a sledovat bezpečnostní události.

</details>

### 16. Jak souvisí audit událostí a SELinux?

<details>
<summary>Odpověď</summary>

Audit událostí slouží k zaznamenání důležitých akcí a bezpečnostních událostí. SELinux je mechanismus povinného řízení přístupu, který vynucuje bezpečnostní politiku nad procesy a soubory. V praxi se doplňují: SELinux omezuje, co proces smí, a audit pomáhá zjistit, co bylo povoleno, odmítnuto nebo podezřelé.

</details>

### 17. Proč jsou důležité zálohy a šifrování disků?

<details>
<summary>Odpověď</summary>

Zálohy chrání dostupnost a obnovitelnost dat po chybě, útoku, výpadku nebo ransomwaru. Šifrování disků chrání důvěrnost dat při ztrátě zařízení, krádeži serveru, neoprávněném přístupu k médiu nebo likvidaci disků.

</details>

### 18. Jaký je cíl monitoringu?

<details>
<summary>Odpověď</summary>

Monitoring má průběžně sledovat dostupnost, výkon, stav služeb, kapacitu a bezpečnostní události. Pomáhá rychle odhalit výpadky, anomálie, útoky, chybné konfigurace a dlouhodobé trendy.

</details>

### 19. Co jsou metriky v monitoringu?

<details>
<summary>Odpověď</summary>

Metriky jsou měřitelné hodnoty, například dostupnost služby, latence, vytížení CPU, RAM, diskový prostor, počet chyb, propustnost sítě, počet neúspěšných přihlášení nebo počet bezpečnostních alertů.

</details>

### 20. Co je logování a syslog server?

<details>
<summary>Odpověď</summary>

Logování ukládá záznamy o událostech. Syslog je běžný protokol a formát pro předávání logů hlavně z unixových systémů a síťových prvků. Syslog server logy centralizuje, takže se dají lépe vyhledávat, korelovat, archivovat a chránit proti smazání na napadeném zařízení.

</details>

### 21. Co je PKI a k čemu slouží certifikáty?

<details>
<summary>Odpověď</summary>

PKI je infrastruktura veřejných klíčů. Zajišťuje vydávání, správu, ověřování a odvolávání certifikátů. Certifikát svazuje veřejný klíč s identitou subjektu a umožňuje ověřit, že komunikujeme se správnou stranou.

</details>

### 22. Co znamená šifrovaná komunikace?

<details>
<summary>Odpověď</summary>

Šifrovaná komunikace chrání přenášená data před odposlechem a často i před neoprávněnou změnou. Typickým příkladem je HTTPS nad TLS, VPN tunel nebo šifrované spojení mezi službami.

</details>

### 23. Co je elektronický podpis?

<details>
<summary>Odpověď</summary>

Elektronický podpis využívá soukromý klíč podepisující osoby nebo systému a veřejný klíč pro ověření. Slouží k ověření původu dokumentu, integrity dokumentu a v některých režimech i k nepopiratelnosti.

</details>

### 24. Co znamená vysoká dostupnost pomocí anycastu, DNS a CDN?

<details>
<summary>Odpověď</summary>

Vysoká dostupnost znamená, že služba zůstává dostupná i při výpadku části infrastruktury. DNS může směrovat uživatele na dostupný uzel, anycast umožňuje směrovat stejnou IP adresu do nejbližší nebo dostupné lokality a CDN rozkládá obsah do více geografických míst.

</details>

### 25. Jaké nástroje patří do ochrany endpointů?

<details>
<summary>Odpověď</summary>

Antivirus, antimalware, EDR, osobní firewall, šifrování disku, správa aktualizací, správa konfigurací, MDM/UEM, aplikační kontrola, ochrana proti phishingu a řízení přístupu zařízení do sítě.

</details>

### 26. Co znamená hromadná správa koncových stanic?

<details>
<summary>Odpověď</summary>

Je to centrální správa notebooků, počítačů a mobilních zařízení. Umožňuje nasazovat aktualizace, politiky, software, konfigurace, certifikáty, šifrování, vzdálené vymazání zařízení a kontrolu souladu s bezpečnostními pravidly.

</details>

### 27. Co je network admission control?

<details>
<summary>Odpověď</summary>

Network admission control ověřuje, zda zařízení smí do sítě. Může kontrolovat identitu uživatele, stav zařízení, certifikát, členství v doméně, aktuálnost systému nebo přítomnost bezpečnostního softwaru. Nevyhovující zařízení může být odmítnuto nebo zařazeno do karanténní VLAN.

</details>

### 28. Co je IP spoofing a jak se proti němu bránit?

<details>
<summary>Odpověď</summary>

IP spoofing je podvržení zdrojové IP adresy. Obrana zahrnuje filtrování provozu na hraně sítě, anti-spoofing pravidla, uRPF, správné ACL, segmentaci a nepovažování samotné IP adresy za dostatečný důkaz identity.

</details>

### 29. Proč se používá VLAN segmentace?

<details>
<summary>Odpověď</summary>

VLAN segmentace odděluje části sítě podle účelu, důvěryhodnosti nebo typu zařízení. Omezuje laterální pohyb útočníka, snižuje dopad kompromitace a umožňuje přesněji řídit pravidla mezi segmenty.

</details>

### 30. Jaký je rozdíl mezi FW, IPS, NGFW, web proxy a VPN?

<details>
<summary>Odpověď</summary>

Firewall filtruje provoz podle pravidel. IPS aktivně detekuje a blokuje škodlivý provoz. NGFW přidává hlubší inspekci, aplikační pravidla a často integraci s identitami. Web proxy zprostředkovává a kontroluje webový provoz. VPN vytváří šifrované propojení přes nedůvěryhodnou síť.

</details>

### 31. Jaký je rozdíl mezi site-to-site VPN a remote-access VPN?

<details>
<summary>Odpověď</summary>

Site-to-site VPN propojuje celé sítě, typicky pobočky nebo datacentra. Remote-access VPN připojuje jednotlivého uživatele nebo zařízení do firemní sítě.

</details>

### 32. Jaký je rozdíl mezi PSK a Enterprise/802.1X u Wi-Fi?

<details>
<summary>Odpověď</summary>

PSK používá sdílené heslo pro více uživatelů nebo zařízení. Enterprise/802.1X používá individuální ověřování, typicky proti RADIUS serveru, a umožňuje lepší správu identit, odvolání přístupu a audit.

</details>

### 33. K čemu slouží wireless controller?

<details>
<summary>Odpověď</summary>

Wireless controller centrálně spravuje přístupové body, konfigurace SSID, roaming, kanály, výkon, autentizaci, monitoring a bezpečnostní politiky bezdrátové sítě.

</details>

### 34. Proč se kontroluje rádiové spektrum a detekují cizí AP?

<details>
<summary>Odpověď</summary>

Kontrola spektra pomáhá najít rušení, přetížené kanály a podezřelé vysílání. Detekce cizích nebo rogue AP odhaluje neautorizované přístupové body, které mohou obcházet bezpečnostní politiku nebo lákat uživatele k připojení.

</details>

### 35. Jaká jsou specifika IoT v bezdrátových sítích?

<details>
<summary>Odpověď</summary>

IoT zařízení mívají slabší výkon, horší podporu aktualizací, dlouhou životnost, jednoduché autentizační mechanismy a často omezenou správu. Proto je vhodné je segmentovat, omezit jejich komunikaci, sledovat provoz a nepouštět je do citlivých částí sítě.

</details>

### 36. K čemu slouží honeypot?

<details>
<summary>Odpověď</summary>

Honeypot je návnadový systém nebo služba, která má přilákat útočníka a umožnit pozorování jeho chování. Pomáhá s detekcí útoků, sběrem indikátorů kompromitace a pochopením metod útočníků.

</details>

### 37. K čemu slouží sandbox?

<details>
<summary>Odpověď</summary>

Sandbox je izolované prostředí pro bezpečné spuštění neznámého nebo podezřelého kódu. Používá se při analýze malwaru, testování příloh, kontrole chování programu a omezení dopadu škodlivé aktivity.

</details>

### 38. Jak serverová virtualizace pomáhá vysoké dostupnosti?

<details>
<summary>Odpověď</summary>

Virtualizace umožňuje provozovat služby ve virtuálních strojích, přesouvat je mezi fyzickými servery, lépe plánovat údržbu a obnovovat služby po selhání. Ve spojení s více hostiteli a sdíleným nebo replikovaným úložištěm pomáhá snížit dopad výpadku hardwaru.

</details>

### 39. Co je osobní údaj a jak se chrání?

<details>
<summary>Odpověď</summary>

Osobní údaj je informace vztahující se k identifikované nebo identifikovatelné fyzické osobě. Chrání se omezením účelu a rozsahu zpracování, řízením přístupů, šifrováním, pseudonymizací, logováním, smlouvami se zpracovateli, školením a pravidly pro incidenty.

</details>

### 40. Co řeší ZKB, GDPR a NIS2?

<details>
<summary>Odpověď</summary>

ZKB řeší kybernetickou bezpečnost v českém právním prostředí. GDPR řeší ochranu osobních údajů. NIS2 rozšiřuje evropské požadavky na kybernetickou bezpečnost, řízení rizik, odpovědnost vedení, hlášení incidentů, dodavatelský řetězec a dohled nad regulovanými subjekty.

</details>

### 41. Jaký je rozdíl mezi kybernetickou bezpečností na úrovni organizace a státu?

<details>
<summary>Odpověď</summary>

Organizace řeší ochranu svých aktiv, služeb, dat, procesů a odpovědností. Stát řeší také kritickou infrastrukturu, regulaci, dohled, národní strategii, koordinaci incidentů, mezinárodní spolupráci a podporu subjektů, které jsou důležité pro fungování společnosti.

</details>

### 42. Jaký je rozdíl mezi CSIRT, CERT a SOC?

<details>
<summary>Odpověď</summary>

CSIRT je tým pro řešení bezpečnostních incidentů. CERT je historicky podobný pojem, často používaný pro týmy koordinující reakci na incidenty a zranitelnosti. SOC je dohledové centrum, které průběžně sleduje logy, alerty a stav bezpečnosti. Zjednodušeně: SOC detekuje a monitoruje, CSIRT/CERT incidenty řeší a koordinuje.

</details>

### 43. Jak CSIRT/CERT/SOC prosazují bezpečnostní politiku?

<details>
<summary>Odpověď</summary>

Používají logování, monitoring, SIEM, pravidla detekce, incident response postupy, eskalace, reporting, doporučení opatření, kontrolu souladu a zpětnou vazbu do bezpečnostních politik. Nejde jen o technické nástroje, ale i o procesy a odpovědnosti.

</details>

### 44. Co je sociální inženýrství?

<details>
<summary>Odpověď</summary>

Sociální inženýrství je útok na člověka a procesy místo přímého útoku na technologii. Útočník se snaží oběť zmanipulovat, aby prozradila heslo, otevřela přílohu, schválila platbu, poskytla přístup nebo obešla pravidla.

</details>

### 45. Co je phishing?

<details>
<summary>Odpověď</summary>

Phishing je podvodná komunikace, nejčastěji e-mail, SMS nebo zpráva, která se tváří jako důvěryhodný zdroj. Cílem je získat přihlašovací údaje, donutit uživatele otevřít škodlivou přílohu nebo ho přimět k jiné akci výhodné pro útočníka.

</details>

### 46. Co je pharming?

<details>
<summary>Odpověď</summary>

Pharming přesměruje uživatele na falešný web i tehdy, když zadá správnou adresu. Může využít manipulaci DNS, kompromitovaný router, škodlivý záznam v systému nebo jiný způsob přesměrování.

</details>

### 47. Jak se bránit sociálnímu inženýrství?

<details>
<summary>Odpověď</summary>

Školením uživatelů, ověřováním neobvyklých požadavků jiným kanálem, MFA, správci hesel, filtrováním e-mailů, ochranou DNS, omezením oprávnění, simulacemi phishingu, jasnými procesy pro platby a incidenty a kulturou, ve které uživatelé podezřelé situace hlásí.

</details>

---

## Rychlý test - hlavní výstupy studia

### 1. Jaký je rozdíl mezi hrozbou, zranitelností a rizikem?

<details>
<summary>Odpověď</summary>

Hrozba je potenciální příčina incidentu, například útočník, malware nebo výpadek elektřiny. Zranitelnost je slabé místo, které může hrozba využít, například neopravená chyba nebo slabé heslo. Riziko je možnost, že hrozba využije zranitelnost a způsobí dopad na aktivum.

</details>

### 2. Proč se v TLS používá kombinace asymetrické a symetrické kryptografie?

<details>
<summary>Odpověď</summary>

Asymetrická kryptografie se používá pro ověření identity a bezpečné ustavení tajemství. Symetrická kryptografie se pak používá pro samotný přenos dat, protože je mnohem rychlejší.

</details>

### 3. Proč hash není šifrování?

<details>
<summary>Odpověď</summary>

Hash je jednosměrný otisk dat. Z hashe se běžně nedá získat původní zpráva, zatímco šifrování je vratné pomocí klíče. Hash slouží hlavně pro integritu, podpisy a bezpečné ukládání hesel.

</details>

### 4. Co znamená AAA?

<details>
<summary>Odpověď</summary>

AAA znamená Authentication, Authorization, Accounting/Auditing. Authentication ověřuje identitu, Authorization určuje oprávnění a Accounting/Auditing zaznamenává činnost pro kontrolu a dohledatelnost.

</details>

### 5. Proč MFA snižuje riziko kompromitace účtu?

<details>
<summary>Odpověď</summary>

Protože útočníkovi nestačí znát heslo. Musí získat i další faktor, například telefon, token, biometrický údaj nebo potvrzení v aplikaci.

</details>

### 6. Jaký je rozdíl mezi monitoringem a logováním?

<details>
<summary>Odpověď</summary>

Monitoring sleduje aktuální stav a metriky systému, například dostupnost, CPU nebo latenci. Logování ukládá záznamy událostí, ze kterých lze zpětně zjistit, co se stalo, kdy a proč.

</details>

### 7. Co je syslog?

<details>
<summary>Odpověď</summary>

Syslog je běžný protokol a formát pro posílání a ukládání textových logů. Používá se hlavně v unixových systémech a síťových zařízeních, často pro centralizované logování.

</details>

### 8. Jaká je minimální sada opatření pro server?

<details>
<summary>Odpověď</summary>

Role a oprávnění, silná autentizace, aktualizace, auditování, logování, zálohy, test obnovy, šifrování citlivých dat a omezení síťové dostupnosti jen na nutné služby.

</details>

### 9. Jaký je rozdíl mezi firewallem, IDS a IPS?

<details>
<summary>Odpověď</summary>

Firewall filtruje provoz podle pravidel. IDS provoz detekuje a upozorňuje na podezřelé chování, ale typicky neblokuje. IPS je inline a podezřelý provoz umí aktivně blokovat.

</details>

### 10. Kdy použít VPN?

<details>
<summary>Odpověď</summary>

VPN se používá pro bezpečné propojení přes nedůvěryhodnou síť, typicky internet. Remote-access VPN slouží pro vzdálené uživatele, site-to-site VPN pro propojení poboček.

</details>

### 11. Co dělá SOC a co CSIRT/CERT?

<details>
<summary>Odpověď</summary>

SOC průběžně monitoruje bezpečnostní události, logy a alerty. CSIRT/CERT řeší incidenty, koordinuje reakci, pomáhá s obnovou a může koordinovat zveřejňování zranitelností.

</details>

### 12. Proč se v kyberbezpečnosti řeší legislativa?

<details>
<summary>Odpověď</summary>

Protože organizace nemají jen technické povinnosti. Musí splnit právní požadavky, například ochranu osobních údajů podle GDPR, povinnosti podle zákona o kybernetické bezpečnosti a požadavky NIS2.

</details>

---

## 01 - Obecné principy bezpečnosti

### 1. Jaké jsou 3 vrstvy kybernetického prostoru a co každá z nich obsahuje?

<details>
<summary>Odpověď</summary>

Fyzická vrstva zahrnuje servery, kabely, datová centra a síťové prvky. Logická vrstva zahrnuje IP adresy, směrování a logické vazby. Sociální vrstva zahrnuje uživatele, identity, e-maily, telefonní čísla a další vazby osob v síti.

</details>

### 2. Jak je definována kybernetická bezpečnost?

<details>
<summary>Odpověď</summary>

Je to souhrn právních, organizačních, technických a vzdělávacích opatření pro ochranu ICT, aplikací, dat a uživatelů. Zároveň jde o schopnost systémů reagovat na hrozby, útoky a jejich následky.

</details>

### 3. Co je aktivum, hrozba, zranitelnost a riziko? Jak se riziko vypočítá?

<details>
<summary>Odpověď</summary>

Aktivum je něco hodnotného pro organizaci. Hrozba je možná příčina škody. Zranitelnost je slabé místo. Riziko vyjadřuje možnost škody a počítá se zjednodušeně jako `R = T × A × V`, tedy hrozba krát hodnota aktiva krát zranitelnost.

</details>

### 4. Jaký je rozdíl mezi primárními a podpůrnými aktivy?

<details>
<summary>Odpověď</summary>

Primární aktiva jsou hlavní informace, služby a znalosti, které organizace potřebuje. Podpůrná aktiva jsou prostředky, které primární aktiva umožňují používat, například hardware, software, sítě, lidé a prostory.

</details>

### 5. Jaké atributy aktiva je třeba evidovat?

<details>
<summary>Odpověď</summary>

Název, vlastník, hodnota, důvěrnost, integrita, dostupnost, závislosti, umístění, odpovědnosti, zranitelnosti a vazby na procesy nebo služby.

</details>

### 6. Co znamená CIA triáda?

<details>
<summary>Odpověď</summary>

CIA znamená Confidentiality, Integrity, Availability. Důvěrnost chrání před neoprávněným přístupem, integrita před neoprávněnou změnou a dostupnost zajišťuje, že systém nebo data jsou k dispozici v době potřeby.

</details>

### 7. Jak se hodnotí úrovně důvěrnosti?

<details>
<summary>Odpověď</summary>

Úrovně se typicky dělí na nízkou, střední, vysokou a kritickou. Čím vyšší úroveň, tím závažnější dopad má únik informací a tím silnější opatření jsou potřeba, například řízení přístupů, šifrování nebo zvláštní ochranné režimy.

</details>

### 8. Jaký je rozdíl mezi integritou dat a integritou systému?

<details>
<summary>Odpověď</summary>

Integrita dat znamená, že data nebyla neoprávněně změněna. Integrita systému znamená, že systém běží v očekávaném a důvěryhodném stavu, bez neoprávněných změn konfigurace nebo funkcí.

</details>

### 9. Jak se hodnotí úrovně dostupnosti?

<details>
<summary>Odpověď</summary>

Podle toho, jak dlouhý výpadek je přijatelný. Nízká dostupnost snese delší obnovu, střední typicky pracovní den, vysoká jen hodiny a kritická často jen minuty nebo žádný významný výpadek.

</details>

### 10. Popište státní a komerční klasifikaci informací.

<details>
<summary>Odpověď</summary>

Státní klasifikace používá stupně podle zákona, například vyhrazené, důvěrné, tajné a přísně tajné. Komerční klasifikace používá interní úrovně typu veřejné, citlivé, interní a chráněné podle dopadu na organizaci.

</details>

### 11. Co je Traffic Light Protocol?

<details>
<summary>Odpověď</summary>

TLP určuje, jak lze sdílet informace. Červená je jen pro konkrétní příjemce, žlutá omezeně v organizaci, zelená v komunitě a bílá bez omezení.

</details>

### 12. Kdo jsou lidé v kontextu prvků kybernetické bezpečnosti?

<details>
<summary>Odpověď</summary>

Jsou to tvůrci bezpečnosti, příjemci pravidel, chráněné subjekty, osoby, které je třeba informovat a školit, a také potenciální zdroj rizika nebo hrozby.

</details>

### 13. Vyjmenujte alespoň 8 procesů kybernetické bezpečnosti.

<details>
<summary>Odpověď</summary>

Řízení aktiv, řízení rizik, správa identit a rolí, autentizace, autorizace, aktualizace, testování zabezpečení, audit, monitoring, detekce anomálií, reakce na incidenty, školení a kontinuita.

</details>

### 14. Popište životní cyklus kybernetické bezpečnosti.

<details>
<summary>Odpověď</summary>

Základní fáze jsou prevence, detekce a reakce. Prevence snižuje pravděpodobnost incidentu, detekce ho odhaluje a reakce řeší dopady, obnovu a poučení.

</details>

### 15. Co je bezpečnostní politika a rozdíl mezi Policy, Standard, Procedure, Guideline a Baseline?

<details>
<summary>Odpověď</summary>

Policy říká, proč a jaký záměr vedení sleduje. Standard říká, co musí být splněno. Procedure popisuje konkrétní postup. Guideline je doporučení. Baseline je minimální bezpečnostní úroveň pro systémy.

</details>

### 16. Popište PDCA cyklus.

<details>
<summary>Odpověď</summary>

Plan znamená plánování opatření, Do jejich implementaci a provoz, Check kontrolu a hodnocení, Act udržování a zlepšování podle zjištění.

</details>

### 17. Vyjmenujte 7 standardních kroků řešení bezpečnosti.

<details>
<summary>Odpověď</summary>

Studie aktuálního stavu, riziková analýza, tvorba bezpečnostní politiky, bezpečnostní standardy, bezpečnostní projekt, implementace a nakonec monitoring/audit.

</details>

### 18. Popište 7 kroků analýzy rizik.

<details>
<summary>Odpověď</summary>

Identifikace aktiv, identifikace hrozeb, určení zranitelností, výpočet rizika, stanovení přijatelných a nepřijatelných rizik, návrh opatření a vyhodnocení ekonomického dopadu.

</details>

### 19. Jak funguje vzorec `R = T × A × V`?

<details>
<summary>Odpověď</summary>

Riziko roste s pravděpodobností hrozby, hodnotou aktiva a mírou zranitelnosti. Například důležitá databáze se známou zranitelností a častou hrozbou bude mít vysoké riziko.

</details>

### 20. Rozdíl mezi fyzickými, technickými a organizačními opatřeními.

<details>
<summary>Odpověď</summary>

Fyzická opatření jsou zámky, ostraha nebo serverovna. Technická opatření jsou firewall, šifrování, IDS nebo zálohování. Organizační opatření jsou politiky, procesy, školení a odpovědnosti.

</details>

---

## 02 - Data and server protection

### 1. Jaká jsou hlavní rizika pro operační systém a jaká protiopatření se používají?

<details>
<summary>Odpověď</summary>

Rizikem jsou škodliví nebo chybující uživatelé, malware a zneužití služeb. Protiopatření jsou autentizace, řízení přístupu, firewall, IDS/IPS, hardening, auditování, zálohy a šifrování.

</details>

### 2. Co znamená OS hardening?

<details>
<summary>Odpověď</summary>

Hardening je zpřísnění konfigurace systému. Patří sem vypnutí zbytečných služeb, aktualizace, firewall, silná hesla, omezení administrátorských práv, auditování a bezpečná konfigurace síťových služeb.

</details>

### 3. Rozdíl mezi administrátorem a běžným uživatelem. Jak funguje `sudo`?

<details>
<summary>Odpověď</summary>

Administrátor má plná oprávnění, běžný uživatel omezená. `sudo` umožní vybranému uživateli spustit konkrétní příkaz s vyššími právy, obvykle po ověření heslem a se záznamem do logu.

</details>

### 4. Proč nestačí spoléhat pouze na heslo?

<details>
<summary>Odpověď</summary>

Heslo může být slabé, uhádnuté, odcizené phishingem nebo uniklé. Alternativy jsou MFA, SSH klíče, certifikáty, biometrie, hardwarové tokeny a SSO s centrální správou identit.

</details>

### 5. Rozdíl mezi POSIX oprávněními a ACL.

<details>
<summary>Odpověď</summary>

POSIX oprávnění pracují se třemi kategoriemi: vlastník, skupina, ostatní, a právy read/write/execute. ACL umožňuje jemnější oprávnění pro více konkrétních uživatelů a skupin. Windows ACL jsou typicky detailnější než základní Unix POSIX model.

</details>

### 6. Co je auditování a čím se audit logy liší od běžných logů?

<details>
<summary>Odpověď</summary>

Auditování zaznamenává bezpečnostně významné události pro dohledatelnost. Audit log má obsahovat kdo, co, kdy, kde, výsledek operace a ideálně zdroj. Běžný log může být jen provozní nebo diagnostický.

</details>

### 7. Co znamenají RPO a RTO?

<details>
<summary>Odpověď</summary>

RPO určuje maximální přijatelnou ztrátu dat v čase. RTO určuje maximální přijatelnou dobu obnovy služby. Společně ovlivňují frekvenci záloh a požadavky na obnovu.

</details>

### 8. Co je pravidlo 3-2-1-0?

<details>
<summary>Odpověď</summary>

Mít 3 kopie dat, na 2 různých typech médií, 1 kopii mimo lokalitu a 0 chyb ověřených testem obnovy. Trvale připojené zálohy jsou rizikové, protože je může zašifrovat ransomware.

</details>

### 9. Proč jsou zálohy zranitelné a kde se doporučuje šifrování celého disku?

<details>
<summary>Odpověď</summary>

Zálohy obsahují citlivá data a často jsou méně chráněné než produkce. Full-disk šifrování se doporučuje hlavně pro notebooky, mobilní zařízení, externí disky a přenosná média.

</details>

### 10. Jak funguje šifrování disku on-the-fly?

<details>
<summary>Odpověď</summary>

Data se šifrují při zápisu a dešifrují při čtení bez ručního zásahu uživatele. Nástroje jsou například BitLocker, FileVault, LUKS nebo VeraCrypt.

</details>

### 11. Proč se full-disk šifrování používá častěji u mobilních zařízení než u serverů?

<details>
<summary>Odpověď</summary>

Mobilní zařízení se snáze ztratí nebo ukradnou. Servery jsou obvykle ve fyzicky chráněném prostředí a šifrování může komplikovat restart, výkon a dostupnost.

</details>

---

## 03 - Kryptografie

### 1. Co znamená `x mod n` a jak souvisí s kongruencí?

<details>
<summary>Odpověď</summary>

`x mod n` je zbytek po dělení čísla `x` číslem `n`. Kongruence `a ≡ b (mod n)` znamená, že `a` a `b` dávají po dělení `n` stejný zbytek.

</details>

### 2. Kdy existuje multiplikativní inverze modulo `n`?

<details>
<summary>Odpověď</summary>

Inverze čísla `a` modulo `n` existuje právě tehdy, když `a` a `n` jsou nesoudělná, tedy `gcd(a, n) = 1`.

</details>

### 3. Jak funguje Eukleidův a rozšířený Eukleidův algoritmus?

<details>
<summary>Odpověď</summary>

Eukleidův algoritmus hledá největšího společného dělitele opakovaným dělením se zbytkem. Rozšířený Eukleidův algoritmus navíc najde koeficienty, ze kterých lze získat modulární inverzi.

</details>

### 4. Co říká malá Fermatova věta?

<details>
<summary>Odpověď</summary>

Pro prvočíslo `p` a číslo `a`, které není dělitelné `p`, platí `a^(p-1) ≡ 1 (mod p)`. Používá se v modulární aritmetice a kryptografii.

</details>

### 5. Jak funguje XOR a proč je vhodný pro jednoduchou symetrickou šifru?

<details>
<summary>Odpověď</summary>

XOR vrací 1, pokud jsou bity různé. Platí, že opakovaný XOR stejným klíčem obnoví původní data, takže stejná operace může šifrovat i dešifrovat.

</details>

### 6. Co je Kerckhoffsův princip?

<details>
<summary>Odpověď</summary>

Bezpečnost šifry nemá záviset na utajení algoritmu, ale na utajení klíče. I když útočník zná algoritmus, bez klíče nemá být schopen zprávu přečíst.

</details>

### 7. Rozdíl mezi kryptografií a kryptoanalýzou.

<details>
<summary>Odpověď</summary>

Kryptografie navrhuje metody pro ochranu informací. Kryptoanalýza zkoumá, jak tyto metody prolomit nebo ověřit jejich bezpečnost.

</details>

### 8. Jaké jsou základní operace šifrování?

<details>
<summary>Odpověď</summary>

Substituce nahrazuje symboly jinými symboly, transpozice mění jejich pořadí, kombinované metody používají obojí.

</details>

### 9. Vysvětli Caesarovu šifru.

<details>
<summary>Odpověď</summary>

Caesarova šifra posouvá každé písmeno o pevný počet pozic. Je snadno prolomitelná, protože existuje málo možných posunů a zachovává statistiku jazyka.

</details>

### 10. Rozdíl mezi transpoziční a substituční šifrou.

<details>
<summary>Odpověď</summary>

Transpoziční šifra mění pořadí znaků. Substituční šifra nahrazuje znaky jinými znaky podle pravidla.

</details>

### 11. Co je frekvenční analýza?

<details>
<summary>Odpověď</summary>

Je to útok využívající četnost písmen v jazyce. Ohrožuje monoalfabetické substituce, protože stejný znak se vždy nahrazuje stejným znakem.

</details>

### 12. Co je Vigenèrova šifra?

<details>
<summary>Odpověď</summary>

Polyalphabetická substituční šifra, která používá opakovaný klíč pro různé posuny znaků. Je silnější než Caesarova šifra, ale při krátkém nebo opakovaném klíči je prolomitelná.

</details>

### 13. Jak funguje Playfairova šifra?

<details>
<summary>Odpověď</summary>

Šifruje dvojice písmen pomocí tabulky 5 × 5. Pravidla závisí na tom, zda jsou písmena ve stejném řádku, sloupci nebo tvoří obdélník.

</details>

### 14. Proč byla Enigma silnější a jaké chyby pomáhaly kryptoanalýze?

<details>
<summary>Odpověď</summary>

Enigma používala rotory a měnila substituci po každém znaku. K prolomení pomáhaly provozní chyby, opakování postupů, předvídatelné texty a špatná disciplína obsluhy.

</details>

### 15. Rozdíl mezi blokovým a proudovým šifrováním.

<details>
<summary>Odpověď</summary>

Bloková šifra šifruje data po blocích pevné délky. Proudová šifra vytváří proud klíče, který se kombinuje s daty po bitech nebo bajtech.

</details>

### 16. Rozdíl mezi symetrickou, asymetrickou a hybridní kryptografií.

<details>
<summary>Odpověď</summary>

Symetrická používá jeden sdílený klíč. Asymetrická používá veřejný a soukromý klíč. Hybridní kombinuje obě: asymetricky se domluví klíč a symetricky se šifrují data.

</details>

### 17. Proč je jednorázové heslo teoreticky neprolomitelné a nepraktické?

<details>
<summary>Odpověď</summary>

One-time pad je neprolomitelný, pokud je klíč opravdu náhodný, stejně dlouhý jako zpráva, použit jen jednou a utajen. Je nepraktický kvůli distribuci a správě obrovských klíčů.

</details>

---

## 04a - Symetrická kryptografie

### 1. Rozdíl mezi blokovou a proudovou symetrickou šifrou.

<details>
<summary>Odpověď</summary>

Bloková šifra zpracovává bloky pevné velikosti. Proudová šifra generuje proud klíče a kombinuje ho s daty průběžně, typicky XORem.

</details>

### 2. Rozdíl mezi ECB a CBC.

<details>
<summary>Odpověď</summary>

ECB šifruje každý blok samostatně, takže stejné bloky dávají stejné ciphertexty. CBC před šifrováním XORuje blok s předchozím ciphertextem, takže skrývá opakování.

</details>

### 3. Proč je ECB málo bezpečný?

<details>
<summary>Odpověď</summary>

Protože zachovává vzory v datech. Stejné bloky otevřeného textu vytvářejí stejné bloky šifrovaného textu.

</details>

### 4. Co je inicializační vektor a proč je potřeba v CBC?

<details>
<summary>Odpověď</summary>

Inicializační vektor je počáteční hodnota pro první blok CBC. Zajišťuje, že stejná zpráva se stejným klíčem nemusí dát stejný ciphertext.

</details>

### 5. Rozdíl mezi CFB a OFB.

<details>
<summary>Odpověď</summary>

CFB zpětně používá předchozí ciphertext, OFB generuje proud z opakovaného šifrování interního stavu. OFB se chová víc jako proudová šifra a chyby se šíří jinak.

</details>

### 6. Co je MAC?

<details>
<summary>Odpověď</summary>

MAC je autentizační kód zprávy vytvořený pomocí tajného klíče. Ověřuje integritu a autenticitu zprávy, dá se chápat jako hash funkce s klíčem.

</details>

### 7. Hlavní parametry DES.

<details>
<summary>Odpověď</summary>

DES je bloková šifra s blokem 64 bitů, efektivním klíčem 56 bitů a Feistelovou strukturou s 16 rundami.

</details>

### 8. Proč je DES zastaralý?

<details>
<summary>Odpověď</summary>

Kvůli krátkému 56bitovému klíči, který je dnes možné prohledat hrubou silou.

</details>

### 9. Jak funguje 3DES?

<details>
<summary>Odpověď</summary>

3DES aplikuje DES třikrát, obvykle v režimu šifrování-dešifrování-šifrování s více klíči. Zvyšuje bezpečnost, ale je pomalý a dnes nahrazovaný AES.

</details>

### 10. Jak funguje Feistelova síť?

<details>
<summary>Odpověď</summary>

Blok se rozdělí na dvě poloviny. V každé rundě se jedna polovina transformuje funkcí s klíčem a kombinuje s druhou. Výhoda je, že stejná struktura umožňuje šifrování i dešifrování.

</details>

### 11. Příklady dalších symetrických algoritmů.

<details>
<summary>Odpověď</summary>

AES, Blowfish, Twofish, IDEA, RC4, ChaCha20 a další.

</details>

### 12. Co řeší Diffie-Hellmanův protokol?

<details>
<summary>Odpověď</summary>

Umožňuje dvěma stranám dohodnout společné tajemství přes nezabezpečený kanál, aniž by si tajný klíč předem předaly.

</details>

### 13. Proč Diffie-Hellman potřebuje autentizaci?

<details>
<summary>Odpověď</summary>

Bez autentizace je zranitelný vůči man-in-the-middle útoku. Strany sice vytvoří klíč, ale nemají jistotu, s kým ho vytvořily.

</details>

### 14. Jak funguje MITM útok na Diffie-Hellman?

<details>
<summary>Odpověď</summary>

Útočník se vloží mezi Alice a Boba, vytvoří jeden klíč s Alicí a druhý s Bobem. Pak zprávy dešifruje, čte nebo mění a znovu šifruje dál.

</details>

---

## 04b - Asymetrická kryptografie, hash a podpis

### 1. Rozdíl mezi veřejným a soukromým klíčem.

<details>
<summary>Odpověď</summary>

Veřejný klíč se smí zveřejnit a používá se pro šifrování pro vlastníka nebo ověření podpisu. Soukromý klíč musí zůstat tajný a používá se pro dešifrování nebo tvorbu podpisu.

</details>

### 2. Proč musí být kanál pro veřejný klíč autentizovaný?

<details>
<summary>Odpověď</summary>

Protože útočník by mohl podstrčit svůj veřejný klíč místo klíče skutečné osoby. Důvěrnost kanálu není nutná, ale autenticita ano.

</details>

### 3. Jak se generují klíče RSA?

<details>
<summary>Odpověď</summary>

Zvolí se velká prvočísla `p` a `q`, spočítá se `n = p × q` a Eulerova funkce. Zvolí se veřejný exponent `e` a dopočítá soukromý exponent `d` jako inverze modulo `φ(n)`.

</details>

### 4. Jak funguje RSA šifrování a dešifrování?

<details>
<summary>Odpověď</summary>

Šifrování používá veřejný klíč `(e, n)` a počítá `c = m^e mod n`. Dešifrování používá soukromý klíč `(d, n)` a počítá `m = c^d mod n`.

</details>

### 5. Proč je RSA bezpečné jen s velkými prvočísly?

<details>
<summary>Odpověď</summary>

Bezpečnost závisí na obtížnosti faktorizace `n` na `p` a `q`. U malých čísel je faktorizace snadná a lze dopočítat soukromý klíč.

</details>

### 6. Jak rozšířený Eukleidův algoritmus pomáhá určit soukromý exponent?

<details>
<summary>Odpověď</summary>

Najde multiplikativní inverzi `e` modulo `φ(n)`, tedy číslo `d`, pro které platí `e × d ≡ 1 mod φ(n)`.

</details>

### 7. Co zajišťuje digitální podpis?

<details>
<summary>Odpověď</summary>

Autenticitu autora, integritu dokumentu a nepopiratelnost. Nezajišťuje důvěrnost obsahu.

</details>

### 8. Proč digitální podpis nezajišťuje důvěrnost?

<details>
<summary>Odpověď</summary>

Protože podpis nešifruje zprávu pro skrytí obsahu. Kdokoliv může zprávu číst, ale může ověřit, zda ji podepsal držitel soukromého klíče a zda nebyla změněna.

</details>

### 9. Proč se podepisuje hash zprávy?

<details>
<summary>Odpověď</summary>

Je efektivnější podepsat krátký digest než celou zprávu. Hash zároveň svazuje podpis s obsahem; změna zprávy změní hash.

</details>

### 10. Vlastnosti bezpečné hash funkce.

<details>
<summary>Odpověď</summary>

Determinismus, pevná délka výstupu, jednosměrnost, odolnost vůči nalezení druhého vstupu a odolnost vůči kolizím.

</details>

### 11. Proč jsou MD5 a SHA-1 problematické?

<details>
<summary>Odpověď</summary>

Mají známé slabiny a kolizní útoky. Nejsou vhodné pro nové bezpečnostní použití, hlavně podpisy a ochranu hesel.

</details>

### 12. Rozdíl mezi CA a RA.

<details>
<summary>Odpověď</summary>

CA vydává a podepisuje certifikáty. RA ověřuje identitu žadatele a předává ověřené požadavky certifikační autoritě.

</details>

### 13. Co obsahuje certifikát veřejného klíče?

<details>
<summary>Odpověď</summary>

Identitu vlastníka, veřejný klíč, informace o vydavateli, dobu platnosti, sériové číslo, použité algoritmy a digitální podpis CA.

</details>

### 14. Co je PKI?

<details>
<summary>Odpověď</summary>

PKI je infrastruktura veřejného klíče pro vydávání, správu, ověřování a odvolávání certifikátů. Umožňuje důvěřovat veřejným klíčům ve větším měřítku.

</details>

### 15. Co je TTP a jaké má režimy?

<details>
<summary>Odpověď</summary>

Trusted Third Party je důvěryhodná třetí strana, které věří účastníci transakce. Může být on-line, tedy dostupná během transakce, nebo off-line, kdy se používá mimo přímý průběh transakce.

</details>

### 16. Co znamená ikona zámku u webové stránky?

<details>
<summary>Odpověď</summary>

Znamená, že spojení používá HTTPS/TLS a certifikát prošel kontrolou prohlížeče. Neznamená to automaticky, že web je poctivý nebo bezpečný obsahově.

</details>

---

## 04c - SSL/TLS

### 1. Co znamenají zkratky SSL a TLS?

<details>
<summary>Odpověď</summary>

SSL je Secure Sockets Layer, TLS je Transport Layer Security. TLS je nástupce SSL a používá se pro zabezpečení komunikace, typicky HTTPS.

</details>

### 2. Jaké tři bezpečnostní vlastnosti SSL/TLS poskytuje?

<details>
<summary>Odpověď</summary>

Autentizaci stran, integritu přenášených dat a důvěrnost komunikace.

</details>

### 3. K čemu slouží SSL/TLS certifikát?

<details>
<summary>Odpověď</summary>

Ověřuje identitu serveru, obsahuje veřejný klíč a umožňuje klientovi bezpečně navázat šifrované spojení.

</details>

### 4. Kde je SSL/TLS umístěn vzhledem k aplikační vrstvě a TCP?

<details>
<summary>Odpověď</summary>

TLS běží nad TCP a pod aplikačním protokolem, například HTTP. HTTPS je HTTP komunikující přes TLS.

</details>

### 5. Co je `PreMasterSecret`?

<details>
<summary>Odpověď</summary>

Je to tajemství použité při odvození klíčů relace ve starších TLS postupech. Klient ho zašifruje veřejným klíčem serveru a obě strany z něj odvodí symetrické klíče.

</details>

### 6. Jaké klíče vznikají v SSL/TLS key bloku?

<details>
<summary>Odpověď</summary>

Vznikají symetrické klíče pro šifrování, klíče pro MAC/integritu a inicializační hodnoty podle použité šifrovací sady.

</details>

### 7. Jak zjednodušeně probíhá SSL/TLS handshake?

<details>
<summary>Odpověď</summary>

Klient se připojí, server pošle certifikát, klient certifikát ověří, strany dohodnou parametry a klíče a poté komunikují symetricky šifrovaně.

</details>

### 8. Co znamená zámek v prohlížeči?

<details>
<summary>Odpověď</summary>

Znamená šifrované spojení a platný certifikát pro danou doménu. Nezaručuje, že stránka není podvodná.

</details>

### 9. Rozdíl mezi DV, OV a EV certifikátem.

<details>
<summary>Odpověď</summary>

DV ověřuje doménu. OV ověřuje doménu i základní informace o organizaci. EV historicky ověřoval organizaci nejpřísněji, ale dnešní prohlížeče jeho viditelné zvýraznění omezily.

</details>

### 10. Proč SSL/TLS kombinuje asymetrickou a symetrickou kryptografii?

<details>
<summary>Odpověď</summary>

Asymetrická část řeší identitu a bezpečné ustavení tajemství. Symetrická část je rychlá a vhodná pro přenos velkého objemu dat.

</details>

---

## 05 - Legislativa

### 1. Proč byla přijata NIS2 a co mění oproti NIS?

<details>
<summary>Odpověď</summary>

NIS2 reaguje na rostoucí závislost společnosti na digitálních službách. Rozšiřuje okruh regulovaných subjektů, zpřísňuje povinnosti, posiluje dohled, zvyšuje sankce a zdůrazňuje odpovědnost vedení.

</details>

### 2. Co je poskytovatel regulované služby?

<details>
<summary>Odpověď</summary>

Organizace, která poskytuje službu spadající pod regulaci kybernetické bezpečnosti a splňuje stanovená kritéria podle typu služby, velikosti nebo zvláštní důležitosti.

</details>

### 3. Jaké dvě podmínky musí organizace typicky splnit?

<details>
<summary>Odpověď</summary>

Musí poskytovat regulovanou službu a zároveň být středním nebo velkým podnikem, případně spadat do zvláštní kategorie bez ohledu na velikost.

</details>

### 4. Které subjekty mohou spadat pod regulaci bez ohledu na velikost?

<details>
<summary>Odpověď</summary>

Například poskytovatelé elektronických komunikací, DNS služeb a služeb vytvářejících důvěru.

</details>

### 5. Rozdíl mezi základními a důležitými subjekty.

<details>
<summary>Odpověď</summary>

Základní subjekty jsou kritičtější a mají přísnější povinnosti i ex-ante dohled. Důležité subjekty mají mírnější režim a typicky ex-post kontrolu.

</details>

### 6. Co je ex-ante a ex-post kontrola?

<details>
<summary>Odpověď</summary>

Ex-ante kontrola probíhá předem nebo průběžně u kritičtějších subjektů. Ex-post kontrola nastává zpětně, například po incidentu nebo na základě zjištění.

</details>

### 7. Jaké oblasti musí pokrývat řízení rizik?

<details>
<summary>Odpověď</summary>

Analýzu rizik, bezpečnostní politiku, incident management, kontinuitu provozu, krizové řízení, dodavatelský řetězec, bezpečný vývoj a údržbu, testování, audit a kryptografii.

</details>

### 8. Proč je důležitá přímá odpovědnost statutárních orgánů?

<details>
<summary>Odpověď</summary>

Kyberbezpečnost není jen problém IT. Vedení musí zajistit zdroje, odpovědnosti, dohled a dodržování opatření, jinak může nést odpovědnost za selhání.

</details>

### 9. Co patří mezi nižší povinnosti?

<details>
<summary>Odpověď</summary>

Minimální úroveň kybernetické bezpečnosti, povinnosti vedení, řízení rizik, HR bezpečnost, kontinuita, řízení přístupu, identity, detekce událostí, incidenty, síťová a aplikační bezpečnost.

</details>

### 10. Co patří mezi vyšší organizační a technická opatření?

<details>
<summary>Odpověď</summary>

Organizačně ISMS, role, dokumentace, řízení aktiv, rizik, dodavatelů, změn, incidentů, kontinuity a audit. Technicky fyzická bezpečnost, sítě, identity, přístupy, detekce, logování, aplikace, kryptografie a dostupnost.

</details>

---

## 05 - Monitoring

### 1. Proč běh procesu nestačí jako důkaz dostupnosti služby?

<details>
<summary>Odpověď</summary>

Proces může běžet, ale služba nemusí odpovídat, může být blokovaná firewallem, mít nedostupnou databázi nebo vracet chyby. Je potřeba ověřovat dostupnost z pohledu uživatele.

</details>

### 2. Jak se liší lokální a vzdálené metriky?

<details>
<summary>Odpověď</summary>

Lokální metriky sledují stav na systému, například CPU, RAM, disk nebo proces. Vzdálené metriky sledují dostupnost a kvalitu služby ze sítě, například ping, port, latenci nebo propustnost.

</details>

### 3. Rozdíl mezi latencí a propustností.

<details>
<summary>Odpověď</summary>

Latence je doba odezvy. Propustnost je objem dat přenesený za čas. Služba může mít nízkou latenci, ale malou propustnost, nebo opačně.

</details>

### 4. Proč je důležitá časová synchronizace?

<details>
<summary>Odpověď</summary>

Bez synchronizovaného času nejde spolehlivě korelovat logy a metriky z více systémů. Není pak jasné, co bylo příčinou a co následkem.

</details>

### 5. Výhody a nevýhody Syslogu a Windows Event Logu.

<details>
<summary>Odpověď</summary>

Syslog je běžný, jednoduchý a interoperabilní, hlavně v Unixu a síťových zařízeních. Windows Event Log je dobře integrovaný ve Windows, ale hůře interoperabilní mimo Windows prostředí.

</details>

### 6. Architektura SNMP manager/agent.

<details>
<summary>Odpověď</summary>

Agent běží na monitorovaném zařízení a poskytuje hodnoty. Manager sbírá data, posílá dotazy Get/Set a přijímá Response nebo Trap zprávy.

</details>

### 7. Jaké porty SNMP používá?

<details>
<summary>Odpověď</summary>

Agent používá UDP port 161. Trapy se posílají na UDP port 162.

</details>

### 8. Co je MIB a OID?

<details>
<summary>Odpověď</summary>

MIB je databáze proměnných dostupných přes SNMP. OID je jednoznačný identifikátor objektu v hierarchické struktuře.

</details>

### 9. Co je flow v NetFlow?

<details>
<summary>Odpověď</summary>

Flow je skupina paketů se stejnou zdrojovou a cílovou IP adresou, porty a protokolem. NetFlow místo paketů ukládá souhrny toků.

</details>

### 10. Rozdíl mezi NetFlow, IPFIX, sFlow a J-Flow.

<details>
<summary>Odpověď</summary>

NetFlow je Cisco protokol. IPFIX je standardizovaná varianta. sFlow používá vzorkování paketů. J-Flow je varianta od Juniperu.

</details>

### 11. K čemu slouží RMON a SMON?

<details>
<summary>Odpověď</summary>

RMON rozšiřuje monitoring fyzické a linkové vrstvy pomocí MIB a SNMP. SMON rozšiřuje RMON pro přepínané sítě.

</details>

### 12. Proč je LLDP vhodnější než CDP?

<details>
<summary>Odpověď</summary>

CDP je proprietární Cisco protokol. LLDP je standard IEEE 802.1AB a funguje napříč vendory, takže je vhodnější pro heterogenní infrastrukturu.

</details>

---

## 07 - PKI, dostupnost, DNS a CDN

### 1. Co je certifikát a proč nestačí jen sdílet veřejný klíč?

<details>
<summary>Odpověď</summary>

Certifikát svazuje veřejný klíč s identitou vlastníka a je podepsán CA. Samotný veřejný klíč bez certifikátu není důvěryhodný, protože nevíme, komu skutečně patří.

</details>

### 2. Rozdíl mezi symetrickou a asymetrickou kryptografií.

<details>
<summary>Odpověď</summary>

Symetrická kryptografie používá jeden sdílený klíč a je rychlá. Asymetrická používá veřejný a soukromý klíč, hodí se pro výměnu klíčů, certifikáty a podpisy.

</details>

### 3. Na čem je založen RSA a ECC?

<details>
<summary>Odpověď</summary>

RSA stojí na obtížnosti faktorizace velkých čísel. ECC stojí na problému diskrétního logaritmu na eliptických křivkách a dosahuje podobné bezpečnosti s kratšími klíči.

</details>

### 4. Tři hlavní funkce PKI a co je CRL.

<details>
<summary>Odpověď</summary>

PKI vydává certifikáty, ukládá a ověřuje certifikáty a řeší jejich odvolání. CRL je seznam odvolaných certifikátů, které už nemají být považovány za platné.

</details>

### 5. Průběh TLS handshake a rozdíl TLS 1.3.

<details>
<summary>Odpověď</summary>

Klient naváže spojení, pošle podporované metody, server vybere parametry a pošle certifikát, klient ho ověří a ustaví session key. TLS 1.3 používá modernější Diffie-Hellman výměnu a odstraňuje staré slabé režimy.

</details>

### 6. Vlastnosti digitálního podpisu a ověření.

<details>
<summary>Odpověď</summary>

Podpis zajišťuje autenticitu, integritu a nepopiratelnost. Ověření probíhá pomocí veřejného klíče z certifikátu a porovnání podpisu s hashem dokumentu.

</details>

### 7. Co znamená uptime ratio 99,999 %?

<details>
<summary>Odpověď</summary>

Znamená velmi vysokou dostupnost, tzv. five nines. Za rok připouští přibližně 52 minut a 30 sekund výpadku.

</details>

### 8. Co je SPoF a jak se eliminuje?

<details>
<summary>Odpověď</summary>

Single Point of Failure je komponenta, jejíž výpadek shodí službu. Eliminuje se redundancí, load balancingem, anycastem, záložním napájením, více servery nebo geografickým rozložením.

</details>

### 9. Jak funguje Anycast?

<details>
<summary>Odpověď</summary>

Více uzlů sdílí jednu anycast adresu a síť doručí paket nejbližšímu dostupnému uzlu. IPv4 typicky vyžaduje BGP, IPv6 má anycast podporu nativně.

</details>

### 10. Bezpečnostní problémy DNS a řešení.

<details>
<summary>Odpověď</summary>

DNS nemá původně autentizaci ani šifrování a běží často přes UDP. Hrozí spoofing a MITM. DNSSEC chrání autenticitu odpovědí mezi DNS servery, DoT a DoH šifrují DNS dotazy klientů.

</details>

---

## 10 - Endpoint protection

### 1. Co je endpoint a hlavní rizika?

<details>
<summary>Odpověď</summary>

Endpoint je klientské zařízení, například PC, notebook nebo mobil. Rizika jsou malware, červi, tiché vzdálené připojení útočníka, phishing a oklamání uživatele.

</details>

### 2. Metody detekce škodlivého kódu.

<details>
<summary>Odpověď</summary>

Signaturová detekce hledá známé vzory. Heuristika hledá podobné nebo podezřelé struktury. Real-time detekce sleduje chování procesu. Detekce manipulace s oprávněními chrání proti rootkitům.

</details>

### 3. Rozdíl mezi osobním a síťovým firewallem.

<details>
<summary>Odpověď</summary>

Osobní firewall chrání jedno zařízení. Síťový firewall chrání síť nebo segment. `DENY ANY` znamená, že vše je blokováno, pokud není výslovně povoleno.

</details>

### 4. Co je UEM a rozdíl proti MDM?

<details>
<summary>Odpověď</summary>

MDM spravuje hlavně mobilní zařízení. UEM rozšiřuje správu na různé typy zařízení, včetně PC, tabletů a mobilů, a řeší provisioning, software, monitoring, aktualizace a bezpečnostní konfigurace.

</details>

### 5. Co je BYOD?

<details>
<summary>Odpověď</summary>

Bring Your Own Device znamená, že uživatel používá vlastní zařízení pro firemní přístup. Vyžaduje MDM/UEM, oddělení osobních a firemních dat, možnost vzdáleného smazání a řízení přístupu.

</details>

### 6. Rozdíl mezi pre-admission a post-admission v NAC.

<details>
<summary>Odpověď</summary>

Pre-admission kontroluje zařízení před přístupem do sítě. Post-admission pustí zařízení s omezenými právy a plný přístup dá až po kontrole.

</details>

### 7. Jak funguje NAC architektura?

<details>
<summary>Odpověď</summary>

Klientský agent kontroluje stav zařízení. Server ověřuje splnění politik a může fungovat jako RADIUS. Po úspěšné kontrole lze změnit VLAN přes IEEE 802.1x.

</details>

### 8. Proč aktualizovat virovou databázi?

<details>
<summary>Odpověď</summary>

Signaturová detekce je účinná jen proti známým vzorům. Bez aktualizací antivirus nezná nové hrozby.

</details>

### 9. Typy pravidel ve Windows Firewallu.

<details>
<summary>Odpověď</summary>

Programová pravidla pro aplikace, portová pravidla pro TCP/UDP porty, předdefinovaná pravidla pro funkce Windows a vlastní pravidla.

</details>

### 10. Klíčové funkce MDM při ztrátě zařízení.

<details>
<summary>Odpověď</summary>

Lokalizace, uzamčení, vzdálené smazání firemních dat, vynucení šifrování, správa aplikací, oddělení firemního kontejneru a odebrání přístupů.

</details>

---

## 11 - Infrastructure protection

### 1. Proč je ARP zranitelný a jak funguje Gratuitous ARP útok?

<details>
<summary>Odpověď</summary>

ARP nemá autentizaci. Útočník může poslat falešnou vazbu IP-MAC, třeba že jeho MAC patří výchozí bráně. Oběť pak posílá provoz útočníkovi a vzniká MITM.

</details>

### 2. Co je Dynamic ARP Inspection?

<details>
<summary>Odpověď</summary>

DAI filtruje ARP pakety na switchi a ověřuje vazby IP-MAC proti důvěryhodné databázi, typicky z DHCP Snoopingu. Neplatné ARP odpovědi zahazuje.

</details>

### 3. Princip DHCP Snoopingu.

<details>
<summary>Odpověď</summary>

Switch rozlišuje trusted porty, odkud smí chodit DHCP odpovědi, a untrusted klientské porty. DHCP offer z nedůvěryhodného portu se zahodí.

</details>

### 4. Co je RA Guard?

<details>
<summary>Odpověď</summary>

RA Guard chrání IPv6 sítě před falešnými Router Advertisement zprávami. Podobá se DHCP Snoopingu, ale filtruje RA zprávy z portů, které nemají být routerové.

</details>

### 5. Rozdíl mezi stateless a stateful firewallem.

<details>
<summary>Odpověď</summary>

Stateless filtruje každý paket izolovaně. Stateful sleduje stav spojení a pozná, zda paket patří k již povolené komunikaci. Stateless neumí složitější politiky podle kontextu.

</details>

### 6. Co přidává NGFW?

<details>
<summary>Odpověď</summary>

NGFW přidává L7 inspekci, aplikační kontrolu, identitu uživatele, IPS, URL filtering, antimalware a často TLS inspekci, protože bez dešifrování nevidí obsah HTTPS.

</details>

### 7. Rozdíl mezi IDS a IPS.

<details>
<summary>Odpověď</summary>

IDS je pasivní detekce a alerting, typicky přes TAP/SPAN. IPS je inline a může provoz blokovat. IPS má vyšší dopad při false positive, protože může zastavit legitimní provoz.

</details>

### 8. Rozdíl mezi Web Proxy a WAF.

<details>
<summary>Odpověď</summary>

Web Proxy chrání klienty a kontroluje odchozí webový provoz. WAF chrání webové aplikace a kontroluje příchozí požadavky na server, například proti SQL injection nebo XSS.

</details>

### 9. IPSec VPN vs. SSL VPN.

<details>
<summary>Odpověď</summary>

IPSec funguje na L3 a hodí se hlavně pro site-to-site VPN. SSL/TLS VPN funguje výše a je vhodná pro remote-access uživatele, protože se snáze nasazuje.

</details>

### 10. Komponenty IPSec frameworku a rozdíl AH/ESP.

<details>
<summary>Odpověď</summary>

IPSec zahrnuje AH, ESP a IKE. AH poskytuje integritu a autentizaci, ale nešifruje. ESP poskytuje šifrování a může poskytovat i integritu a autentizaci, proto se používá častěji.

</details>

---

## 12 - Wireless

### 1. Co je IEEE 802.1x a jaké jsou role?

<details>
<summary>Odpověď</summary>

IEEE 802.1x je standard pro autentizaci přístupu k síti. Supplicant je klient, authenticator je switch nebo AP a authentication server je typicky RADIUS.

</details>

### 2. Rozdíl mezi WPA, WPA2 a WPA3.

<details>
<summary>Odpověď</summary>

WPA bylo dočasné řešení s TKIP. WPA2 implementuje 802.11i a AES. WPA3 nahrazuje PSK bezpečnějším SAE.

</details>

### 3. Rozdíl mezi WPA-PSK a WPA-Enterprise.

<details>
<summary>Odpověď</summary>

WPA-PSK používá sdílenou frázi a hodí se pro malé sítě. WPA-Enterprise používá 802.1x a RADIUS, takže je vhodný pro organizace.

</details>

### 4. Jak funguje PSK ve WPA2?

<details>
<summary>Odpověď</summary>

Sdílená fráze se společně se SSID použije jako vstup pro odvození 256bitového PSK. Z něj se odvozují klíče pro zařízení.

</details>

### 5. Co je WLC?

<details>
<summary>Odpověď</summary>

Wireless LAN Controller centrálně spravuje AP, SSID, bezpečnostní nastavení, kanály, měření signálu a detekci rogue AP.

</details>

### 6. Rozdíly mezi pásmy 2,4 GHz, 5 GHz a 6 GHz.

<details>
<summary>Odpověď</summary>

2,4 GHz má větší dosah, ale více rušení a překryv kanálů. 5 GHz má více kanálů a menší překryv. 6 GHz přidává další kapacitu, ale závisí na regulaci a podpoře zařízení.

</details>

### 7. Co je Rogue AP?

<details>
<summary>Odpověď</summary>

Rogue AP je přístupový bod mimo kontrolu správce. Může lákat klienty, odposlouchávat, rušit legitimní AP, obcházet síťovou politiku nebo způsobit DoS. WLC ho může detekovat a lokalizovat.

</details>

### 8. Technologie IoT krátkého a dlouhého dosahu.

<details>
<summary>Odpověď</summary>

Krátký dosah: Wi-Fi, Bluetooth, ZigBee, NFC, RFID, Z-Wave. Delší dosah: 5G, LTE, LoRaWAN, SigFox, NB-IoT, VSAT.

</details>

### 9. Proč nestačí dát IoT do separátní VLAN?

<details>
<summary>Odpověď</summary>

IoT zařízení často potřebují komunikovat do cloudu, takže izolace sama nestačí. Je potřeba měnit výchozí hesla, aktualizovat, omezit přístupy, sledovat provoz a oddělit je od citlivé LAN.

</details>

---

## 13 - Special tools

### 1. Co je honeypot a co může napodobovat?

<details>
<summary>Odpověď</summary>

Honeypot je návnada pro útočníky. Může napodobovat aplikační server, router, switch, firewall, DNS server nebo klientské zařízení.

</details>

### 2. Rozdíl mezi low-, medium- a high-interaction honeypoty.

<details>
<summary>Odpověď</summary>

Low-interaction emuluje jednu službu. Medium-interaction emuluje více služeb. High-interaction poskytuje téměř plný systém nebo VM, ale musí být dobře izolovaný.

</details>

### 3. Rozdíl mezi server honeypot a client honeypot.

<details>
<summary>Odpověď</summary>

Server honeypot pasivně čeká na útoky. Client honeypot aktivně vyhledává rizikové služby nebo weby a sleduje, zda ho napadnou.

</details>

### 4. Co je honeywall?

<details>
<summary>Odpověď</summary>

Specializovaný firewall oddělující honeypot od produkční sítě. Řídí, co může jít dovnitř a ven, aby honeypot neohrozil reálnou infrastrukturu.

</details>

### 5. Co je honeynet?

<details>
<summary>Odpověď</summary>

Více spolupracujících honeypotů. Působí věrohodněji než jeden systém a umožňuje sledovat složitější útoky a laterální pohyb.

</details>

### 6. Hlavní problémy honeypotu.

<details>
<summary>Odpověď</summary>

Přilákat relevantní provoz, přesvědčit útočníka, bezpečně izolovat prostředí, zabránit zneužití honeypotu k dalším útokům a analyzovat zachycená data.

</details>

### 7. Co je sandboxing?

<details>
<summary>Odpověď</summary>

Spouštění programu v izolovaném prostředí, kde nemůže ovlivnit zbytek systému. Používá se pro analýzu malwaru, zero-day hrozby a testování neznámých aplikací.

</details>

### 8. Výhoda serverové virtualizace.

<details>
<summary>Odpověď</summary>

Virtualizace umožňuje flexibilní správu, migraci VM mezi fyzickými servery, lepší využití zdrojů a snazší údržbu s menším výpadkem.

</details>

### 9. Problémy serverové virtualizace.

<details>
<summary>Odpověď</summary>

Správný odhad CPU, RAM a disku, zvládání špiček, plánování výpadků, potřeba více fyzických serverů pro HA a riziko špatného rozdělení zdrojů.

</details>

### 10. Rozdíl mezi VM a kontejnerem.

<details>
<summary>Odpověď</summary>

VM obsahuje celý operační systém nad hypervizorem. Kontejner sdílí jádro hostitelského OS, je lehčí a rychlejší, ale je omezen stejným OS a má jiný bezpečnostní model.

</details>
