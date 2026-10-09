---
lang: en
translation_id: beancount/01-system-overview
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: System Overview
description: Explains the purpose, components, and normal user workflow of the bookkeeping system.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 01 - System Overview

## Purpose

The bookkeeping system records all financial activity for the associations in a structured, checkable way. It is designed to answer normal bookkeeping questions:

- How much money is currently available?
- Which income and expenses belong to the association itself?
- Which income and expenses belong to a specific project?
- Are Sparkasse, PayPal, and cash balances correct?
- Which receipts and documents belong to which transactions?
- Which projects are active, finished, or already closed?

## Main components

| Component | What it does |
| --- | --- |
| Beancount | The accounting data format. Transactions are written in plain text files. |
| Fava | The browser interface for viewing and filtering the Beancount data. |
| Fava Dashboards | Custom dashboard pages inside Fava for management overview and project views. |
| Obsidian | The note system from which bookkeeping can be opened through buttons. |
| CSV import scripts | Helper scripts that convert Sparkasse CSV exports into Beancount entries. |

## How the parts fit together

1. Bank or PayPal data is exported as CSV.
2. The CSV is converted into temporary Beancount entries.
3. The new entries are copied into the correct ledger file.
4. The user checks, classifies, and corrects the entries.
5. Balance checks confirm that the ledger matches the bank or PayPal balance.
6. Fava displays reports, account pages, income statements, balance sheets, and dashboards.

## Two separate associations

| Association | Ledger | Typical account prefix |
| --- | --- | --- |
| NICA e.V. | `nica.beancount` | `Sparkasse-NICA`, `NICA` |
| Tohuwabohu Halle e.V. | `2023.beancount` | `Sparkasse-Tohuwabohu`, `Tohuwabohu` |

There is also an experimental combined file: `1. Vereinsverwaltung/Buchhaltung/all.beancount`. Normal day-to-day work should happen in the individual ledger of the relevant association.

## Basic workflow

1. Open the correct Fava instance.
2. Find the last completed balance check.
3. Export new bank transactions from Sparkasse starting from the last checked date.
4. Convert the CSV into Beancount format.
5. Paste the generated entries into the `Bank Dump` section first.
6. Move or classify entries into the correct association or project sections.
7. Add receipts, links, comments, or tags when needed.
8. Add a new balance check.
9. Reload Fava and verify there are no errors.

## What a new user should learn first

1. [Opening Fava](02-opening-fava.md)
2. [Beancount Basics for Users](04-beancount-basics-for-users.md)
3. [Bank CSV Import and Reconciliation](07-bank-csv-import-and-reconciliation.md)
4. [Accounts and Categories](05-accounts-and-categories.md)
5. [Projects and Restricted Funds](08-projects-and-restricted-funds.md)
