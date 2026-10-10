---
lang: hu
translation_id: beancount/12-troubleshooting
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Hibaelhárítás
description: Gyakori Fava és Beancount problémák és megoldásaik.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/12-troubleshooting.md
translation_source_body_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_source_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:25+00:00
translation_source_localized_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_source_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:25+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 12 - Hibaelhárítás

## A Fava nem nyílik meg

Ellenőrizze:

- Nyitva van még a terminál ablak?
- A Fava a megfelelő mappában lett indítva?
- A megfelelő portot használja?
- Fut már egy másik Fava példány ugyanazon a porton?
- A Fava telepítve van és elérhető a terminálban?

Parancsok:

```powershell
fava nica.beancount --port 4998
fava 2023.beancount --port 4999
```

Mindegyik parancsot csak a megfelelő ledger mappából futtassa.

## A Fava Beancount hibát jelez

Gyakori okok:

- Elírás a számla nevében.
- Hiányzó számla `open` direktíva.
- Az összeg pont helyett vesszőt használ.
- Hiányoznak az idézőjelek a kedvezményezett vagy az elbeszélés körül.
- Egy tranzakció nem kiegyensúlyozott.
- Egy egyenlegellenőrzés nem egyezik.
- Egy tranzakció egy számlát használ annak bezárása után.

Javítsa ki a szöveges fájlt, mentse el, majd töltse újra a Favát.

## Az egyenlegellenőrzés sikertelen

Ne törölje az egyenlegellenőrzést munkakerülő megoldásként. Vizsgálja meg a különbséget.

Csekklista:

- A CSV dátumtartománya teljes volt?
- Ugyanaz a CSV lett importálva kétszer?
- Néhány tranzakció a rossz ledgerbe lett beillesztve?
- Egy tranzakció a rossz Sparkasse al-számlához lett rendelve?
- Egy összeg előjelét helytelenül változtatták meg?
- Egy PayPal vagy készpénz átutalás csak az egyik oldalon lett bevezetve?
- Vannak régebbi manuális szerkesztések az előző egyenlegellenőrzés után?

## A CSV konverzió sikertelen

Ellenőrizze:

- A CSV fájl ugyanabban a `test` mappában van, mint a `csv2bean.py`.
- A parancsban szereplő fájlnév pontos.
- A fájl a Sparkasse `Excel (CSV-CAMT V2)` exportja.
- A fájl pontosvesszővel van elválasztva.
- A CSV-t nem nyitották meg és nem mentették újra úgy, hogy megváltozott volna a formátuma.

## Az importált bejegyzések túl általánosnak tűnnek

Ez várható. A konverter tartalék kategóriákat használ, mint például:

- `Ausgaben:Sonstiges`
- `Einnahmen:Sonstiges`

A felhasználónak manuálisan kell felülvizsgálnia és osztályoznia az importált bejegyzéseket.

## A műszerfal hiányzik

Ellenőrizze:

- A `fava-dashboards` telepítve van.
- A ledger tartalmazza a `custom "fava-extension" "fava_dashboards"` direktívát.
- Egy `dashboards.yaml` fájl létezik a ledger mellett.
- A Fava újra lett indítva a telepítés vagy a konfigurációs változtatások után.

## Egy projekt nem jelenik meg a műszerfalakon

Ellenőrizze:

- A projekt rendelkezik projekt eszköz számlával a várt Sparkasse vagy PayPal előtag alatt.
- A projekt számla nincs lezárva.
- A projekt egyenlege nem pontosan nulla.
- A számla neve megegyezik a műszerfal lekérdezési mintájával.

## A dokumentum link nem működik

Ellenőrizze:

- A fájl elérési útja relatív a ledger fájl mappájához.
- A fájlnév pontosan van elírva.
- A dokumentumot nem mozgatták el a hivatkozás után.
- Az elérési út perjeleket vagy normál relatív elérési út stílust használ.

## Bizonytalan egy tranzakció osztályozásában

Használja ezt a sorrendet:

1. Keressen hasonló régebbi tranzakciókat a Favában.
2. Ellenőrizze a projekt vagy a számla kontextusát.
3. Ellenőrizze, hogy tartozik-e egy támogató költségvetési sorhoz.
4. Adjon hozzá egy megjegyzést, ha bizonytalan.
5. Használjon ideiglenesen `Sonstiges`-t, csak ha nem ismer jobb kategóriát.
6. Kérdezze meg a felelős projekt vagy pénzügyi személyt a véglegesítés előtt.
