---
lang: cs
translation_id: beancount/08-projects-and-restricted-funds
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Projekty a účelově vázané fondy
description: Vysvětluje, jak jsou projektové peníze a účelově vázané fondy reprezentovány a kontrolovány.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/08-projects-and-restricted-funds.md
translation_source_body_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_source_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:25+00:00
translation_source_localized_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_source_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:25+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 08 - Projekty a účelově vázané fondy

Projekty jsou klíčovou součástí tohoto účetního systému. Mnoho grantů a aktivit je třeba sledovat odděleně od peněz volného sdružení.

## Co projekt znamená v účetnictví

| Typ účtu | Příklad | Účel |
| --- | --- | --- |
| Projektový majetek | `Vermoegen:Bank:Sparkasse-NICA:25-ZGV` | Vnitřní zůstatek peněz projektu. |
| Projektové příjmy | `Einnahmen:Projekt:25-ZGV:Sachmittel` | Financování projektu nebo projektové příjmy. |
| Projektové výdaje | `Ausgaben:Projekt:25-ZGV:Sachmittel` | Výdaje projektu. |

Skutečný bankovní účet může být jeden účet Sparkasse, ale účetnictví odděluje vnitřní projektové zůstatky, aby tým mohl vidět, co patří ke každému projektu.

## Aktivní a uzavřené projekty

Aktivní projekty mají otevřené účty a relevantní zůstatky. Uzavřené projekty obvykle mají závěrečnou kontrolu zůstatku `0.00 EUR` a direktivy `close` pro účty projektového majetku, příjmů a výdajů.

Nezadávejte nové transakce do uzavřených projektů, pokud záměrně znovu neotevíráte nebo neopravujete historická data.

## Aktuální příklady v NICA

- `26-JEP-Buehnenreif`
- `25-ZGV`
- `25-CircusWiki`
- `25-Machen-UnitedAges`
- `25-Erasmus`
- uzavřené projekty z roku 2024, jako například `24-AWO`, `24-HONY`, `24-Peter`

## Aktuální příklady v Tohuwabohu

- `VHS-TOHU-25`
- `ZMS-TOHU-25`
- `CEDU-25`
- `TOHUCON-25`
- uzavřené projekty jako `Revierpionier-25`, `OAC-25`, `TohuCon2024`, `ZGV-TOHU-24`, `TohuCon2023`

## Vytvoření nového projektu

Nový projekt obvykle vyžaduje otevření účtů před zadáním transakcí.

```beancount
2026-01-01 open Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject:Honorar
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sachmittel
2026-01-01 open Ausgaben:Projekt:26-NewProject:Aufwand
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sonstiges
2026-01-01 open Einnahmen:Projekt:26-NewProject
2026-01-01 open Einnahmen:Projekt:26-NewProject:Honorar
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sachmittel
2026-01-01 open Einnahmen:Projekt:26-NewProject:Aufwand
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sonstiges
```

Otevřete pouze kategorie, které jsou pro projekt skutečně užitečné.

## Zadávání financování projektu

```beancount
2026-02-01 ! "Funding Body" "First payment NewProject"
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject  3000.00 EUR
  Einnahmen:Projekt:26-NewProject:Sachmittel
```

## Zadávání výdajů projektu

```beancount
2026-02-10 ! "Supplier" "Project material"
  Ausgaben:Projekt:26-NewProject:Sachmittel  250.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject
```

## Porozumění projektovým zůstatkům

Kladný zůstatek projektového majetku znamená, že danému projektu jsou stále přiděleny peníze. Nulový zůstatek projektového majetku znamená, že projekt nemá žádný zbývající vnitřní bankovní zůstatek. Záporný zůstatek projektového majetku obvykle znamená, že projekt utratil více, než byly přidělené prostředky, nebo chybí přidělení.

## Uzavření projektu

Před uzavřením projektu musí být zadány všechny příjmy a výdaje, účtenky musí být dohledatelné, účet projektového majetku musí být přesně nula a jakékoli zbývající peníze musí být správně přesunuty nebo vráceny.

```beancount
2026-12-31 balance Vermoegen:Bank:Sparkasse-NICA:26-NewProject 0.00 EUR
2026-12-31 close Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-12-31 close Ausgaben:Projekt:26-NewProject
2026-12-31 close Einnahmen:Projekt:26-NewProject
```

Pokud byly otevřeny samostatně, uzavřete i podúcty.
