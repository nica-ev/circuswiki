---
lang: en
translation_id: beancount/13-glossary
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Glossary
description: Definitions of bookkeeping, Beancount, Fava, and project accounting terms used in this documentation.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 13 - Glossary

## Account

A named place where Beancount records money or value. Example: `Ausgaben:Buero:Miete`.

## Asset

Something the association owns or controls, such as bank money, PayPal balance, cash, or inventory. In this system assets are under `Vermoegen`.

## Balance check

A line that confirms an account has a specific balance on a specific date. Balance checks are used to verify that the ledger matches bank, PayPal, or cash records.

## Bank Dump

A staging section near the bottom of the ledger where imported bank transactions are first pasted before they are fully classified.

## Beancount

The plaintext accounting format used as the system's source of truth.

## CSV

A spreadsheet-like export file. Sparkasse exports CSV files that are converted into Beancount transactions.

## Equity

Beancount account family used for opening balances and balancing historical starting points.

## Fava

The browser interface for viewing and working with Beancount ledgers.

## Fava Dashboards

An extension that adds custom dashboard pages to Fava.

## Freies-Geld

Free or unrestricted money that is not assigned to a restricted project budget.

## Income

Money received. In this system income accounts start with `Einnahmen`.

## Ledger

The accounting file containing accounts, transactions, balance checks, and documents. The main ledgers are `nica.beancount` and `2023.beancount`.

## Liability

Money owed to someone else. In this system liabilities are under `Verbindlichkeiten`.

## Payee

The person or organisation named in a transaction.

## Project account

An account used to track money for a specific project separately from general association money.

## Reconciliation

The process of checking that Beancount and the real bank or PayPal balance match.

## Receipt

A document proving an expense, such as an invoice, contract, or cash receipt.

## Sonstiges

German for miscellaneous or other. Useful as a temporary fallback, but specific categories are better for final bookkeeping.

## Transaction

A dated accounting entry describing one financial event.

## Verwendungsnachweis

A project funder report explaining how granted money was used.
