---
lang: hu
translation_id: beancount/01-system-overview
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Rendszer áttekintése
description: A könyvelési rendszer célját, összetevőit és normál felhasználói munkafolyamatát ismerteti.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/01-system-overview.md
translation_source_body_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_source_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:32:23+00:00
translation_source_localized_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_source_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:32:23+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 01 - Rendszeráttekintés

## Cél

A könyvelési rendszer strukturált, ellenőrizhető módon rögzíti az egyesületek minden pénzügyi tevékenységét. Célja, hogy megválaszolja a szokásos könyvelési kérdéseket:

- Mennyi pénz áll jelenleg rendelkezésre?
- Mely bevételek és kiadások tartoznak magához az egyesülethez?
- Mely bevételek és kiadások tartoznak egy adott projekthez?
- Helyesek-e a Sparkasse, a PayPal és a készpénz egyenlegek?
- Mely bizonylatok és dokumentumok tartoznak melyik tranzakcióhoz?
- Mely projektek aktívak, befejezettek vagy már lezártak?

## Fő komponensek

| Komponens | Mit csinál |
| --- | --- |
| Beancount | A könyvelési adatformátum. A tranzakciók egyszerű szöveges fájlokban vannak rögzítve. |
| Fava | A böngészőfelület a Beancount adatok megtekintésére és szűrésére. |
| Fava Dashboards | Egyéni irányítópult oldalak a Faván belül a vezetőség áttekintéséhez és projekt nézetekhez. |
| Obsidian | A jegyzetrendszer, ahonnan gombokon keresztül nyitható meg a könyvelés. |
| CSV import szkriptek | Segédszkriptek, amelyek a Sparkasse CSV exportokat Beancount bejegyzésekké alakítják. |

## Hogyan illeszkednek össze az alkatrészek

1. A banki vagy PayPal adatok CSV formátumban exportálásra kerülnek.
2. A CSV ideiglenes Beancount bejegyzésekké alakul.
3. Az új bejegyzések bemásolásra kerülnek a megfelelő főkönyvi fájlba.
4. A felhasználó ellenőrzi, osztályozza és javítja a bejegyzéseket.
5. Az egyenlegellenőrzések megerősítik, hogy a főkönyv megegyezik a banki vagy PayPal egyenleggel.
6. A Fava jelentéseket, számlakivonatokat, eredménykimutatásokat, mérlegeket és irányítópultokat jelenít meg.

## Két külön egyesület

| Egyesület | Főkönyv | Tipikus számlaprefix |
| --- | --- | --- |
| NICA e.V. | `nica.beancount` | `Sparkasse-NICA`, `NICA` |
| Tohuwabohu Halle e.V. | `2023.beancount` | `Sparkasse-Tohuwabohu`, `Tohuwabohu` |

Létezik egy kísérleti, kombinált fájl is: `1. Vereinsverwaltung/Buchhaltung/all.beancount`. A normál, napi munkát az adott egyesület egyedi főkönyvében kell végezni.

## Alapvető munkafolyamat

1. Nyissa meg a megfelelő Fava példányt.
2. Keresse meg az utolsó befejezett egyenlegellenőrzést.
3. Exportálja az új banki tranzakciókat a Sparkasse-ból az utolsó ellenőrzött dátumtól kezdve.
4. Alakítsa át a CSV-t Beancount formátummá.
5. Illessze be a generált bejegyzéseket először a `Bank Dump` (Banki mentés) részbe.
6. Helyezze át vagy osztályozza a bejegyzéseket a megfelelő egyesületi vagy projekt részlegekbe.
7. Adjon hozzá bizonylatokat, hivatkozásokat, megjegyzéseket vagy címkéket, ha szükséges.
8. Adjon hozzá egy új egyenlegellenőrzést.
9. Töltse újra a Favát, és győződjön meg arról, hogy nincsenek hibák.

## Mit kell megtanulnia először egy új felhasználónak

1. [A Fava megnyitása](02-opening-fava.md)
2. [Beancount alapok felhasználóknak](04-beancount-basics-for-users.md)
3. [Banki CSV import és egyeztetés](07-bank-csv-import-and-reconciliation.md)
4. [Számlák és kategóriák](05-accounts-and-categories.md)
5. [Projektek és lekötött alapok](08-projects-and-restricted-funds.md)
