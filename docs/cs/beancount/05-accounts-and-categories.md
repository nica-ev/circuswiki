---
lang: cs
translation_id: beancount/05-accounts-and-categories
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Účty a kategorie
description: Vysvětluje německou strukturu účtů a konvence kategorií používané v účetních knihách.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/05-accounts-and-categories.md
translation_source_body_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_source_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:37:36+00:00
translation_source_localized_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_source_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:37:36+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 05 - Účty a kategorie

Tato stránka vysvětluje strukturu účtů používanou v účetních knihách.

## Jazyk názvů

Názvy účtů jsou v němčině. Používejte stávající názvy účtů, aby byly zprávy konzistentní.

| Německy | Anglický význam |
| --- | --- |
| `Vermoegen` | Aktiva |
| `Verbindlichkeiten` | Závazky |
| `Einnahmen` | Příjmy |
| `Ausgaben` | Výdaje |
| `Buero` | Kancelář |
| `Verein` | Sdružení/obecná činnost sdružení |
| `Projekt` | Projekt |
| `Barkasse` | Pokladna |
| `Freies-Geld` | Volné/neomezené prostředky |

## Účty aktiv

Příklady NICA:

- `Vermoegen:Bank:Sparkasse-NICA`
- `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:NICA:Barkasse`
- `Vermoegen:Inventar`

Příklady Tohuwabohu:

- `Vermoegen:Bank:Sparkasse-Tohuwabohu`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:Tohuwabohu:Barkasse`

## Obecné účty příjmů

| Účet | Použití pro |
| --- | --- |
| `Einnahmen:Vereinsbeitrag` | Členské příspěvky. |
| `Einnahmen:Spende` | Dary. |
| `Einnahmen:Verleih` | Příjmy z pronájmu nebo půjčování. |
| `Einnahmen:Sonstiges` | Ostatní příjmy, které se jinam nevejdou. |

## Obecné účty výdajů

| Účet | Použití pro |
| --- | --- |
| `Ausgaben:Buero:Miete` | Nájem kanceláře nebo místnosti. |
| `Ausgaben:Buero:Internet` | Internet a digitální služby. |
| `Ausgaben:Buero:Sonstiges` | Ostatní kancelářské výdaje. |
| `Ausgaben:Verein:Versicherung` | Pojištění sdružení. |
| `Ausgaben:Verein:Ehrenamt` | Příspěvky dobrovolníkům nebo náklady na dobrovolnickou činnost sdružení. |
| `Ausgaben:Essen` | Výdaje za jídlo mimo konkrétní projekt. |
| `Ausgaben:Sonstiges` | Dočasná záloha pro nejasné výdaje. |

`Ausgaben:Sonstiges` a `Einnahmen:Sonstiges` jsou užitečné při importu, ale neměly by se stát konečnou kategorií, pokud existuje přesnější kategorie.

## Projektové účty

Projektové účty se řídí tímto vzorem:

```text
Vermoegen:Bank:Sparkasse-ASSOCIATION:PROJECT
Ausgaben:Projekt:PROJECT
Einnahmen:Projekt:PROJECT
```

Příklady:

- `Vermoegen:Bank:Sparkasse-NICA:25-ZGV`
- `Ausgaben:Projekt:25-ZGV:Honorar`
- `Einnahmen:Projekt:25-ZGV:Sachmittel`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:TOHUCON-25`
- `Ausgaben:Projekt:TOHUCON-25:Essen`
- `Einnahmen:Projekt:TOHUCON-25:ConTickets`

## Typické podkategorie projektů

| Podkategorie | Význam |
| --- | --- |
| `Honorar` | Poplatky placené lidem nebo přijaté za práci. |
| `Aufwand` | Náklady nebo paušál na výdaje. |
| `Sachmittel` | Materiály a zásoby. |
| `Sonstiges` | Ostatní náklady nebo příjmy projektu. |
| `Pauschale` / `Pauschalen` | Paušální nebo fixní rozpočet projektu. |

## Závazky vůči osobám

Účty závazků sledují peníze dlužné osobám nebo vrácené osobám. Příklady zahrnují `Verbindlichkeiten:Person:Marc-Bielert`, `Verbindlichkeiten:Person:Peter-Huhndorf` a `Verbindlichkeiten:Person:Charleen-Hoffmann`.

## Výběr správného účtu

1. Jedná se o úroveň sdružení nebo úroveň projektu?
2. Pokud úroveň projektu, který projekt peníze vlastní?
3. Jedná se o příjem, výdaj, pohyb aktiva nebo splátku závazku?
4. Existuje již otevřená přesná kategorie?
5. Pokud neexistuje vhodná kategorie, použijte dočasně `Sonstiges` a přidejte komentář.
