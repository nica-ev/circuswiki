---
lang: pl
translation_id: beancount/01-system-overview
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Przegląd systemu
description: Wyjaśnia cel, komponenty i typowy przepływ pracy użytkownika systemu księgowego.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/01-system-overview.md
translation_source_body_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_source_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:32:17+00:00
translation_source_localized_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_source_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:32:17+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 01 - Przegląd systemu

## Cel

System księgowy rejestruje całą działalność finansową stowarzyszeń w sposób uporządkowany i możliwy do sprawdzenia. Został zaprojektowany tak, aby odpowiadać na typowe pytania księgowe:

- Ile pieniędzy jest aktualnie dostępnych?
- Które dochody i wydatki należą do samego stowarzyszenia?
- Które dochody i wydatki należą do konkretnego projektu?
- Czy salda Sparkasse, PayPal i gotówki są prawidłowe?
- Które dowody i dokumenty należą do których transakcji?
- Które projekty są aktywne, zakończone lub już zamknięte?

## Główne komponenty

| Komponent | Co robi |
| --- | --- |
| Beancount | Format danych księgowych. Transakcje są zapisywane w plikach tekstowych. |
| Fava | Interfejs przeglądarki do przeglądania i filtrowania danych Beancount. |
| Fava Dashboards | Niestandardowe strony pulpitów nawigacyjnych w Fava do przeglądu zarządczego i widoków projektów. |
| Obsidian | System notatek, z którego można otwierać księgowość za pomocą przycisków. |
| Skrypty importu CSV | Pomocnicze skrypty, które konwertują eksporty CSV z Sparkasse na wpisy Beancount. |

## Jak części pasują do siebie

1. Dane bankowe lub PayPal są eksportowane jako CSV.
2. Plik CSV jest konwertowany na tymczasowe wpisy Beancount.
3. Nowe wpisy są kopiowane do odpowiedniego pliku księgi.
4. Użytkownik sprawdza, klasyfikuje i koryguje wpisy.
5. Kontrole sald potwierdzają, że księga zgadza się z saldem bankowym lub PayPal.
6. Fava wyświetla raporty, strony kont, rachunki zysków i strat, bilanse oraz pulpity nawigacyjne.

## Dwa oddzielne stowarzyszenia

| Stowarzyszenie | Księga | Typowy prefiks konta |
| --- | --- | --- |
| NICA e.V. | `nica.beancount` | `Sparkasse-NICA`, `NICA` |
| Tohuwabohu Halle e.V. | `2023.beancount` | `Sparkasse-Tohuwabohu`, `Tohuwabohu` |

Istnieje również eksperymentalny połączony plik: `1. Vereinsverwaltung/Buchhaltung/all.beancount`. Normalna praca codzienna powinna odbywać się w indywidualnej księdze odpowiedniego stowarzyszenia.

## Podstawowy przepływ pracy

1. Otwórz odpowiednią instancję Fava.
2. Znajdź ostatnią zakończoną kontrolę salda.
3. Wyeksportuj nowe transakcje bankowe ze Sparkasse, zaczynając od ostatniej sprawdzonej daty.
4. Skonwertuj plik CSV do formatu Beancount.
5. Wklej wygenerowane wpisy najpierw do sekcji `Bank Dump`.
6. Przenieś lub sklasyfikuj wpisy do odpowiednich sekcji stowarzyszenia lub projektu.
7. Dodaj dowody, linki, komentarze lub tagi w razie potrzeby.
8. Dodaj nową kontrolę salda.
9. Odśwież Fava i zweryfikuj, czy nie ma błędów.

## Czego nowy użytkownik powinien nauczyć się najpierw

1. [Otwieranie Fava](02-opening-fava.md)
2. [Podstawy Beancount dla użytkowników](04-beancount-basics-for-users.md)
3. [Import CSV z banku i uzgodnienie](07-bank-csv-import-and-reconciliation.md)
4. [Konta i kategorie](05-accounts-and-categories.md)
5. [Projekty i fundusze celowe](08-projects-and-restricted-funds.md)
