# Indicie a stopy — kompletní matice

Tento soubor obsahuje **všechny indicie**, které děti během hry sbírají, plus **matici** "**který tým / který den / proti komu**".

## Třídění indicií

- **F** = fyzické stopy (otisk, vlas, předmět, foto)
- **S** = svědectví (výpověď osoby)
- **D** = dešifrované zprávy (anonymní dopisy, fragmenty)
- **T** = táborové noviny (denní vydání, sloupek)

---

## Kompletní seznam indicií

### Fyzické stopy (F)

| Kód | Indicie | Den | Kde nalezena | Klíčový směr |
|---|---|---|---|---|
| F01 | Padělek závěti v sejfu (papír 80 g, novodobý) | 2 | sejf velitelství | krádež jistá |
| F02 | Originál závěti chybí | 2 | sejf velitelství | krádež jistá |
| F03 | Otisk pravého palce u zámku sejfu | 2 | sejf | později prokáže Petra |
| F04 | Stopa boty u velitelství (vel. 44, sportovní) | 2 | venku, schody | později prokáže Petra |
| F05 | Stopy v rose — 2 páry, jeden Konvičkův, druhý cizí | 2 | venku, ráno | Pepa fotil |
| F06 | Pepovy fotky z rána (mobilem) | 2 | u Pepy | autentický důkaz |
| F07 | Drobný škrábanec na zámku sejfu | 2 | sejf | někdo páčil/zkoušel |
| F08 | Otisk pravého palce **shoda s Petrem** | 4 | + lab. | usvědčuje Petra |
| F09 | Stopa pneumatiky 200 m od tábora v lese | 4 | les | cizí auto |
| F10 | Vlas tmavý u sejfu (městský, ne personál) | 4 | sejf | cizí osoba |
| F11 | **Mezera v knize služby Drábka** (23:00–02:00) | 5 | sklad | usvědčuje Drábka |
| F12 | Tužka Caran d'Ache s monogramem "PK" | 8 | rybník | usvědčuje Petra |
| F13 | **Kamerový záznam benzínky 12. 7. 04:32** | 8 | EuroOil | usvědčuje Petra |
| F14 | Smlouva o zprostředkování prodeje (od Kotrby) | 8 | volitelné | motiv Petra |
| F15 | Drábkovy boty se stopami **lesního bahna** | 8 | dílna Drábka | proč v lese? |
| F16 | **Pravá závěť** v dutině buku | 10 | les | finále |
| F17 | 300 000 Kč hotovost u Drábka | 9 | po přiznání | motiv Drábka |

### Svědectví (S)

| Kód | Svědectví | Den | Kdo |
|---|---|---|---|
| S01 | Pepa našel Konvičku, ukazuje fotky | 2 | Pepa |
| S02 | Alena: alibi (porada s Tomášem 23:00–02:00) | 3 | Alena |
| S03 | Tomáš: nemůže říct kde byl 02:00–03:30 | 3 | Tomáš |
| S04 | Drábek: alibi (sklad, sám) | 3 | Drábek |
| S05 | **Marie: viděla v noci postavu** (až den 6!) | 6 | Marie |
| S06 | Lucie: alibi (chatka, sama) | 3 | Lucie |
| S07 | Petra: alibi (telefon matka) | 3 | Petra |
| S08 | Pepa: detaily nálezu, čas | 3 | Pepa |
| S09 | Magdaléna: závěť se měla číst, **mám kopii** | 5 | Magdaléna |
| S10 | Petr: alibi (Praha, rodinná večeře) | 5 | Petr |
| S11 | Hájek: nezná žádné plány obce na pozemek | 6 | Hájek |
| S12 | Lucie: vzdálená příbuzná, žádné dědictví | 6 | Lucie |
| S13 | Tomáš: skutečné alibi (matka, rakovina) | 6 | Tomáš (přes Alenu) |
| S14 | Petra: výpis hovorů (matka Praha, FN Bulovka) | 7 | Petra |
| S15 | **Drábkovo přiznání (vše)** | 9 | Drábek |
| S16 | Petr po dopadení: krátké přiznání | 10 | Petr |

### Dešifrované zprávy (D)

| Kód | Zpráva | Den | Šifra |
|---|---|---|---|
| D01 | Anonymní dopis #1 — "klíče má ten, co zná tábor" | 4 | Caesar (posun 3) |
| D02 | Anonymní dopis #2 — "podívejte se do knihy služby" | 6 | Substituce (klíč: LIPA) |
| D03 | Vzkaz Konvičky z nemocnice (videovzkaz) | 7 | jasný text |
| D04 | Fragment závěti od Magdalény (§ 1, § 2) | 8 | jasný text |
| D05 | Email Petra realitnímu makléři (zachycen) | 8 | jasný text |

(Detail šifer viz `09_SIFRY_KATALOG.md`.)

### Táborové noviny (T)

| Kód | Název vydání | Den |
|---|---|---|
| T01 | Mimořádné vydání: "Krádež v noci" | 2 |
| T02 | "Vyšetřování pokračuje" | 3 |
| T03 | "Forenzní stanoviště odhalují" | 4 |
| T04 | "Hosté přijíždějí" | 5 |
| T05 | "Den klidu, ale nová stopa" | 6 |
| T06 | "Konvička se probouzí!" | 7 |
| T07 | "Výjezd do Mladé Boleslavi" | 8 |
| T08 | **MIMOŘÁDNÉ:** "Pachatel odhalen!" | 9 |
| T09 | "Závěť nalezena" | 10 |
| T10 | **VÝROČNÍ VYDÁNÍ:** "30 let Staré Lípy" | 11 |

(Detail viz `11_TABOROVE_NOVINY.md`.)

---

## Matice "stopa × podezřelý"

Tabulka ukazuje, **jakou indicií je každý podezřelý dotčen**. Tučně = potvrzuje vinu, kurzíva = potvrzuje nevinu.

| Stopa | Alena | Tomáš | **Drábek** | Marie | Lucie | Petra | Pepa | **Petr** | Magdaléna | Hájek |
|---|---|---|---|---|---|---|---|---|---|---|
| F03 (otisk u sejfu) | – | – | – | – | – | – | – | **F08 shoda** | – | – |
| F04 (stopa boty 44) | – | *vel. 42* | *vel. 43, prac.* | – | – | *vel. 38* | – | **vel. 44** | – | – |
| F05 (2 páry stop) | – | – | – | – | – | – | – | **shoda** | – | – |
| F09 (stopa pneu lesů) | *–* | *–* | *–* | – | – | – | – | **Audi Q7 odpovídá** | – | – |
| F10 (vlas u sejfu) | *–* | *–* | *–* | – | – | – | – | **městský typ** | – | – |
| F11 (mezera v knize) | – | – | **3 hod chybí** | – | – | – | – | – | – | – |
| F13 (kamera 04:32) | – | – | – | – | – | – | – | **SPZ Audi Q7** | – | – |
| F15 (lesní bahno boty) | – | – | **proč les?** | – | – | – | – | – | – | – |
| S02 (Alenina alibi) | *✓* | – | – | – | – | – | – | – | – | – |
| S05 (Marie z okna) | – | – | **kráčel** | – | – | – | – | – | – | – |
| S07 (Petra telefon) | – | – | – | – | – | *✓* | – | – | – | – |
| S13 (Tomáš matka) | – | *✓* | – | – | – | – | – | – | – | – |
| S15 (Drábek přizná) | – | – | **VŠE** | – | – | – | – | **kde**, **jak** | – | – |

---

## Distribuce indicií týmům

**Některé stopy** dostává **každý tým** (společné — vyšetřuje celý tábor). **Jiné stopy** jdou **jen 1–2 týmům** (= "exkluzivní" stopa toho týmu).

### Společné indicie (všechny týmy)

- F01, F02 (sejf, padělek vs. originál) — den 2
- F05 (Pepovy fotky) — den 2
- T01–T10 (noviny) — postupně
- S01, S02, S03, S04, S06, S07, S08 (alibi) — den 3
- F08 (otisk shoda Petra) — den 4
- D01 (anonymní dopis #1) — den 4
- S09 (notářka) — den 5
- S10 (Petr alibi oficiální) — den 5
- D02 (anonymní dopis #2) — den 6
- S05 (Marie z okna) — den 6
- D03 (videovzkaz) — den 7
- S14 (Petra výpis) — den 7
- D04 (fragment závěti) — den 8
- F13 (kamera) — den 8
- S15 (Drábek přiznání) — den 9
- F16 (závěť v buku) — den 10
- S16 (Petr přiznání) — den 10

### Exkluzivní indicie (jen některé týmy)

| Indicie | Tým, který objeví | Den |
|---|---|---|
| F11 (mezera v knize) | jeden tým, který pracuje s Drábkem den 5 | 5 |
| F12 (tužka u rybníka) | jeden tým na hledání u rybníka den 8 | 8 |
| F15 (bahno na botách) | jeden tým na výjezdu k Drábkově dílně | 8 |
| Lucie matrika | jeden tým, který kontroluje matriku | 4 |

**Tip:** vedoucí mohou **prohazovat indicie** mezi týmy podle toho, jak týmy postupují. Pokud někdo zaostává, dostane novou exkluzivní stopu. Pokud někdo vyhrává moc rychle, **chybí mu nějaká stopa, ostatní ji mají**.

---

## Posloupnost indicií (jak se hra vyvíjí)

```
Den 2 — Místo činu → F01–F07, S01
Den 3 — Výslechy → S02–S08, eliminace Alena/Pepa
Den 4 — Forenzika → F08–F10, D01, eliminace Tomáš začíná
Den 5 — Návštěvy → S09, S10, F14
Den 6 — Klid + zlom → S05, D02, S11–S13, eliminace Lucie/Hájek
Den 7 — Zlom → D03, S14, eliminace Petra
Den 8 — Město → D04, D05, F12, F13, F15, F11
Den 9 — Konfrontace → S15
Den 10 — Honička → F16, F17, S16
Den 11 — Závěť čtena
```

---

## Klíčové stopy proti pachatelům (souhrn)

### Proti Drábkovi (5 stop = nevyvratitelné)

1. F11 — mezera v knize služby (3 hodiny chybí)
2. S05 — Mariino svědectví z okna kuchyně
3. F15 — bahno z lesa na botách
4. F17 — 300 000 Kč v hotovosti
5. S15 — vlastní přiznání

### Proti Petrovi (6 stop = nevyvratitelné)

1. F03/F08 — otisk u sejfu odpovídá
2. F04 — stopa boty (vel. 44)
3. F09 — stopa pneumatiky (Audi Q7)
4. F10 — vlas u sejfu (městský)
5. F13 — kamerový záznam 04:32 ráno
6. F12 — vlastní tužka u rybníka

---

## Tip pro vedoucí: indicie nejsou zbraně

Děti by neměly **akumulovat indicie jako zbraně**. Cílem je **pochopit příběh**. Indicie slouží **rekonstrukci** — kdo, kdy, kde, proč, jak.

Vedoucí v 9. den **udělají s týmy reflexi**: *"Máme XY stop. Co z nich plyne? Kdo je vinen, **a hlavně proč?**"* Motiv je **víc než důkaz** v této hře.

---

## Falešné stopy (rudé herringy)

Hra obsahuje **3 záměrné rudé stopy**, které děti zavedou na špatnou cestu:

### 1. Lucie Nováková–Konvičková (den 4)

**Zdá se:** vzdálená příbuzná = motiv dědictví. **Realita:** žádná dědická linie, vděčná zaměstnankyně.

### 2. Hájek a obec (den 5)

**Zdá se:** starosta by mohl chtít pozemek. **Realita:** obec respektuje tábor jako kulturní památku.

### 3. Zdravotnice Petra (dny 3–6)

**Zdá se:** nová, lékařské znalosti, první u zraněného. **Realita:** alibi telefonem, profesionální.

**Tip:** Rudé stopy jsou **zdravé**. Učí, že **detektiv musí pochybovat o sobě**. Když tým **přijme rudou stopu**, vedoucí ho **nesouvisí** — nechá tým **pochopit sám**.
