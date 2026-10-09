---
lang: it
translation_id: beancount/06-entering-and-editing-transactions
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Inserimento e modifica delle transazioni
description: Descrive come gli utenti rivedono, classificano, correggono e inseriscono le transazioni contabili.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/06-entering-and-editing-transactions.md
translation_source_body_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_source_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:38:13+00:00
translation_source_localized_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_source_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:38:13+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 06 - Inserimento e modifica delle transazioni

La maggior parte delle voci proviene da dati bancari importati, ma gli utenti devono comunque rivedere, classificare, correggere e talvolta inserire le transazioni manualmente.

## Stato della transazione

I registri utilizzano comunemente `!` nelle transazioni importate:

```beancount
2026-03-12 ! "Beneficiario" "Testo bancario"
```

Utilizzare questo come marcatore normale, a meno che il team non decida una convenzione di stato più rigorosa.

## Inserimento di base delle entrate

```beancount
2026-01-15 ! "Max Mustermann" "Quota associativa 2026"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  60.00 EUR
  Einnahmen:Vereinsbeitrag
```

## Inserimento di base delle spese

```beancount
2026-01-20 ! "Nome fornitore" "Fattura 123"
  Ausgaben:Buero:Sonstiges  25.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Entrate di progetto

```beancount
2026-02-10 ! "Ente finanziatore" "Pagamento sovvenzione progetto 25-ZGV"
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV  5000.00 EUR
  Einnahmen:Projekt:25-ZGV:Sachmittel
```

## Spese di progetto

```beancount
2026-02-15 ! "Nome persona" "Onorario progetto 25-ZGV"
  Ausgaben:Projekt:25-ZGV:Honorar  450.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV
```

## Movimento interno tra fondi di progetto e fondi liberi

A volte una transazione deve allocare denaro bancario tra un conto patrimoniale specifico del progetto e fondi liberi. Il conto bancario reale è un unico conto fisico Sparkasse, ma il registro tiene traccia separatamente dei saldi interni del progetto.

```beancount
2026-02-20 ! "Allocazione interna" "Spostare i fondi rimanenti del progetto in fondi liberi"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  100.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV      -100.00 EUR
```

Effettuare trasferimenti interni solo quando si comprende il motivo per cui il saldo interno del progetto deve cambiare.

## Rimborsi a persone

Se qualcuno ha pagato privatamente e viene rimborsato in seguito, lo schema corretto consiste solitamente nel registrare la spesa contro una passività e quindi saldare la passività con il pagamento bancario.

```beancount
2026-03-01 ! "Negozio" "Materiale acquistato da Marc"
  Ausgaben:Projekt:25-ZGV:Sachmittel  35.00 EUR
  Verbindlichkeiten:Person:Marc-Bielert
```

```beancount
2026-03-05 ! "Marc Bielert" "Rimborso materiale"
  Verbindlichkeiten:Person:Marc-Bielert  35.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Commenti per decisioni poco chiare

```beancount
; Non è chiaro se questo appartenga ai fondi CEDU-25 o ai fondi dell'associazione libera. Controllare la fattura.
2026-03-10 ! "Fornitore" "Fattura 456"
  Ausgaben:Sonstiges  120.00 EUR
  Vermoegen:Bank:Sparkasse-Tohuwabohu
```

## Modifica in sicurezza

Prima di modificare, verificare:

- Ci si trova nel registro corretto dell'associazione.
- Non si sta modificando l'output generato dall'importazione come se fosse il registro definitivo.
- La data della transazione è corretta.
- L'importo utilizza un punto come separatore decimale, ad esempio `12.50 EUR`.
- I nomi degli account sono scritti esattamente come gli account esistenti.
- Le transazioni di progetto utilizzano in modo coerente l'account patrimoniale del progetto e la categoria di entrate/spese del progetto.

Dopo la modifica, salvare il file, ricaricare Fava, verificare la presenza di errori e ispezionare la pagina dell'account pertinente.
