---
lang: en
translation_id: beancount/07-bank-csv-import-and-reconciliation
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Bank CSV Import and Reconciliation
description: Workflow for importing Sparkasse CSV data and reconciling bank balances.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 07 - Bank CSV Import and Reconciliation

This workflow brings new Sparkasse transactions into Beancount and confirms that the ledger still matches the real bank account.

## Where imports happen

| Association | Import folder | Script | Output file |
| --- | --- | --- | --- |
| NICA | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/test` | `csv2bean.py` | `beancount_file.beancount` |
| Tohuwabohu | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/test` | `csv2bean.py` | `beancount_file.beancount` |

## Before exporting from Sparkasse

1. Open the correct ledger file.
2. Find the `Balance Checks` section.
3. Find the latest balance date for the Sparkasse account.
4. Also check the `Bank Dump` section at the bottom for the last imported date.
5. Use the later of those dates as your starting point.

This avoids missing transactions or importing the same period twice.

## Exporting from Sparkasse

1. Open the account overview.
2. Filter by date range.
3. Start from the last checked or imported date.
4. End with today or the desired reconciliation date.
5. Export as `Excel (CSV-CAMT V2)`.
6. Copy the downloaded CSV into the correct `test` folder.

The scripts expect the Sparkasse CSV-CAMT-V2 format with semicolon-separated columns.

## Converting the CSV

Open a terminal in the correct `test` folder and run:

```powershell
python csv2bean.py "NAME-OF-DOWNLOADED-FILE.CSV"
```

Example:

```powershell
python csv2bean.py "20260312-1894137139-umsatz.CSV"
```

If it works, the script prints `Process finished.` and creates or overwrites `beancount_file.beancount`.

## What the converter does

The converter creates basic Beancount entries:

- Incoming amounts go to the Sparkasse asset account and `Einnahmen:Sonstiges` by default.
- Outgoing amounts go to `Ausgaben:Sonstiges` and the Sparkasse asset account by default.
- Some income descriptions are automatically classified as `Einnahmen:Vereinsbeitrag`.
- Some Tohuwabohu-related text may be classified as a project income account.

The converter is only a first pass. It does not know the final bookkeeping meaning of every transaction.

## Copying into the main ledger

1. Open `test/beancount_file.beancount`.
2. Ignore the generated option header.
3. Copy only the transactions.
4. Paste them into the main ledger under `Bank Dump` first.
5. Add a dated separator for the import date if needed.

```beancount
****************************************************************************
** 2026-01-13
****************************************************************************
```

The `Bank Dump` is a staging area. Imported transactions can later be moved into the correct thematic or project section.

## Classifying imported entries

For each imported transaction, decide:

- Is it association-level or project-level?
- Is it income or expense?
- Is it a reimbursement or liability payment?
- Does it belong to `Freies-Geld` or a project-specific asset account?
- Is there a receipt or invoice to attach?

Replace broad fallback accounts such as `Ausgaben:Sonstiges` when a more accurate account exists.

## Adding a balance check

NICA example:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Tohuwabohu example:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-Tohuwabohu 2345.67 EUR
```

Use the balance shown by Sparkasse for that exact date.

## Validating in Fava

1. Save the ledger file.
2. Reload Fava.
3. Check for errors at the top of the Fava page.
4. Open the Sparkasse account page.
5. Confirm the running balance and latest transactions.
6. Check the Balance Sheet.
7. Check project dashboards if project accounts were affected.

## If the balance check fails

Common causes:

- The CSV export missed one day at the beginning or end.
- A transaction was imported twice.
- A transaction was pasted into the wrong association ledger.
- A number was edited incorrectly.
- A project split used the wrong sign.
- PayPal or cash movements were not also recorded.

Do not remove the balance check just to make the error disappear. Fix the underlying transaction difference.
