---
lang: nl
translation_id: beancount/04-beancount-basics-for-users
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Beancount Basis voor Gebruikers
description: Introduceert het Beancount tekstformaat en de transactiepatronen die in de grootboeken worden gebruikt.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/04-beancount-basics-for-users.md
translation_source_body_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_source_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:36:03+00:00
translation_source_localized_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_source_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:36:03+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 04 - Beancount Basis voor Gebruikers

Beancount slaat boekhouding op als leesbare tekst. Elke transactie geeft aan wat er gebeurde, op welke datum, wie erbij betrokken was en welke rekeningen werden gewijzigd.

## Basisstructuur van een transactie

```beancount
2026-01-13 ! "Tragerwerk Soziale Dienste in Sachsen-Anhalt GmbH" "RgNr. T-2504"
  Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld  680.00 EUR
  Einnahmen:Sonstiges
```

| Deel | Betekenis |
| --- | --- |
| `2026-01-13` | Datum van de transactie. |
| `!` | Statusmarkering. In dit systeem wordt dit vaak gebruikt voor geïmporteerde of nog niet definitief beoordeelde posten. |
| Eerste geciteerde tekst | Ontvanger of afzender. |
| Tweede geciteerde tekst | Omschrijving of boekingskenmerk van de bank. |
| Eerste rekeningregel | Waar het geld naartoe ging of vandaan kwam. |
| Tweede rekeningregel | De tegenrekening. Als er geen bedrag wordt ingevuld, berekent Beancount dit automatisch. |

## Rekeningnamen

Rekeningnamen worden gescheiden door dubbele punten:

```text
Vermoegen:Bank:Sparkasse-NICA:Freies-Geld
```

Lees dit van links naar rechts: bezit, bankrekening, NICA Sparkasse, vrij beschikbaar saldo.

## De vijf rekeningfamilies

| Familie | Betekenis | Voorbeeld |
| --- | --- | --- |
| `Vermoegen` | Bezittingen: bank, PayPal, contant geld, voorraad. | `Vermoegen:Bank:Sparkasse-NICA` |
| `Verbindlichkeiten` | Schulden: geld verschuldigd aan personen of anderen. | `Verbindlichkeiten:Person:Marc-Bielert` |
| `Equity` | Openingssaldi en correctieboekingen. | `Equity:Opening-Balances` |
| `Einnahmen` | Inkomsten. | `Einnahmen:Vereinsbeitrag` |
| `Ausgaben` | Uitgaven. | `Ausgaben:Buero:Miete` |

## Tekens voor inkomsten en uitgaven

In Beancount-rapporten verschijnen inkomsten intern vaak met een minteken en uitgaven met een plusteken. Fava en de dashboards presenteren deze waarden vaak op een gebruiksvriendelijkere manier. Wijzig transacties niet zomaar omdat een inkomstengetal negatief lijkt in een ruwe query.

## Saldocontroles

Een saldocontrole stelt dat een rekening op een bepaalde datum een specifiek saldo moet hebben:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Als Beancount dat saldo niet kan matchen met de transacties van vóór die datum, geeft Fava een foutmelding. Saldocontroles zijn het belangrijkste kwaliteitscontrolemechanisme.

## Rekeningen openen en sluiten

Voordat een rekening wordt gebruikt, wordt deze geopend:

```beancount
2025-04-01 open Ausgaben:Projekt:25-ZGV:Honorar
```

Wanneer een project is afgerond en de projectrekening op nul staat, kan deze worden gesloten:

```beancount
2026-02-27 close Ausgaben:Projekt:TOHUCON-25
```

Gesloten rekeningen mogen normaal gesproken geen nieuwe transacties meer ontvangen.

## Opmerkingen en documenten

Regels die beginnen met `;` zijn opmerkingen. Ze leggen beslissingen of onzekere situaties uit en hebben geen invloed op de cijfers.

Bonnen kunnen worden gekoppeld met `document`-regels:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```
