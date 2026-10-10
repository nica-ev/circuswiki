---
lang: it
translation_id: beancount/05-accounts-and-categories
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Conti e Categorie
description: Spiega la struttura dei conti tedeschi e le convenzioni di categoria utilizzate nei libri contabili.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/05-accounts-and-categories.md
translation_source_body_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_source_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:51+00:00
translation_source_localized_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_source_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:51+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 05 - Conti e Categorie

Questa pagina spiega la struttura dei conti utilizzata nei registri contabili.

## Lingua dei nomi

I nomi dei conti sono in tedesco. Continuare a utilizzare i nomi dei conti esistenti per mantenere la coerenza dei report.

| Tedesco | Significato in inglese |
| --- | --- |
| `Vermoegen` | Attività |
| `Verbindlichkeiten` | Passività |
| `Einnahmen` | Entrate |
| `Ausgaben` | Uscite |
| `Buero` | Ufficio |
| `Verein` | Associazione/attività generale dell'associazione |
| `Projekt` | Progetto |
| `Barkasse` | Cassa contanti |
| `Freies-Geld` | Fondi liberi/non vincolati |

## Conti attività

Esempi NICA:

- `Vermoegen:Bank:Sparkasse-NICA`
- `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:NICA:Barkasse`
- `Vermoegen:Inventar`

Esempi Tohuwabohu:

- `Vermoegen:Bank:Sparkasse-Tohuwabohu`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:Tohuwabohu:Barkasse`

## Conti entrate generali

| Conto | Utilizzo per |
| --- | --- |
| `Einnahmen:Vereinsbeitrag` | Quote associative. |
| `Einnahmen:Spende` | Donazioni. |
| `Einnahmen:Verleih` | Entrate da affitto o prestito. |
| `Einnahmen:Sonstiges` | Altre entrate che non rientrano altrove. |

## Conti uscite generali

| Conto | Utilizzo per |
| --- | --- |
| `Ausgaben:Buero:Miete` | Affitto ufficio o locali. |
| `Ausgaben:Buero:Internet` | Internet e servizi digitali. |
| `Ausgaben:Buero:Sonstiges` | Altre spese d'ufficio. |
| `Ausgaben:Verein:Versicherung` | Assicurazione dell'associazione. |
| `Ausgaben:Verein:Ehrenamt` | Rimborsi spese volontari o costi per volontari dell'associazione. |
| `Ausgaben:Essen` | Spese alimentari al di fuori di un progetto specifico. |
| `Ausgaben:Sonstiges` | Fallback temporaneo per spese non chiare. |

`Ausgaben:Sonstiges` e `Einnahmen:Sonstiges` sono utili durante l'importazione, ma non dovrebbero diventare la categoria finale se esiste una categoria più precisa.

## Conti di progetto

I conti di progetto seguono questo schema:

```text
Vermoegen:Bank:Sparkasse-ASSOCIAZIONE:PROGETTO
Ausgaben:Projekt:PROGETTO
Einnahmen:Projekt:PROGETTO
```

Esempi:

- `Vermoegen:Bank:Sparkasse-NICA:25-ZGV`
- `Ausgaben:Projekt:25-ZGV:Honorar`
- `Einnahmen:Projekt:25-ZGV:Sachmittel`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:TOHUCON-25`
- `Ausgaben:Projekt:TOHUCON-25:Essen`
- `Einnahmen:Projekt:TOHUCON-25:ConTickets`

## Sottocategorie tipiche di progetto

| Sottocategoria | Significato |
| --- | --- |
| `Honorar` | Compensi pagati a persone o ricevuti per lavoro. |
| `Aufwand` | Rimborso spese o indennità di trasferta. |
| `Sachmittel` | Materiali e forniture. |
| `Sonstiges` | Altri costi o entrate del progetto. |
| `Pauschale` / `Pauschalen` | Budget forfettario o a importo fisso per il progetto. |

## Passività verso persone

I conti di passività tracciano il denaro dovuto a persone o rimborsato a persone. Gli esempi includono `Verbindlichkeiten:Person:Marc-Bielert`, `Verbindlichkeiten:Person:Peter-Huhndorf` e `Verbindlichkeiten:Person:Charleen-Hoffmann`.

## Scelta del conto corretto

1. Si tratta di un livello associativo o di un livello di progetto?
2. Se a livello di progetto, quale progetto possiede il denaro?
3. Si tratta di entrate, uscite, movimento di attività o rimborso di passività?
4. Esiste già una categoria precisa aperta?
5. Se non esiste una categoria adeguata, utilizzare temporaneamente `Sonstiges` e aggiungere un commento.
