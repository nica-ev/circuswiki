---
lang: it
translation_id: beancount/11-regular-bookkeeping-routine
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Routine di Contabilità Regolare
description: Una pratica checklist ricorrente per mantenere aggiornate le scritture contabili.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/11-regular-bookkeeping-routine.md
translation_source_body_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_source_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:51+00:00
translation_source_localized_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_source_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:51+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 11 - Routine di Contabilità Regolare

Questa pagina descrive una routine pratica per mantenere aggiornati i libri contabili.

## Routine settimanale o bisettimanale

Utilizzare questa routine quando ci sono movimenti bancari regolari.

1. Aprire la corretta istanza di Fava.
2. Verificare se Fava mostra errori.
3. Trovare l'ultimo controllo del saldo.
4. Esportare i nuovi dati CSV di Sparkasse.
5. Convertire il CSV con `csv2bean.py`.
6. Incollare le nuove voci in `Bank Dump`.
7. Classificare le voci nei conti corretti.
8. Allegare o fare riferimento alle ricevute dove necessario.
9. Aggiungere un nuovo controllo del saldo.
10. Ricaricare Fava e risolvere gli errori.
11. Rivedere `Ausgaben:Sonstiges` (Spese:Altro) e `Einnahmen:Sonstiges` (Entrate:Altro) per le voci che dovrebbero essere più specifiche.

## Routine mensile

A fine mese:

1. Riconciliare Sparkasse.
2. Riconciliare PayPal, se utilizzato.
3. Riconciliare la cassa, se è stato utilizzato contante.
4. Controllare le passività aperte verso terzi.
5. Controllare i saldi dei progetti attivi.
6. Rivedere le voci `Sonstiges` non classificate.
7. Controllare le ricevute mancanti.
8. Verificare se qualche progetto concluso dovrebbe essere preparato per la chiusura.

## Routine di rendicontazione di progetto

Prima di preparare un rapporto di progetto o un Verwendungsnachweis (documento giustificativo):

1. Aprire le pagine del conto di progetto in Fava.
2. Esportare o rivedere tutte le entrate e le spese del progetto.
3. Confermare che le categorie corrispondano alle linee di budget del finanziatore.
4. Confermare che tutte le ricevute e i documenti relativi agli onorari esistano.
5. Verificare se rimborsi, cancellazioni e indennizzi sono registrati come correzioni piuttosto che come entrate errate.
6. Confermare che il saldo patrimoniale del progetto sia spiegabile.
7. Se il progetto è concluso, trasferire correttamente il denaro rimanente e chiudere i conti del progetto.

## Routine di fine anno

A fine anno:

1. Riconciliare tutti i conti bancari.
2. Riconciliare PayPal.
3. Riconciliare le casse.
4. Controllare le passività.
5. Controllare i saldi dei progetti aperti.
6. Assicurarsi che tutte le ricevute siano archiviate e collegate o reperibili.
7. Rivedere le categorie di entrate e spese.
8. Aggiungere i controlli finali del saldo.
9. Preparare i rapporti da Fava.
10. Archiviare i CSV esportati e i documenti di supporto.

## Controlli di qualità

Un libro contabile è in buone condizioni quando:

- Fava si apre senza errori.
- L'ultimo controllo del saldo Sparkasse corrisponde a quello della banca.
- I saldi PayPal e cassa sono controllati dove pertinente.
- I saldi dei progetti sono intenzionali e spiegabili.
- I progetti chiusi hanno un saldo patrimoniale pari a zero.
- I conti `Sonstiges` non contengono voci non categorizzate evitabili.
- Le ricevute per le spese sono reperibili.
- I commenti spiegano correzioni o presupposti insoliti.

## Checklist per il passaggio di consegne a un'altra persona

Prima di passare la contabilità a qualcun altro:

- Mostrare il file del libro contabile corretto per ogni associazione.
- Mostrare come avviare Fava.
- Mostrare l'ultimo controllo del saldo.
- Mostrare come vengono importati i CSV in `Bank Dump`.
- Mostrare dove sono archiviate le ricevute.
- Mostrare un esempio di progetto, dall'entrata dei fondi alla chiusura finale.
- Indicare la cartella di questa documentazione.
