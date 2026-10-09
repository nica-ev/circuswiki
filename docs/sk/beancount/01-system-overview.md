---
lang: sk
translation_id: beancount/01-system-overview
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Prehľad systému
description: Vysvetľuje účel, komponenty a bežný pracovný postup používateľa účtovného systému.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/01-system-overview.md
translation_source_body_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_source_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:33:07+00:00
translation_source_localized_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_source_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:33:07+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 01 - Prehľad systému

## Účel

Účtovný systém zaznamenáva všetku finančnú činnosť združení štruktúrovaným a kontrolovateľným spôsobom. Je navrhnutý tak, aby odpovedal na bežné účtovné otázky:

- Koľko peňazí je momentálne k dispozícii?
- Ktoré príjmy a výdavky patria samotnému združeniu?
- Ktoré príjmy a výdavky patria konkrétnemu projektu?
- Sú zostatky na účtoch Sparkasse, PayPal a v hotovosti správne?
- Ktoré doklady a dokumenty patria k jednotlivým transakciám?
- Ktoré projekty sú aktívne, dokončené alebo už uzatvorené?

## Hlavné komponenty

| Komponent | Čo robí |
| --- | --- |
| Beancount | Formát účtovných dát. Transakcie sú zapisované v textových súboroch. |
| Fava | Rozhranie prehliadača na prezeranie a filtrovanie dát Beancount. |
| Fava Dashboards | Vlastné prehľadové stránky vo Favě pre manažérsky prehľad a pohľady na projekty. |
| Obsidian | Systém poznámok, z ktorého je možné otvoriť účtovníctvo prostredníctvom tlačidiel. |
| CSV importné skripty | Pomocné skripty, ktoré konvertujú CSV exporty zo Sparkasse na záznamy Beancount. |

## Ako spolu časti fungujú

1. Bankové alebo PayPal dáta sa exportujú ako CSV.
2. CSV sa konvertuje na dočasné záznamy Beancount.
3. Nové záznamy sa skopírujú do správneho účtovného súboru.
4. Používateľ skontroluje, klasifikuje a opraví záznamy.
5. Kontroly zostatkov potvrdzujú, že účtovný súbor zodpovedá bankovému alebo PayPal zostatku.
6. Fava zobrazuje prehľady, stránky účtov, výkazy ziskov a strát, súvahy a prehľadové panely.

## Dve samostatné združenia

| Združenie | Účtovný súbor | Typický predpona účtu |
| --- | --- | --- |
| NICA e.V. | `nica.beancount` | `Sparkasse-NICA`, `NICA` |
| Tohuwabohu Halle e.V. | `2023.beancount` | `Sparkasse-Tohuwabohu`, `Tohuwabohu` |

Existuje aj experimentálny kombinovaný súbor: `1. Vereinsverwaltung/Buchhaltung/all.beancount`. Bežná denná práca by sa mala vykonávať v individuálnom účtovnom súbore príslušného združenia.

## Základný pracovný postup

1. Otvorte správnu inštanciu Favy.
2. Nájdite poslednú dokončenú kontrolu zostatku.
3. Exportujte nové bankové transakcie zo Sparkasse počnúc od posledného kontrolovaného dátumu.
4. Konvertujte CSV do formátu Beancount.
5. Vložené vygenerované záznamy najprv do sekcie `Bank Dump`.
6. Presuňte alebo klasifikujte záznamy do správnych sekcií združenia alebo projektu.
7. V prípade potreby pridajte doklady, odkazy, komentáre alebo značky.
8. Pridajte novú kontrolu zostatku.
9. Znovu načítajte Favu a overte, že nie sú žiadne chyby.

## Čo by sa mal nový používateľ naučiť najprv

1. [Otvorenie Favy](02-opening-fava.md)
2. [Základy Beancount pre používateľov](04-beancount-basics-for-users.md)
3. [Import bankových CSV a zúčtovanie](07-bank-csv-import-and-reconciliation.md)
4. [Účty a kategórie](05-accounts-and-categories.md)
5. [Projekty a účelové fondy](08-projects-and-restricted-funds.md)
