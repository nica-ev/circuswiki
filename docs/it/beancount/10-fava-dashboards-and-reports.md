---
lang: it
translation_id: beancount/10-fava-dashboards-and-reports
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Dashboard e Report Fava
description: Panoramica dei report Fava e delle dashboard personalizzate utilizzate per la revisione della contabilità.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/10-fava-dashboards-and-reports.md
translation_source_body_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_source_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:14+00:00
translation_source_localized_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_source_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:14+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 10 - Dashboard e Report di Fava

Fava fornisce report contabili standard. Il sistema utilizza anche `fava-dashboards` per pagine di panoramica personalizzate.

## Viste standard di Fava

| Vista | Utilizzo per |
| --- | --- |
| Stato Patrimoniale | Verificare attività, passività, fondi liberi, PayPal, contanti e saldi dei progetti. |
| Conto Economico | Visualizzare entrate e uscite nel tempo. |
| Pagina Conto | Ispezionare tutte le transazioni di un singolo conto. |
| Giornale | Cercare la cronologia delle transazioni in ordine cronologico. |
| Query | Eseguire query Beancount personalizzate quando necessario. |
| Documenti | Trovare ricevute e file collegati. |

## Estensione Dashboard

I registri includono questa direttiva:

```beancount
2010-01-01 custom "fava-extension" "fava_dashboards"
```

Ciò attiva l'estensione dashboard se `fava-dashboards` è installato.

## File di configurazione Dashboard

I file dashboard sono denominati `dashboards.yaml`. Sono archiviati vicino ai file del registro e a livello di contabilità condivisa.

## Sezioni principali del Dashboard

| Dashboard | Scopo |
| --- | --- |
| `Vorstand-Cockpit` | Panoramica gestionale: denaro libero, saldo totale Sparkasse, PayPal, contanti, trend di liquidità, risultato mensile, saldi dei progetti attivi. |
| `Details & Daten` | Grafici dettagliati: spese per categoria, entrate per categoria, flusso di denaro, rete progetti/persone. |

## Indicatori importanti del Dashboard

### Freies Geld (Denaro Libero)

Mostra il denaro disponibile al di fuori dei fondi di progetto vincolati. Gli account tipici sono `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld` e `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`.

### Sparkasse Gesamt (Totale Sparkasse)

Mostra il saldo totale Sparkasse tra il conto bancario principale e i sotto-conti interni.

### PayPal

Mostra il saldo PayPal. Un saldo PayPal negativo indica che qualcosa deve essere controllato.

### Barkasse (Cassa Contanti)

Mostra il saldo della cassa contanti.

### Saldo Aktiver Projekte (Saldo Progetti Attivi)

Mostra i saldi dei progetti non a zero. Questo è utile per vedere quali progetti hanno ancora denaro o sono in deficit.

### Monatlicher Ueberschuss / Fehlbetrag (Avanzo / Deficit Mensile)

Mostra l'avanzo o il deficit operativo mensile, escludendo i conti di progetto nella query del dashboard.

## Come utilizzare i dashboard in modo responsabile

I dashboard sono riassunti. Se un numero appare sorprendente:

1. Clicca sul conto o report Fava collegato.
2. Ispeziona le transazioni sottostanti.
3. Verifica se una transazione è ancora in `Sonstiges` (Altro) o `Bank Dump`.
4. Verifica se il nome del conto corrisponde al pattern della query del dashboard.
5. Conferma i controlli del saldo prima di fidarti dei numeri gestionali.

## Quando i numeri del dashboard sembrano errati

Cause comuni:

- Una transazione è stata registrata sul conto bancario principale invece che sul sotto-conto del progetto.
- Un conto di progetto è stato chiuso ma ha ancora un saldo non a zero.
- Un nuovo progetto utilizza uno schema di denominazione non incluso nella query del dashboard.
- Una transazione è ancora in una categoria generica di fallback.
- Il file del dashboard appartiene a un registro diverso da quello attualmente aperto.
