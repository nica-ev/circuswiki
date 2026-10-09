---
lang: en
translation_id: beancount/08-projects-and-restricted-funds
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Projects and Restricted Funds
description: Explains how project money and restricted funds are represented and checked.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 08 - Projects and Restricted Funds

Projects are central to this bookkeeping system. Many grants and activities must be tracked separately from free association money.

## What a project means in the ledger

| Account type | Example | Purpose |
| --- | --- | --- |
| Project asset | `Vermoegen:Bank:Sparkasse-NICA:25-ZGV` | Internal balance of project money. |
| Project income | `Einnahmen:Projekt:25-ZGV:Sachmittel` | Project funding or project income. |
| Project expense | `Ausgaben:Projekt:25-ZGV:Sachmittel` | Project spending. |

The real bank account may be one Sparkasse account, but the ledger separates internal project balances so the team can see what belongs to each project.

## Active and closed projects

Active projects have open accounts and relevant balances. Closed projects usually have a final `0.00 EUR` balance check and `close` directives for the project asset, income, and expense accounts.

Do not book new transactions into closed projects unless you intentionally reopen or correct historical data.

## Current examples in NICA

- `26-JEP-Buehnenreif`
- `25-ZGV`
- `25-CircusWiki`
- `25-Machen-UnitedAges`
- `25-Erasmus`
- closed 2024 projects such as `24-AWO`, `24-HONY`, `24-Peter`

## Current examples in Tohuwabohu

- `VHS-TOHU-25`
- `ZMS-TOHU-25`
- `CEDU-25`
- `TOHUCON-25`
- closed projects such as `Revierpionier-25`, `OAC-25`, `TohuCon2024`, `ZGV-TOHU-24`, `TohuCon2023`

## Creating a new project

A new project normally needs accounts opened before transactions are entered.

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

Only open categories that are actually useful for the project.

## Booking project funding

```beancount
2026-02-01 ! "Funding Body" "First payment NewProject"
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject  3000.00 EUR
  Einnahmen:Projekt:26-NewProject:Sachmittel
```

## Booking project expenses

```beancount
2026-02-10 ! "Supplier" "Project material"
  Ausgaben:Projekt:26-NewProject:Sachmittel  250.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject
```

## Understanding project balances

A positive project asset balance means money is still allocated to that project. A zero project asset balance means the project has no remaining internal bank balance. A negative project asset balance usually means the project has spent more than its allocated funds or an allocation is missing.

## Closing a project

Before closing a project, all income and expenses must be entered, receipts must be findable, the project asset account must be exactly zero, and any remaining money must be moved or returned correctly.

```beancount
2026-12-31 balance Vermoegen:Bank:Sparkasse-NICA:26-NewProject 0.00 EUR
2026-12-31 close Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-12-31 close Ausgaben:Projekt:26-NewProject
2026-12-31 close Einnahmen:Projekt:26-NewProject
```

Close subaccounts too if they were opened separately.
