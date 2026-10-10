---
lang: it
translation_id: beancount/08-projects-and-restricted-funds
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Progetti e Fondi Vincolati
description: Spiega come vengono rappresentati e verificati i fondi di progetto e i fondi vincolati.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/08-projects-and-restricted-funds.md
translation_source_body_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_source_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:03+00:00
translation_source_localized_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_source_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:03+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 08 - Progetti e Fondi Vincolati

I progetti sono centrali in questo sistema di contabilità. Molte sovvenzioni e attività devono essere tracciate separatamente dai fondi a libera disposizione.

## Cosa significa un progetto nel registro contabile

| Tipo di conto | Esempio | Scopo |
| --- | --- | --- |
| Attività di progetto | `Vermoegen:Bank:Sparkasse-NICA:25-ZGV` | Saldo interno dei fondi del progetto. |
| Entrate di progetto | `Einnahmen:Projekt:25-ZGV:Sachmittel` | Finanziamento del progetto o entrate del progetto. |
| Spese di progetto | `Ausgaben:Projekt:25-ZGV:Sachmittel` | Spese del progetto. |

Il conto bancario effettivo può essere un unico conto Sparkasse, ma il registro contabile separa i saldi interni dei progetti in modo che il team possa vedere cosa appartiene a ciascun progetto.

## Progetti attivi e chiusi

I progetti attivi hanno conti aperti e saldi pertinenti. I progetti chiusi di solito hanno un controllo finale del saldo di `0,00 EUR` e direttive `close` per i conti di attività, entrate e spese del progetto.

Non registrare nuove transazioni in progetti chiusi a meno che non si intenda riaprire o correggere dati storici.

## Esempi attuali in NICA

- `26-JEP-Buehnenreif`
- `25-ZGV`
- `25-CircusWiki`
- `25-Machen-UnitedAges`
- `25-Erasmus`
- progetti chiusi 2024 come `24-AWO`, `24-HONY`, `24-Peter`

## Esempi attuali in Tohuwabohu

- `VHS-TOHU-25`
- `ZMS-TOHU-25`
- `CEDU-25`
- `TOHUCON-25`
- progetti chiusi come `Revierpionier-25`, `OAC-25`, `TohuCon2024`, `ZGV-TOHU-24`, `TohuCon2023`

## Creazione di un nuovo progetto

Un nuovo progetto richiede normalmente l'apertura dei conti prima dell'inserimento delle transazioni.

```beancount
2026-01-01 open Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject:Honorar
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sachmittel
2026-01-01 open Ausgaben:Projekt:26-NewProject:Aufwand
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sonstiges
2026-01-01 open Einnahmen:Projekt:26-NewProject
2026-01-01 open Einnahmen:Projekt:26-NewProject:Honorar
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sachmittel
2026-01-01 open Einnahmen:Projekt:26-NewProject:Aufwand
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sonstiges
```

Apri solo le categorie che sono effettivamente utili per il progetto.

## Registrazione dei finanziamenti del progetto

```beancount
2026-02-01 ! "Funding Body" "First payment NewProject"
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject  3000.00 EUR
  Einnahmen:Projekt:26-NewProject:Sachmittel
```

## Registrazione delle spese del progetto

```beancount
2026-02-10 ! "Supplier" "Project material"
  Ausgaben:Projekt:26-NewProject:Sachmittel  250.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject
```

## Comprensione dei saldi di progetto

Un saldo positivo dell'attività di progetto indica che ci sono ancora fondi allocati a quel progetto. Un saldo nullo dell'attività di progetto indica che il progetto non ha più un saldo bancario interno residuo. Un saldo negativo dell'attività di progetto di solito indica che il progetto ha speso più dei fondi allocati o che manca un'allocazione.

## Chiusura di un progetto

Prima di chiudere un progetto, tutte le entrate e le spese devono essere registrate, le ricevute devono essere reperibili, il conto dell'attività di progetto deve essere esattamente a zero e qualsiasi denaro rimanente deve essere spostato o restituito correttamente.

```beancount
2026-12-31 balance Vermoegen:Bank:Sparkasse-NICA:26-NewProject 0.00 EUR
2026-12-31 close Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-12-31 close Ausgaben:Projekt:26-NewProject
2026-12-31 close Einnahmen:Projekt:26-NewProject
```

Chiudi anche i sottoconti se sono stati aperti separatamente.
