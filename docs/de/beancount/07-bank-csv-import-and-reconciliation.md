---
lang: de
translation_id: beancount/07-bank-csv-import-and-reconciliation
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Bank-CSV-Import und Abgleich
description: Workflow zum Importieren von Sparkassen-CSV-Daten und Abgleichen von Bankguthaben.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/07-bank-csv-import-and-reconciliation.md
translation_source_body_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_source_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:54:10+00:00
translation_source_localized_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_source_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:54:10+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 07 - CSV-Import und Abgleich mit der Bank

Dieser Workflow bringt neue Sparkassen-Transaktionen in Beancount und bestätigt, dass das Buchhaltungsjournal noch mit dem realen Bankkonto übereinstimmt.

## Wo Importe stattfinden

| Verein | Importordner | Skript | Ausgabedatei |
| --- | --- | --- | --- |
| NICA | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/test` | `csv2bean.py` | `beancount_file.beancount` |
| Tohuwabohu | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/test` | `csv2bean.py` | `beancount_file.beancount` |

## Vor dem Export aus der Sparkasse

1. Öffnen Sie die richtige Buchhaltungsdatei.
2. Suchen Sie den Abschnitt `Kontenabgleiche`.
3. Finden Sie das letzte Saldo-Datum für das Sparkassenkonto.
4. Überprüfen Sie auch den Abschnitt `Bank-Dump` am Ende auf das letzte importierte Datum.
5. Verwenden Sie das spätere dieser Daten als Ihren Ausgangspunkt.

Dies vermeidet, dass Transaktionen übersehen oder derselbe Zeitraum zweimal importiert werden.

## Export aus der Sparkasse

1. Öffnen Sie die Kontenübersicht.
2. Filtern Sie nach dem Datumsbereich.
3. Beginnen Sie mit dem letzten geprüften oder importierten Datum.
4. Enden Sie mit dem heutigen Datum oder dem gewünschten Abgleichdatum.
5. Exportieren Sie als `Excel (CSV-CAMT V2)`.
6. Kopieren Sie die heruntergeladene CSV-Datei in den richtigen `test`-Ordner.

Die Skripte erwarten das Sparkassen CSV-CAMT-V2-Format mit Semikolon-getrennten Spalten.

## Konvertierung der CSV

Öffnen Sie ein Terminal im richtigen `test`-Ordner und führen Sie aus:

```powershell
python csv2bean.py "NAME-DER-HERUNTERGELADENEN-DATEI.CSV"
```

Beispiel:

```powershell
python csv2bean.py "20260312-1894137139-umsatz.CSV"
```

Wenn es funktioniert, gibt das Skript `Process finished.` aus und erstellt oder überschreibt `beancount_file.beancount`.

## Was der Konverter tut

Der Konverter erstellt grundlegende Beancount-Einträge:

- Eingehende Beträge gehen standardmäßig auf das Sparkassen-Asset-Konto und `Einnahmen:Sonstiges`.
- Ausgehende Beträge gehen standardmäßig auf `Ausgaben:Sonstiges` und das Sparkassen-Asset-Konto.
- Einige Einkommensbeschreibungen werden automatisch als `Einnahmen:Vereinsbeitrag` klassifiziert.
- Einige Tohuwabohu-bezogene Texte können einem Projekt-Einkommenskonto zugeordnet werden.

Der Konverter ist nur ein erster Schritt. Er kennt nicht die endgültige buchhalterische Bedeutung jeder Transaktion.

## Kopieren in das Hauptbuchhaltungsjournal

1. Öffnen Sie `test/beancount_file.beancount`.
2. Ignorieren Sie die generierte Optionsüberschrift.
3. Kopieren Sie nur die Transaktionen.
4. Fügen Sie sie zuerst unter `Bank-Dump` in das Hauptbuchhaltungsjournal ein.
5. Fügen Sie bei Bedarf einen datierten Trenner für das Importdatum hinzu.

```beancount
****************************************************************************
** 2026-01-13
****************************************************************************
```

Der `Bank-Dump` ist ein Wartebereich. Importierte Transaktionen können später in den richtigen thematischen oder Projektbereich verschoben werden.

## Klassifizierung importierter Einträge

Entscheiden Sie für jede importierte Transaktion:

- Handelt es sich um eine Transaktion auf Verbandsebene oder Projektebene?
- Handelt es sich um Einnahmen oder Ausgaben?
- Handelt es sich um eine Rückerstattung oder eine Verbindlichkeitszahlung?
- Gehört es zu `Freies-Geld` oder einem projektspezifischen Asset-Konto?
- Gibt es eine Quittung oder Rechnung, die angehängt werden kann?

Ersetzen Sie allgemeine Fallback-Konten wie `Ausgaben:Sonstiges`, wenn ein genaueres Konto existiert.

## Hinzufügen einer Saldenprüfung

NICA-Beispiel:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Tohuwabohu-Beispiel:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-Tohuwabohu 2345.67 EUR
```

Verwenden Sie den von der Sparkasse angezeigten Saldo für genau dieses Datum.

## Validierung in Fava

1. Speichern Sie die Buchhaltungsdatei.
2. Laden Sie Fava neu.
3. Überprüfen Sie auf Fehler am oberen Rand der Fava-Seite.
4. Öffnen Sie die Sparkassen-Kontoübersicht.
5. Bestätigen Sie den laufenden Saldo und die neuesten Transaktionen.
6. Überprüfen Sie die Bilanz.
7. Überprüfen Sie die Projekt-Dashboards, wenn Projektkonten betroffen waren.

## Wenn die Saldenprüfung fehlschlägt

Häufige Ursachen:

- Der CSV-Export hat einen Tag am Anfang oder Ende verpasst.
- Eine Transaktion wurde doppelt importiert.
- Eine Transaktion wurde in das falsche Verbandsbuchhaltungsjournal kopiert.
- Eine Zahl wurde falsch bearbeitet.
- Eine Projekt-Aufteilung verwendete das falsche Vorzeichen.
- PayPal- oder Bargeldbewegungen wurden nicht ebenfalls erfasst.

Entfernen Sie die Saldenprüfung nicht einfach, um den Fehler verschwinden zu lassen. Beheben Sie die zugrunde liegende Transaktionsdifferenz.
