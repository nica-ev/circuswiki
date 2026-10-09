---
lang: pl
translation_id: beancount/06-entering-and-editing-transactions
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Wprowadzanie i edycja transakcji
description: Opisuje, jak użytkownicy przeglądają, klasyfikują, korygują i wprowadzają transakcje księgowe.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/06-entering-and-editing-transactions.md
translation_source_body_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_source_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:38:03+00:00
translation_source_localized_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_source_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:38:03+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 06 - Wprowadzanie i edycja transakcji

Większość wpisów pochodzi z importowanych danych bankowych, ale użytkownicy nadal muszą przeglądać, klasyfikować, korygować, a czasem ręcznie wprowadzać transakcje.

## Status transakcji

W księgach często używa się znaku `!` w importowanych transakcjach:

```beancount
2026-03-12 ! "Wystawca" "Tekst bankowy"
```

Używaj tego jako domyślnego znacznika, chyba że zespół zdecyduje się na bardziej rygorystyczną konwencję statusów.

## Podstawowe wprowadzenie dochodu

```beancount
2026-01-15 ! "Max Mustermann" "Składka członkowska 2026"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  60.00 EUR
  Einnahmen:Vereinsbeitrag
```

## Podstawowe wprowadzenie wydatku

```beancount
2026-01-20 ! "Nazwa dostawcy" "Faktura 123"
  Ausgaben:Buero:Sonstiges  25.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Dochód z projektu

```beancount
2026-02-10 ! "Organ finansujący" "Płatność grantowa projekt 25-ZGV"
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV  5000.00 EUR
  Einnahmen:Projekt:25-ZGV:Sachmittel
```

## Wydatek projektowy

```beancount
2026-02-15 ! "Imię i nazwisko" "Wynagrodzenie projekt 25-ZGV"
  Ausgaben:Projekt:25-ZGV:Honorar  450.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV
```

## Wewnętrzny przepływ środków między projektem a funduszami wolnymi

Czasami transakcja musi alokować środki bankowe między konto aktywów specyficzne dla projektu a fundusze wolne. Rzeczywiste konto bankowe to jedno fizyczne konto Sparkasse, ale księga śledzi salda projektów wewnętrznie oddzielnie.

```beancount
2026-02-20 ! "Alokacja wewnętrzna" "Przeniesienie pozostałych środków projektu na wolne środki"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  100.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV      -100.00 EUR
```

Dokonuj przelewów wewnętrznych tylko wtedy, gdy rozumiesz, dlaczego saldo projektu wewnętrznego musi ulec zmianie.

## Zwroty kosztów dla osób

Jeśli ktoś zapłacił z własnych środków i otrzymał później zwrot, czysty schemat zazwyczaj polega na zarejestrowaniu wydatku jako zobowiązania, a następnie rozliczeniu tego zobowiązania płatnością z banku.

```beancount
2026-03-01 ! "Sklep" "Materiał kupiony przez Marca"
  Ausgaben:Projekt:25-ZGV:Sachmittel  35.00 EUR
  Verbindlichkeiten:Person:Marc-Bielert
```

```beancount
2026-03-05 ! "Marc Bielert" "Zwrot kosztów materiału"
  Verbindlichkeiten:Person:Marc-Bielert  35.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Komentarze dotyczące niejasnych decyzji

```beancount
; Niejasne, czy to należy do CEDU-25, czy do funduszy wolnego stowarzyszenia. Sprawdzić fakturę.
2026-03-10 ! "Sprzedawca" "Faktura 456"
  Ausgaben:Sonstiges  120.00 EUR
  Vermoegen:Bank:Sparkasse-Tohuwabohu
```

## Bezpieczna edycja

Przed edycją sprawdź:

- Jesteś w odpowiedniej księdze stowarzyszenia.
- Nie edytujesz wygenerowanego wyniku importu tak, jakby to była ostateczna księga.
- Data transakcji jest poprawna.
- Kwota używa kropki jako separatora dziesiętnego, na przykład `12.50 EUR`.
- Nazwy kont są napisane dokładnie tak samo jak istniejące konta.
- Transakcje projektowe konsekwentnie używają projektowego konta aktywów i kategorii dochodów/wydatków projektowych.

Po edycji zapisz plik, przeładuj Fava, sprawdź błędy i przejrzyj odpowiednią stronę konta.
