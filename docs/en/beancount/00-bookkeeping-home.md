---
lang: en
translation_id: beancount/00-bookkeeping-home
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Bookkeeping System Documentation
description: Overview and starting point for the NICA e.V. and Tohuwabohu Halle e.V. Beancount bookkeeping documentation.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# Bookkeeping System Documentation

This documentation explains how the bookkeeping system for NICA e.V. and Tohuwabohu Halle e.V. works from a normal user perspective.

The system uses plaintext accounting files in Beancount and a browser interface called Fava. You do not need to understand programming to use it, but you do need to follow the bookkeeping workflow carefully: import bank data, classify transactions, attach receipts where needed, and check balances.

## Start here

- [01 - System Overview](01-system-overview.md)
- [02 - Opening Fava](02-opening-fava.md)
- [03 - Folder and File Map](03-folder-and-file-map.md)
- [04 - Beancount Basics for Users](04-beancount-basics-for-users.md)
- [05 - Accounts and Categories](05-accounts-and-categories.md)
- [06 - Entering and Editing Transactions](06-entering-and-editing-transactions.md)
- [07 - Bank CSV Import and Reconciliation](07-bank-csv-import-and-reconciliation.md)
- [08 - Projects and Restricted Funds](08-projects-and-restricted-funds.md)
- [09 - Receipts and Documents](09-receipts-and-documents.md)
- [10 - Fava Dashboards and Reports](10-fava-dashboards-and-reports.md)
- [11 - Regular Bookkeeping Routine](11-regular-bookkeeping-routine.md)
- [12 - Troubleshooting](12-troubleshooting.md)
- [13 - Glossary](13-glossary.md)

## The most important rule

The accounting file is the source of truth. Fava only displays what is written in the `.beancount` files. If something looks wrong in Fava, correct the Beancount entry and reload Fava.

## Current ledgers

| Organisation | Main file | Fava address | Port |
| --- | --- | --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` | `http://127.0.0.1:4998/` | `4998` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` | `http://127.0.0.1:4999/` | `4999` |

## What this documentation is not

This is not legal or tax advice. It describes how this specific local bookkeeping system is organised and how users should work with it consistently.
