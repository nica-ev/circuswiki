---
lang: pl
translation_id: beancount/03-folder-and-file-map
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Mapa folderów i plików
description: Mapuje ważne foldery księgowe, pliki ksiąg, pulpity nawigacyjne i pliki pomocnicze.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/03-folder-and-file-map.md
translation_source_body_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_source_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:34:46+00:00
translation_source_localized_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_source_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:34:46+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 03 - Mapa folderów i plików

Ta strona wyjaśnia, gdzie przechowywane są ważne pliki księgowe.

## Główny folder księgowy

```text
1. Vereinsverwaltung/Buchhaltung
```

Ten folder zawiera księgi rachunkowe, pliki pulpitu nawigacyjnego, dokumenty źródłowe i foldery pomocnicze.

## Ważne pliki najwyższego poziomu

| Plik | Cel |
| --- | --- |
| `Buchhaltung Home.md` | Strona wejściowa Obsidian z przyciskami i krótką notatką o przepływie pracy. |
| `all.beancount` | Eksperymentalna połączona księga zawierająca zarówno NICA, jak i Tohuwabohu. |
| `dashboards.yaml` | Definicja pulpitu nawigacyjnego dla pulpitów Fava na poziomie współdzielonym. |

## Struktura NICA

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA
```

| Ścieżka | Cel |
| --- | --- |
| `2023/nica.beancount` | Główna księga NICA. Jest to plik, który jest normalnie edytowany. |
| `2023/dashboards.yaml` | Konfiguracja pulpitu nawigacyjnego dla księgi NICA. |
| `2023/Buchhaltung NICA eV.md` | Notatka pomocnicza Obsidian do otwierania księgowości NICA. |
| `2023/CSV/` | Przechowywane eksporty CSV. |
| `test/csv2bean.py` | Konwertuje CSV z Sparkasse na tymczasowe wpisy Beancount. |
| `test/beancount_file.beancount` | Wygenerowany wynik konwersji CSV. |
| `test/paypal2bean.py` | Pomocnik do importu CSV z PayPal. |
| `test/output_file_paypal.beancount` | Wygenerowany plik wyjściowy PayPal. |
| `test/old files/` | Starsze pliki CSV i wygenerowane pliki. |

## Struktura Tohuwabohu

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu
```

| Ścieżka | Cel |
| --- | --- |
| `2023/2023.beancount` | Główna księga Tohuwabohu. Jest to plik, który jest normalnie edytowany. |
| `2021/2021.beancount` | Starsze dane księgowe uwzględnione w `all.beancount`. |
| `all.beancount` | Połączony plik Tohuwabohu zawierający pliki księgowe z lat 2021 i 2023. |
| `2023/dashboards.yaml` | Konfiguracja pulpitu nawigacyjnego dla księgi Tohuwabohu. |
| `2023/Buchhaltung Tohuwabohu Halle eV.md` | Notatka pomocnicza Obsidian. |
| `2023/Belege Ausgaben/` | Potwierdzenia i dokumenty źródłowe wydatków. |
| `2023/Belege Ausgaben/Eingetragen/` | Potwierdzenia już wprowadzone do księgi. |
| `test/csv2bean.py` | Konwertuje CSV z Sparkasse na tymczasowe wpisy Beancount. |
| `test/beancount_file.beancount` | Wygenerowany wynik konwersji CSV. |
| `test/paypal2bean.py` | Pomocnik do importu CSV z PayPal. |
| `test/output_file_paypal.beancount` | Wygenerowany plik wyjściowy PayPal. |
| `test/CSV - old files/` | Starsze pliki CSV i wygenerowane pliki. |

## Zasada nazewnictwa plików

Foldery nadal zawierają historyczne nazwy, takie jak `2023`, nawet jeśli zawierają również późniejsze działania z lat 2024, 2025 i 2026. Traktuj aktualnie odwoływane główne pliki księgowe jako aktywne księgi, chyba że struktura zostanie celowo zmieniona.

## Gdzie edytować

| Stowarzyszenie | Edytuj ten plik |
| --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` |

Nie edytuj wygenerowanych plików wyjściowych jako trwałych zapisów. Są to tymczasowe pliki przejściowe.
