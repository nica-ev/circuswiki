---
lang: hu
translation_id: beancount/03-folder-and-file-map
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Mappa és fájltérkép
description: A fontos könyvelési mappákat, főkönyvi fájlokat, irányítópultokat és segédletfájlokat térképezi fel.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/03-folder-and-file-map.md
translation_source_body_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_source_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:34:52+00:00
translation_source_localized_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_source_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:34:52+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 03 - Mappa mappák és fájlok

Ez az oldal magyarázza el, hol tároljuk a fontos könyvelési fájlokat.

## Fő könyvelési mappa

```text
1. Vereinsverwaltung/Buchhaltung
```

Ez a mappa tartalmazza a főkönyveket, irányítópult-fájlokat, alátámasztó dokumentumokat és segédmappákat.

## Fontos legfelső szintű fájlok

| Fájl | Cél |
| --- | --- |
| `Buchhaltung Home.md` | Obsidian belépő oldal gombokkal és egy rövid munkafolyamat-jegyzet. |
| `all.beancount` | Kísérleti, egyesített főkönyv, amely tartalmazza mind a NICA, mind a Tohuwabohu adatait. |
| `dashboards.yaml` | Irányítópult-definíció a Fava irányítópultjaihoz a megosztott szinten. |

## NICA struktúra

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA
```

| Útvonal | Cél |
| --- | --- |
| `2023/nica.beancount` | Fő NICA főkönyv. Ez a fájl a szokásosan szerkesztett. |
| `2023/dashboards.yaml` | Irányítópult-konfiguráció a NICA főkönyvhöz. |
| `2023/Buchhaltung NICA eV.md` | Obsidian segédjegyzet a NICA könyvelés megnyitásához. |
| `2023/CSV/` | Tárolt CSV exportok. |
| `test/csv2bean.py` | Sparkasse CSV fájlokat ideiglenes Beancount bejegyzésekké alakít át. |
| `test/beancount_file.beancount` | A CSV konverzióból származó generált kimenet. |
| `test/paypal2bean.py` | Segédprogram a PayPal CSV importálásához. |
| `test/output_file_paypal.beancount` | Generált PayPal kimeneti fájl. |
| `test/old files/` | Régebbi CSV-k és generált fájlok. |

## Tohuwabohu struktúra

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu
```

| Útvonal | Cél |
| --- | --- |
| `2023/2023.beancount` | Fő Tohuwabohu főkönyv. Ez a fájl a szokásosan szerkesztett. |
| `2021/2021.beancount` | Régebbi főkönyvi adatok, amelyek az `all.beancount` fájlon keresztül vannak bevonva. |
| `all.beancount` | Tohuwabohu egyesített fájl, amely tartalmazza a 2021-es és 2023-as főkönyvi fájlokat. |
| `2023/dashboards.yaml` | Irányítópult-konfiguráció a Tohuwabohu főkönyvhöz. |
| `2023/Buchhaltung Tohuwabohu Halle eV.md` | Obsidian segédjegyzet. |
| `2023/Belege Ausgaben/` | Nyugták és alátámasztó dokumentumok a kiadásokhoz. |
| `2023/Belege Ausgaben/Eingetragen/` | A főkönyvbe már bejegyzett nyugták. |
| `test/csv2bean.py` | Sparkasse CSV fájlokat ideiglenes Beancount bejegyzésekké alakít át. |
| `test/beancount_file.beancount` | A CSV konverzióból származó generált kimenet. |
| `test/paypal2bean.py` | Segédprogram a PayPal CSV importálásához. |
| `test/output_file_paypal.beancount` | Generált PayPal kimeneti fájl. |
| `test/CSV - old files/` | Régebbi CSV-k és generált fájlok. |

## Fájlnév elv

A mappák továbbra is tartalmaznak történelmi neveket, mint például a `2023`, még akkor is, ha 2024-ből, 2025-ből és 2026-ból származó későbbi tevékenységeket is tartalmaznak. Tekintsék az aktuálisan hivatkozott fő főkönyvi fájlokat az aktív főkönyvekként, hacsak a struktúrát szándékosan nem változtatják meg.

## Hol szerkesszünk

| Egyesület | Szerkeszd ezt a fájlt |
| --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` |

Ne szerkesszék a generált kimeneti fájlokat, mint állandó nyilvántartást. Ezek ideiglenes tárolófájlok.
