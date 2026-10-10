---
lang: cs
translation_id: beancount/04-beancount-basics-for-users
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Základy Beancount pro uživatele
description: Představuje textový formát Beancount a vzory transakcí používané v účetních knihách.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/04-beancount-basics-for-users.md
translation_source_body_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_source_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:40+00:00
translation_source_localized_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_source_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:40+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 04 - Základy Beancountu pro uživatele

Beancount ukládá účetnictví ve formátu čitelného textu. Každá transakce uvádí, co se stalo, kdy, kdo byl zapojen a které účty se změnily.

## Základní tvar transakce

```beancount
2026-01-13 ! "Tragerwerk Soziale Dienste in Sachsen-Anhalt GmbH" "RgNr. T-2504"
  Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld  680.00 EUR
  Einnahmen:Sonstiges
```

| Část | Význam |
| --- | --- |
| `2026-01-13` | Datum transakce. |
| `!` | Příznak stavu. V tomto systému se běžně používá pro importované nebo ještě ne zcela zkontrolované položky. |
| První text v uvozovkách | Příjemce nebo odesílatel. |
| Druhý text v uvozovkách | Popis nebo účetní text z banky. |
| První řádek účtu | Kam peníze šly nebo odkud přišly. |
| Druhý řádek účtu | Protikladná kategorie. Pokud není uvedena žádná částka, Beancount ji vypočítá automaticky. |

## Názvy účtů

Názvy účtů jsou odděleny dvojtečkami:

```text
Vermoegen:Bank:Sparkasse-NICA:Freies-Geld
```

Čtěte zleva doprava: aktivum, bankovní účet, Sparkasse NICA, volně dostupné prostředky.

## Pět rodin účtů

| Rodina | Význam | Příklad |
| --- | --- | --- |
| `Vermoegen` | Aktiva: banka, PayPal, hotovost, zásoby. | `Vermoegen:Bank:Sparkasse-NICA` |
| `Verbindlichkeiten` | Závazky: peníze dlužné lidem nebo jiným. | `Verbindlichkeiten:Person:Marc-Bielert` |
| `Equity` | Počáteční zůstatky a vyrovnávací položky. | `Equity:Opening-Balances` |
| `Einnahmen` | Příjmy. | `Einnahmen:Vereinsbeitrag` |
| `Ausgaben` | Výdaje. | `Ausgaben:Buero:Miete` |

## Znaménka u příjmů a výdajů

V přehledech Beancountu se příjmy interně často zobrazují se záporným znaménkem a výdaje s kladným znaménkem. Fava a dashboardy často prezentují tyto hodnoty uživatelsky přívětivějším způsobem. Neměňte transakce jen proto, že číslo příjmu vypadá v surovém dotazu záporně.

## Kontroly zůstatku

Kontrola zůstatku uvádí, že účet musí mít k určitému datu specifický zůstatek:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Pokud Beancount nemůže tento zůstatek dohledat z transakcí před tímto datem, Fava zobrazí chybu. Kontroly zůstatku jsou hlavním mechanismem kontroly kvality.

## Otevření a uzavření účtů

Před použitím účtu se otevře:

```beancount
2025-04-01 open Ausgaben:Projekt:25-ZGV:Honorar
```

Když je projekt dokončen a účet projektu je nulový, může být uzavřen:

```beancount
2026-02-27 close Ausgaben:Projekt:TOHUCON-25
```

Uzavřené účty by obvykle neměly přijímat nové transakce.

## Komentáře a dokumenty

Řádky začínající na `;` jsou komentáře. Vysvětlují rozhodnutí nebo nejisté situace a neovlivňují čísla.

Účtenky lze propojit řádky `document`:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```
