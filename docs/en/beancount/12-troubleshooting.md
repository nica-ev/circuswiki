---
lang: en
translation_id: beancount/12-troubleshooting
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Troubleshooting
description: Common Fava and Beancount problems and how to resolve them.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 12 - Troubleshooting

## Fava does not open

Check:

- Is the terminal window still open?
- Was Fava started in the correct folder?
- Is the correct port used?
- Is another Fava instance already running on the same port?
- Is Fava installed and available in the terminal?

Commands:

```powershell
fava nica.beancount --port 4998
fava 2023.beancount --port 4999
```

Run each command only from the correct ledger folder.

## Fava shows a Beancount error

Common causes:

- Typo in an account name.
- Missing account `open` directive.
- Amount uses comma instead of dot.
- Quotes are missing around payee or narration.
- A transaction does not balance.
- A balance check does not match.
- A transaction uses an account after it was closed.

Fix the text file, save it, then reload Fava.

## Balance check fails

Do not delete the balance check as a workaround. Investigate the difference.

Checklist:

- Was the CSV date range complete?
- Was the same CSV imported twice?
- Were some transactions pasted into the wrong ledger?
- Was a transaction assigned to the wrong Sparkasse subaccount?
- Was an amount sign changed incorrectly?
- Was a PayPal or cash transfer only entered on one side?
- Are there older manual edits after the previous balance check?

## CSV conversion fails

Check:

- The CSV file is in the same `test` folder as `csv2bean.py`.
- The file name in the command is exact.
- The file is the Sparkasse `Excel (CSV-CAMT V2)` export.
- The file is semicolon-separated.
- The CSV was not opened and resaved in a way that changed its format.

## Imported entries look too generic

This is expected. The converter uses fallback categories such as:

- `Ausgaben:Sonstiges`
- `Einnahmen:Sonstiges`

The user must review and classify imported entries manually.

## Dashboard is missing

Check:

- `fava-dashboards` is installed.
- The ledger contains the `custom "fava-extension" "fava_dashboards"` directive.
- A `dashboards.yaml` file exists next to the ledger.
- Fava was restarted after installation or configuration changes.

## A project does not appear in dashboards

Check:

- The project has a project asset account under the expected Sparkasse or PayPal prefix.
- The project account is not closed.
- The project balance is not exactly zero.
- The account name matches the dashboard query pattern.

## Document link does not work

Check:

- The file path is relative to the ledger file folder.
- The file name is spelled exactly.
- The document was not moved after linking.
- The path uses forward slashes or normal relative path style.

## Unsure how to classify a transaction

Use this order:

1. Search for similar older transactions in Fava.
2. Check the project or invoice context.
3. Check whether it belongs to a funder budget line.
4. Add a comment if uncertain.
5. Temporarily use `Sonstiges` only if no better category is known.
6. Ask the responsible project or finance person before finalising.
