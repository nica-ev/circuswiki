---
lang: en
translation_id: beancount/05-accounts-and-categories
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Accounts and Categories
description: Explains the German account structure and category conventions used in the ledgers.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 05 - Accounts and Categories

This page explains the account structure used in the ledgers.

## Naming language

The account names are German. Keep using the existing account names to keep reports consistent.

| German | English meaning |
| --- | --- |
| `Vermoegen` | Assets |
| `Verbindlichkeiten` | Liabilities |
| `Einnahmen` | Income |
| `Ausgaben` | Expenses |
| `Buero` | Office |
| `Verein` | Association/general association activity |
| `Projekt` | Project |
| `Barkasse` | Cash box |
| `Freies-Geld` | Free/unrestricted funds |

## Asset accounts

NICA examples:

- `Vermoegen:Bank:Sparkasse-NICA`
- `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:NICA:Barkasse`
- `Vermoegen:Inventar`

Tohuwabohu examples:

- `Vermoegen:Bank:Sparkasse-Tohuwabohu`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:Tohuwabohu:Barkasse`

## General income accounts

| Account | Use for |
| --- | --- |
| `Einnahmen:Vereinsbeitrag` | Membership fees. |
| `Einnahmen:Spende` | Donations. |
| `Einnahmen:Verleih` | Rental or lending income. |
| `Einnahmen:Sonstiges` | Other income that does not fit elsewhere. |

## General expense accounts

| Account | Use for |
| --- | --- |
| `Ausgaben:Buero:Miete` | Office or room rent. |
| `Ausgaben:Buero:Internet` | Internet and digital services. |
| `Ausgaben:Buero:Sonstiges` | Other office expenses. |
| `Ausgaben:Verein:Versicherung` | Association insurance. |
| `Ausgaben:Verein:Ehrenamt` | Volunteer allowances or association volunteer costs. |
| `Ausgaben:Essen` | Food expenses outside a specific project. |
| `Ausgaben:Sonstiges` | Temporary fallback for unclear expenses. |

`Ausgaben:Sonstiges` and `Einnahmen:Sonstiges` are useful during import, but should not become the final category if a more precise category exists.

## Project accounts

Project accounts follow this pattern:

```text
Vermoegen:Bank:Sparkasse-ASSOCIATION:PROJECT
Ausgaben:Projekt:PROJECT
Einnahmen:Projekt:PROJECT
```

Examples:

- `Vermoegen:Bank:Sparkasse-NICA:25-ZGV`
- `Ausgaben:Projekt:25-ZGV:Honorar`
- `Einnahmen:Projekt:25-ZGV:Sachmittel`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:TOHUCON-25`
- `Ausgaben:Projekt:TOHUCON-25:Essen`
- `Einnahmen:Projekt:TOHUCON-25:ConTickets`

## Typical project subcategories

| Subcategory | Meaning |
| --- | --- |
| `Honorar` | Fees paid to people or received for work. |
| `Aufwand` | Effort or expense allowance. |
| `Sachmittel` | Materials and supplies. |
| `Sonstiges` | Other project costs or income. |
| `Pauschale` / `Pauschalen` | Lump sum or flat-rate project budget. |

## Liabilities to people

Liability accounts track money owed to people or paid back to people. Examples include `Verbindlichkeiten:Person:Marc-Bielert`, `Verbindlichkeiten:Person:Peter-Huhndorf`, and `Verbindlichkeiten:Person:Charleen-Hoffmann`.

## Choosing the correct account

1. Is this association-level or project-level?
2. If project-level, which project owns the money?
3. Is it income, expense, asset movement, or liability repayment?
4. Is there a precise category already open?
5. If there is no good category, use `Sonstiges` temporarily and add a comment.
