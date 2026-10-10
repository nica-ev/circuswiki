---
lang: pl
translation_id: beancount/08-projects-and-restricted-funds
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Projekty i Fundusze Ograniczone
description: Wyjaśnia, jak reprezentowane i sprawdzane są pieniądze projektowe i fundusze ograniczone.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/08-projects-and-restricted-funds.md
translation_source_body_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_source_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:05:55+00:00
translation_source_localized_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_source_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:05:55+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 08 - Projekty i fundusze ograniczone

Projekty są kluczowe dla tego systemu księgowego. Wiele dotacji i działań musi być śledzonych oddzielnie od środków wolnego stowarzyszenia.

## Co oznacza projekt w księdze

| Typ konta | Przykład | Cel |
| --- | --- | --- |
| Aktywa projektu | `Vermoegen:Bank:Sparkasse-NICA:25-ZGV` | Wewnętrzne saldo środków projektu. |
| Przychody projektu | `Einnahmen:Projekt:25-ZGV:Sachmittel` | Finansowanie projektu lub przychody projektu. |
| Wydatki projektu | `Ausgaben:Projekt:25-ZGV:Sachmittel` | Wydatki projektu. |

Rzeczywiste konto bankowe może być jednym kontem Sparkasse, ale księga rozdziela wewnętrzne salda projektów, aby zespół mógł zobaczyć, co należy do każdego projektu.

## Aktywne i zamknięte projekty

Aktywne projekty mają otwarte konta i odpowiednie salda. Zamknięte projekty zazwyczaj mają końcową weryfikację salda `0.00 EUR` i dyrektywy `close` dla kont aktywów projektu, przychodów i wydatków.

Nie wprowadzaj nowych transakcji do zamkniętych projektów, chyba że celowo ponownie otwierasz lub korygujesz dane historyczne.

## Aktualne przykłady w NICA

- `26-JEP-Buehnenreif`
- `25-ZGV`
- `25-CircusWiki`
- `25-Machen-UnitedAges`
- `25-Erasmus`
- zamknięte projekty z 2024 r., takie jak `24-AWO`, `24-HONY`, `24-Peter`

## Aktualne przykłady w Tohuwabohu

- `VHS-TOHU-25`
- `ZMS-TOHU-25`
- `CEDU-25`
- `TOHUCON-25`
- zamknięte projekty, takie jak `Revierpionier-25`, `OAC-25`, `TohuCon2024`, `ZGV-TOHU-24`, `TohuCon2023`

## Tworzenie nowego projektu

Nowy projekt zazwyczaj wymaga otwarcia kont przed wprowadzeniem transakcji.

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

Otwieraj tylko te kategorie, które są faktycznie przydatne dla projektu.

## Rejestrowanie finansowania projektu

```beancount
2026-02-01 ! "Funding Body" "First payment NewProject"
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject  3000.00 EUR
  Einnahmen:Projekt:26-NewProject:Sachmittel
```

## Rejestrowanie wydatków projektu

```beancount
2026-02-10 ! "Supplier" "Project material"
  Ausgaben:Projekt:26-NewProject:Sachmittel  250.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject
```

## Zrozumienie sald projektów

Dodatnie saldo aktywów projektu oznacza, że środki są nadal przypisane do tego projektu. Zerowe saldo aktywów projektu oznacza, że projekt nie ma pozostałego wewnętrznego salda bankowego. Ujemne saldo aktywów projektu zazwyczaj oznacza, że projekt wydał więcej niż przydzielone mu środki lub brakuje alokacji.

## Zamykanie projektu

Przed zamknięciem projektu należy wprowadzić wszystkie przychody i wydatki, upewnić się, że rachunki są dostępne, saldo konta aktywów projektu musi wynosić dokładnie zero, a wszelkie pozostałe środki muszą zostać prawidłowo przeniesione lub zwrócone.

```beancount
2026-12-31 balance Vermoegen:Bank:Sparkasse-NICA:26-NewProject 0.00 EUR
2026-12-31 close Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-12-31 close Ausgaben:Projekt:26-NewProject
2026-12-31 close Einnahmen:Projekt:26-NewProject
```

Zamknij również subkonta, jeśli zostały otwarte oddzielnie.
