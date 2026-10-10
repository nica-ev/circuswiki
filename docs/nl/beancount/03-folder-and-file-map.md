---
lang: nl
translation_id: beancount/03-folder-and-file-map
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Map van Mappen en Bestanden
description: Brengt de belangrijkste boekhoudmappen, grootboekbestanden, dashboards en hulpprogramma's in kaart.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/03-folder-and-file-map.md
translation_source_body_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_source_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:19+00:00
translation_source_localized_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_source_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:19+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 03 - Mappen- en bestandsstructuur

Deze pagina legt uit waar de belangrijke boekhoudkundige bestanden zijn opgeslagen.

## Hoofdmap boekhouding

```text
1. Vereinsverwaltung/Buchhaltung
```

Deze map bevat de grootboeken, dashboardbestanden, ondersteunende documenten en hulpmappen.

## Belangrijke bestanden op het hoogste niveau

| Bestand | Doel |
| --- | --- |
| `Buchhaltung Home.md` | Obsidian startpagina met knoppen en een korte workflow-notitie. |
| `all.beancount` | Experimenteel gecombineerd grootboek, inclusief zowel NICA als Tohuwabohu. |
| `dashboards.yaml` | Dashboarddefinitie voor Fava-dashboards op gedeeld niveau. |

## NICA-structuur

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA
```

| Pad | Doel |
| --- | --- |
| `2023/nica.beancount` | Hoofd NICA-grootboek. Dit is het bestand dat normaal gesproken wordt bewerkt. |
| `2023/dashboards.yaml` | Dashboardconfiguratie voor het NICA-grootboek. |
| `2023/Buchhaltung NICA eV.md` | Obsidian hulpnotitie voor het openen van de NICA-boekhouding. |
| `2023/CSV/` | Opgeslagen CSV-exports. |
| `test/csv2bean.py` | Converteert Sparkasse CSV naar tijdelijke Beancount-invoer. |
| `test/beancount_file.beancount` | Gegenereerde uitvoer van de CSV-conversie. |
| `test/paypal2bean.py` | Hulp voor PayPal CSV-import. |
| `test/output_file_paypal.beancount` | Gegenereerd PayPal-uitvoerbestand. |
| `test/old files/` | Oudere CSV's en gegenereerde bestanden. |

## Tohuwabohu-structuur

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu
```

| Pad | Doel |
| --- | --- |
| `2023/2023.beancount` | Hoofd Tohuwabohu-grootboek. Dit is het bestand dat normaal gesproken wordt bewerkt. |
| `2021/2021.beancount` | Oudere grootboekgegevens inbegrepen via `all.beancount`. |
| `all.beancount` | Tohuwabohu gecombineerd bestand inclusief 2021 en 2023 grootboekbestanden. |
| `2023/dashboards.yaml` | Dashboardconfiguratie voor het Tohuwabohu-grootboek. |
| `2023/Buchhaltung Tohuwabohu Halle eV.md` | Obsidian hulpnotitie. |
| `2023/Belege Ausgaben/` | Bonnen en ondersteunende documenten voor uitgaven. |
| `2023/Belege Ausgaben/Eingetragen/` | Bonnen die al in het grootboek zijn ingevoerd. |
| `test/csv2bean.py` | Converteert Sparkasse CSV naar tijdelijke Beancount-invoer. |
| `test/beancount_file.beancount` | Gegenereerde uitvoer van de CSV-conversie. |
| `test/paypal2bean.py` | Hulp voor PayPal CSV-import. |
| `test/output_file_paypal.beancount` | Gegenereerd PayPal-uitvoerbestand. |
| `test/CSV - old files/` | Oudere CSV's en gegenereerde bestanden. |

## Naamgevingsprincipe voor bestanden

De mappen bevatten nog steeds historische namen zoals `2023`, zelfs als ze ook latere activiteiten uit 2024, 2025 en 2026 bevatten. Behandel de momenteel genoemde hoofdgrootboekbestanden als de actieve grootboeken, tenzij de structuur opzettelijk wordt gewijzigd.

## Waar te bewerken

| Vereniging | Bewerk dit bestand |
| --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` |

Bewerk gegenereerde uitvoerbestanden niet als het permanente archief. Het zijn tijdelijke tussenliggende bestanden.
