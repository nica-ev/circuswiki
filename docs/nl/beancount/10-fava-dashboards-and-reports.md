---
lang: nl
translation_id: beancount/10-fava-dashboards-and-reports
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Fava Dashboards en Rapporten
description: Overzicht van Fava-rapporten en aangepaste dashboards voor boekhoudkundige controle.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/10-fava-dashboards-and-reports.md
translation_source_body_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_source_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:18+00:00
translation_source_localized_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_source_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:18+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 10 - Fava Dashboards en Rapporten

Fava biedt standaard boekhoudkundige rapporten. Het systeem gebruikt ook `fava-dashboards` voor aangepaste overzichtspagina's.

## Standaard Fava-weergaven

| Weergave | Gebruik voor |
| --- | --- |
| Balans | Controleren van activa, passiva, vrij geld, PayPal, contanten en projectsaldi. |
| Winst- en verliesrekening | Inkomsten en uitgaven over tijd bekijken. |
| Rekeningpagina | Alle transacties voor één rekening inspecteren. |
| Journaal | Chronologische transactiegeschiedenis doorzoeken. |
| Query | Aangepaste Beancount-queries uitvoeren indien nodig. |
| Documenten | Gekoppelde bonnetjes en bestanden vinden. |

## Dashboard-uitbreiding

De ledgers bevatten deze directive:

```beancount
2010-01-01 custom "fava-extension" "fava_dashboards"
```

Dit activeert de dashboard-uitbreiding als `fava-dashboards` is geïnstalleerd.

## Dashboard-configuratiebestanden

Dashboardbestanden heten `dashboards.yaml`. Ze worden opgeslagen in de buurt van de ledgerbestanden en op het gedeelde boekhoudkundige niveau.

## Belangrijkste dashboardsecties

| Dashboard | Doel |
| --- | --- |
| `Vorstand-Cockpit` | Managementoverzicht: vrij geld, totaal Sparkasse-saldo, PayPal, contanten, liquiditeitstrend, maandelijks resultaat, actieve projectsaldi. |
| `Details & Daten` | Gedetailleerde grafieken: uitgaven per categorie, inkomsten per categorie, geldstroom, project/persoon-netwerk. |

## Belangrijke dashboardindicatoren

### Freies Geld (Vrij Geld)

Toont beschikbaar geld buiten de beperkte projectfondsen. Typische rekeningen zijn `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld` en `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`.

### Sparkasse Gesamt (Totaal Sparkasse)

Toont het totale Sparkasse-saldo van de hoofdbetaalrekening en interne subrekeningen.

### PayPal

Toont het PayPal-saldo. Een negatief PayPal-saldo geeft aan dat er iets gecontroleerd moet worden.

### Barkasse (Kassalade)

Toont het saldo van de kassalade.

### Saldo Aktiver Projekte (Saldo Actieve Projecten)

Toont projectsaldi die niet nul zijn. Dit is nuttig om te zien welke projecten nog geld bevatten of overschreden zijn.

### Monatlicher Ueberschuss / Fehlbetrag (Maandelijkse Overschot / Tekort)

Toont het maandelijkse operationele overschot of tekort, exclusief projectrekeningen in de dashboardquery.

## Hoe dashboards verantwoord te gebruiken

Dashboards zijn samenvattingen. Als een getal verrassend lijkt:

1. Klik op de gekoppelde Fava-rekening of het rapport.
2. Inspecteer de onderliggende transacties.
3. Controleer of een transactie nog in `Sonstiges` (Overig) of `Bank Dump` staat.
4. Controleer of de rekeningnaam overeenkomt met het patroon van de dashboardquery.
5. Bevestig saldocontroles voordat u managementcijfers vertrouwt.

## Wanneer dashboardcijfers onjuist lijken

Veelvoorkomende oorzaken:

- Een transactie is geboekt op de hoofdbetaalrekening in plaats van op de projectsubrekening.
- Een projectrekening is gesloten, maar heeft nog steeds een niet-nul saldo.
- Een nieuw project gebruikt een naamgevingspatroon dat niet is opgenomen in de dashboardquery.
- Een transactie bevindt zich nog in een brede vangnetcategorie.
- Het dashboardbestand behoort tot een andere ledger dan de momenteel geopende.
