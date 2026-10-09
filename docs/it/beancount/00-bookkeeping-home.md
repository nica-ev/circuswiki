---
lang: it
translation_id: beancount/00-bookkeeping-home
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Documentazione del Sistema di Contabilità
description: Panoramica e punto di partenza per la documentazione di contabilità Beancount di NICA e.V. e Tohuwabohu Halle e.V.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/00-bookkeeping-home.md
translation_source_body_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_source_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:31:21+00:00
translation_source_localized_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_source_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:31:21+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# Documentazione del Sistema di Contabilità

Questa documentazione spiega come funziona il sistema di contabilità per NICA e.V. e Tohuwabohu Halle e.V. dal punto di vista di un utente normale.

Il sistema utilizza file di contabilità in formato testo semplice (plaintext) in Beancount e un'interfaccia browser chiamata Fava. Non è necessario conoscere la programmazione per utilizzarlo, ma è necessario seguire attentamente il flusso di lavoro della contabilità: importare i dati bancari, classificare le transazioni, allegare le ricevute dove necessario e controllare i saldi.

## Inizia da qui

- [01 - Panoramica del Sistema](01-system-overview.md)
- [02 - Aprire Fava](02-opening-fava.md)
- [03 - Mappa delle Cartelle e dei File](03-folder-and-file-map.md)
- [04 - Basi di Beancount per Utenti](04-beancount-basics-for-users.md)
- [05 - Conti e Categorie](05-accounts-and-categories.md)
- [06 - Inserimento e Modifica delle Transazioni](06-entering-and-editing-transactions.md)
- [07 - Importazione CSV Bancario e Riconciliazione](07-bank-csv-import-and-reconciliation.md)
- [08 - Progetti e Fondi Vincolati](08-projects-and-restricted-funds.md)
- [09 - Ricevute e Documenti](09-receipts-and-documents.md)
- [10 - Dashboard e Report di Fava](10-fava-dashboards-and-reports.md)
- [11 - Routine di Contabilità Regolare](11-regular-bookkeeping-routine.md)
- [12 - Risoluzione dei Problemi](12-troubleshooting.md)
- [13 - Glossario](13-glossary.md)

## La regola più importante

Il file di contabilità è la fonte della verità. Fava visualizza solo ciò che è scritto nei file `.beancount`. Se qualcosa appare errato in Fava, correggi la voce in Beancount e ricarica Fava.

## Registri contabili attuali

| Organizzazione | File principale | Indirizzo Fava | Porta |
| --- | --- | --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` | `http://127.0.0.1:4998/` | `4998` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` | `http://127.0.0.1:4999/` | `4999` |

## Cosa non è questa documentazione

Questa non è una consulenza legale o fiscale. Descrive come è organizzato questo specifico sistema di contabilità locale e come gli utenti dovrebbero lavorarci in modo coerente.
