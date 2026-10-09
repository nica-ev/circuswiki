---
lang: en
translation_id: beancount/06-entering-and-editing-transactions
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Entering and Editing Transactions
description: Describes how users review, classify, correct, and enter bookkeeping transactions.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 06 - Entering and Editing Transactions

Most entries come from imported bank data, but users still need to review, classify, correct, and sometimes enter transactions manually.

## Transaction status

The ledgers commonly use `!` in imported transactions:

```beancount
2026-03-12 ! "Payee" "Bank text"
```

Use this as the normal marker unless the team decides on a stricter status convention.

## Basic income entry

```beancount
2026-01-15 ! "Max Mustermann" "Mitgliedsbeitrag 2026"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  60.00 EUR
  Einnahmen:Vereinsbeitrag
```

## Basic expense entry

```beancount
2026-01-20 ! "Provider Name" "Invoice 123"
  Ausgaben:Buero:Sonstiges  25.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Project income

```beancount
2026-02-10 ! "Funding Body" "Grant payment project 25-ZGV"
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV  5000.00 EUR
  Einnahmen:Projekt:25-ZGV:Sachmittel
```

## Project expense

```beancount
2026-02-15 ! "Person Name" "Honorar project 25-ZGV"
  Ausgaben:Projekt:25-ZGV:Honorar  450.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV
```

## Internal movement between project and free funds

Sometimes a transaction must allocate bank money between a project-specific asset account and free funds. The real bank account is one physical Sparkasse account, but the ledger tracks internal project balances separately.

```beancount
2026-02-20 ! "Internal allocation" "Move remaining project funds to free money"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  100.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV      -100.00 EUR
```

Only make internal transfers when you understand why the internal project balance must change.

## Reimbursements to people

If someone paid privately and is reimbursed later, the clean pattern is usually to record the expense against a liability and then clear the liability with the bank payment.

```beancount
2026-03-01 ! "Shop" "Material bought by Marc"
  Ausgaben:Projekt:25-ZGV:Sachmittel  35.00 EUR
  Verbindlichkeiten:Person:Marc-Bielert
```

```beancount
2026-03-05 ! "Marc Bielert" "Reimbursement material"
  Verbindlichkeiten:Person:Marc-Bielert  35.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Comments for unclear decisions

```beancount
; Unclear whether this belongs to CEDU-25 or free association funds. Check invoice.
2026-03-10 ! "Vendor" "Invoice 456"
  Ausgaben:Sonstiges  120.00 EUR
  Vermoegen:Bank:Sparkasse-Tohuwabohu
```

## Editing safely

Before editing, check:

- You are in the correct association ledger.
- You are not editing the generated import output as if it were the final ledger.
- The transaction date is correct.
- The amount uses a dot as decimal separator, for example `12.50 EUR`.
- Account names are spelled exactly like existing accounts.
- Project transactions use the project asset account and project income/expense category consistently.

After editing, save the file, reload Fava, check for errors, and inspect the relevant account page.
