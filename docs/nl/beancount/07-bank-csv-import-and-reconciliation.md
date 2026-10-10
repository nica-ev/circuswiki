---
lang: nl
translation_id: beancount/07-bank-csv-import-and-reconciliation
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Bank CSV Import en Afstemming
description: Workflow voor het importeren van Sparkasse CSV-gegevens en het afstemmen van banksaldi.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/07-bank-csv-import-and-reconciliation.md
translation_source_body_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_source_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:05:22+00:00
translation_source_localized_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_source_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:05:22+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 07 - Bank CSV-import en afstemming

Deze workflow brengt nieuwe Sparkasse-transacties in Beancount en bevestigt dat het grootboek nog steeds overeenkomt met de echte bankrekening.

## Waar imports plaatsvinden

| Vereniging | Importmap | Script | Uitvoerbestand |
| --- | --- | --- | --- |
| NICA | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/test` | `csv2bean.py` | `beancount_file.beancount` |
| Tohuwabohu | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/test` | `csv2bean.py` | `beancount_file.beancount` |

## Vóór het exporteren uit Sparkasse

1. Open het juiste grootboekbestand.
2. Zoek de sectie `Balance Checks`.
3. Zoek de laatste saldostatusdatum voor de Sparkasse-rekening.
4. Controleer ook de sectie `Bank Dump` onderaan voor de laatst geïmporteerde datum.
5. Gebruik de laatste van die datums als uw startpunt.

Dit voorkomt het missen van transacties of het dubbel importeren van dezelfde periode.

## Exporteren uit Sparkasse

1. Open het rekeningoverzicht.
2. Filter op datumbereik.
3. Begin vanaf de laatst gecontroleerde of geïmporteerde datum.
4. Eindig met vandaag of de gewenste afstemmingsdatum.
5. Exporteer als `Excel (CSV-CAMT V2)`.
6. Kopieer de gedownloade CSV naar de juiste `test`-map.

De scripts verwachten het Sparkasse CSV-CAMT-V2-formaat met door puntkomma's gescheiden kolommen.

## De CSV converteren

Open een terminal in de juiste `test`-map en voer uit:

```powershell
python csv2bean.py "NAAM-VAN-GEDOWNLOADE-BESTAND.CSV"
```

Voorbeeld:

```powershell
python csv2bean.py "20260312-1894137139-umsatz.CSV"
```

Als het werkt, drukt het script `Process finished.` af en maakt het `beancount_file.beancount` aan of overschrijft het.

## Wat de converter doet

De converter maakt basis Beancount-boekingen aan:

- Inkomende bedragen gaan standaard naar de Sparkasse-activa-rekening en `Einnahmen:Sonstiges`.
- Uitgaande bedragen gaan standaard naar `Ausgaben:Sonstiges` en de Sparkasse-activa-rekening.
- Sommige inkomstenbeschrijvingen worden automatisch geclassificeerd als `Einnahmen:Vereinsbeitrag`.
- Sommige Tohuwabohu-gerelateerde tekst kan worden geclassificeerd als een projectinkomstenrekening.

De converter is slechts een eerste stap. Het kent niet de uiteindelijke boekhoudkundige betekenis van elke transactie.

## Kopiëren naar het hoofdgrootboek

1. Open `test/beancount_file.beancount`.
2. Negeer de gegenereerde optie-header.
3. Kopieer alleen de transacties.
4. Plak ze eerst onder `Bank Dump` in het hoofdgrootboek.
5. Voeg indien nodig een gedateerde scheiding toe voor de importdatum.

```beancount
****************************************************************************
** 2026-01-13
****************************************************************************
```

De `Bank Dump` is een tussenopslag. Geïmporteerde transacties kunnen later naar de juiste thematische of projectsectie worden verplaatst.

## Geïmporteerde boekingen classificeren

Beslis voor elke geïmporteerde transactie:

- Is het op verenigingsniveau of projectniveau?
- Is het inkomsten of uitgaven?
- Is het een vergoeding of een afbetaling van een schuld?
- Behoort het tot `Freies-Geld` of een projectspecifieke activa-rekening?
- Is er een ontvangstbewijs of factuur om bij te voegen?

Vervang brede standaardrekeningen zoals `Ausgaben:Sonstiges` wanneer er een nauwkeurigere rekening bestaat.

## Een saldocheck toevoegen

NICA-voorbeeld:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Tohuwabohu-voorbeeld:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-Tohuwabohu 2345.67 EUR
```

Gebruik het saldo dat Sparkasse voor die exacte datum aangeeft.

## Valideren in Fava

1. Sla het grootboekbestand op.
2. Laad Fava opnieuw.
3. Controleer op fouten bovenaan de Fava-pagina.
4. Open de Sparkasse-rekeningspagina.
5. Bevestig het lopende saldo en de laatste transacties.
6. Controleer de Balans.
7. Controleer projectdashboards als projectrekeningen zijn beïnvloed.

## Als de saldocheck mislukt

Veelvoorkomende oorzaken:

- De CSV-export heeft één dag aan het begin of einde gemist.
- Een transactie is dubbel geïmporteerd.
- Een transactie is in het verkeerde verenigingsgrootboek geplakt.
- Een getal is onjuist bewerkt.
- Een projectverdeling gebruikte het verkeerde teken.
- PayPal- of contante transacties zijn niet ook geregistreerd.

Verwijder de saldocheck niet zomaar om de fout te laten verdwijnen. Los het onderliggende verschil in transacties op.
