---
lang: cs
translation_id: beancount/02-opening-fava
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Otevření Favy
description: Jak spustit a otevřít lokální rozhraní pro účetnictví Fava.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/02-opening-fava.md
translation_source_body_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_source_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:34:21+00:00
translation_source_localized_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_source_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:34:21+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 02 - Spuštění Favy

Fava je webové rozhraní používané k prohlížení účetnictví. Běží lokálně na počítači a otevírá se v prohlížeči nebo v prohlížeči Obsidianu.

## Požadavky

Na počítači musí být nainstalovány a dostupné tyto programy:

- Python
- Beancount
- Fava
- `fava-dashboards`, pokud má být rozšíření pro dashboardy viditelné
- Obsidian, pokud používáte tlačítka v Obsidianu

## Otevření z Obsidianu

Poznámka `1. Vereinsverwaltung/Buchhaltung/Buchhaltung Home.md` obsahuje tlačítka pro otevření účetnictví. Tlačítka spouštějí Favu prostřednictvím Obsidian Shell Commands a následně otevírají lokální URL Favy.

| Tlačítko | Otevírá |
| --- | --- |
| `NICA e.V. Buchhaltung` | NICA Fava na portu `4998` |
| `Tohuwabohu Halle Buchhaltung` | Tohuwabohu Fava na portu `4999` |

Nezavírejte okno terminálu, které spouští Favu. Pokud terminál zavřete, Fava se ukončí.

## Manuální otevření

### NICA e.V.

Otevřete terminál v adresáři:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023
```

Spusťte:

```powershell
fava nica.beancount --port 4998
```

Poté otevřete `http://127.0.0.1:4998/`.

### Tohuwabohu Halle e.V.

Otevřete terminál v adresáři:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023
```

Spusťte:

```powershell
fava 2023.beancount --port 4999
```

Poté otevřete `http://127.0.0.1:4999/`.

## Spouštěcí dávkové soubory

| Soubor | Účel |
| --- | --- |
| `startup-nica.bat` | Spustí NICA Fava na portu `4998`. |
| `startup-tohu.bat` | Spustí Tohuwabohu Fava na portu `4999`. |
| `startup-all.bat` | Spustí Obsidian, několik nástrojů a obě instance Favy. |

## Důležité URL adresy

| Zobrazení | NICA | Tohuwabohu |
| --- | --- | --- |
| Domů | `http://127.0.0.1:4998/` | `http://127.0.0.1:4999/` |
| Dashboardy | `http://127.0.0.1:4998/nica-ev/extension/FavaDashboards/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/extension/FavaDashboards/` |
| Výkaz zisku a ztráty | `http://127.0.0.1:4998/nica-ev/income_statement/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/income_statement/` |

## Když Fava již běží

Pokud Fava již běží, stačí otevřít URL. Pokud je port již obsazen a Fava se odmítá spustit, je možné, že je již otevřena jiná instance Favy. Použijte stávající stránku prohlížeče nebo zavřete staré okno terminálu a zkuste to znovu.
