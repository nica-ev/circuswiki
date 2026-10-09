---
lang: nl
translation_id: beancount/01-system-overview
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Systeemoverzicht
description: Legt het doel, de componenten en de normale gebruikersworkflow van het boekhoudsysteem uit.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/01-system-overview.md
translation_source_body_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_source_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:32:35+00:00
translation_source_localized_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_source_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:32:35+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 01 - Systeemoverzicht

## Doel

Het boekhoudsysteem registreert alle financiële activiteiten van de verenigingen op een gestructureerde, controleerbare manier. Het is ontworpen om gebruikelijke boekhoudkundige vragen te beantwoorden:

- Hoeveel geld is er momenteel beschikbaar?
- Welke inkomsten en uitgaven behoren tot de vereniging zelf?
- Welke inkomsten en uitgaven behoren tot een specifiek project?
- Kloppen de saldi van de Sparkasse, PayPal en contant geld?
- Welke bonnetjes en documenten horen bij welke transacties?
- Welke projecten zijn actief, voltooid of al afgesloten?

## Hoofdcomponenten

| Component | Wat het doet |
| --- | --- |
| Beancount | Het dataformaat voor de boekhouding. Transacties worden geschreven in platte tekstbestanden. |
| Fava | De browserinterface voor het bekijken en filteren van de Beancount-gegevens. |
| Fava Dashboards | Aangepaste dashboardpagina's binnen Fava voor een managementoverzicht en projectweergaven. |
| Obsidian | Het notitiesysteem van waaruit de boekhouding via knoppen geopend kan worden. |
| CSV import scripts | Hulp-scripts die Sparkasse CSV-exports converteren naar Beancount-boekingen. |

## Hoe de onderdelen samenkomen

1. Bank- of PayPal-gegevens worden als CSV geëxporteerd.
2. De CSV wordt geconverteerd naar tijdelijke Beancount-boekingen.
3. De nieuwe boekingen worden in het juiste grootboekbestand gekopieerd.
4. De gebruiker controleert, classificeert en corrigeert de boekingen.
5. Saldocontroles bevestigen dat het grootboek overeenkomt met het bank- of PayPal-saldo.
6. Fava toont rapporten, rekeningspecificaties, winst- en verliesrekeningen, balansen en dashboards.

## Twee aparte verenigingen

| Vereniging | Grootboek | Typische rekeningprefix |
| --- | --- | --- |
| NICA e.V. | `nica.beancount` | `Sparkasse-NICA`, `NICA` |
| Tohuwabohu Halle e.V. | `2023.beancount` | `Sparkasse-Tohuwabohu`, `Tohuwabohu` |

Er is ook een experimenteel gecombineerd bestand: `1. Vereinsverwaltung/Buchhaltung/all.beancount`. Normaal dagelijks werk moet plaatsvinden in het individuele grootboek van de betreffende vereniging.

## Basisworkflow

1. Open de juiste Fava-instantie.
2. Zoek de laatst voltooide saldocontrole.
3. Exporteer nieuwe banktransacties van Sparkasse vanaf de laatst gecontroleerde datum.
4. Converteer de CSV naar Beancount-formaat.
5. Plak de gegenereerde boekingen eerst in de sectie `Bank Dump`.
6. Verplaats of classificeer boekingen naar de juiste verenigings- of projectsecties.
7. Voeg indien nodig bonnetjes, links, opmerkingen of tags toe.
8. Voeg een nieuwe saldocontrole toe.
9. Laad Fava opnieuw en controleer of er geen fouten zijn.

## Wat een nieuwe gebruiker eerst moet leren

1. [Fava openen](02-opening-fava.md)
2. [Beancount Basis voor Gebruikers](04-beancount-basics-for-users.md)
3. [Bank CSV Import en Afstemming](07-bank-csv-import-and-reconciliation.md)
4. [Rekeningen en Categorieën](05-accounts-and-categories.md)
5. [Projecten en Bestemde Fondsen](08-projects-and-restricted-funds.md)
