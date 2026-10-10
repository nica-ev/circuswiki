---
lang: pl
translation_id: beancount/10-fava-dashboards-and-reports
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Panele i raporty Fava
description: Przegląd raportów Fava i niestandardowych paneli używanych do przeglądu księgowości.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/10-fava-dashboards-and-reports.md
translation_source_body_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_source_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:06+00:00
translation_source_localized_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_source_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:06+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 10 – Pulpity i raporty Favy

Fava udostępnia standardowe raporty księgowe. System wykorzystuje również `fava-dashboards` do tworzenia niestandardowych stron przeglądowych.

## Standardowe widoki Favy

| Widok | Zastosowanie |
| --- | --- |
| Bilans | Sprawdzanie aktywów, pasywów, wolnych środków, salda PayPal, gotówki i projektów. |
| Rachunek zysków i strat | Podgląd przychodów i wydatków w czasie. |
| Strona konta | Inspekcja wszystkich transakcji dla danego konta. |
| Dziennik | Wyszukiwanie chronologicznej historii transakcji. |
| Zapytanie | Uruchamianie niestandardowych zapytań Beancount w razie potrzeby. |
| Dokumenty | Znajdowanie powiązanych potwierdzeń i plików. |

## Rozszerzenie pulpitu nawigacyjnego

Dzienniki zawierają następującą dyrektywę:

```beancount
2010-01-01 custom "fava-extension" "fava_dashboards"
```

Aktywuje to rozszerzenie pulpitu nawigacyjnego, jeśli zainstalowano `fava-dashboards`.

## Pliki konfiguracyjne pulpitu nawigacyjnego

Pliki pulpitu nawigacyjnego nazywają się `dashboards.yaml`. Przechowywane są w pobliżu plików dziennika oraz na współdzielonym poziomie księgowości.

## Główne sekcje pulpitu nawigacyjnego

| Pulpit nawigacyjny | Cel |
| --- | --- |
| `Vorstand-Cockpit` | Przegląd zarządczy: wolne środki, całkowite saldo Sparkasse, PayPal, gotówka, trend płynności, miesięczny wynik, aktywne salda projektów. |
| `Details & Daten` | Szczegółowe wykresy: wydatki według kategorii, przychody według kategorii, przepływ pieniędzy, sieć projektów/osób. |

## Ważne wskaźniki na pulpicie nawigacyjnym

### Wolne środki (Freies Geld)

Pokazuje środki dostępne poza środkami przeznaczonymi na ograniczone cele projektowe. Typowe konta to `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld` i `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`.

### Całkowite saldo Sparkasse (Sparkasse Gesamt)

Pokazuje całkowite saldo Sparkasse na głównym koncie bankowym i wewnętrznych subkontach.

### PayPal

Pokazuje saldo PayPal. Ujemne saldo PayPal wskazuje, że coś należy sprawdzić.

### Kasa (Barkasse)

Pokazuje saldo kasy fiskalnej.

### Saldo Aktywnych Projektów (Saldo Aktiver Projekte)

Pokazuje niezerowe salda projektów. Jest to przydatne do sprawdzenia, które projekty nadal posiadają środki lub są przekroczone.

### Miesięczny Nadwyżka / Deficyt (Monatlicher Ueberschuss / Fehlbetrag)

Pokazuje miesięczną nadwyżkę lub deficyt operacyjny, z wyłączeniem kont projektowych w zapytaniu pulpitu nawigacyjnego.

## Jak odpowiedzialnie korzystać z pulpitów nawigacyjnych

Pulpity nawigacyjne to podsumowania. Jeśli jakaś liczba wygląda zaskakująco:

1. Kliknij powiązane konto lub raport Favy.
2. Sprawdź leżące u podstaw transakcje.
3. Sprawdź, czy transakcja nadal znajduje się w sekcji `Sonstiges` (Inne) lub `Bank Dump` (Zrzut bankowy).
4. Sprawdź, czy nazwa konta pasuje do wzorca zapytania pulpitu nawigacyjnego.
5. Potwierdź kontrole salda przed zaufaniem liczbom zarządczym.

## Kiedy liczby na pulpicie nawigacyjnym wyglądają nieprawidłowo

Częste przyczyny:

- Transakcja została zaksięgowana na głównym koncie bankowym zamiast na subkoncie projektu.
- Konto projektu zostało zamknięte, ale nadal ma niezerowe saldo.
- Nowy projekt używa wzorca nazewnictwa, który nie jest uwzględniony w zapytaniu pulpitu nawigacyjnego.
- Transakcja nadal znajduje się w szerokiej kategorii zapasowej.
- Plik pulpitu nawigacyjnego należy do innego dziennika niż ten aktualnie otwarty.
