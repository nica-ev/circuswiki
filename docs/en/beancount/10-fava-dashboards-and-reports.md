---
lang: en
translation_id: beancount/10-fava-dashboards-and-reports
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Fava Dashboards and Reports
description: Overview of Fava reports and custom dashboards used for bookkeeping review.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 10 - Fava Dashboards and Reports

Fava provides standard accounting reports. The system also uses `fava-dashboards` for custom overview pages.

## Standard Fava views

| View | Use for |
| --- | --- |
| Balance Sheet | Checking assets, liabilities, free funds, PayPal, cash, and project balances. |
| Income Statement | Seeing income and expenses over time. |
| Account page | Inspecting all transactions for one account. |
| Journal | Searching chronological transaction history. |
| Query | Running custom Beancount queries when needed. |
| Documents | Finding linked receipts and files. |

## Dashboard extension

The ledgers include this directive:

```beancount
2010-01-01 custom "fava-extension" "fava_dashboards"
```

This activates the dashboard extension if `fava-dashboards` is installed.

## Dashboard configuration files

Dashboard files are named `dashboards.yaml`. They are stored near the ledger files and at the shared bookkeeping level.

## Main dashboard sections

| Dashboard | Purpose |
| --- | --- |
| `Vorstand-Cockpit` | Management overview: free money, total Sparkasse balance, PayPal, cash, liquidity trend, monthly result, active project balances. |
| `Details & Daten` | Detailed charts: expenses by category, income by category, money flow, project/person network. |

## Important dashboard indicators

### Freies Geld

Shows money available outside restricted project funds. Typical accounts are `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld` and `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`.

### Sparkasse Gesamt

Shows the total Sparkasse balance across the main bank account and internal subaccounts.

### PayPal

Shows PayPal balance. A negative PayPal balance indicates something should be checked.

### Barkasse

Shows cash box balance.

### Saldo Aktiver Projekte

Shows non-zero project balances. This is useful for seeing which projects still hold money or are overspent.

### Monatlicher Ueberschuss / Fehlbetrag

Shows monthly operating surplus or deficit, excluding project accounts in the dashboard query.

## How to use dashboards responsibly

Dashboards are summaries. If a number looks surprising:

1. Click into the linked Fava account or report.
2. Inspect the underlying transactions.
3. Check whether a transaction is still in `Sonstiges` or `Bank Dump`.
4. Check whether the account name matches the dashboard query pattern.
5. Confirm balance checks before trusting management numbers.

## When dashboard numbers look wrong

Common causes:

- A transaction was booked to the main bank account instead of the project subaccount.
- A project account was closed but still has a non-zero balance.
- A new project uses a naming pattern not included in the dashboard query.
- A transaction is still in a broad fallback category.
- The dashboard file belongs to a different ledger than the one currently opened.
