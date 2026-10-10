---
lang: pl
translation_id: beancount/07-bank-csv-import-and-reconciliation
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Importowanie i uzgadnianie wyciągów bankowych CSV
description: Przepływ pracy do importowania danych CSV z Sparkasse i uzgadniania sald bankowych.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/07-bank-csv-import-and-reconciliation.md
translation_source_body_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_source_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:05:07+00:00
translation_source_localized_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_source_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:05:07+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 07 - Importowanie i uzgadnianie wyciągów bankowych CSV

Ten przepływ pracy wprowadza nowe transakcje z Sparkasse do Beancount i potwierdza, że księga nadal zgadza się z rzeczywistym kontem bankowym.

## Gdzie odbywają się importy

| Stowarzyszenie | Folder importu | Skrypt | Plik wyjściowy |
| --- | --- | --- | --- |
| NICA | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/test` | `csv2bean.py` | `beancount_file.beancount` |
| Tohuwabohu | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/test` | `csv2bean.py` | `beancount_file.beancount` |

## Przed eksportem z Sparkasse

1. Otwórz właściwy plik księgi.
2. Znajdź sekcję `Balance Checks` (Kontrola sald).
3. Znajdź najnowszą datę salda dla konta Sparkasse.
4. Sprawdź również sekcję `Bank Dump` (Zrzut bankowy) na dole pod kątem ostatniej zaimportowanej daty.
5. Użyj późniejszej z tych dat jako punktu wyjścia.

Zapobiega to pominięciu transakcji lub dwukrotnemu zaimportowaniu tego samego okresu.

## Eksport z Sparkasse

1. Otwórz przegląd konta.
2. Filtruj według zakresu dat.
3. Zacznij od ostatniej sprawdzonej lub zaimportowanej daty.
4. Zakończ dzisiejszą datą lub pożądaną datą uzgodnienia.
5. Eksportuj jako `Excel (CSV-CAMT V2)`.
6. Skopiuj pobrany plik CSV do właściwego folderu `test`.

Skrypty oczekują formatu Sparkasse CSV-CAMT-V2 z kolumnami rozdzielonymi średnikiem.

## Konwersja CSV

Otwórz terminal w odpowiednim folderze `test` i uruchom:

```powershell
python csv2bean.py "NAZWA-POBRANEGO-PLIKU.CSV"
```

Przykład:

```powershell
python csv2bean.py "20260312-1894137139-umsatz.CSV"
```

Jeśli się powiedzie, skrypt wyświetli `Process finished.` (Proces zakończony) i utworzy lub nadpisze plik `beancount_file.beancount`.

## Co robi konwerter

Konwerter tworzy podstawowe wpisy Beancount:

- Kwoty przychodzące domyślnie trafiają na konto aktywów Sparkasse i `Einnahmen:Sonstiges` (Przychody:Inne).
- Kwoty wychodzące domyślnie trafiają na `Ausgaben:Sonstiges` (Wydatki:Inne) i konto aktywów Sparkasse.
- Niektóre opisy przychodów są automatycznie klasyfikowane jako `Einnahmen:Vereinsbeitrag` (Przychody:Składki członkowskie).
- Niektóre teksty związane z Tohuwabohu mogą być klasyfikowane jako konto przychodów projektu.

Konwerter jest tylko pierwszym krokiem. Nie zna ostatecznego znaczenia księgowego każdej transakcji.

## Kopiowanie do głównej księgi

1. Otwórz `test/beancount_file.beancount`.
2. Zignoruj wygenerowany nagłówek opcji.
3. Skopiuj tylko transakcje.
4. Wklej je najpierw do głównej księgi pod sekcją `Bank Dump`.
5. Dodaj separator daty importu, jeśli jest potrzebny.

```beancount
****************************************************************************
** 2026-01-13
****************************************************************************
```

`Bank Dump` jest obszarem przejściowym. Zaimportowane transakcje można później przenieść do odpowiedniej sekcji tematycznej lub projektowej.

## Klasyfikowanie zaimportowanych wpisów

Dla każdej zaimportowanej transakcji zdecyduj:

- Czy dotyczy ona poziomu stowarzyszenia, czy projektu?
- Czy jest to przychód, czy wydatek?
- Czy jest to zwrot kosztów, czy spłata zobowiązania?
- Czy należy do `Freies-Geld` (Wolne pieniądze), czy na konto aktywów specyficzne dla projektu?
- Czy istnieje dowód wpłaty lub faktura do załączenia?

Zastąp ogólne konta zapasowe, takie jak `Ausgaben:Sonstiges`, gdy istnieje dokładniejsze konto.

## Dodawanie kontroli salda

Przykład NICA:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Przykład Tohuwabohu:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-Tohuwabohu 2345.67 EUR
```

Użyj salda pokazanego przez Sparkasse na tę dokładną datę.

## Walidacja w Fava

1. Zapisz plik księgi.
2. Odśwież Fava.
3. Sprawdź błędy na górze strony Fava.
4. Otwórz stronę konta Sparkasse.
5. Potwierdź bieżące saldo i najnowsze transakcje.
6. Sprawdź Bilans.
7. Sprawdź pulpity projektowe, jeśli dotyczyły konta projektowe.

## Jeśli kontrola salda się nie powiedzie

Częste przyczyny:

- Eksport CSV pominął jeden dzień na początku lub końcu.
- Transakcja została zaimportowana dwukrotnie.
- Transakcja została wklejona do niewłaściwej księgi stowarzyszenia.
- Numer został nieprawidłowo edytowany.
- Podział projektu użył niewłaściwego znaku.
- Ruchy PayPal lub gotówkowe nie zostały również zarejestrowane.

Nie usuwaj kontroli salda tylko po to, aby błąd zniknął. Napraw podstawową różnicę w transakcjach.
