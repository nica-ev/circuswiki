---
lang: sk
translation_id: beancount/05-accounts-and-categories
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Účty a kategórie
description: Vysvetľuje nemeckú štruktúru účtov a konvencie kategórií používané v účtovných knihách.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/05-accounts-and-categories.md
translation_source_body_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_source_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:37:44+00:00
translation_source_localized_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_source_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:37:44+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 05 - Účty a kategórie

Táto stránka vysvetľuje štruktúru účtov používanú v účtovných knihách.

## Názvoslovie

Názvy účtov sú v nemčine. Používajte existujúce názvy účtov, aby boli výkazy konzistentné.

| Nemčina | Anglický význam |
| --- | --- |
| `Vermoegen` | Aktíva |
| `Verbindlichkeiten` | Záväzky |
| `Einnahmen` | Príjmy |
| `Ausgaben` | Výdavky |
| `Buero` | Kancelária |
| `Verein` | Združenie/všeobecná činnosť združenia |
| `Projekt` | Projekt |
| `Barkasse` | Pokladňa |
| `Freies-Geld` | Voľné/neobmedzené prostriedky |

## Účty aktív

Príklady NICA:

- `Vermoegen:Bank:Sparkasse-NICA`
- `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:NICA:Barkasse`
- `Vermoegen:Inventar`

Príklady Tohuwabohu:

- `Vermoegen:Bank:Sparkasse-Tohuwabohu`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:Tohuwabohu:Barkasse`

## Všeobecné účty príjmov

| Účet | Použitie pre |
| --- | --- |
| `Einnahmen:Vereinsbeitrag` | Členské príspevky. |
| `Einnahmen:Spende` | Dary. |
| `Einnahmen:Verleih` | Príjmy z prenájmu alebo požičiavania. |
| `Einnahmen:Sonstiges` | Ostatné príjmy, ktoré sa nehodia inam. |

## Všeobecné účty výdavkov

| Účet | Použitie pre |
| --- | --- |
| `Ausgaben:Buero:Miete` | Nájom kancelárie alebo priestoru. |
| `Ausgaben:Buero:Internet` | Internet a digitálne služby. |
| `Ausgaben:Buero:Sonstiges` | Ostatné kancelárske výdavky. |
| `Ausgaben:Verein:Versicherung` | Poistenie združenia. |
| `Ausgaben:Verein:Ehrenamt` | Príspevky dobrovoľníkom alebo náklady na dobrovoľníkov združenia. |
| `Ausgaben:Essen` | Výdavky na jedlo mimo konkrétneho projektu. |
| `Ausgaben:Sonstiges` | Dočasná záloha pre nejasné výdavky. |

`Ausgaben:Sonstiges` a `Einnahmen:Sonstiges` sú užitočné počas importu, ale nemali by sa stať konečnou kategóriou, ak existuje presnejšia kategória.

## Projektové účty

Projektové účty sa riadia týmto vzorom:

```text
Vermoegen:Bank:Sparkasse-ASSOCIATION:PROJECT
Ausgaben:Projekt:PROJECT
Einnahmen:Projekt:PROJECT
```

Príklady:

- `Vermoegen:Bank:Sparkasse-NICA:25-ZGV`
- `Ausgaben:Projekt:25-ZGV:Honorar`
- `Einnahmen:Projekt:25-ZGV:Sachmittel`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:TOHUCON-25`
- `Ausgaben:Projekt:TOHUCON-25:Essen`
- `Einnahmen:Projekt:TOHUCON-25:ConTickets`

## Typické projektové podkategórie

| Podkategória | Význam |
| --- | --- |
| `Honorar` | Poplatky vyplatené osobám alebo prijaté za prácu. |
| `Aufwand` | Náklady alebo príspevok na úsilie. |
| `Sachmittel` | Materiály a zásoby. |
| `Sonstiges` | Ostatné projektové náklady alebo príjmy. |
| `Pauschale` / `Pauschalen` | Paušálny alebo fixný projektový rozpočet. |

## Záväzky voči osobám

Účty záväzkov sledujú peniaze dlžné osobám alebo vyplatené späť osobám. Príklady zahŕňajú `Verbindlichkeiten:Person:Marc-Bielert`, `Verbindlichkeiten:Person:Peter-Huhndorf` a `Verbindlichkeiten:Person:Charleen-Hoffmann`.

## Výber správneho účtu

1. Ide o úroveň združenia alebo úroveň projektu?
2. Ak ide o úroveň projektu, ktorý projekt vlastní peniaze?
3. Ide o príjem, výdavok, pohyb aktív alebo splatenie záväzku?
4. Existuje už otvorená presná kategória?
5. Ak neexistuje vhodná kategória, dočasne použite `Sonstiges` a pridajte komentár.
