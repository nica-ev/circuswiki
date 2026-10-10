---
lang: nl
translation_id: beancount/08-projects-and-restricted-funds
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Projecten en Gereserveerde Fondsen
description: Legt uit hoe projectgeld en gereserveerde fondsen worden weergegeven en gecontroleerd.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/08-projects-and-restricted-funds.md
translation_source_body_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_source_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:07+00:00
translation_source_localized_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_source_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:07+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 08 - Projecten en Gereserveerde Fondsen

Projecten vormen de kern van dit boekhoudsysteem. Veel subsidies en activiteiten moeten apart worden bijgehouden van het geld van de vrije vereniging.

## Wat een project betekent in het grootboek

| Rekeningtype | Voorbeeld | Doel |
| --- | --- | --- |
| Projectbezitting | `Vermoegen:Bank:Sparkasse-NICA:25-ZGV` | Interne balans van projectgeld. |
| Projectinkomsten | `Einnahmen:Projekt:25-ZGV:Sachmittel` | Projectfinanciering of projectinkomsten. |
| Projectuitgaven | `Ausgaben:Projekt:25-ZGV:Sachmittel` | Projectuitgaven. |

Het werkelijke bankrekeningnummer kan één Sparkasse-rekening zijn, maar het grootboek scheidt interne projectbalansen zodat het team kan zien wat bij elk project hoort.

## Actieve en afgesloten projecten

Actieve projecten hebben openstaande rekeningen en relevante saldi. Afgesloten projecten hebben meestal een definitieve saldocheck van `0,00 EUR` en `close`-instructies voor de projectbezittingen, inkomsten en uitgavenrekeningen.

Boek geen nieuwe transacties in afgesloten projecten, tenzij u opzettelijk historische gegevens heropent of corrigeert.

## Huidige voorbeelden in NICA

- `26-JEP-Buehnenreif`
- `25-ZGV`
- `25-CircusWiki`
- `25-Machen-UnitedAges`
- `25-Erasmus`
- afgesloten projecten uit 2024 zoals `24-AWO`, `24-HONY`, `24-Peter`

## Huidige voorbeelden in Tohuwabohu

- `VHS-TOHU-25`
- `ZMS-TOHU-25`
- `CEDU-25`
- `TOHUCON-25`
- afgesloten projecten zoals `Revierpionier-25`, `OAC-25`, `TohuCon2024`, `ZGV-TOHU-24`, `TohuCon2023`

## Een nieuw project aanmaken

Voor een nieuw project moeten normaal gesproken rekeningen worden geopend voordat transacties worden ingevoerd.

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

Open alleen categorieën die daadwerkelijk nuttig zijn voor het project.

## Projectfinanciering boeken

```beancount
2026-02-01 ! "Funding Body" "First payment NewProject"
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject  3000.00 EUR
  Einnahmen:Projekt:26-NewProject:Sachmittel
```

## Projectuitgaven boeken

```beancount
2026-02-10 ! "Supplier" "Project material"
  Ausgaben:Projekt:26-NewProject:Sachmittel  250.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject
```

## Projectsaldi begrijpen

Een positief projectbezitsaldo betekent dat er nog geld aan dat project is toegewezen. Een projectbezitsaldo van nul betekent dat het project geen resterend intern banksaldo heeft. Een negatief projectbezitsaldo betekent meestal dat het project meer heeft uitgegeven dan de toegewezen middelen, of dat een toewijzing ontbreekt.

## Een project afsluiten

Voordat een project wordt afgesloten, moeten alle inkomsten en uitgaven zijn ingevoerd, moeten de bonnen vindbaar zijn, moet het projectbezitsaldo precies nul zijn, en moet eventueel resterend geld correct zijn verplaatst of teruggestuurd.

```beancount
2026-12-31 balance Vermoegen:Bank:Sparkasse-NICA:26-NewProject 0.00 EUR
2026-12-31 close Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-12-31 close Ausgaben:Projekt:26-NewProject
2026-12-31 close Einnahmen:Projekt:26-NewProject
```

Sluit ook subrekeningen af als deze afzonderlijk zijn geopend.
