---
lang: pl
translation_id: beancount/05-accounts-and-categories
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Konta i kategorie
description: Wyjaśnia niemiecką strukturę kont i konwencje kategorii używane w księgach rachunkowych.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/05-accounts-and-categories.md
translation_source_body_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_source_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:43+00:00
translation_source_localized_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_source_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:43+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 05 - Konten und Kategorien

Diese Seite erklärt die Kontenstruktur, die in den Büchern verwendet wird.

## Benennungssprache

Die Kontennamen sind deutsch. Verwenden Sie weiterhin die bestehenden Kontennamen, um die Berichte konsistent zu halten.

| Deutsch | Englische Bedeutung |
| --- | --- |
| `Vermoegen` | Assets |
| `Verbindlichkeiten` | Liabilities |
| `Einnahmen` | Income |
| `Ausgaben` | Expenses |
| `Buero` | Office |
| `Verein` | Association/general association activity |
| `Projekt` | Project |
| `Barkasse` | Cash box |
| `Freies-Geld` | Free/unrestricted funds |

## Vermögenskonten

NICA-Beispiele:

- `Vermoegen:Bank:Sparkasse-NICA`
- `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:NICA:Barkasse`
- `Vermoegen:Inventar`

Tohuwabohu-Beispiele:

- `Vermoegen:Bank:Sparkasse-Tohuwabohu`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:Tohuwabohu:Barkasse`

## Allgemeine Einnahmenkonten

| Konto | Verwendung für |
| --- | --- |
| `Einnahmen:Vereinsbeitrag` | Mitgliedsbeiträge. |
| `Einnahmen:Spende` | Spenden. |
| `Einnahmen:Verleih` | Einnahmen aus Vermietung oder Verleih. |
| `Einnahmen:Sonstiges` | Sonstige Einnahmen, die nirgendwo anders passen. |

## Allgemeine Ausgabenkonten

| Konto | Verwendung für |
| --- | --- |
| `Ausgaben:Buero:Miete` | Büro- oder Raummiete. |
| `Ausgaben:Buero:Internet` | Internet- und digitale Dienste. |
| `Ausgaben:Buero:Sonstiges` | Sonstige Bürokosten. |
| `Ausgaben:Verein:Versicherung` | Vereinsversicherung. |
| `Ausgaben:Verein:Ehrenamt` | Aufwandsentschädigungen für Ehrenamtliche oder Kosten für ehrenamtliche Vereinsarbeit. |
| `Ausgaben:Essen` | Essenskosten außerhalb eines bestimmten Projekts. |
| `Ausgaben:Sonstiges` | Vorübergehender Auffang für unklare Ausgaben. |

`Ausgaben:Sonstiges` und `Einnahmen:Sonstiges` sind beim Import nützlich, sollten aber nicht zur endgültigen Kategorie werden, wenn eine genauere Kategorie existiert.

## Projektkonten

Projektkonten folgen diesem Muster:

```text
Vermoegen:Bank:Sparkasse-VEREIN:PROJEKT
Ausgaben:Projekt:PROJEKT
Einnahmen:Projekt:PROJEKT
```

Beispiele:

- `Vermoegen:Bank:Sparkasse-NICA:25-ZGV`
- `Ausgaben:Projekt:25-ZGV:Honorar`
- `Einnahmen:Projekt:25-ZGV:Sachmittel`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:TOHUCON-25`
- `Ausgaben:Projekt:TOHUCON-25:Essen`
- `Einnahmen:Projekt:TOHUCON-25:ConTickets`

## Typische Projektunterkategorien

| Unterkategorie | Bedeutung |
| --- | --- |
| `Honorar` | Honorare, die an Personen gezahlt oder für Arbeit erhalten werden. |
| `Aufwand` | Aufwandsentschädigung oder Pauschale für Aufwand. |
| `Sachmittel` | Materialien und Verbrauchsgüter. |
| `Sonstiges` | Sonstige Projektkosten oder -einnahmen. |
| `Pauschale` / `Pauschalen` | Pauschalbetrag oder Pauschalbudget für ein Projekt. |

## Verbindlichkeiten gegenüber Personen

Verbindlichkeitskonten erfassen Geld, das Personen geschuldet wird oder an Personen zurückgezahlt wird. Beispiele hierfür sind `Verbindlichkeiten:Person:Marc-Bielert`, `Verbindlichkeiten:Person:Peter-Huhndorf` und `Verbindlichkeiten:Person:Charleen-Hoffmann`.

## Auswahl des richtigen Kontos

1. Handelt es sich um eine Ebene des Vereins oder des Projekts?
2. Wenn es sich um eine Projektebene handelt, welches Projekt besitzt das Geld?
3. Handelt es sich um Einnahmen, Ausgaben, Vermögensbewegung oder Rückzahlung einer Verbindlichkeit?
4. Gibt es bereits eine genaue Kategorie?
5. Wenn es keine passende Kategorie gibt, verwenden Sie vorübergehend `Sonstiges` und fügen Sie einen Kommentar hinzu.
