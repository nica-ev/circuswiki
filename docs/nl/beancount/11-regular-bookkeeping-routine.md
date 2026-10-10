---
lang: nl
translation_id: beancount/11-regular-bookkeeping-routine
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Regelmatige Boekhoudroutine
description: Een praktische, terugkerende checklist om de grootboeken up-to-date te houden.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/11-regular-bookkeeping-routine.md
translation_source_body_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_source_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:54+00:00
translation_source_localized_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_source_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:54+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 11 - Standaard Boekhoudroutine

Deze pagina beschrijft een praktische routine voor het actueel houden van de grootboeken.

## Wekelijkse of tweewekelijkse routine

Gebruik dit wanneer er regelmatige banktransacties zijn.

1. Open de juiste Fava-instantie.
2. Controleer of Fava fouten aangeeft.
3. Zoek de laatste saldocheck.
4. Exporteer nieuwe Sparkasse CSV-gegevens.
5. Converteer de CSV met `csv2bean.py`.
6. Plak nieuwe transacties in `Bank Dump`.
7. Classificeer transacties in de juiste rekeningen.
8. Voeg waar nodig bonnetjes toe of verwijs ernaar.
9. Voeg een nieuwe saldocheck toe.
10. Herlaad Fava en los fouten op.
11. Controleer `Ausgaben:Sonstiges` en `Einnahmen:Sonstiges` op transacties die specifieker moeten zijn.

## Maandelijkse routine

Aan het einde van de maand:

1. Reconciliation van Sparkasse.
2. Reconciliation van PayPal indien gebruikt.
3. Reconciliation van de kas indien contant geld is gebruikt.
4. Controleer openstaande schulden aan personen.
5. Controleer de saldi van actieve projecten.
6. Controleer niet-geclassificeerde `Sonstiges`-transacties.
7. Controleer ontbrekende bonnetjes.
8. Controleer of afgeronde projecten klaar zijn voor afsluiting.

## Projectrapportage routine

Voordat een projectrapport of gebruiksverantwoording wordt opgesteld:

1. Open de projectrekeningpagina's in Fava.
2. Exporteer of bekijk alle projectinkomsten en -uitgaven.
3. Bevestig dat de categorieën overeenkomen met de budgetlijnen van de financier.
4. Bevestig dat alle bonnetjes en honorariumbewijzen aanwezig zijn.
5. Controleer of terugbetalingen, annuleringen en vergoedingen worden geboekt als correcties en niet als valse inkomsten.
6. Bevestig dat het projectactivasaldo verklaarbaar is.
7. Als het project is afgerond, verplaats dan het resterende geld correct en sluit de projectrekeningen af.

## Jaareinde routine

Aan het einde van het jaar:

1. Reconciliation van alle bankrekeningen.
2. Reconciliation van PayPal.
3. Reconciliation van de kassen.
4. Controleer schulden.
5. Controleer openstaande projectsaldi.
6. Zorg ervoor dat alle bonnetjes zijn opgeslagen en gekoppeld of vindbaar zijn.
7. Controleer inkomsten- en uitgavencategorieën.
8. Voeg definitieve saldochecks toe.
9. Bereid rapporten voor vanuit Fava.
10. Archiveer geëxporteerde CSV's en ondersteunende documenten.

## Kwaliteitscontroles

Een grootboek is in goede staat wanneer:

- Fava zonder fouten opent.
- De laatste Sparkasse-saldocheck overeenkomt met de bank.
- PayPal- en kassaldi worden gecontroleerd waar relevant.
- Projectsaldi zijn bedoeld en verklaarbaar.
- Afgesloten projecten een activasaldo van nul hebben.
- `Sonstiges`-rekeningen geen vermijdbare niet-gecategoriseerde transacties bevatten.
- Bonnetjes voor uitgaven te vinden zijn.
- Opmerkingen ongebruikelijke correcties of aannames verklaren.

## Overdrachtschecklist voor een andere persoon

Voordat de boekhouding aan iemand anders wordt overgedragen:

- Laat hen het juiste grootboekbestand voor elke vereniging zien.
- Laat hen zien hoe Fava gestart moet worden.
- Laat hen de laatste saldocheck zien.
- Laat hen zien hoe CSV-imports worden gestaged in `Bank Dump`.
- Laat hen zien waar bonnetjes worden opgeslagen.
- Laat hen één voorbeeldproject zien, van financieringsinkomsten tot de definitieve afsluiting.
- Wijs hen op deze documentatiemap.
