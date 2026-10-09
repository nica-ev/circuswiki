---
lang: de
translation_id: beancount/10-fava-dashboards-and-reports
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Fava Dashboards und Berichte
description: Übersicht über Fava-Berichte und benutzerdefinierte Dashboards zur Buchprüfung.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/10-fava-dashboards-and-reports.md
translation_source_body_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_source_hash: 41b405dcd3dcff9db7a8c27a1843563c515f0f703a4801cedbf2fce9608327dc
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T15:14:04+00:00
translation_source_localized_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_source_metadata_hash: f508998c195026d33f551d49d2373ce607979b149f524c4e84651765e23bb970
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T15:14:04+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 10 - Fava Dashboards und Berichte

Fava bietet Standard-Buchhaltungsberichte. Das System nutzt außerdem `fava-dashboards` für benutzerdefinierte Übersichtsseiten.

## Standard-Fava-Ansichten

| Ansicht | Verwendung für |
| --- | --- |
| Bilanz | Überprüfung von Vermögenswerten, Verbindlichkeiten, frei verfügbaren Mitteln, PayPal, Bargeld und Projektguthaben. |
| Gewinn- und Verlustrechnung | Anzeige von Einnahmen und Ausgaben über die Zeit. |
| Kontoübersicht | Einsicht in alle Transaktionen eines einzelnen Kontos. |
| Journal | Suche im chronologischen Transaktionsverlauf. |
| Abfrage | Ausführung benutzerdefinierter Beancount-Abfragen bei Bedarf. |
| Dokumente | Auffinden verknüpfter Belege und Dateien. |

## Dashboard-Erweiterung

Die Ledgers enthalten diese Direktive:

```beancount
2010-01-01 custom "fava-extension" "fava_dashboards"
```

Dies aktiviert die Dashboard-Erweiterung, wenn `fava-dashboards` installiert ist.

## Dashboard-Konfigurationsdateien

Dashboard-Dateien heißen `dashboards.yaml`. Sie werden in der Nähe der Ledger-Dateien und auf der gemeinsamen Buchhaltungsebene gespeichert.

## Haupt-Dashboard-Bereiche

| Dashboard | Zweck |
| --- | --- |
| `Vorstand-Cockpit` | Management-Übersicht: freies Geld, gesamtes Sparkassen-Guthaben, PayPal, Bargeld, Liquiditätstrend, monatliches Ergebnis, Guthaben aktiver Projekte. |
| `Details & Daten` | Detaillierte Diagramme: Ausgaben nach Kategorie, Einnahmen nach Kategorie, Geldfluss, Projekt-/Personennetzwerk. |

## Wichtige Dashboard-Indikatoren

### Freies Geld

Zeigt verfügbares Geld außerhalb von zweckgebundenen Projektmitteln an. Typische Konten sind `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld` und `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`.

### Sparkasse Gesamt

Zeigt den gesamten Sparkassen-Saldo über das Hauptbankkonto und interne Unterkonten an.

### PayPal

Zeigt den PayPal-Saldo an. Ein negativer PayPal-Saldo deutet auf Prüfungsbedarf hin.

### Barkasse

Zeigt den Kassenbestand an.

### Saldo Aktiver Projekte

Zeigt Projektguthaben an, die nicht Null sind. Dies ist nützlich, um zu sehen, welche Projekte noch Geld enthalten oder überzogen sind.

### Monatlicher Überschuss / Fehlbetrag

Zeigt den monatlichen betrieblichen Überschuss oder Fehlbetrag an, wobei Projektkonten in der Dashboard-Abfrage ausgeschlossen sind.

## Verantwortungsvoller Umgang mit Dashboards

Dashboards sind Zusammenfassungen. Wenn eine Zahl überraschend erscheint:

1. Klicken Sie auf das verknüpfte Fava-Konto oder den Bericht.
2. Untersuchen Sie die zugrunde liegenden Transaktionen.
3. Prüfen Sie, ob eine Transaktion noch unter `Sonstiges` oder `Bank Dump` steht.
4. Prüfen Sie, ob der Kontoname dem Muster der Dashboard-Abfrage entspricht.
5. Bestätigen Sie die Saldenprüfungen, bevor Sie den Managementzahlen vertrauen.

## Wenn Dashboard-Zahlen falsch erscheinen

Häufige Ursachen:

- Eine Transaktion wurde auf das Hauptbankkonto statt auf das Projektunterkonto gebucht.
- Ein Projektkonto wurde geschlossen, hat aber immer noch einen Saldo ungleich Null.
- Ein neues Projekt verwendet ein Namensmuster, das nicht in der Dashboard-Abfrage enthalten ist.
- Eine Transaktion befindet sich noch in einer allgemeinen Fallback-Kategorie.
- Die Dashboard-Datei gehört zu einem anderen Ledger als dem aktuell geöffneten.
