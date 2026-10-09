---
lang: it
translation_id: beancount/01-system-overview
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Panoramica del Sistema
description: Spiega lo scopo, i componenti e il normale flusso di lavoro dell'utente del sistema di contabilità.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/01-system-overview.md
translation_source_body_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_source_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:32:29+00:00
translation_source_localized_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_source_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:32:29+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 01 - Panoramica del Sistema

## Scopo

Il sistema di contabilità registra tutte le attività finanziarie delle associazioni in modo strutturato e verificabile. È progettato per rispondere alle normali domande di contabilità:

- Quanto denaro è attualmente disponibile?
- Quali entrate e spese appartengono all'associazione stessa?
- Quali entrate e spese appartengono a un progetto specifico?
- I saldi di Sparkasse, PayPal e contanti sono corretti?
- Quali ricevute e documenti appartengono a quali transazioni?
- Quali progetti sono attivi, in corso o già chiusi?

## Componenti principali

| Componente | Cosa fa |
| --- | --- |
| Beancount | Il formato dei dati contabili. Le transazioni sono scritte in file di testo semplice. |
| Fava | L'interfaccia browser per visualizzare e filtrare i dati di Beancount. |
| Dashboard Fava | Pagine dashboard personalizzate all'interno di Fava per una panoramica gestionale e viste di progetto. |
| Obsidian | Il sistema di note da cui la contabilità può essere aperta tramite pulsanti. |
| Script di importazione CSV | Script di supporto che convertono gli esport di CSV di Sparkasse in voci Beancount. |

## Come le parti si incastrano

1. I dati bancari o di PayPal vengono esportati come CSV.
2. Il CSV viene convertito in voci Beancount temporanee.
3. Le nuove voci vengono copiate nel file di registro corretto.
4. L'utente controlla, classifica e corregge le voci.
5. I controlli dei saldi confermano che il registro corrisponde al saldo bancario o di PayPal.
6. Fava visualizza report, pagine dei conti, rendiconti finanziari, bilanci e dashboard.

## Due associazioni separate

| Associazione | Registro | Prefisso conto tipico |
| --- | --- | --- |
| NICA e.V. | `nica.beancount` | `Sparkasse-NICA`, `NICA` |
| Tohuwabohu Halle e.V. | `2023.beancount` | `Sparkasse-Tohuwabohu`, `Tohuwabohu` |

Esiste anche un file combinato sperimentale: `1. Vereinsverwaltung/Buchhaltung/all.beancount`. Il normale lavoro quotidiano dovrebbe avvenire nel registro individuale dell'associazione pertinente.

## Flusso di lavoro di base

1. Aprire l'istanza Fava corretta.
2. Trovare l'ultimo controllo dei saldi completato.
3. Esportare le nuove transazioni bancarie da Sparkasse a partire dalla data dell'ultimo controllo.
4. Convertire il CSV in formato Beancount.
5. Incollare le voci generate prima nella sezione `Bank Dump`.
6. Spostare o classificare le voci nelle sezioni corrette dell'associazione o del progetto.
7. Aggiungere ricevute, collegamenti, commenti o tag quando necessario.
8. Aggiungere un nuovo controllo dei saldi.
9. Ricaricare Fava e verificare che non ci siano errori.

## Cosa dovrebbe imparare prima un nuovo utente

1. [Aprire Fava](02-opening-fava.md)
2. [Basi di Beancount per utenti](04-beancount-basics-for-users.md)
3. [Importazione e riconciliazione CSV bancario](07-bank-csv-import-and-reconciliation.md)
4. [Conti e categorie](05-accounts-and-categories.md)
5. [Progetti e fondi vincolati](08-projects-and-restricted-funds.md)
