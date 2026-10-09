---
lang: cs
translation_id: beancount/03-folder-and-file-map
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Mapa složek a souborů
description: Mapuje důležité účetní složky, účetní soubory, řídicí panely a pomocné soubory.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/03-folder-and-file-map.md
translation_source_body_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_source_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:35:32+00:00
translation_source_localized_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_source_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:35:32+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 03 - Mapa složek a souborů

Tato stránka vysvětluje, kde jsou uloženy důležité účetní soubory.

## Hlavní účetní složka

```text
1. Vereinsverwaltung/Buchhaltung
```

Tato složka obsahuje hlavní účetní knihy, soubory s přehledy, podpůrné dokumenty a pomocné složky.

## Důležité soubory na nejvyšší úrovni

| Soubor | Účel |
| --- | --- |
| `Buchhaltung Home.md` | Vstupní stránka v Obsidianu s tlačítky a stručnou poznámkou k pracovnímu postupu. |
| `all.beancount` | Experimentální kombinovaná účetní kniha zahrnující NICA i Tohuwabohu. |
| `dashboards.yaml` | Definice dashboardů pro Fava na sdílené úrovni. |

## Struktura NICA

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA
```

| Cesta | Účel |
| --- | --- |
| `2023/nica.beancount` | Hlavní účetní kniha NICA. Toto je soubor, který se obvykle upravuje. |
| `2023/dashboards.yaml` | Konfigurace dashboardů pro účetní knihu NICA. |
| `2023/Buchhaltung NICA eV.md` | Pomocná poznámka v Obsidianu pro otevření účetnictví NICA. |
| `2023/CSV/` | Uložené exporty CSV. |
| `test/csv2bean.py` | Převádí CSV ze Sparkasse na dočasné záznamy Beancount. |
| `test/beancount_file.beancount` | Vygenerovaný výstup z převodu CSV. |
| `test/paypal2bean.py` | Pomocník pro importy CSV z PayPal. |
| `test/output_file_paypal.beancount` | Vygenerovaný výstupní soubor PayPal. |
| `test/old files/` | Starší CSV a vygenerované soubory. |

## Struktura Tohuwabohu

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu
```

| Cesta | Účel |
| --- | --- |
| `2023/2023.beancount` | Hlavní účetní kniha Tohuwabohu. Toto je soubor, který se obvykle upravuje. |
| `2021/2021.beancount` | Starší data účetní knihy zahrnutá prostřednictvím `all.beancount`. |
| `all.beancount` | Kombinovaný soubor Tohuwabohu zahrnující účetní knihy z let 2021 a 2023. |
| `2023/dashboards.yaml` | Konfigurace dashboardů pro účetní knihu Tohuwabohu. |
| `2023/Buchhaltung Tohuwabohu Halle eV.md` | Pomocná poznámka v Obsidianu. |
| `2023/Belege Ausgaben/` | Účtenky a podpůrné dokumenty k výdajům. |
| `2023/Belege Ausgaben/Eingetragen/` | Účtenky již zapsané v účetní knize. |
| `test/csv2bean.py` | Převádí CSV ze Sparkasse na dočasné záznamy Beancount. |
| `test/beancount_file.beancount` | Vygenerovaný výstup z převodu CSV. |
| `test/paypal2bean.py` | Pomocník pro importy CSV z PayPal. |
| `test/output_file_paypal.beancount` | Vygenerovaný výstupní soubor PayPal. |
| `test/CSV - old files/` | Starší CSV a vygenerované soubory. |

## Princip pojmenování souborů

Složky stále obsahují historické názvy, jako je `2023`, i když obsahují i pozdější aktivitu z let 2024, 2025 a 2026. S hlavními referencovanými účetními knihami zacházejte jako s aktivními, pokud není struktura záměrně změněna.

## Kde upravovat

| Spolek | Upravit tento soubor |
| --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` |

Neupravujte vygenerované výstupní soubory jako trvalý záznam. Jsou to dočasné pracovní soubory.
