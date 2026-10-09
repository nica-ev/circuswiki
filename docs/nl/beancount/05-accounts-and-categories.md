---
lang: nl
translation_id: beancount/05-accounts-and-categories
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Rekeningen en Categorieën
description: Legt de Duitse rekeningstructuur en categorieconventies uit die in de grootboeken worden gebruikt.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/05-accounts-and-categories.md
translation_source_body_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_source_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:37:06+00:00
translation_source_localized_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_source_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:37:06+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 05 - Rekeningen en Categorieën

Deze pagina legt de rekenstructuur uit die in de grootboeken wordt gebruikt.

## Naamgeving

De rekeningnamen zijn Duits. Blijf de bestaande rekeningnamen gebruiken om rapporten consistent te houden.

| Duits | Engelse betekenis |
| --- | --- |
| `Vermoegen` | Bezittingen |
| `Verbindlichkeiten` | Verplichtingen |
| `Einnahmen` | Inkomsten |
| `Ausgaben` | Uitgaven |
| `Buero` | Kantoor |
| `Verein` | Vereniging/algemene verenigingsactiviteit |
| `Projekt` | Project |
| `Barkasse` | Kassa |
| `Freies-Geld` | Vrij/onbeperkt geld |

## Bezittingenrekeningen

NICA-voorbeelden:

- `Vermoegen:Bank:Sparkasse-NICA`
- `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:NICA:Barkasse`
- `Vermoegen:Inventar`

Tohuwabohu-voorbeelden:

- `Vermoegen:Bank:Sparkasse-Tohuwabohu`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:Tohuwabohu:Barkasse`

## Algemene inkomstenrekeningen

| Rekening | Gebruik voor |
| --- | --- |
| `Einnahmen:Vereinsbeitrag` | Lidmaatschapsgelden. |
| `Einnahmen:Spende` | Donaties. |
| `Einnahmen:Verleih` | Huur- of uitleeninkomsten. |
| `Einnahmen:Sonstiges` | Overige inkomsten die elders niet passen. |

## Algemene uitgavenrekeningen

| Rekening | Gebruik voor |
| --- | --- |
| `Ausgaben:Buero:Miete` | Huur van kantoor of ruimte. |
| `Ausgaben:Buero:Internet` | Internet en digitale diensten. |
| `Ausgaben:Buero:Sonstiges` | Overige kantoorkosten. |
| `Ausgaben:Verein:Versicherung` | Verzekeringen van de vereniging. |
| `Ausgaben:Verein:Ehrenamt` | Vrijwilligersvergoedingen of kosten voor vrijwilligers van de vereniging. |
| `Ausgaben:Essen` | Kosten voor eten buiten een specifiek project. |
| `Ausgaben:Sonstiges` | Tijdelijke vangnet voor onduidelijke uitgaven. |

`Ausgaben:Sonstiges` en `Einnahmen:Sonstiges` zijn nuttig tijdens de import, maar mogen niet de definitieve categorie worden als er een specifiekere categorie bestaat.

## Projectrekeningen

Projectrekeningen volgen dit patroon:

```text
Vermoegen:Bank:Sparkasse-VERENIGING:PROJECT
Ausgaben:Projekt:PROJECT
Einnahmen:Projekt:PROJECT
```

Voorbeelden:

- `Vermoegen:Bank:Sparkasse-NICA:25-ZGV`
- `Ausgaben:Projekt:25-ZGV:Honorar`
- `Einnahmen:Projekt:25-ZGV:Sachmittel`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:TOHUCON-25`
- `Ausgaben:Projekt:TOHUCON-25:Essen`
- `Einnahmen:Projekt:TOHUCON-25:ConTickets`

## Typische projectsubcategorieën

| Subcategorie | Betekenis |
| --- | --- |
| `Honorar` | Vergoedingen betaald aan of ontvangen voor werk. |
| `Aufwand` | Inspanning of onkostenvergoeding. |
| `Sachmittel` | Materialen en benodigdheden. |
| `Sonstiges` | Overige projectkosten of inkomsten. |
| `Pauschale` / `Pauschalen` | Vaste prijs of forfaitair projectbudget. |

## Verplichtingen aan personen

Verplichtingenrekeningen houden geld bij dat aan personen verschuldigd is of aan personen wordt terugbetaald. Voorbeelden zijn `Verbindlichkeiten:Person:Marc-Bielert`, `Verbindlichkeiten:Person:Peter-Huhndorf` en `Verbindlichkeiten:Person:Charleen-Hoffmann`.

## De juiste rekening kiezen

1. Is dit op verenigingsniveau of projectniveau?
2. Zo ja, welk project is eigenaar van het geld?
3. Is het een inkomst, uitgave, bezittingenbeweging of terugbetaling van een verplichting?
4. Bestaat er al een specifieke categorie?
5. Als er geen geschikte categorie is, gebruik dan tijdelijk `Sonstiges` en voeg een opmerking toe.
