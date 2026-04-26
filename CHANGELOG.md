# Changelog

Všechny významné změny tohoto projektu jsou zachycovány v tomto souboru.

Formát: založeno na [Keep a Changelog](https://keepachangelog.com/cs/1.1.0/),
verzování dle [SemVer](https://semver.org/lang/cs/).

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
