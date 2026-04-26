# Changelog

Všechny významné změny tohoto projektu jsou zachycovány v tomto souboru.

Formát: založeno na [Keep a Changelog](https://keepachangelog.com/cs/1.1.0/),
verzování dle [SemVer](https://semver.org/lang/cs/).

## [Unreleased]

### Probíhající korekce

- ⏳ Propagace nových názvů postav (Marek Stanislav, Karel/Pavel Malík, Jenda,
  Anička Kellnerová, Magdaléna Hamanová, Aleš Tomek) do souborů 02–15.
- ⏳ Propagace nového motivu pachatele (Vladimír Stehlík, hospodář, myslivecký
  revír) do indicií, denních scénářů, finálového skriptu a šablon.
- ⏳ Aktualizace lokálních detailů (Šéfka místo „velitelství", studánka, latrýny,
  bez elektřiny) v denních scénářích a forenzních stanovištích.
- ⏳ Doplnění/upřesnění mladší kuchařky.

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
- **Hlavní postavy** (kompletně přejmenovány):
  - Josef Konvička → **Marek Stanislav** (zakladatel)
  - Alena Procházková → **Karel Malík** (hlavní vedoucí)
  - Tomáš Veselý → **Pavel Malík** (zástupce, bratr Karla)
  - Karel Drábek → **Jenda** (zásobovač)
  - Marie Hradilová → **Anička Kellnerová** (st. kuchařka)
  - MUDr. Petra Svobodová → **Magdaléna Hamanová** (zdravotnice, 50 let)
  - Pepa Bouček → **Aleš Tomek** (údržbář)
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

### Stav korekcí napříč soubory

| Soubor | Stav korekce |
|---|---|
| `00_README.md` | ✅ aktualizováno |
| `01_PRIBEH_setting.md` | ✅ aktualizováno |
| `02_HLAVNI_LINIE.md` | ⏳ nezměněno (čeká na propagaci) |
| `03_PODEZRELI_kompletni.md` | ⏳ nezměněno |
| `04_ROLE_OBSAZENI.md` | ⏳ nezměněno |
| `05_VYSETROVACI_TYMY.md` | ⏳ nezměněno |
| `06_VOLITELNE_ROLE_HOSTI.md` | ⏳ nezměněno |
| `07_CASOVA_OSA.md` | ⏳ nezměněno |
| `08_INDICIE_MATICE.md` | ⏳ nezměněno |
| `09_SIFRY_KATALOG.md` | ⏳ nezměněno |
| `10_FORENZNI_STANOVISTE.md` | ⏳ nezměněno |
| `11_TABOROVE_NOVINY.md` | ⏳ nezměněno |
| `12_FINALE_skript.md` | ⏳ nezměněno |
| `13_BODOVANI.md` | ⏳ nezměněno |
| `14_MATERIAL_seznam.md` | ⏳ nezměněno |
| `15_DOPLNKOVE_AKTIVITY.md` | ⏳ nezměněno |
| `dny/den_01..12_*.md` | ⏳ nezměněno |
| `sablony/*.md` | ⏳ nezměněno |

> **Poznámka:** soubory označené ⏳ stále obsahují staré jméno tábora
> (Stará Lípa), staré postavy (Konvička, Drábek, atd.) a starou logiku
> (sejf, velitelství, finanční motiv). Při čtení je třeba mít to na paměti
> — finální propagace bude provedena postupně po vyjasnění otevřených otázek.

## [0.1.0] – 2026-04-26 — *První iterace*

### Přidáno

- Hrubá struktura projektu: 16 hlavních souborů, 12 denních scénářů,
  5 šablon (33 souborů celkem).
- Kompletní zápletka, postavy, indicie, šifry, výsledný dědický list.
- Bodovací systém pro 3 věkové kategorie.
- Forenzní stanoviště (otisky, identikit, lupa, mikroskop).

[Unreleased]: https://github.com/sotoniak/tabor_2026/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/sotoniak/tabor_2026/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/sotoniak/tabor_2026/releases/tag/v0.1.0
