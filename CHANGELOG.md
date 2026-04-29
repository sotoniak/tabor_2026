# Changelog

Všechny významné změny tohoto projektu jsou zachycovány v tomto souboru.

Formát: založeno na [Keep a Changelog](https://keepachangelog.com/cs/1.1.0/),
verzování dle [SemVer](https://semver.org/lang/cs/).

## [0.5.1] – 2026-04-29 — *Konzistenční oprava: F03, F09, časová osa*

### Opraveno

- **F03 — otisk u truhly**: sjednoceno napříč soubory (02, 03, 08, 16) — otisk je **dlaně přes rukavici** (neúplný, deformovaný), ne přímý otisk Stehlíka. Stehlíka konkrétně usvědčí až F10 (vlas z rukavice) + F12 (popel z dýmky).
- **F09 — pickup vs. pěšky**: vyřešen rozpor mezi *„Stehlík přichází lesem pěšky"* a *„F09 stopa pickupu na lesní cestě"*. **Stehlík nyní v 00:25 zaparkuje pickup u zatáčky 200 m od tábora**, dál pokračuje pěšky. Po zločinu pěšky zpět k pickupu, pickupem na samotu. Tím vznikají dvě stopy F09 (příjezd + odjezd). Aktualizováno v 02_HLAVNI a dny/den_01.
- **SoTův návrat 5:00 → 5:30**: posunut na 5:30, aby seděl s Tomášem Kellnerovým svědectvím S19 (Tomáš Kellner viděl Santanu v 5:30 cestou k Jedovnicím). SoTo má krátký odpočinek 20 min ve stanu, pak v 6:00 vyjíždí znovu do Blanska, je tam v 6:30 u notářky.
- **Hospitalizace 6 dní → ~9 dní**: opraveno v 02 a 01_PRIBEH (Marek se vrací den 11, tedy 9 dní v nemocnici).
- **07_CASOVA_OSA**: přepracována časová osa zločinu (00:25 Stehlík parkuje pickup, 00:40 SoTo opouští Šéfku, 00:45 Stehlík vstupuje, atd.) + den 2 timetable (07:30 SoTo se vrací, 07:45 mimořádný nástup, Páter Lacina ve 14:00).
- **01_PRIBEH ř. 214**: opraveno *„Aleš Tomek vstává a najde Marka"* → *„Anička Kellnerová cestou ke studánce najde Marka"* (sedí s aktualizovanou zápletkou).
- **Herecký tip pro Karla**: doplněn v 04_ROLE_OBSAZENI — Karel-postava ve hře neví o Markově pověření SoTa, i když Karel-herec to ví (dvojí role i v tomto smyslu).

### Bez dopadů

- Žádné změny v hlavní zápletce, charakterech postav ani v rozdělení rolí.

## [0.5.0] – 2026-04-29 — *Korekce: Karel hraje Marka, Preclík bez příbuzenství, Santana*

### Změněno

- **Karel Malík hraje Marka Stanislava (dvojí role)** — uživatel nemá k dispozici staršího herce na roli zakladatele. Karel (real, 44) hraje **dvě postavy ve hře**: Karla Malíka (hl. vedoucí, dny 1–12, vlastní oblečení) a Marka Stanislava (zakladatel, **jen den 1 večer + den 11 odpoledne**) s výrazně odlišným kostýmem (sako, čepice, vycházková hůl, šedavé vousy lepené, pomalejší tempo, hlubší klidný hlas). V herní rovině zůstávají postavy Marek a Karel **rozdílné**. Nová sekce „Logistika dvojí role Karel/Marek" v `04_ROLE_OBSAZENI.md` s detailním scénářem kostýmové změny v 3 scénách (den 1 zahájení, den 11 odpoledne, den 7 vzkaz). **Klíčové:** Marek u večerního ohně den 11 NEZŮSTÁVÁ — po čtení závěti odjíždí zpět do FN Brno, večer pak vede Karel sám za sebe. Karlovo alibi (porada se SoTou 23:30–00:15) se nemění — v herní rovině jsou Karel a Marek dva lidé.
- **Pavel „Preclík" Malík NENÍ synovec Karla** — v 0.4.0 jsem omylem zavedl příbuzenskou vazbu (synovec Karla, bratranec Klárky a Lucky). Příjmení Malík je shoda jmen, žádný příbuzenský vztah. Opraveno na 8 výskytů (03_PODEZRELI, 04_ROLE_OBSAZENI, README, sablony, dny/den_03).
- **Vůz SoTa: Octavia → Santana** — kosmetická úprava (Volkswagen Santana — méně obvyklé, dramaticky zajímavější). Nahrazení napříč ~15 výskyty bez dopadů na herní logiku.

### Záměrně NEZAŘAZENO

- **Spor Marek↔SoTo o Aleše (R11)** — uživatel rozhodl příběh **NEPŘIDÁVAT další vrstvu**. Existující rudá stopa proti SoTovi (5 kusů) je dostatečně silná. Mladší kadety chrání rámování instruktorek. Komplikovanost příběhu pro 1.–4. třídu zůstává v rozumných mezích.

### Migrace souborů

- ✅ Korekce 1 (Preclík): 03, 04, README, sablony, dny/den_03 (8 výskytů)
- ✅ Korekce 2 (Karel→Marek): 04 (A1+D1+nová sekce „Logistika dvojí role"), dny/den_01 (kostýmová změna v ceremoniálu), dny/den_07 (Markův vzkaz čte Karel papírově), dny/den_11 (kostýmová logistika + Markův odjezd po čtení závěti, večerní oheň vede Karel), 01, 12, README
- ✅ Korekce 3 (Santana): napříč 16 soubory globální nahrazení

## [0.4.0] – 2026-04-29 — *Obsazení reálného personálu, hlavní rudá stopa SoTo*

### Přidáno

- **Tomáš „Tony" Sotoniak (SoTo, 42)** jako **zástupce hlavního vedoucího + vzdálený synovec Marka + HLAVNÍ rudá stopa**. Drží se podezření 7 dní (krevní pouto, klíče, zmizelá Santana v noci, vyhýbavé odpovědi). Eliminace den 8 — notářka v Blansku potvrdí, že SoTo plnil **tajné Markovo přání** (noční mise do Brna pro kopii dodatku smlouvy s podpisem). Den 11 finále: **veřejná omluva před dětmi**.
- **Adriana (30)** — partnerka Jendy, **klíčový postřeh den 4** o Octavii na jiném místě (R02).
- **Pavel „Preclík" Malík (28)** — vedoucí oddílu Jezevci, **drobná komická rudá stopa den 4** (krádež koláče v noci). _(V 0.5.0 opraveno: shoda příjmení s Karlem, žádný příbuzenský vztah.)_
- **Tom Buchta (28)** — vedoucí oddílu Sojky, atletická pomoc v honičce den 10, **housle při čtení závěti den 11**.
- **9 mladých instruktorů (~18 let)**: Klárka Malíková a Lucka Malíková (dcery Karla), Martin, Martina, Alča, Jeník, Lucka Ravasová, Vája, Ondra. Vedoucí 5 ze 6 týmů (+ Preclík vede Jezevce, Tom Buchta vede Sojky).
- **Tomáš Kellner** — řezník z Jedovnic, **bratr Aničky a Anežky**, drobné návštěvy den 2 (přiveze maso) a den 6 (drobná stopa S19 — viděl Octavii v 5:30).
- **Páter Lacina** — kněz z Jedovnic, drobná návštěva den 2 (modlitba za Marka), telefonát den 7 (potvrzení S20 — viděl Octavii v 3:30 v Brně).
- **Exkluzivní stopy mladých instruktorů**: S22 (Klárka — pamatuje Marka mluvícího se SoTou), S23 (Lucka R. — analýza otisku 44), S24 (Jeník — turistická stopa pneumatiky).
- **Komická drobnost den 4** — Preclík přizná noční nájezd na koláč (R07).

### Změněno

- **Pavel Malík (zástupce, bratr Karla, 40+)** — **odstraněn**. Funkci zástupce přebírá **SoTo** (NENÍ Malík). Karel přestává být něčí bratr; má dvě dcery (Klárka, Lucka).
- **Klára Stanislavová (ml. kuchařka, vzdálená sestřenice Marka, 28)** — **odstraněna**. Funkci ml. kuchařky přebírá **Anežka Kellnerová** (sous-chef, **mladší sestra Aničky**, bez příbuzenství s Markem). Rudou stopu „vzdálený příbuzný Marka" přebírá **SoTo** (silnější, déle drží napětí).
- **Magdaléna Hamanová (zdravotnice, 50)** → **Magda Hamanová (25, zasnoubená)** — omlazení role, mladá energická persona, lehká sebe-ironie o „kmetovství". Ostatní funkce zachovány (lékařský deník alibi, Markův vzkaz den 7).
- **Aleš Tomek (50+)** → **Aleš Tomek (19, mladý správce/údržbář)** — backstory předělána. Místo vlastní nehody z 90. let nyní **otcův dluh** Stehlíkovým z 2010 (otec zemřel 2018, Vladimír drží papír nad mladým Alešem a matkou-vdovou). Úplatek 30 000 Kč → na exekuce matky.
- **Pavlův původní „ranní výjezd v 5:45 pro chleba"** se přepisuje na **SoTův noční výjezd Octavií 0:45 → 5:00 do Brna a zpět** (Markova mise). To drží rudou stopu proti SoTovi soudržně.

### Příběhové důsledky

- **Hlavní rudá stopa se přesouvá** z Kláry (dny 4–6, slabá) na SoTa (dny 3–8, silná). Děti několikrát mění hlavního podezřelého: SoTo → Stehlík → Aleš.
- **Den 7 vzkaz Marka** přidává klíčové slovo: *„...a Tomáši, můžeš to říct."* Otevírá SoTovo přiznání.
- **Den 8 v Blansku** notářka definitivně eliminuje SoTa (S21).
- **Den 11 finále** přidává **veřejnou omluvu** SoTem před dětmi — morální lekce „omluva je odvaha".
- **Strom rodinných vazeb v táboře:** Karel (44) ↔ dcery Klárka & Lucka (18). Anička ↔ sestra Anežka ↔ bratr Tomáš Kellner. SoTo ↔ vzdálený synovec Marka. _(V 0.5.0 opraveno: Preclík NENÍ Karlův synovec, jen shoda příjmení.)_

### Migrace souborů

- ✅ 02_HLAVNI_LINIE.md, 03_PODEZRELI_kompletni.md, 04_ROLE_OBSAZENI.md, 08_INDICIE_MATICE.md (kompletní přepis)
- ✅ 16_STOPY_VIZUAL.md (kompletní přepis vizualizací)
- ✅ dny/den_01–07 (kompletní přepis nebo cílené úpravy)
- ✅ dny/den_08–12 (cílené úpravy: jména, role SoTa, eliminace, finále)
- ✅ 05_VYSETROVACI_TYMY.md (přidáno konkrétní obsazení 6 týmů)
- ✅ 06_VOLITELNE_ROLE_HOSTI.md (přidáni Tomáš Kellner + Páter Lacina jako pevné role)
- ✅ Šablony, README, ostatní soubory (cílené úpravy jmen)

## [0.3.0] – 2026-04-26 — *Dokončená migrace na verzi A*

### Změněno (sjednocení napříč všemi 33 soubory)

- **Jména postav** — kompletně propsáno do všech souborů:
  - Josef Konvička → **Marek Stanislav** (zakladatel, 60+, založil 1997)
  - Petr Konvička (synovec) → **Vladimír Stehlík** (soused-hospodář, hl. pachatel)
  - Karel Drábek (zásobovač) → **Aleš Tomek** (údržbář, pomocník zločinu)
  - Pepa Bouček (údržbář) → **Jenda** (zásobovač, NEvinný svědek)
  - Alena Procházková → **Karel Malík** (hlavní vedoucí)
  - Tomáš Veselý → **Pavel Malík** (zástupce, **bratr Karla**)
  - Marie Hradilová → **Anička Kellnerová** (starší kuchařka, klíčová svědkyně)
  - Lucie Nováková → **Klára Stanislavová** (mladší kuchařka, vzdálená sestřenice Marka — NEvinná rudá stopa)
  - MUDr. Petra Svobodová → **Magdaléna Hamanová** (zdravotnice, 50)
  - JUDr. Magdaléna Růžičková (notářka) — beze změny
  - Bohumil Hájek (starosta Jedovnic) — beze změny
- **Místa**:
  - Mladá Boleslav → **Blansko** (notářka, pohotovost)
  - nemocnice Frýdek-Místek/Mladá Boleslav → **FN Brno**
  - Praha (Petrovo bydliště) → **Stehlíkova samota 1 km od tábora**
  - Borová pod Lípou → **Jedovnice**
- **Motiv pachatele** (klíčové!): NE peněžní motiv. Stehlík chce kus lesa
  pro **myslivecký revír**. Marek připravil **dodatek smlouvy s Mendelovou
  univerzitou o prodloužení propůjčení o 30 let** — příloha závěti.
  Když závěť (s dodatkem) zmizí, propůjčení 2027 vyprší a univerzita pronajme
  plochu Stehlíkovi.
- **Motiv pomocníka** (Aleš Tomek): stará nehoda v 90. letech (Aleš porazil
  strom na cizí kůlnu hospodáře Stehlíka st.). Vydíráním + 30 000 Kč „na dluhy"
  (NE 300 000 Kč).
- **Mechanika dramatické noci**: pád ze schodů velitelství → **pád v lese
  za Šéfkou** (klopýtnutí o kořen smrku, úder hlavou o kámen).
- **Místo úschovy závěti**: sejf ve velitelství → **kufr s mapami v Šéfce**
  (dřevěná truhla, NEzamčená klíčem, jen víkem).
- **Místo schování pravé závěti**: rybník → **dutina starého buku u potoka**.
- **Auto pachatele**: Audi Q7 → **starší pickup** (Toyota Hilux nebo
  Mitsubishi L200) s dřevěnou korbou.
- **Forenzní stopy nahrazeny přírodními** (verze A je stanový tábor bez
  elektřiny — žádné kamery):
  - F12 tužka „PK" → **popel z dýmky** (Stehlíkova zvláštní směs) v rohu Šéfky
  - F13 kamerový záznam benzínky → **dodatek smlouvy s univerzitou**
    (Magdaléna v Blansku) jako důkaz motivu
  - F15 lesní bahno na botách Drábka → **lesní bahno specifické pro
    Stehlíkovu louku** na botách Aleše
  - F10 vlas tmavý městský → **vlas z kožené rukavice** Stehlíka
  - F04 sportovní bota Nike → **kožená bota velikosti 44** (Stehlíkův styl)
- **Den 8 výjezd**: Mladá Boleslav → **Blansko** (notářka, 20 km).
  Bonus pro 2–3 nejstarší kadety: **Brno (Mendelova univerzita, LDF)** kvůli
  kopii smlouvy.
- **Padělek závěti**: vyrobil **Stehlíkův kamarád z Brna, právník-amatér**
  (pro hru ne nutné mít na scéně, jen v Stehlíkově výpovědi po dopadení).
- **Rok dění**: 2025 → **2026** (jubilejní 30. ročník; 1997 = 1. ročník).

### Vyřešené otevřené otázky (ze sekce v `01_PRIBEH_setting.md`)

1. **Mladší kuchařka** zachována jako **Klára Stanislavová** (28, vzdálená
   sestřenice Marka — otec její matky byl bratrancem Marka). Pomáhá Aničce.
   NEvinná rudá stopa: den 4 si tým povšimne podobnosti příjmení; den 6
   Magdaléna Růžičková potvrdí vzdálené pokrevní spojení a žádné dědické
   nároky → eliminace.
2. **Stehlíkův motiv**: pozemek + myslivecký revír + dodatek smlouvy
   s Mendelovou univerzitou (preferovaná verze; alternativa „pomsta za
   90. léta" zamítnuta).
3. **Sousední tábory**: zapojen 1 z 3 — **Pavel Konečný** (vedoucí skautského
   tábora Borovice, 45 let). Kdysi navrhl Markovi sloučení táborů, byl
   odmítnut. Krátká rudá stopa den 5–6, eliminace den 6 (alibi: byl s vedoucími
   tábora Údolí na poradě).
4. **Aleš Tomek jako pomocník** potvrzeno (preferováno proti Jendovi).
5. **Den 8 výjezd**: Blansko (notářka) jako hlavní; Brno (univerzita)
   jako bonus pro starší tým.
6. **Padělek závěti**: Stehlíkův kamarád z Brna, právník-amatér.

### Opraveno

- **Časový rozpor v souboru `07_CASOVA_OSA.md`**: konfrontace v den 9
  posunuta na **14:00** (synchronizováno s `dny/den_09_konfrontace.md`).
- **Neodpovídající logika spánku**: Marek Stanislav nyní spí ve **stanu
  zakladatele vedle Šéfky** (ne „v hostinském pokoji nad velitelstvím" —
  verze A je čistě stanový tábor).
- **Kdo ráno najde Marka**: nyní **Anička Kellnerová** (cestou ze studánky
  pro vodu), ne Aleš (ten Marka v noci viděl, nemůže přesvědčivě hrát
  překvapeného).

### Stav korekcí napříč soubory

| Soubor | Stav |
|---|---|
| `00_README.md` | ✅ |
| `01_PRIBEH_setting.md` | ✅ |
| `02_HLAVNI_LINIE.md` | ✅ |
| `03_PODEZRELI_kompletni.md` | ✅ |
| `04_ROLE_OBSAZENI.md` | ✅ |
| `05_VYSETROVACI_TYMY.md` | ✅ |
| `06_VOLITELNE_ROLE_HOSTI.md` | ✅ |
| `07_CASOVA_OSA.md` | ✅ |
| `08_INDICIE_MATICE.md` | ✅ |
| `09_SIFRY_KATALOG.md` | ✅ |
| `10_FORENZNI_STANOVISTE.md` | ✅ |
| `11_TABOROVE_NOVINY.md` | ✅ |
| `12_FINALE_skript.md` | ✅ |
| `13_BODOVANI.md` | ✅ |
| `14_MATERIAL_seznam.md` | ✅ |
| `15_DOPLNKOVE_AKTIVITY.md` | ✅ |
| `dny/den_01..12_*.md` | ✅ |
| `sablony/*.md` | ✅ |
| `README.md` | ✅ |

## [0.2.0] – 2026-04-26 — *Druhá iterace, základní korekce*

### Změněno

- **Název tábora:** Stará Lípa → **Světlo**.
- **Rok hry a oslav:** 2025 → **2026** (jubilejní 30. ročník; 1997 = 1. ročník).
- **Lokace:** obecná „les u rybníka" → **Rakovecké údolí, 6 km od Jedovnic**
  (okres Blansko, Jihomoravský kraj).
- **Charakter tábora:** budovy + ploty → **stanový tábor** (Šéfka, teepee,
  stany, kopané latrýny, studánka, altán; bez elektřiny, slabý mobilní signál).
- **Pozemek:** „15 ha v lese, tržní hodnota 30–40 mil. Kč" → **propůjčeno**
  od Mendelovy univerzity (LDF, ŠLP Křtiny) + místních hospodářů Stehlíkových.
  Žádná tržní hodnota.
- **Filozofie tábora:** ziskový provoz → **dobrovolnická akce, vyrovnané
  finance, nikdo placený**.
- **Místo úschovy závěti:** sejf ve velitelství → **kufr v Šéfce** (truhla
  s mapami).
- **Terminologie:** „zaměstnanci tábora" → **vedoucí, personál, účastníci**.
- **Hlavní postavy** (kompletně přejmenovány) — viz seznam ve verzi 0.3.0.
- **Hlavní pachatel:** Petr Konvička (synovec, finanční motiv) → **Vladimír
  Stehlík** (místní hospodář, motiv = myslivecký revír / soukromé hospodářské
  využití lesa). **Motiv NENÍ peněžní.**
- **Pomocník zločinu:** Karel Drábek → **Aleš Tomek** (vyrostl s rodinou
  Stehlíkových, vydírán starou křivdou).
- **Mechanika dramatické noci:** pád ze schodů velitelství → **pád v lese
  za Šéfkou** (kořen smrku, kámen).
- **Nemocnice:** Mladá Boleslav → **FN Brno**.
- **Den 8 výjezd:** Mladá Boleslav → **Blansko** (notářka), případně Brno
  (Mendelova univerzita) jako bonus.
- **Princip podezřelosti:** „personál + návštěvníci" → **VŠICHNI** (personál,
  jiné týmy účastníků, vedoucí 3 sousedních táborů, návštěvníci).

### Přidáno

- **3 sousední tábory** v Rakoveckém údolí jako potenciální zdroj podezřelých.
- Sekce **Otevřené otázky k dořešení** v `01_PRIBEH_setting.md`.
- Důraz na **deník vyšetřovatele** (osobní deník každého účastníka) a
  **vlastní mapu tábora** (každý tým si svou kreslí).
- Tento `CHANGELOG.md` a `README.md` (kořenový pro GitHub).
- `.gitignore` se sensitive daty (seznamy účastníků, kontakty).

## [0.1.0] – 2026-04-26 — *První iterace*

### Přidáno

- Hrubá struktura projektu: 16 hlavních souborů, 12 denních scénářů,
  5 šablon (33 souborů celkem).
- Kompletní zápletka, postavy, indicie, šifry, výsledný dědický list.
- Bodovací systém pro 3 věkové kategorie.
- Forenzní stanoviště (otisky, identikit, lupa, mikroskop).

[Unreleased]: https://github.com/sotoniak/tabor_2026/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/sotoniak/tabor_2026/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/sotoniak/tabor_2026/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/sotoniak/tabor_2026/releases/tag/v0.1.0
