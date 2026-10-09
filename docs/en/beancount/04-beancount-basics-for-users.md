---
lang: en
translation_id: beancount/04-beancount-basics-for-users
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Beancount Basics for Users
description: Introduces the Beancount text format and the transaction patterns used in the ledgers.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 04 - Beancount Basics for Users

Beancount stores accounting as readable text. Each transaction says what happened, on which date, who was involved, and which accounts changed.

## Basic transaction shape

```beancount
2026-01-13 ! "Tragerwerk Soziale Dienste in Sachsen-Anhalt GmbH" "RgNr. T-2504"
  Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld  680.00 EUR
  Einnahmen:Sonstiges
```

| Part | Meaning |
| --- | --- |
| `2026-01-13` | Date of the transaction. |
| `!` | Status marker. In this system it is commonly used for imported or not-yet-finally-reviewed entries. |
| First quoted text | Payee or sender. |
| Second quoted text | Description or booking text from the bank. |
| First account line | Where money went or came from. |
| Second account line | The opposite category. If no amount is written, Beancount calculates it automatically. |

## Account names

Account names are separated by colons:

```text
Vermoegen:Bank:Sparkasse-NICA:Freies-Geld
```

Read it from left to right: asset, bank account, NICA Sparkasse, freely available funds.

## The five account families

| Family | Meaning | Example |
| --- | --- | --- |
| `Vermoegen` | Assets: bank, PayPal, cash, inventory. | `Vermoegen:Bank:Sparkasse-NICA` |
| `Verbindlichkeiten` | Liabilities: money owed to people or others. | `Verbindlichkeiten:Person:Marc-Bielert` |
| `Equity` | Opening balances and balancing entries. | `Equity:Opening-Balances` |
| `Einnahmen` | Income. | `Einnahmen:Vereinsbeitrag` |
| `Ausgaben` | Expenses. | `Ausgaben:Buero:Miete` |

## Income and expense signs

In Beancount reports, income often appears with a negative sign internally and expenses with a positive sign. Fava and the dashboards often present these values in a more user-friendly way. Do not change transactions just because an income number looks negative in a raw query.

## Balance checks

A balance check states that an account must have a specific balance on a date:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

If Beancount cannot match that balance from the transactions before that date, Fava shows an error. Balance checks are the main quality control mechanism.

## Open and close accounts

Before an account is used, it is opened:

```beancount
2025-04-01 open Ausgaben:Projekt:25-ZGV:Honorar
```

When a project is finished and the project account is zero, it can be closed:

```beancount
2026-02-27 close Ausgaben:Projekt:TOHUCON-25
```

Closed accounts should normally not receive new transactions.

## Comments and documents

Lines starting with `;` are comments. They explain decisions or uncertain situations and do not affect the numbers.

Receipts can be connected with `document` lines:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```
