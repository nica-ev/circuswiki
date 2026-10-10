---
lang: sk
translation_id: beancount/08-projects-and-restricted-funds
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Projekty a účelové fondy
description: Vysvetľuje, ako sú projektové peniaze a účelové fondy reprezentované a kontrolované.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/08-projects-and-restricted-funds.md
translation_source_body_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_source_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:29+00:00
translation_source_localized_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_source_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:29+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 08 - Projekty a účelovo viazané prostriedky

Projekty sú kľúčové pre tento účtovný systém. Mnohé granty a aktivity sa musia sledovať oddelene od peňazí voľného združenia.

## Čo znamená projekt v účtovníctve

| Typ účtu | Príklad | Účel |
| --- | --- | --- |
| Projektový majetok | `Vermoegen:Bank:Sparkasse-NICA:25-ZGV` | Interný zostatok projektových peňazí. |
| Projektové príjmy | `Einnahmen:Projekt:25-ZGV:Sachmittel` | Financovanie projektu alebo projektové príjmy. |
| Projektové výdavky | `Ausgaben:Projekt:25-ZGV:Sachmittel` | Projektové výdavky. |

Skutočný bankový účet môže byť jeden účet Sparkasse, ale účtovný systém oddeľuje interné projektové zostatky, aby tím videl, čo patrí ku ktorému projektu.

## Aktívne a uzatvorené projekty

Aktívne projekty majú otvorené účty a relevantné zostatky. Uzatvorené projekty zvyčajne majú konečnú kontrolu zostatku vo výške `0,00 EUR` a smernice `close` pre účet projektového majetku, príjmov a výdavkov.

Nezadávajte nové transakcie do uzatvorených projektov, pokiaľ zámerne neotvárate alebo neopravujete historické údaje.

## Aktuálne príklady v NICA

- `26-JEP-Buehnenreif`
- `25-ZGV`
- `25-CircusWiki`
- `25-Machen-UnitedAges`
- `25-Erasmus`
- uzatvorené projekty z roku 2024, ako napríklad `24-AWO`, `24-HONY`, `24-Peter`

## Aktuálne príklady v Tohuwabohu

- `VHS-TOHU-25`
- `ZMS-TOHU-25`
- `CEDU-25`
- `TOHUCON-25`
- uzatvorené projekty ako `Revierpionier-25`, `OAC-25`, `TohuCon2024`, `ZGV-TOHU-24`, `TohuCon2023`

## Vytvorenie nového projektu

Nový projekt zvyčajne potrebuje otvorené účty pred zadaním transakcií.

```beancount
2026-01-01 open Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject:Honorar
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sachmittel
2026-01-01 open Ausgaben:Projekt:26-NewProject:Aufwand
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sonstiges
2026-01-01 open Einnahmen:Projekt:26-NewProject
2026-01-01 open Einnahmen:Projekt:26-NewProject:Honorar
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sachmittel
2026-01-01 open Einnahmen:Projekt:26-NewProject:Aufwand
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sonstiges
```

Otvárajte len kategórie, ktoré sú pre projekt skutočne užitočné.

## Zadanie financovania projektu

```beancount
2026-02-01 ! "Funding Body" "First payment NewProject"
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject  3000.00 EUR
  Einnahmen:Projekt:26-NewProject:Sachmittel
```

## Zadanie projektových výdavkov

```beancount
2026-02-10 ! "Supplier" "Project material"
  Ausgaben:Projekt:26-NewProject:Sachmittel  250.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject
```

## Pochopenie projektových zostatkov

Kladný zostatok projektového majetku znamená, že projektu sú stále pridelené peniaze. Nulový zostatok projektového majetku znamená, že projekt nemá žiadny interný bankový zostatok. Záporný zostatok projektového majetku zvyčajne znamená, že projekt vynaložil viac, ako boli jeho pridelené prostriedky, alebo chýba alokácia.

## Uzatvorenie projektu

Pred uzatvorením projektu musia byť zadané všetky príjmy a výdavky, potvrdenky musia byť dohľadateľné, účet projektového majetku musí byť presne nula a akékoľvek zostávajúce peniaze musia byť správne presunuté alebo vrátené.

```beancount
2026-12-31 balance Vermoegen:Bank:Sparkasse-NICA:26-NewProject 0.00 EUR
2026-12-31 close Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-12-31 close Ausgaben:Projekt:26-NewProject
2026-12-31 close Einnahmen:Projekt:26-NewProject
```

Ak boli podúčty otvorené samostatne, uzatvorte aj tie.
