---
lang: pl
translation_id: beancount/02-opening-fava
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Otwarcie Favvy
description: Jak uruchomić i otworzyć lokalny interfejs księgowy Favvy.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/02-opening-fava.md
translation_source_body_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_source_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:33:17+00:00
translation_source_localized_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_source_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:33:17+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 02 - Uruchamianie Favvy

Favva to interfejs internetowy służący do przeglądania księgowości. Działa lokalnie na komputerze i otwiera się w przeglądarce lub widoku internetowym Obsidian.

## Wymagania

Na komputerze muszą być zainstalowane i dostępne następujące programy:

- Python
- Beancount
- Favva
- `fava-dashboards`, jeśli rozszerzenie pulpitów nawigacyjnych ma być widoczne
- Obsidian, jeśli używane są przyciski Obsidian

## Uruchamianie z poziomu Obsidian

Notatka `1. Vereinsverwaltung/Buchhaltung/Buchhaltung Home.md` zawiera przyciski do otwierania księgowości. Przyciski te uruchamiają Favvę za pomocą Obsidian Shell Commands, a następnie otwierają lokalny adres URL Favvy.

| Przycisk | Otwiera |
| --- | --- |
| `NICA e.V. Buchhaltung` | NICA Favva na porcie `4998` |
| `Tohuwabohu Halle Buchhaltung` | Tohuwabohu Favva na porcie `4999` |

Nie zamykaj okna terminala, które uruchamia Favvę. Zamknięcie terminala spowoduje zatrzymanie Favvy.

## Uruchamianie ręczne

### NICA e.V.

Otwórz terminal w katalogu:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023
```

Uruchom polecenie:

```powershell
fava nica.beancount --port 4998
```

Następnie otwórz adres `http://127.0.0.1:4998/`.

### Tohuwabohu Halle e.V.

Otwórz terminal w katalogu:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023
```

Uruchom polecenie:

```powershell
fava 2023.beancount --port 4999
```

Następnie otwórz adres `http://127.0.0.1:4999/`.

## Skrypty wsadowe uruchamiające

| Plik | Cel |
| --- | --- |
| `startup-nica.bat` | Uruchamia NICA Favva na porcie `4998`. |
| `startup-tohu.bat` | Uruchamia Tohuwabohu Favva na porcie `4999`. |
| `startup-all.bat` | Uruchamia Obsidian, kilka narzędzi i obie instancje Favvy. |

## Ważne adresy URL

| Widok | NICA | Tohuwabohu |
| --- | --- | --- |
| Strona główna | `http://127.0.0.1:4998/` | `http://127.0.0.1:4999/` |
| Pulpity nawigacyjne | `http://127.0.0.1:4998/nica-ev/extension/FavaDashboards/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/extension/FavaDashboards/` |
| Rachunek zysków i strat | `http://127.0.0.1:4998/nica-ev/income_statement/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/income_statement/` |

## Gdy Favva jest już uruchomiona

Jeśli Favva jest już uruchomiona, wystarczy otworzyć adres URL. Jeśli port jest już zajęty i Favva nie chce się uruchomić, możliwe, że inna instancja Favvy jest już otwarta. Skorzystaj z istniejącej strony w przeglądarce lub zamknij stare okno terminala i uruchom ponownie.
