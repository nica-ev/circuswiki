---
lang: nl
translation_id: beancount/00-bookkeeping-home
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Boekhoudsysteem Documentatie
description: Overzicht en startpunt voor de NICA e.V. en Tohuwabohu Halle e.V. Beancount boekhoud documentatie.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/00-bookkeeping-home.md
translation_source_body_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_source_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:03:44+00:00
translation_source_localized_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_source_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:03:44+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# Documentatie Boekhoudsysteem

Deze documentatie legt uit hoe het boekhoudsysteem voor NICA e.V. en Tohuwabohu Halle e.V. werkt vanuit het perspectief van een normale gebruiker.

Het systeem maakt gebruik van platte tekst boekhoudbestanden in Beancount en een browsertoepassing genaamd Fava. Je hoeft geen programmeerkennis te hebben om het te gebruiken, maar je moet wel zorgvuldig de boekhoudworkflow volgen: bankgegevens importeren, transacties classificeren, waar nodig bonnetjes bijvoegen en saldi controleren.

## Begin hier

- [01 - Overzicht Systeem](01-system-overview.md)
- [02 - Fava Openen](02-opening-fava.md)
- [03 - Map- en Bestandsstructuur](03-folder-and-file-map.md)
- [04 - Beancount Basis voor Gebruikers](04-beancount-basics-for-users.md)
- [05 - Rekeningen en Categorieën](05-accounts-and-categories.md)
- [06 - Transacties Invoeren en Bewerken](06-entering-and-editing-transactions.md)
- [07 - Bank CSV Import en Afstemming](07-bank-csv-import-and-reconciliation.md)
- [08 - Projecten en Bestemmingsgelden](08-projects-and-restricted-funds.md)
- [09 - Bonnen en Documenten](09-receipts-and-documents.md)
- [10 - Fava Dashboards en Rapporten](10-fava-dashboards-and-reports.md)
- [11 - Routinematige Boekhouding](11-regular-bookkeeping-routine.md)
- [12 - Probleemoplossing](12-troubleshooting.md)
- [13 - Woordenlijst](13-glossary.md)

## De belangrijkste regel

Het boekhoudbestand is de bron van waarheid. Fava toont alleen wat er in de `.beancount` bestanden staat. Als iets er verkeerd uitziet in Fava, corrigeer dan de Beancount-invoer en laad Fava opnieuw.

## Huidige grootboeken

| Organisatie | Hoofdbestand | Fava adres | Poort |
| --- | --- | --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` | `http://127.0.0.1:4998/` | `4998` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` | `http://127.0.0.1:4999/` | `4999` |

## Wat deze documentatie niet is

Dit is geen juridisch of fiscaal advies. Het beschrijft hoe dit specifieke lokale boekhoudsysteem is georganiseerd en hoe gebruikers er consequent mee moeten werken.
