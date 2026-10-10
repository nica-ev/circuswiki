---
lang: sk
translation_id: beancount/00-bookkeeping-home
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Dokumentácia účtovného systému
description: Prehľad a východiskový bod pre dokumentáciu účtovníctva Beancount pre NICA e.V. a Tohuwabohu Halle e.V.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/00-bookkeeping-home.md
translation_source_body_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_source_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:03:51+00:00
translation_source_localized_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_source_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:03:51+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# Dokumentácia účtovného systému

Táto dokumentácia vysvetľuje, ako funguje účtovný systém pre NICA e.V. a Tohuwabohu Halle e.V. z pohľadu bežného používateľa.

Systém využíva účtovné súbory v čistom texte vo formáte Beancount a prehliadačové rozhranie s názvom Fava. Na jeho používanie nemusíte rozumieť programovaniu, ale musíte starostlivo dodržiavať pracovný postup účtovníctva: importovať bankové údaje, klasifikovať transakcie, pripojiť príjmové doklady tam, kde je to potrebné, a kontrolovať zostatky.

## Začnite tu

- [01 - Prehľad systému](01-system-overview.md)
- [02 - Otvorenie Favу](02-opening-fava.md)
- [03 - Mapa priečinkov a súborov](03-folder-and-file-map.md)
- [04 - Základy Beancount pre používateľov](04-beancount-basics-for-users.md)
- [05 - Účty a kategórie](05-accounts-and-categories.md)
- [06 - Zadanie a úprava transakcií](06-entering-and-editing-transactions.md)
- [07 - Import CSV z banky a zúčtovanie](07-bank-csv-import-and-reconciliation.md)
- [08 - Projekty a účelové fondy](08-projects-and-restricted-funds.md)
- [09 - Príjmové doklady a dokumenty](09-receipts-and-documents.md)
- [10 - Prístrojové dosky a prehľady Favу](10-fava-dashboards-and-reports.md)
- [11 - Pravidelná účtovná rutina](11-regular-bookkeeping-routine.md)
- [12 - Riešenie problémov](12-troubleshooting.md)
- [13 - Slovník pojmov](13-glossary.md)

## Najdôležitejšie pravidlo

Účtovný súbor je zdrojom pravdy. Fava zobrazuje iba to, čo je napísané v súboroch `.beancount`. Ak sa vo Favу niečo zobrazuje nesprávne, opravte záznam v Beancount a znova načítajte Favу.

## Aktuálne účtovné knihy

| Organizácia | Hlavný súbor | Adresa Favу | Port |
| --- | --- | --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` | `http://127.0.0.1:4998/` | `4998` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` | `http://127.0.0.1:4999/` | `4999` |

## Čo táto dokumentácia nie je

Toto nie je právne ani daňové poradenstvo. Opisuje, ako je tento konkrétny lokálny účtovný systém organizovaný a ako by s ním mali používatelia konzistentne pracovať.
