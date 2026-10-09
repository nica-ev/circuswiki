---
lang: de
translation_id: beancount/00-bookkeeping-home
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Buchhaltungssystem-Dokumentation
description: Überblick und Ausgangspunkt für die Beancount-Buchhaltungsdokumentation von NICA e.V. und Tohuwabohu Halle e.V.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/00-bookkeeping-home.md
translation_source_body_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_source_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:30:57+00:00
translation_source_localized_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_source_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:30:57+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# Dokumentation des Buchhaltungssystems

Diese Dokumentation erklärt, wie das Buchhaltungssystem für NICA e.V. und Tohuwabohu Halle e.V. aus der Perspektive eines normalen Benutzers funktioniert.

Das System verwendet Klartext-Buchhaltungsdateien im Beancount-Format und eine Browser-Oberfläche namens Fava. Sie müssen keine Programmierkenntnisse haben, um es zu nutzen, aber Sie müssen den Buchhaltungsworkflow sorgfältig befolgen: Bankdaten importieren, Transaktionen zuordnen, Belege bei Bedarf anhängen und Salden prüfen.

## Hier beginnen

- [01 - Systemübersicht](01-system-overview.md)
- [02 - Fava öffnen](02-opening-fava.md)
- [03 - Ordner- und Dateistruktur](03-folder-and-file-map.md)
- [04 - Beancount-Grundlagen für Benutzer](04-beancount-basics-for-users.md)
- [05 - Konten und Kategorien](05-accounts-and-categories.md)
- [06 - Transaktionen eingeben und bearbeiten](06-entering-and-editing-transactions.md)
- [07 - Bank-CSV-Import und Abgleich](07-bank-csv-import-and-reconciliation.md)
- [08 - Projekte und zweckgebundene Mittel](08-projects-and-restricted-funds.md)
- [09 - Belege und Dokumente](09-receipts-and-documents.md)
- [10 - Fava-Dashboards und Berichte](10-fava-dashboards-and-reports.md)
- [11 - Regelmäßige Buchhaltungspraxis](11-regular-bookkeeping-routine.md)
- [12 - Fehlerbehebung](12-troubleshooting.md)
- [13 - Glossar](13-glossary.md)

## Die wichtigste Regel

Die Buchhaltungsdatei ist die maßgebliche Quelle. Fava zeigt nur an, was in den `.beancount`-Dateien steht. Wenn in Fava etwas falsch aussieht, korrigieren Sie den Beancount-Eintrag und laden Sie Fava neu.

## Aktuelle Bücher

| Organisation | Hauptdatei | Fava-Adresse | Port |
| --- | --- | --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` | `http://127.0.0.1:4998/` | `4998` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` | `http://127.0.0.1:4999/` | `4999` |

## Was diese Dokumentation nicht ist

Dies ist keine Rechts- oder Steuerberatung. Sie beschreibt, wie dieses spezifische lokale Buchhaltungssystem organisiert ist und wie Benutzer damit konsistent arbeiten sollten.
