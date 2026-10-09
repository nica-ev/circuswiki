---
lang: de
translation_id: beancount/03-folder-and-file-map
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Ordner- und Dateizuordnung
description: Ordnet die wichtigen Buchhaltungsordner, Hauptbuchdateien, Dashboards und Hilfsdateien zu.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/03-folder-and-file-map.md
translation_source_body_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_source_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:34:31+00:00
translation_source_localized_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_source_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:34:31+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 03 - Ordner- und Dateistruktur

Diese Seite erklärt, wo die wichtigen Buchhaltungsdateien gespeichert sind.

## Hauptordner Buchhaltung

```text
1. Vereinsverwaltung/Buchhaltung
```

Dieser Ordner enthält die Hauptbücher, Dashboard-Dateien, Belege und Hilfsordner.

## Wichtige Dateien auf oberster Ebene

| Datei | Zweck |
| --- | --- |
| `Buchhaltung Home.md` | Obsidian-Einstiegsseite mit Schaltflächen und einer kurzen Workflow-Notiz. |
| `all.beancount` | Experimentelles kombiniertes Hauptbuch, das sowohl NICA als auch Tohuwabohu enthält. |
| `dashboards.yaml` | Dashboard-Definition für Fava-Dashboards auf gemeinsamer Ebene. |

## NICA-Struktur

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA
```

| Pfad | Zweck |
| --- | --- |
| `2023/nica.beancount` | Hauptbuch für NICA. Dies ist die Datei, die normalerweise bearbeitet wird. |
| `2023/dashboards.yaml` | Dashboard-Konfiguration für das NICA-Hauptbuch. |
| `2023/Buchhaltung NICA eV.md` | Obsidian-Hilfsnotiz zum Öffnen der NICA-Buchhaltung. |
| `2023/CSV/` | Gespeicherte CSV-Exporte. |
| `test/csv2bean.py` | Konvertiert Sparkassen-CSV in temporäre Beancount-Einträge. |
| `test/beancount_file.beancount` | Generierte Ausgabe aus der CSV-Konvertierung. |
| `test/paypal2bean.py` | Hilfsprogramm für PayPal-CSV-Importe. |
| `test/output_file_paypal.beancount` | Generierte PayPal-Ausgabedatei. |
| `test/old files/` | Ältere CSVs und generierte Dateien. |

## Tohuwabohu-Struktur

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu
```

| Pfad | Zweck |
| --- | --- |
| `2023/2023.beancount` | Hauptbuch für Tohuwabohu. Dies ist die Datei, die normalerweise bearbeitet wird. |
| `2021/2021.beancount` | Ältere Hauptbuchdaten, die über `all.beancount` einbezogen werden. |
| `all.beancount` | Kombinierte Tohuwabohu-Datei, die die Hauptbuchdateien von 2021 und 2023 enthält. |
| `2023/dashboards.yaml` | Dashboard-Konfiguration für das Tohuwabohu-Hauptbuch. |
| `2023/Buchhaltung Tohuwabohu Halle eV.md` | Obsidian-Hilfsnotiz. |
| `2023/Belege Ausgaben/` | Belege und unterstützende Dokumente für Ausgaben. |
| `2023/Belege Ausgaben/Eingetragen/` | Belege, die bereits in das Hauptbuch eingetragen wurden. |
| `test/csv2bean.py` | Konvertiert Sparkassen-CSV in temporäre Beancount-Einträge. |
| `test/beancount_file.beancount` | Generierte Ausgabe aus der CSV-Konvertierung. |
| `test/paypal2bean.py` | Hilfsprogramm für PayPal-CSV-Importe. |
| `test/output_file_paypal.beancount` | Generierte PayPal-Ausgabedatei. |
| `test/CSV - old files/` | Ältere CSVs und generierte Dateien. |

## Namensprinzip für Dateien

Die Ordner enthalten weiterhin historische Namen wie `2023`, auch wenn sie spätere Aktivitäten aus den Jahren 2024, 2025 und 2026 enthalten. Behandeln Sie die aktuell referenzierten Hauptbuchdateien als die aktiven Hauptbücher, es sei denn, die Struktur wird absichtlich geändert.

## Wo zu bearbeiten

| Verein | Diese Datei bearbeiten |
| --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` |

Bearbeiten Sie keine generierten Ausgabedateien als dauerhafte Aufzeichnung. Es handelt sich um temporäre Staging-Dateien.
