---
lang: it
translation_id: beancount/12-troubleshooting
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Risoluzione dei problemi
description: Problemi comuni di Fava e Beancount e come risolverli.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/12-troubleshooting.md
translation_source_body_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_source_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:28+00:00
translation_source_localized_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_source_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:28+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 12 - Risoluzione dei problemi

## Fava non si apre

Verifica:

- La finestra del terminale è ancora aperta?
- Fava è stato avviato nella cartella corretta?
- Viene utilizzata la porta corretta?
- Un'altra istanza di Fava è già in esecuzione sulla stessa porta?
- Fava è installato e disponibile nel terminale?

Comandi:

```powershell
fava nica.beancount --port 4998
fava 2023.beancount --port 4999
```

Esegui ciascun comando solo dalla cartella del ledger corretta.

## Fava mostra un errore di Beancount

Cause comuni:

- Errore di battitura nel nome di un conto.
- Direttiva `open` del conto mancante.
- L'importo utilizza la virgola invece del punto.
- Mancano le virgolette attorno al beneficiario o alla descrizione.
- Una transazione non è bilanciata.
- Un controllo del saldo non corrisponde.
- Una transazione utilizza un conto dopo la sua chiusura.

Correggi il file di testo, salvalo, quindi ricarica Fava.

## Il controllo del saldo fallisce

Non eliminare il controllo del saldo come soluzione temporanea. Indaga sulla differenza.

Checklist:

- L'intervallo di date del CSV era completo?
- Lo stesso CSV è stato importato due volte?
- Alcune transazioni sono state incollate nel ledger sbagliato?
- Una transazione è stata assegnata al sottoconto Sparkasse sbagliato?
- Un segno di importo è stato modificato in modo errato?
- Un trasferimento PayPal o in contanti è stato inserito solo da un lato?
- Ci sono modifiche manuali più vecchie dopo il precedente controllo del saldo?

## La conversione CSV fallisce

Verifica:

- Il file CSV si trova nella stessa cartella `test` di `csv2bean.py`.
- Il nome del file nel comando è esatto.
- Il file è l'esportazione Sparkasse `Excel (CSV-CAMT V2)`.
- Il file è separato da punto e virgola.
- Il CSV non è stato aperto e risalvato in modo da modificarne il formato.

## Le voci importate appaiono troppo generiche

Questo è previsto. Il convertitore utilizza categorie di fallback come:

- `Ausgaben:Sonstiges`
- `Einnahmen:Sonstiges`

L'utente deve rivedere e classificare manualmente le voci importate.

## Dashboard mancante

Verifica:

- `fava-dashboards` è installato.
- Il ledger contiene la direttiva `custom "fava-extension" "fava_dashboards"`.
- Esiste un file `dashboards.yaml` accanto al ledger.
- Fava è stato riavviato dopo l'installazione o le modifiche alla configurazione.

## Un progetto non appare nelle dashboard

Verifica:

- Il progetto ha un conto di asset di progetto sotto il prefisso Sparkasse o PayPal previsto.
- Il conto del progetto non è chiuso.
- Il saldo del progetto non è esattamente zero.
- Il nome del conto corrisponde al modello di query della dashboard.

## Il collegamento del documento non funziona

Verifica:

- Il percorso del file è relativo alla cartella del file del ledger.
- Il nome del file è scritto esattamente.
- Il documento non è stato spostato dopo il collegamento.
- Il percorso utilizza barre oblique o uno stile di percorso relativo normale.

## Non sono sicuro di come classificare una transazione

Usa questo ordine:

1. Cerca transazioni simili più vecchie in Fava.
2. Controlla il contesto del progetto o della fattura.
3. Verifica se appartiene a una linea di budget di un finanziatore.
4. Aggiungi un commento in caso di incertezza.
5. Usa temporaneamente `Sonstiges` solo se non si conosce una categoria migliore.
6. Chiedi alla persona responsabile del progetto o delle finanze prima di finalizzare.
