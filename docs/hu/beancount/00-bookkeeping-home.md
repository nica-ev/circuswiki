---
lang: hu
translation_id: beancount/00-bookkeeping-home
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Könyvelési Rendszer Dokumentáció
description: Az NICA e.V. és a Tohuwabohu Halle e.V. Beancount könyvelési dokumentáció áttekintése és kiindulópontja.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/00-bookkeeping-home.md
translation_source_body_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_source_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:31:17+00:00
translation_source_localized_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_source_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:31:17+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# Dokumentáció a könyvelési rendszerről

Ez a dokumentáció elmagyarázza, hogyan működik a NICA e.V. és a Tohuwabohu Halle e.V. könyvelési rendszere egy átlagos felhasználó szemszögéből.

A rendszer egyszerű szöveges könyvelési fájlokat használ a Beancount formátumban, valamint egy Fava nevű böngészőfelületet. Nem szükséges programozási ismeret a használatához, de szigorúan be kell tartani a könyvelési munkafolyamatot: banki adatok importálása, tranzakciók kategorizálása, bizonylatok csatolása szükség szerint, és egyenlegek ellenőrzése.

## Kezdje itt

- [01 - Rendszer áttekintése](01-system-overview.md)
- [02 - A Fava megnyitása](02-opening-fava.md)
- [03 - Mappa- és fájlszerkezet](03-folder-and-file-map.md)
- [04 - Beancount alapok felhasználóknak](04-beancount-basics-for-users.md)
- [05 - Számlák és kategóriák](05-accounts-and-categories.md)
- [06 - Tranzakciók rögzítése és szerkesztése](06-entering-and-editing-transactions.md)
- [07 - Banki CSV import és egyeztetés](07-bank-csv-import-and-reconciliation.md)
- [08 - Projektek és elkülönített alapok](08-projects-and-restricted-funds.md)
- [09 - Bizonylatok és dokumentumok](09-receipts-and-documents.md)
- [10 - Fava irányítópultok és jelentések](10-fava-dashboards-and-reports.md)
- [11 - Rendszeres könyvelési feladatok](11-regular-bookkeeping-routine.md)
- [12 - Hibaelhárítás](12-troubleshooting.md)
- [13 - Szójegyzék](13-glossary.md)

## A legfontosabb szabály

A könyvelési fájl az "igazság forrása". A Fava csak azt jeleníti meg, ami a `.beancount` fájlokban szerepel. Ha valami hibásnak tűnik a Favában, javítsa ki a Beancount bejegyzést, és töltse újra a Favát.

## Jelenlegi főkönyvek

| Szervezet | Fő fájl | Fava cím | Port |
| --- | --- | --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` | `http://127.0.0.1:4998/` | `4998` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` | `http://127.0.0.1:4999/` | `4999` |

## Mihez nem nyújt ez a dokumentáció

Ez nem jogi vagy adótanácsadás. Ez a dokumentáció leírja, hogyan szerveződik ez a specifikus, helyi könyvelési rendszer, és hogyan kell a felhasználóknak következetesen dolgozniuk vele.
