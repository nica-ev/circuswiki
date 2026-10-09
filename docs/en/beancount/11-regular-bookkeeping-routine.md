---
lang: en
translation_id: beancount/11-regular-bookkeeping-routine
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Regular Bookkeeping Routine
description: A practical recurring checklist for keeping the ledgers current.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 11 - Regular Bookkeeping Routine

This page describes a practical routine for keeping the ledgers current.

## Weekly or biweekly routine

Use this when there are regular bank movements.

1. Open the correct Fava instance.
2. Check whether Fava shows errors.
3. Find the latest balance check.
4. Export new Sparkasse CSV data.
5. Convert the CSV with `csv2bean.py`.
6. Paste new entries into `Bank Dump`.
7. Classify entries into correct accounts.
8. Attach or reference receipts where needed.
9. Add a new balance check.
10. Reload Fava and resolve errors.
11. Review `Ausgaben:Sonstiges` and `Einnahmen:Sonstiges` for entries that should be more specific.

## Monthly routine

At month end:

1. Reconcile Sparkasse.
2. Reconcile PayPal if used.
3. Reconcile cash box if cash was used.
4. Check open liabilities to people.
5. Check active project balances.
6. Review unclassified `Sonstiges` entries.
7. Check missing receipts.
8. Check whether any finished project should be prepared for closing.

## Project reporting routine

Before preparing a project report or Verwendungsnachweis:

1. Open the project account pages in Fava.
2. Export or review all project income and expenses.
3. Confirm the categories match the funder budget lines.
4. Confirm all receipts and honorarium documents exist.
5. Check whether repayments, cancellations, and reimbursements are booked as corrections rather than false income.
6. Confirm the project asset balance is explainable.
7. If the project is finished, move remaining money correctly and close the project accounts.

## Year-end routine

At year end:

1. Reconcile all bank accounts.
2. Reconcile PayPal.
3. Reconcile cash boxes.
4. Check liabilities.
5. Check open project balances.
6. Ensure all receipts are stored and linked or findable.
7. Review income and expense categories.
8. Add final balance checks.
9. Prepare reports from Fava.
10. Archive exported CSVs and supporting documents.

## Quality checks

A ledger is in good shape when:

- Fava opens without errors.
- Latest Sparkasse balance check matches the bank.
- PayPal and cash balances are checked where relevant.
- Project balances are intentional and explainable.
- Closed projects have zero asset balance.
- `Sonstiges` accounts do not contain avoidable uncategorised entries.
- Receipts for expenses can be found.
- Comments explain unusual corrections or assumptions.

## Handover checklist for another person

Before handing bookkeeping to someone else:

- Show them the correct ledger file for each association.
- Show them how to start Fava.
- Show them the latest balance check.
- Show them how CSV imports are staged in `Bank Dump`.
- Show them where receipts are stored.
- Show them one example project from funding income to final closing.
- Point them to this documentation folder.
