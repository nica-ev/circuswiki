---
lang: it
translation_id: beancount/13-glossary
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Glossario
description: Definizioni dei termini di contabilità, Beancount, Fava e contabilità di progetto utilizzati in questa documentazione.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/13-glossary.md
translation_source_body_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_source_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:03+00:00
translation_source_localized_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_source_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:03+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 13 - Glossario

## Account (Conto)

Un luogo denominato dove Beancount registra denaro o valore. Esempio: `Ausgaben:Buero:Miete`.

## Asset (Attività)

Qualcosa che l'associazione possiede o controlla, come denaro in banca, saldo PayPal, contanti o inventario. In questo sistema le attività sono sotto `Vermoegen`.

## Balance check (Verifica del saldo)

Una riga che conferma che un conto ha un saldo specifico in una data specifica. Le verifiche del saldo vengono utilizzate per accertare che il registro corrisponda ai rendiconti bancari, PayPal o contanti.

## Bank Dump (Scarico bancario)

Una sezione temporanea in fondo al registro dove vengono incollate inizialmente le transazioni bancarie importate, prima che siano completamente classificate.

## Beancount

Il formato di contabilità in testo semplice utilizzato come fonte di verità del sistema.

## CSV

Un file di esportazione simile a un foglio di calcolo. Sparkasse esporta file CSV che vengono convertiti in transazioni Beancount.

## Equity (Patrimonio netto)

Famiglia di conti Beancount utilizzata per i saldi di apertura e per bilanciare i punti di partenza storici.

## Fava

L'interfaccia browser per visualizzare e lavorare con i registri Beancount.

## Fava Dashboards (Dashboard Fava)

Un'estensione che aggiunge pagine dashboard personalizzate a Fava.

## Freies-Geld (Denaro libero)

Denaro libero o non vincolato che non è assegnato a un budget di progetto limitato.

## Income (Entrate)

Denaro ricevuto. In questo sistema i conti delle entrate iniziano con `Einnahmen`.

## Ledger (Registro)

Il file di contabilità contenente conti, transazioni, verifiche del saldo e documenti. I registri principali sono `nica.beancount` e `2023.beancount`.

## Liability (Passività)

Denaro dovuto a qualcun altro. In questo sistema le passività sono sotto `Verbindlichkeiten`.

## Payee (Beneficiario)

La persona o l'organizzazione indicata in una transazione.

## Project account (Conto di progetto)

Un conto utilizzato per tracciare separatamente il denaro di un progetto specifico rispetto al denaro generale dell'associazione.

## Reconciliation (Riconciliazione)

Il processo di verifica della corrispondenza tra Beancount e il saldo effettivo della banca o di PayPal.

## Receipt (Ricevuta)

Un documento che prova una spesa, come una fattura, un contratto o una ricevuta di cassa.

## Sonstiges (Varie)

Tedesco per "varie" o "altro". Utile come soluzione temporanea di ripiego, ma categorie specifiche sono migliori per la contabilità finale.

## Transaction (Transazione)

Una voce contabile datata che descrive un evento finanziario.

## Verwendungsnachweis (Prova di utilizzo)

Un rapporto del finanziatore del progetto che spiega come sono stati utilizzati i fondi concessi.
