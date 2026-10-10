---
lang: nl
translation_id: beancount/12-troubleshooting
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Probleemoplossing
description: Veelvoorkomende Fava- en Beancount-problemen en hoe u ze kunt oplossen.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/12-troubleshooting.md
translation_source_body_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_source_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:32+00:00
translation_source_localized_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_source_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:32+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 12 - Probleemoplossing

## Fava wordt niet geopend

Controleer:

- Is het terminalvenster nog open?
- Is Fava gestart in de juiste map?
- Wordt de juiste poort gebruikt?
- Draait er al een andere Fava-instantie op dezelfde poort?
- Is Fava geïnstalleerd en beschikbaar in de terminal?

Commando's:

```powershell
fava nica.beancount --port 4998
fava 2023.beancount --port 4999
```

Voer elk commando alleen uit vanuit de juiste ledger-map.

## Fava toont een Beancount-fout

Veelvoorkomende oorzaken:

- Typfout in een rekeningnaam.
- Ontbrekende `open` directive voor een rekening.
- Bedrag gebruikt een komma in plaats van een punt.
- Aanhalingstekens ontbreken rond de begunstigde of de omschrijving.
- Een transactie is niet in balans.
- Een saldocheck komt niet overeen.
- Een transactie gebruikt een rekening nadat deze is gesloten.

Corrigeer het tekstbestand, sla het op en laad Fava opnieuw.

## Saldocheck mislukt

Verwijder de saldocheck niet als tijdelijke oplossing. Onderzoek het verschil.

Checklist:

- Was het datumbereik van de CSV compleet?
- Is dezelfde CSV dubbel geïmporteerd?
- Zijn er transacties in de verkeerde ledger geplakt?
- Is een transactie toegewezen aan de verkeerde Sparkasse-subrekening?
- Is een bedragteken incorrect gewijzigd?
- Is een PayPal- of contantstransfer slechts aan één kant ingevoerd?
- Zijn er oudere handmatige bewerkingen na de vorige saldocheck?

## CSV-conversie mislukt

Controleer:

- De CSV-bestand bevindt zich in dezelfde `test`-map als `csv2bean.py`.
- De bestandsnaam in het commando is exact.
- Het bestand is de Sparkasse `Excel (CSV-CAMT V2)` export.
- Het bestand is puntkomma-gescheiden.
- De CSV is niet geopend en opnieuw opgeslagen op een manier die het formaat heeft gewijzigd.

## Geïmporteerde vermeldingen zien er te algemeen uit

Dit is verwacht. De converter gebruikt standaardcategorieën zoals:

- `Ausgaben:Sonstiges`
- `Einnahmen:Sonstiges`

De gebruiker moet geïmporteerde vermeldingen handmatig beoordelen en classificeren.

## Dashboard ontbreekt

Controleer:

- `fava-dashboards` is geïnstalleerd.
- De ledger bevat de directive `custom "fava-extension" "fava_dashboards"`.
- Er bestaat een `dashboards.yaml`-bestand naast de ledger.
- Fava is opnieuw gestart na installatie of configuratiewijzigingen.

## Een project verschijnt niet in dashboards

Controleer:

- Het project heeft een project activa-rekening onder het verwachte Sparkasse- of PayPal-prefix.
- De projectrekening is niet gesloten.
- Het projectsaldo is niet exact nul.
- De rekeningnaam komt overeen met het dashboard query-patroon.

## Documentlink werkt niet

Controleer:

- Het bestandspad is relatief ten opzichte van de map van het ledger-bestand.
- De bestandsnaam is exact gespeld.
- Het document is niet verplaatst na het linken.
- Het pad gebruikt forward slashes of normale relatieve padstijl.

## Onzeker hoe een transactie te classificeren

Gebruik deze volgorde:

1. Zoek naar vergelijkbare oudere transacties in Fava.
2. Controleer de project- of factuurcontext.
3. Controleer of het behoort tot een budgetlijn van een financier.
4. Voeg een opmerking toe als u onzeker bent.
5. Gebruik tijdelijk `Sonstiges` alleen als er geen betere categorie bekend is.
6. Vraag de verantwoordelijke project- of financiële persoon voordat u definitief maakt.
