---
lang: pl
translation_id: beancount/00-bookkeeping-home
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Dokumentacja systemu księgowego
description: Przegląd i punkt wyjścia do dokumentacji księgowej Beancount dla NICA e.V. i Tohuwabohu Halle e.V.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/00-bookkeeping-home.md
translation_source_body_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_source_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:31:06+00:00
translation_source_localized_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_source_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:31:06+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# Dokumentacja systemu księgowego

Niniejsza dokumentacja wyjaśnia, jak działa system księgowy dla NICA e.V. i Tohuwabohu Halle e.V. z perspektywy zwykłego użytkownika.

System wykorzystuje pliki księgowe w formacie tekstowym Beancount oraz interfejs przeglądarkowy o nazwie Fava. Nie musisz rozumieć programowania, aby z niego korzystać, ale musisz dokładnie przestrzegać przepływu pracy księgowej: importować dane bankowe, klasyfikować transakcje, dołączać potwierdzenia tam, gdzie jest to potrzebne, i sprawdzać salda.

## Zacznij tutaj

- [01 - Przegląd systemu](01-system-overview.md)
- [02 - Uruchamianie Favvy](02-opening-fava.md)
- [03 - Mapa folderów i plików](03-folder-and-file-map.md)
- [04 - Podstawy Beancount dla użytkowników](04-beancount-basics-for-users.md)
- [05 - Konta i kategorie](05-accounts-and-categories.md)
- [06 - Wprowadzanie i edycja transakcji](06-entering-and-editing-transactions.md)
- [07 - Import CSV z banku i uzgadnianie](07-bank-csv-import-and-reconciliation.md)
- [08 - Projekty i fundusze celowe](08-projects-and-restricted-funds.md)
- [09 - Potwierdzenia i dokumenty](09-receipts-and-documents.md)
- [10 - Pulpity nawigacyjne i raporty Favvy](10-fava-dashboards-and-reports.md)
- [11 - Regularna rutyna księgowa](11-regular-bookkeeping-routine.md)
- [12 - Rozwiązywanie problemów](12-troubleshooting.md)
- [13 - Słownik pojęć](13-glossary.md)

## Najważniejsza zasada

Plik księgowy jest źródłem prawdy. Fava wyświetla tylko to, co jest zapisane w plikach `.beancount`. Jeśli coś wygląda nieprawidłowo w Favvie, popraw wpis w Beancount i przeładuj Favvę.

## Aktualne księgi

| Organizacja | Główny plik | Adres Favvy | Port |
| --- | --- | --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` | `http://127.0.0.1:4998/` | `4998` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` | `http://127.0.0.1:4999/` | `4999` |

## Czym ta dokumentacja nie jest

Nie jest to porada prawna ani podatkowa. Opisuje ona, jak zorganizowany jest ten konkretny lokalny system księgowy i jak użytkownicy powinni go konsekwentnie używać.
