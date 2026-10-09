---
lang: en
translation_id: beancount/09-receipts-and-documents
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Receipts and Documents
description: Explains where supporting documents are stored and how transactions reference receipts.
authors:
  - Marc Bielert
translation_status: original
translation_source_lang: en
---
# 09 - Receipts and Documents

Receipts, invoices, contracts, and other supporting documents make transactions auditable. The ledger should make it possible to find the document behind an expense.

## Where documents are stored

Tohuwabohu currently has a clear receipts folder:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben
```

Receipts already entered into the ledger are often in:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben/Eingetragen
```

NICA uses supporting files in its bookkeeping folder and project folders. If a consistent NICA receipt folder is introduced later, document it here and use it consistently.

## `document` entries

A document entry links a file to an account and date:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```

The file path is relative to the folder containing the ledger file.

## Document links with tags

Some older entries include document tags such as:

```beancount
2023-01-05 document Ausgaben:Buero:Sonstiges "Belege Ausgaben/Eingetragen/2023_001.jpg" ^2023_001
```

The `^2023_001` part is a Beancount link. It can connect a receipt to the related transaction if the same link is used there.

## Meaning of `scanned`

Comments in the ledgers define the convention for scanned receipts. When the tag `scanned` is used, it means:

- The receipt was scanned or digitised.
- The image was reduced and optimised, for example with TinyPNG.
- The file was saved using a year and number pattern, for example `2023_002.jpg`.
- The number is referenced in the related ledger entry.

## Good file names

Good receipt file names are stable and readable:

```text
2026_001.jpg
2026_002.pdf
Quittung-Tohu25-001.pdf
Invoice406-Schwarze_Risse-marc-bielert.pdf
```

Avoid names like `scan.jpg`, `image1.jpg`, or `download.pdf`.

## Workflow for a new receipt

1. Save the receipt in the correct receipt folder.
2. Rename it so it can be recognised later.
3. Enter or find the related transaction.
4. Add a `document` line or link metadata if useful.
5. If the receipt has been processed, move it to `Eingetragen` if that is the folder convention.
6. Reload Fava and check that the document link works.

## When a receipt is missing

If a receipt is missing, add a comment near the transaction:

```beancount
; Receipt missing. Ask responsible person.
```

Do not pretend there is a document if it is not available.

## Contracts and honorarium documents

Contracts and honorarium invoices should be stored near the related project or bookkeeping folder and referenced clearly. For project audits, the important question is not only that the transaction exists, but that the document proving the expense can be found quickly.
