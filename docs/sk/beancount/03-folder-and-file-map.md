---
lang: sk
translation_id: beancount/03-folder-and-file-map
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Mapa priečinkov a súborov
description: Mapuje dôležité účtovné priečinky, súbory denníkov, dashboardy a pomocné súbory.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/03-folder-and-file-map.md
translation_source_body_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_source_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:26+00:00
translation_source_localized_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_source_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:26+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 03 - Rozloženie priečinkov a súborov

Táto stránka vysvetľuje, kde sú uložené dôležité účtovné súbory.

## Hlavný účtovný priečinok

```text
1. Vereinsverwaltung/Buchhaltung
```

Tento priečinok obsahuje hlavné knihy, súbory s prehľadmi, podporné dokumenty a pomocné priečinky.

## Dôležité súbory na najvyššej úrovni

| Súbor | Účel |
| --- | --- |
| `Buchhaltung Home.md` | Vstupná stránka v Obsidiane s tlačidlami a krátkou poznámkou k pracovnému postupu. |
| `all.beancount` | Experimentálna kombinovaná hlavná kniha vrátane NICA aj Tohuwabohu. |
| `dashboards.yaml` | Definícia prehľadov pre Fava dashboards na zdieľanej úrovni. |

## Štruktúra NICA

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA
```

| Cesta | Účel |
| --- | --- |
| `2023/nica.beancount` | Hlavná hlavná kniha NICA. Toto je súbor, ktorý sa bežne upravuje. |
| `2023/dashboards.yaml` | Konfigurácia prehľadov pre hlavnú knihu NICA. |
| `2023/Buchhaltung NICA eV.md` | Pomocná poznámka v Obsidiane na otvorenie účtovníctva NICA. |
| `2023/CSV/` | Uložené exporty CSV. |
| `test/csv2bean.py` | Konvertuje CSV zo Sparkasse na dočasné záznamy Beancount. |
| `test/beancount_file.beancount` | Vygenerovaný výstup z konverzie CSV. |
| `test/paypal2bean.py` | Pomocník pre importy CSV z PayPalu. |
| `test/output_file_paypal.beancount` | Vygenerovaný výstupný súbor z PayPalu. |
| `test/old files/` | Staršie CSV a vygenerované súbory. |

## Štruktúra Tohuwabohu

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu
```

| Cesta | Účel |
| --- | --- |
| `2023/2023.beancount` | Hlavná hlavná kniha Tohuwabohu. Toto je súbor, ktorý sa bežne upravuje. |
| `2021/2021.beancount` | Staršie údaje hlavnej knihy zahrnuté cez `all.beancount`. |
| `all.beancount` | Kombinovaný súbor Tohuwabohu vrátane súborov hlavných kníh z rokov 2021 a 2023. |
| `2023/dashboards.yaml` | Konfigurácia prehľadov pre hlavnú knihu Tohuwabohu. |
| `2023/Buchhaltung Tohuwabohu Halle eV.md` | Pomocná poznámka v Obsidiane. |
| `2023/Belege Ausgaben/` | Potvrdenia a podporné dokumenty k výdavkom. |
| `2023/Belege Ausgaben/Eingetragen/` | Potvrdenia už zadané do hlavnej knihy. |
| `test/csv2bean.py` | Konvertuje CSV zo Sparkasse na dočasné záznamy Beancount. |
| `test/beancount_file.beancount` | Vygenerovaný výstup z konverzie CSV. |
| `test/paypal2bean.py` | Pomocník pre importy CSV z PayPalu. |
| `test/output_file_paypal.beancount` | Vygenerovaný výstupný súbor z PayPalu. |
| `test/CSV - old files/` | Staršie CSV a vygenerované súbory. |

## Princíp pomenovania súborov

Priečinky stále obsahujú historické názvy, ako napríklad `2023`, aj keď obsahujú aj neskoršiu aktivitu z rokov 2024, 2025 a 2026. Hlavné referencované súbory hlavných kníh považujte za aktívne hlavné knihy, pokiaľ sa štruktúra zámerne nezmení.

## Kde upravovať

| Združenie | Upravte tento súbor |
| --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` |

Neupravujte vygenerované výstupné súbory ako trvalý záznam. Sú to dočasné súbory na spracovanie.
