---
lang: cs
translation_id: beancount/01-system-overview
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Přehled systému
description: Vysvětluje účel, komponenty a běžný pracovní postup uživatele účetního systému.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/01-system-overview.md
translation_source_body_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_source_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:03+00:00
translation_source_localized_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_source_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:03+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 01 - Přehled systému

## Účel

Účetní systém zaznamenává veškerou finanční činnost spolků strukturovaným a kontrolovatelným způsobem. Je navržen tak, aby odpovídal na běžné účetní otázky:

- Kolik peněz je aktuálně k dispozici?
- Které příjmy a výdaje patří samotnému spolku?
- Které příjmy a výdaje patří konkrétnímu projektu?
- Jsou zůstatky na účtech Sparkasse, PayPal a v hotovosti správné?
- Které účtenky a dokumenty patří ke kterým transakcím?
- Které projekty jsou aktivní, dokončené nebo již uzavřené?

## Hlavní komponenty

| Komponenta | Co dělá |
| --- | --- |
| Beancount | Formát účetních dat. Transakce jsou zapisovány v prostých textových souborech. |
| Fava | Rozhraní prohlížeče pro prohlížení a filtrování dat Beancount. |
| Fava Dashboards | Vlastní stránky s přehledy uvnitř Favě pro manažerský přehled a pohledy na projekty. |
| Obsidian | Systém poznámek, ze kterého lze otevřít účetnictví pomocí tlačítek. |
| Skripty pro import CSV | Pomocné skripty, které převádějí CSV exporty ze Sparkasse do záznamů Beancount. |

## Jak části do sebe zapadají

1. Bankovní nebo PayPal data jsou exportována jako CSV.
2. CSV je převedeno na dočasné záznamy Beancount.
3. Nové záznamy jsou zkopírovány do správného účetního souboru.
4. Uživatel kontroluje, klasifikuje a opravuje záznamy.
5. Kontroly zůstatků potvrzují, že účetní kniha odpovídá zůstatku v bance nebo na PayPalu.
6. Fava zobrazuje přehledy, stránky účtů, výkazy zisků a ztrát, rozvahy a přehledy.

## Dva samostatné spolky

| Spolek | Účetní kniha | Typický prefix účtu |
| --- | --- | --- |
| NICA e.V. | `nica.beancount` | `Sparkasse-NICA`, `NICA` |
| Tohuwabohu Halle e.V. | `2023.beancount` | `Sparkasse-Tohuwabohu`, `Tohuwabohu` |

Existuje také experimentální kombinovaný soubor: `1. Vereinsverwaltung/Buchhaltung/all.beancount`. Běžná denní práce by měla probíhat v individuální účetní knize příslušného spolku.

## Základní pracovní postup

1. Otevřete správnou instanci Favě.
2. Najděte poslední dokončenou kontrolu zůstatku.
3. Exportujte nové bankovní transakce ze Sparkasse počínaje posledním zkontrolovaným datem.
4. Převeďte CSV do formátu Beancount.
5. Vložte vygenerované záznamy nejprve do sekce `Bank Dump`.
6. Přesuňte nebo klasifikujte záznamy do správných sekcí spolku nebo projektu.
7. V případě potřeby přidejte účtenky, odkazy, komentáře nebo štítky.
8. Přidejte novou kontrolu zůstatku.
9. Znovu načtěte Favě a ověřte, že nejsou žádné chyby.

## Co by se měl nový uživatel naučit jako první

1. [Otevření Favě](02-opening-fava.md)
2. [Základy Beancount pro uživatele](04-beancount-basics-for-users.md)
3. [Import a odsouhlasení bankovních CSV](07-bank-csv-import-and-reconciliation.md)
4. [Účty a kategorie](05-accounts-and-categories.md)
5. [Projekty a účelově vázané fondy](08-projects-and-restricted-funds.md)
