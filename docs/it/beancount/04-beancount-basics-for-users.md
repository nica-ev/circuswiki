---
lang: it
translation_id: beancount/04-beancount-basics-for-users
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Fondamenti di Beancount per Utenti
description: Introduce il formato testuale di Beancount e i pattern di transazione utilizzati nei registri.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/04-beancount-basics-for-users.md
translation_source_body_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_source_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:29+00:00
translation_source_localized_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_source_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:29+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 04 - Fondamenti di Beancount per gli Utenti

Beancount memorizza la contabilità come testo leggibile. Ogni transazione indica cosa è successo, in quale data, chi è stato coinvolto e quali conti sono cambiati.

## Struttura base di una transazione

```beancount
2026-01-13 ! "Tragerwerk Soziale Dienste in Sachsen-Anhalt GmbH" "RgNr. T-2504"
  Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld  680.00 EUR
  Einnahmen:Sonstiges
```

| Parte | Significato |
| --- | --- |
| `2026-01-13` | Data della transazione. |
| `!` | Indicatore di stato. In questo sistema è comunemente usato per voci importate o non ancora revisionate definitivamente. |
| Primo testo tra virgolette | Beneficiario o mittente. |
| Secondo testo tra virgolette | Descrizione o testo di addebito dalla banca. |
| Prima riga del conto | Dove sono andati o da dove sono venuti i soldi. |
| Seconda riga del conto | La categoria opposta. Se non viene specificato un importo, Beancount lo calcola automaticamente. |

## Nomi dei conti

I nomi dei conti sono separati da due punti:

```text
Vermoegen:Bank:Sparkasse-NICA:Freies-Geld
```

Leggilo da sinistra a destra: patrimonio, conto bancario, Sparkasse NICA, fondi liberamente disponibili.

## Le cinque famiglie di conti

| Famiglia | Significato | Esempio |
| --- | --- | --- |
| `Vermoegen` | Attività: banca, PayPal, contanti, inventario. | `Vermoegen:Bank:Sparkasse-NICA` |
| `Verbindlichkeiten` | Passività: denaro dovuto a persone o ad altri. | `Verbindlichkeiten:Person:Marc-Bielert` |
| `Equity` | Saldi di apertura e scritture di assestamento. | `Equity:Opening-Balances` |
| `Einnahmen` | Entrate. | `Einnahmen:Vereinsbeitrag` |
| `Ausgaben` | Uscite. | `Ausgaben:Buero:Miete` |

## Segni per entrate e uscite

Nei report di Beancount, le entrate appaiono spesso con un segno negativo internamente e le uscite con un segno positivo. Fava e le dashboard spesso presentano questi valori in modo più user-friendly. Non modificare le transazioni solo perché un numero di entrate appare negativo in una query grezza.

## Verifiche di saldo

Una verifica di saldo dichiara che un conto deve avere un saldo specifico in una determinata data:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Se Beancount non riesce a far corrispondere quel saldo con le transazioni precedenti a quella data, Fava mostra un errore. Le verifiche di saldo sono il principale meccanismo di controllo qualità.

## Aprire e chiudere conti

Prima che un conto venga utilizzato, viene aperto:

```beancount
2025-04-01 open Ausgaben:Projekt:25-ZGV:Honorar
```

Quando un progetto è terminato e il conto del progetto è a zero, può essere chiuso:

```beancount
2026-02-27 close Ausgaben:Projekt:TOHUCON-25
```

I conti chiusi normalmente non dovrebbero ricevere nuove transazioni.

## Commenti e documenti

Le righe che iniziano con `;` sono commenti. Spiegano decisioni o situazioni incerte e non influenzano i numeri.

Le ricevute possono essere collegate con righe `document`:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```
