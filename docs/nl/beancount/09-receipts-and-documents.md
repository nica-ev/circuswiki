---
lang: nl
translation_id: beancount/09-receipts-and-documents
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Bonnen en Documenten
description: Legt uit waar ondersteunende documenten worden opgeslagen en hoe transacties verwijzen naar bonnen.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/09-receipts-and-documents.md
translation_source_body_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_source_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:43+00:00
translation_source_localized_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_source_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:43+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 09 - Bonnen en Documenten

Bonnen, facturen, contracten en andere ondersteunende documenten maken transacties controleerbaar. Het grootboek moet het mogelijk maken om het document achter een uitgave te vinden.

## Waar documenten worden opgeslagen

Tohuwabohu heeft momenteel een duidelijke bonnenmap:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben
```

Bonnen die al in het grootboek zijn opgenomen, bevinden zich vaak in:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben/Eingetragen
```

NICA gebruikt ondersteunende bestanden in zijn boekhoudmap en projectmappen. Als er later een consistente NICA-bonnenmap wordt geïntroduceerd, documenteer dit dan hier en gebruik deze consequent.

## `document` vermeldingen

Een documentvermelding koppelt een bestand aan een rekening en datum:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```

Het bestandspad is relatief ten opzichte van de map die het grootboekbestand bevat.

## Documentkoppelingen met tags

Sommige oudere vermeldingen bevatten documenttags zoals:

```beancount
2023-01-05 document Ausgaben:Buero:Sonstiges "Belege Ausgaben/Eingetragen/2023_001.jpg" ^2023_001
```

Het deel `^2023_001` is een Beancount-koppeling. Het kan een bon koppelen aan de gerelateerde transactie als dezelfde koppeling daar wordt gebruikt.

## Betekenis van `scanned`

Opmerkingen in de grootboeken definiëren de conventie voor gescande bonnen. Wanneer de tag `scanned` wordt gebruikt, betekent dit:

- De bon is gescand of gedigitaliseerd.
- De afbeelding is verkleind en geoptimaliseerd, bijvoorbeeld met TinyPNG.
- Het bestand is opgeslagen met een jaar- en nummerpatroon, bijvoorbeeld `2023_002.jpg`.
- Het nummer wordt vermeld in de gerelateerde grootboekvermelding.

## Goede bestandsnamen

Goede bestandsnamen voor bonnen zijn stabiel en leesbaar:

```text
2026_001.jpg
2026_002.pdf
Quittung-Tohu25-001.pdf
Invoice406-Schwarze_Risse-marc-bielert.pdf
```

Vermijd namen zoals `scan.jpg`, `image1.jpg` of `download.pdf`.

## Workflow voor een nieuwe bon

1. Sla de bon op in de juiste bonnenmap.
2. Hernoem deze zodat deze later herkend kan worden.
3. Voer de gerelateerde transactie in of zoek deze op.
4. Voeg een `document` regel of koppel metadata toe indien nuttig.
5. Als de bon is verwerkt, verplaats deze dan naar `Eingetragen` als dat de mapconventie is.
6. Laad Fava opnieuw en controleer of de documentkoppeling werkt.

## Wanneer een bon ontbreekt

Als een bon ontbreekt, voeg dan een opmerking toe bij de transactie:

```beancount
; Bon ontbreekt. Vraag verantwoordelijke persoon.
```

Doe niet alsof er een document is als het niet beschikbaar is.

## Contracten en honorariumbonnen

Contracten en honorariafacturen moeten worden opgeslagen in de buurt van het gerelateerde project of de boekhoudmap en duidelijk worden vermeld. Voor projectaudits is de belangrijke vraag niet alleen of de transactie bestaat, maar ook of het document dat de uitgave bewijst snel kan worden gevonden.
