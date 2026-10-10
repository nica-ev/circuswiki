---
lang: pl
translation_id: beancount/12-troubleshooting
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Rozwiązywanie problemów
description: Typowe problemy z Fava i Beancount oraz sposoby ich rozwiązania.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/12-troubleshooting.md
translation_source_body_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_source_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:21+00:00
translation_source_localized_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_source_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:21+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 12 - Rozwiązywanie problemów

## Fava się nie otwiera

Sprawdź:

- Czy okno terminala jest nadal otwarte?
- Czy Fava została uruchomiona w odpowiednim folderze?
- Czy używany jest właściwy port?
- Czy na tym samym porcie nie działa już inna instancja Favy?
- Czy Fava jest zainstalowana i dostępna w terminalu?

Polecenia:

```powershell
fava nica.beancount --port 4998
fava 2023.beancount --port 4999
```

Uruchom każde polecenie tylko z odpowiedniego folderu księgi.

## Fava wyświetla błąd Beancount

Typowe przyczyny:

- Literówka w nazwie konta.
- Brak dyrektywy `open` dla konta.
- Kwota używa przecinka zamiast kropki.
- Brak cudzysłowów wokół odbiorcy lub opisu.
- Transakcja nie jest zbilansowana.
- Sprawdzenie salda nie zgadza się.
- Transakcja używa konta po jego zamknięciu.

Popraw plik tekstowy, zapisz go, a następnie przeładuj Favę.

## Sprawdzenie salda nie powiodło się

Nie usuwaj sprawdzenia salda jako obejścia problemu. Zbadaj różnicę.

Lista kontrolna:

- Czy zakres dat pliku CSV był kompletny?
- Czy ten sam plik CSV został zaimportowany dwukrotnie?
- Czy niektóre transakcje zostały wklejone do niewłaściwej księgi?
- Czy transakcja została przypisana do niewłaściwego subkonta Sparkasse?
- Czy znak kwoty został nieprawidłowo zmieniony?
- Czy przelew PayPal lub gotówkowy został wprowadzony tylko po jednej stronie?
- Czy istnieją starsze ręczne edycje po poprzednim sprawdzeniu salda?

## Konwersja CSV nie powiodła się

Sprawdź:

- Czy plik CSV znajduje się w tym samym folderze `test` co `csv2bean.py`.
- Czy nazwa pliku w poleceniu jest dokładna.
- Czy plik jest eksportem Sparkasse `Excel (CSV-CAMT V2)`.
- Czy plik jest rozdzielony średnikami.
- Czy plik CSV nie został otwarty i ponownie zapisany w sposób, który zmienił jego format.

## Zaimportowane wpisy wyglądają zbyt ogólnie

Jest to oczekiwane. Konwerter używa kategorii zastępczych, takich jak:

- `Ausgaben:Sonstiges`
- `Einnahmen:Sonstiges`

Użytkownik musi ręcznie przejrzeć i sklasyfikować zaimportowane wpisy.

## Pulpit nawigacyjny jest niedostępny

Sprawdź:

- Czy zainstalowano `fava-dashboards`.
- Czy księga zawiera dyrektywę `custom "fava-extension" "fava_dashboards"`.
- Czy plik `dashboards.yaml` znajduje się obok księgi.
- Czy Fava została zrestartowana po instalacji lub zmianach konfiguracji.

## Projekt nie pojawia się na pulpitach nawigacyjnych

Sprawdź:

- Czy projekt ma konto aktywów projektowych pod oczekiwanym prefiksem Sparkasse lub PayPal.
- Czy konto projektu nie jest zamknięte.
- Czy saldo projektu nie jest dokładnie zerowe.
- Czy nazwa konta pasuje do wzorca zapytania pulpitu nawigacyjnego.

## Link do dokumentu nie działa

Sprawdź:

- Czy ścieżka pliku jest względna do folderu pliku księgi.
- Czy nazwa pliku jest dokładnie przeliterowana.
- Czy dokument nie został przeniesiony po utworzeniu linku.
- Czy ścieżka używa ukośników lub standardowego stylu ścieżki względnej.

## Niepewność co do klasyfikacji transakcji

Użyj tej kolejności:

1. Wyszukaj podobne starsze transakcje w Favie.
2. Sprawdź kontekst projektu lub faktury.
3. Sprawdź, czy należy do linii budżetowej fundatora.
4. Dodaj komentarz, jeśli nie jesteś pewien.
5. Tymczasowo używaj `Sonstiges` tylko wtedy, gdy nie znasz lepszej kategorii.
6. Zapytaj odpowiedzialną osobę ds. projektu lub finansów przed finalizacją.
