---
lang: it
translation_id: beancount/07-bank-csv-import-and-reconciliation
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Importazione e Riconciliazione CSV Bancario
description: Flusso di lavoro per l'importazione dei dati CSV Sparkasse e la riconciliazione dei saldi bancari.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/07-bank-csv-import-and-reconciliation.md
translation_source_body_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_source_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:05:17+00:00
translation_source_localized_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_source_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:05:17+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 07 - Importazione e Riconciliazione CSV della Banca

Questo flusso di lavoro porta le nuove transazioni di Sparkasse in Beancount e conferma che il libro mastro corrisponde ancora all'estratto conto bancario reale.

## Dove avvengono le importazioni

| Associazione | Cartella di importazione | Script | File di output |
| --- | --- | --- | --- |
| NICA | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/test` | `csv2bean.py` | `beancount_file.beancount` |
| Tohuwabohu | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/test` | `csv2bean.py` | `beancount_file.beancount` |

## Prima di esportare da Sparkasse

1. Apri il file del libro mastro corretto.
2. Trova la sezione `Balance Checks`.
3. Trova la data del saldo più recente per il conto Sparkasse.
4. Controlla anche la sezione `Bank Dump` in fondo per l'ultima data importata.
5. Usa la data più recente tra queste come punto di partenza.

Ciò evita di perdere transazioni o di importare lo stesso periodo due volte.

## Esportazione da Sparkasse

1. Apri la panoramica del conto.
2. Filtra per intervallo di date.
3. Inizia dalla data dell'ultima verifica o importazione.
4. Termina con oggi o con la data di riconciliazione desiderata.
5. Esporta come `Excel (CSV-CAMT V2)`.
6. Copia il CSV scaricato nella cartella `test` corretta.

Gli script si aspettano il formato CSV-CAMT-V2 di Sparkasse con colonne separate da punto e virgola.

## Conversione del CSV

Apri un terminale nella cartella `test` corretta ed esegui:

```powershell
python csv2bean.py "NOME-DEL-FILE-SCARICATO.CSV"
```

Esempio:

```powershell
python csv2bean.py "20260312-1894137139-umsatz.CSV"
```

Se funziona, lo script stampa `Process finished.` e crea o sovrascrive `beancount_file.beancount`.

## Cosa fa il convertitore

Il convertitore crea voci Beancount di base:

- Gli importi in entrata vanno all'asset account di Sparkasse e, per impostazione predefinita, a `Einnahmen:Sonstiges`.
- Gli importi in uscita vanno a `Ausgaben:Sonstiges` e, per impostazione predefinita, all'asset account di Sparkasse.
- Alcune descrizioni di entrate vengono classificate automaticamente come `Einnahmen:Vereinsbeitrag`.
- Alcuni testi relativi a Tohuwabohu potrebbero essere classificati come un conto di entrate di progetto.

Il convertitore è solo una prima fase. Non conosce il significato contabile finale di ogni transazione.

## Copia nel libro mastro principale

1. Apri `test/beancount_file.beancount`.
2. Ignora l'intestazione delle opzioni generata.
3. Copia solo le transazioni.
4. Incollale prima nel libro mastro principale sotto `Bank Dump`.
5. Aggiungi un separatore datato per la data di importazione, se necessario.

```beancount
****************************************************************************
** 2026-01-13
****************************************************************************
```

Il `Bank Dump` è un'area di staging. Le transazioni importate possono essere successivamente spostate nella sezione tematica o di progetto corretta.

## Classificazione delle voci importate

Per ogni transazione importata, decidi:

- È a livello di associazione o di progetto?
- È un'entrata o un'uscita?
- È un rimborso o un pagamento di passività?
- Appartiene a `Freies-Geld` o a un conto asset specifico del progetto?
- Esiste una ricevuta o una fattura da allegare?

Sostituisci i conti generici di fallback come `Ausgaben:Sonstiges` quando esiste un conto più preciso.

## Aggiunta di un controllo del saldo

Esempio NICA:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Esempio Tohuwabohu:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-Tohuwabohu 2345.67 EUR
```

Usa il saldo mostrato da Sparkasse per quella data esatta.

## Validazione in Fava

1. Salva il file del libro mastro.
2. Ricarica Fava.
3. Controlla la presenza di errori nella parte superiore della pagina di Fava.
4. Apri la pagina del conto Sparkasse.
5. Conferma il saldo corrente e le ultime transazioni.
6. Controlla il Bilancio.
7. Controlla le dashboard di progetto se sono stati interessati conti di progetto.

## Se il controllo del saldo fallisce

Cause comuni:

- L'esportazione CSV ha saltato un giorno all'inizio o alla fine.
- Una transazione è stata importata due volte.
- Una transazione è stata incollata nel libro mastro dell'associazione sbagliata.
- Un numero è stato modificato in modo errato.
- Uno split di progetto ha utilizzato il segno sbagliato.
- Movimenti PayPal o in contanti non sono stati registrati.

Non rimuovere il controllo del saldo solo per far scomparire l'errore. Correggi la differenza di transazione sottostante.
