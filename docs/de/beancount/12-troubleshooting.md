---
lang: de
translation_id: beancount/12-troubleshooting
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Fehlerbehebung
description: Häufige Probleme mit Fava und Beancount und deren Lösungen.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/12-troubleshooting.md
translation_source_body_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_source_hash: 26fac2a1c31bc57e29098f19db69045861ba45fbd9d67bb53161a10036da7127
translation_model: openai/codex
translation_updated: 2026-10-10T00:00:00+00:00
translation_source_localized_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_source_metadata_hash: 057b766ece200d595e0b9c1b2d9361b62bdcfa02f03d388656053c057d1cd7dd
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T15:14:23+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 12 - Fehlerbehebung

## Fava lässt sich nicht öffnen

Prüfen Sie:

- Ist das Terminalfenster noch geöffnet?
- Wurde Fava im richtigen Ordner gestartet?
- Wird der richtige Port verwendet?
- Läuft bereits eine andere Fava-Instanz auf demselben Port?
- Ist Fava im Terminal installiert und verfügbar?

Befehle:

```powershell
fava nica.beancount --port 4998
fava 2023.beancount --port 4999
```

Führen Sie jeden Befehl nur vom korrekten Ledger-Ordner aus.

## Fava zeigt einen Beancount-Fehler an

Häufige Ursachen:

- Tippfehler im Kontonamen.
- Fehlende `open`-Direktive für ein Konto.
- Betrag verwendet Komma statt Punkt.
- Anführungszeichen fehlen um Zahlungsempfänger oder Beschreibung.
- Eine Transaktion ist nicht ausgeglichen.
- Eine Saldenprüfung stimmt nicht überein.
- Eine Transaktion verwendet ein Konto, nachdem es geschlossen wurde.

Korrigieren Sie die Textdatei, speichern Sie sie und laden Sie Fava neu.

## Saldenprüfung schlägt fehl

Löschen Sie die Saldenprüfung nicht als Workaround. Untersuchen Sie die Differenz.

Checkliste:

- War der CSV-Datumsbereich vollständig?
- Wurde dieselbe CSV zweimal importiert?
- Wurden einige Transaktionen in das falsche Ledger kopiert?
- Wurde eine Transaktion dem falschen Sparkassen-Unterkonto zugeordnet?
- Wurde ein Betragszeichen falsch geändert?
- Wurde eine PayPal- oder Bargeldüberweisung nur auf einer Seite eingetragen?
- Gibt es ältere manuelle Bearbeitungen nach der vorherigen Saldenprüfung?

## CSV-Konvertierung schlägt fehl

Prüfen Sie:

- Die CSV-Datei befindet sich im selben `test`-Ordner wie `csv2bean.py`.
- Der Dateiname im Befehl ist exakt.
- Die Datei ist der Sparkassen-Export `Excel (CSV-CAMT V2)`.
- Die Datei ist durch Semikolons getrennt.
- Die CSV-Datei wurde nicht auf eine Weise geöffnet und erneut gespeichert, die ihr Format verändert hat.

## Importierte Einträge wirken zu allgemein

Das ist zu erwarten. Der Konverter verwendet Auffangkategorien wie:

- `Ausgaben:Sonstiges`
- `Einnahmen:Sonstiges`

Importierte Einträge müssen anschließend manuell geprüft und zugeordnet werden.

## Dashboard fehlt

Prüfen Sie:

- `fava-dashboards` ist installiert.
- Die Buchungsdatei enthält die Direktive `custom "fava-extension" "fava_dashboards"`.
- Neben der Buchungsdatei befindet sich eine `dashboards.yaml`-Datei.
- Fava wurde nach Änderungen an Installation oder Konfiguration neu gestartet.

## Ein Projekt erscheint nicht in den Dashboards

Prüfen Sie:

- Das Projekt besitzt ein Projekt-Vermögenskonto unter dem erwarteten Sparkassen- oder PayPal-Präfix.
- Das Projektkonto ist nicht geschlossen.
- Der Projektsaldo ist nicht genau null.
- Der Kontoname entspricht dem Abfragemuster des Dashboards.

## Dokumentverknüpfung funktioniert nicht

Prüfen Sie:

- Der Dateipfad ist relativ zum Ordner der Buchungsdatei.
- Der Dateiname ist exakt geschrieben.
- Das Dokument wurde nach dem Verknüpfen nicht verschoben.
- Der Pfad verwendet Schrägstriche oder einen üblichen relativen Pfadstil.

## Unklar, wie eine Buchung zuzuordnen ist

Gehen Sie in dieser Reihenfolge vor:

1. Suchen Sie in Fava nach ähnlichen älteren Buchungen.
2. Prüfen Sie den Projekt- oder Rechnungskontext.
3. Prüfen Sie, ob die Buchung zu einer Budgetposition eines Fördermittelgebers gehört.
4. Ergänzen Sie bei Unsicherheit einen Kommentar.
5. Verwenden Sie `Sonstiges` vorübergehend nur dann, wenn keine bessere Kategorie bekannt ist.
6. Fragen Sie vor der endgültigen Zuordnung die verantwortliche Projekt- oder Finanzperson.
