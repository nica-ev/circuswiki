---
lang: nl
translation_id: beancount/06-entering-and-editing-transactions
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Transacties Invoeren en Bewerken
description: Beschrijft hoe gebruikers boekhoudkundige transacties beoordelen, classificeren, corrigeren en invoeren.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/06-entering-and-editing-transactions.md
translation_source_body_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_source_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:38:26+00:00
translation_source_localized_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_source_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:38:26+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 06 - Transacties invoeren en bewerken

De meeste boekingen komen uit geïmporteerde bankgegevens, maar gebruikers moeten transacties nog steeds beoordelen, classificeren, corrigeren en soms handmatig invoeren.

## Transactiestatus

De grootboeken gebruiken vaak `!` bij geïmporteerde transacties:

```beancount
2026-03-12 ! "Betaalde partij" "Banktekst"
```

Gebruik dit als de normale markering, tenzij het team een strengere statusconventie afspreekt.

## Basis inkomstenboeking

```beancount
2026-01-15 ! "Max Mustermann" "Mitgliedsbeitrag 2026"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  60.00 EUR
  Einnahmen:Vereinsbeitrag
```

## Basis uitgavenboeking

```beancount
2026-01-20 ! "Naam leverancier" "Factuur 123"
  Ausgaben:Buero:Sonstiges  25.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Projectinkomsten

```beancount
2026-02-10 ! "Subsidieverstrekker" "Subsidiebetaling project 25-ZGV"
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV  5000.00 EUR
  Einnahmen:Projekt:25-ZGV:Sachmittel
```

## Projectuitgaven

```beancount
2026-02-15 ! "Naam persoon" "Honorarium project 25-ZGV"
  Ausgaben:Projekt:25-ZGV:Honorar  450.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV
```

## Interne overboeking tussen project- en vrije middelen

Soms moet een transactie bankgeld toewijzen tussen een projectspecifiek actiefaccount en vrije middelen. Het werkelijke bankrekening is één fysieke Sparkasse-rekening, maar het grootboek houdt de interne projectsaldi afzonderlijk bij.

```beancount
2026-02-20 ! "Interne toewijzing" "Restant projectmiddelen naar vrije middelen verplaatsen"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  100.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV      -100.00 EUR
```

Voer alleen interne overboekingen uit als u begrijpt waarom het interne projectsaldo moet veranderen.

## Vergoedingen aan personen

Als iemand privé heeft betaald en later wordt vergoed, is het gebruikelijke patroon om de uitgave tegen een schuld te boeken en vervolgens de schuld te vereffenen met de bankbetaling.

```beancount
2026-03-01 ! "Winkel" "Materiaal gekocht door Marc"
  Ausgaben:Projekt:25-ZGV:Sachmittel  35.00 EUR
  Verbindlichkeiten:Person:Marc-Bielert
```

```beancount
2026-03-05 ! "Marc Bielert" "Vergoeding materiaal"
  Verbindlichkeiten:Person:Marc-Bielert  35.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Opmerkingen bij onduidelijke beslissingen

```beancount
; Onduidelijk of dit bij CEDU-25 of bij de vrije verenigingskas hoort. Factuur controleren.
2026-03-10 ! "Leverancier" "Factuur 456"
  Ausgaben:Sonstiges  120.00 EUR
  Vermoegen:Bank:Sparkasse-Tohuwabohu
```

## Veilig bewerken

Controleer voordat u gaat bewerken:

- U bevindt zich in het juiste verenigingsgrootboek.
- U bewerkt de gegenereerde importuitvoer niet alsof het het definitieve grootboek is.
- De transactiedatum is correct.
- Het bedrag gebruikt een punt als decimaalteken, bijvoorbeeld `12.50 EUR`.
- Rekeningnamen zijn exact gespeld zoals bestaande rekeningen.
- Projecttransacties gebruiken consequent het projectactiefaccount en de projectinkomsten-/uitgavencategorie.

Sla na het bewerken het bestand op, laad Fava opnieuw, controleer op fouten en inspecteer de relevante rekeningpagina.
