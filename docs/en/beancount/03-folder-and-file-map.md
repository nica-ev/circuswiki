---
lang: en
translation_id: beancount/03-folder-and-file-map
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Folder and File Map
description: Maps the important bookkeeping folders, ledger files, dashboards, and helper files.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 03 - Folder and File Map

This page explains where the important bookkeeping files are stored.

## Main bookkeeping folder

```text
1. Vereinsverwaltung/Buchhaltung
```

This folder contains the ledgers, dashboard files, supporting documents, and helper folders.

## Important top-level files

| File | Purpose |
| --- | --- |
| `Buchhaltung Home.md` | Obsidian entry page with buttons and a short workflow note. |
| `all.beancount` | Experimental combined ledger including both NICA and Tohuwabohu. |
| `dashboards.yaml` | Dashboard definition for Fava dashboards at the shared level. |

## NICA structure

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA
```

| Path | Purpose |
| --- | --- |
| `2023/nica.beancount` | Main NICA ledger. This is the file normally edited. |
| `2023/dashboards.yaml` | Dashboard configuration for the NICA ledger. |
| `2023/Buchhaltung NICA eV.md` | Obsidian helper note for opening NICA bookkeeping. |
| `2023/CSV/` | Stored CSV exports. |
| `test/csv2bean.py` | Converts Sparkasse CSV to temporary Beancount entries. |
| `test/beancount_file.beancount` | Generated output from the CSV conversion. |
| `test/paypal2bean.py` | Helper for PayPal CSV imports. |
| `test/output_file_paypal.beancount` | Generated PayPal output file. |
| `test/old files/` | Older CSVs and generated files. |

## Tohuwabohu structure

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu
```

| Path | Purpose |
| --- | --- |
| `2023/2023.beancount` | Main Tohuwabohu ledger. This is the file normally edited. |
| `2021/2021.beancount` | Older ledger data included through `all.beancount`. |
| `all.beancount` | Tohuwabohu combined file including 2021 and 2023 ledger files. |
| `2023/dashboards.yaml` | Dashboard configuration for the Tohuwabohu ledger. |
| `2023/Buchhaltung Tohuwabohu Halle eV.md` | Obsidian helper note. |
| `2023/Belege Ausgaben/` | Receipts and supporting documents for expenses. |
| `2023/Belege Ausgaben/Eingetragen/` | Receipts already entered into the ledger. |
| `test/csv2bean.py` | Converts Sparkasse CSV to temporary Beancount entries. |
| `test/beancount_file.beancount` | Generated output from the CSV conversion. |
| `test/paypal2bean.py` | Helper for PayPal CSV imports. |
| `test/output_file_paypal.beancount` | Generated PayPal output file. |
| `test/CSV - old files/` | Older CSVs and generated files. |

## File naming principle

The folders still contain historical names such as `2023`, even when they also contain later activity from 2024, 2025, and 2026. Treat the currently referenced main ledger files as the active ledgers unless the structure is intentionally changed.

## Where to edit

| Association | Edit this file |
| --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` |

Do not edit generated output files as the permanent record. They are temporary staging files.
