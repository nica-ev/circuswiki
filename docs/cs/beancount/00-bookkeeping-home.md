---
lang: cs
translation_id: beancount/00-bookkeeping-home
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Dokumentace účetního systému
description: Přehled a výchozí bod pro dokumentaci účetnictví Beancount pro NICA e.V. a Tohuwabohu Halle e.V.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/00-bookkeeping-home.md
translation_source_body_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_source_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:31:58+00:00
translation_source_localized_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_source_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:31:58+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# Dokumentace účetního systému

Tato dokumentace vysvětluje, jak funguje účetní systém pro NICA e.V. a Tohuwabohu Halle e.V. z pohledu běžného uživatele.

Systém používá účetní soubory v prostém textu ve formátu Beancount a webové rozhraní nazvané Fava. Abyste jej mohli používat, nemusíte rozumět programování, ale musíte pečlivě dodržovat pracovní postup účetnictví: importovat bankovní data, klasifikovat transakce, připojovat účtenky tam, kde je to nutné, a kontrolovat zůstatky.

## Začněte zde

- [01 - Přehled systému](01-system-overview.md)
- [02 - Spuštění Favě](02-opening-fava.md)
- [03 - Mapa složek a souborů](03-folder-and-file-map.md)
- [04 - Základy Beancountu pro uživatele](04-beancount-basics-for-users.md)
- [05 - Účty a kategorie](05-accounts-and-categories.md)
- [06 - Zadávání a úprava transakcí](06-entering-and-editing-transactions.md)
- [07 - Import CSV z banky a párování](07-bank-csv-import-and-reconciliation.md)
- [08 - Projekty a účelově vázané fondy](08-projects-and-restricted-funds.md)
- [09 - Účtenky a dokumenty](09-receipts-and-documents.md)
- [10 - Přehledy a reporty Favě](10-fava-dashboards-and-reports.md)
- [11 - Pravidelná účetní rutina](11-regular-bookkeeping-routine.md)
- [12 - Řešení problémů](12-troubleshooting.md)
- [13 - Slovníček pojmů](13-glossary.md)

## Nejdůležitější pravidlo

Účetní soubor je zdrojem pravdy. Fava pouze zobrazuje to, co je zapsáno v souborech `.beancount`. Pokud se ve Favě něco jeví jako nesprávné, opravte záznam v Beancountu a znovu načtěte Favě.

## Aktuální účetní knihy

| Organizace | Hlavní soubor | Adresa Favě | Port |
| --- | --- | --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` | `http://127.0.0.1:4998/` | `4998` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` | `http://127.0.0.1:4999/` | `4999` |

## Čím tato dokumentace není

Toto není právní ani daňové poradenství. Popisuje, jak je tento konkrétní lokální účetní systém organizován a jak by s ním měli uživatelé důsledně pracovat.
