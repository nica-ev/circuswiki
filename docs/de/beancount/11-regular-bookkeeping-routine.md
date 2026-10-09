---
lang: de
translation_id: beancount/11-regular-bookkeeping-routine
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Regelmäßige Buchführungsroutine
description: Eine praktische Checkliste für wiederkehrende Aufgaben, um die Bücher aktuell zu halten.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/11-regular-bookkeeping-routine.md
translation_source_body_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_source_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T15:14:10+00:00
translation_source_localized_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_source_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T15:14:10+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 11 - Regelmäßige Buchführungsroutine

Diese Seite beschreibt eine praktische Routine, um die Bücher aktuell zu halten.

## Wöchentliche oder zweiwöchentliche Routine

Verwenden Sie diese Routine bei regelmäßigen Bankbewegungen.

1. Öffnen Sie die korrekte Fava-Instanz.
2. Prüfen Sie, ob Fava Fehler anzeigt.
3. Suchen Sie die letzte Saldenprüfung.
4. Exportieren Sie neue Sparkassen-CSV-Daten.
5. Konvertieren Sie die CSV mit `csv2bean.py`.
6. Fügen Sie neue Einträge in `Bank Dump` ein.
7. Ordnen Sie Einträge den korrekten Konten zu.
8. Hängen Sie Belege an oder verweisen Sie darauf, wo nötig.
9. Fügen Sie eine neue Saldenprüfung hinzu.
10. Laden Sie Fava neu und beheben Sie Fehler.
11. Überprüfen Sie `Ausgaben:Sonstiges` und `Einnahmen:Sonstiges` auf Einträge, die spezifischer sein sollten.

## Monatliche Routine

Am Monatsende:

1. Gleichen Sie die Sparkasse ab.
2. Gleichen Sie PayPal ab, falls verwendet.
3. Gleichen Sie die Kasse ab, falls Bargeld verwendet wurde.
4. Prüfen Sie offene Verbindlichkeiten gegenüber Personen.
5. Prüfen Sie die Salden laufender Projekte.
6. Überprüfen Sie nicht zugeordnete `Sonstiges`-Einträge.
7. Prüfen Sie fehlende Belege.
8. Prüfen Sie, ob abgeschlossene Projekte für die Schließung vorbereitet werden sollten.

## Projektberichtsroutine

Bevor Sie einen Projektbericht oder Verwendungsnachweis vorbereiten:

1. Öffnen Sie die Projektkontoseiten in Fava.
2. Exportieren Sie alle Projekteinnahmen und -ausgaben oder überprüfen Sie diese.
3. Bestätigen Sie, dass die Kategorien mit den Budgetlinien des Geldgebers übereinstimmen.
4. Bestätigen Sie, dass alle Belege und Honorardokumente vorhanden sind.
5. Prüfen Sie, ob Rückzahlungen, Stornierungen und Erstattungen als Korrekturen und nicht als falsche Einnahmen verbucht werden.
6. Bestätigen Sie, dass der Projektvermögenssaldo nachvollziehbar ist.
7. Wenn das Projekt abgeschlossen ist, verschieben Sie verbleibendes Geld korrekt und schließen Sie die Projektkonten.

## Jahresabschlussroutine

Am Jahresende:

1. Gleichen Sie alle Bankkonten ab.
2. Gleichen Sie PayPal ab.
3. Gleichen Sie die Kassen ab.
4. Prüfen Sie Verbindlichkeiten.
5. Prüfen Sie offene Projektbudgets.
6. Stellen Sie sicher, dass alle Belege gespeichert und verknüpft oder auffindbar sind.
7. Überprüfen Sie Einnahmen- und Ausgabenkategorien.
8. Fügen Sie abschließende Saldenprüfungen hinzu.
9. Erstellen Sie Berichte aus Fava.
10. Archivieren Sie exportierte CSVs und unterstützende Dokumente.

## Qualitätskontrollen

Ein Buchhaltungsbuch ist in gutem Zustand, wenn:

- Fava fehlerfrei geöffnet wird.
- Die letzte Sparkassen-Saldenprüfung mit der Bank übereinstimmt.
- PayPal- und Kassensalden, wo relevant, geprüft werden.
- Projektbudgets beabsichtigt und nachvollziehbar sind.
- Abgeschlossene Projekte einen Vermögenssaldo von Null aufweisen.
- `Sonstiges`-Konten keine vermeidbaren, unkategorisierten Einträge enthalten.
- Belege für Ausgaben gefunden werden können.
- Kommentare ungewöhnliche Korrekturen oder Annahmen erklären.

## Checkliste für die Übergabe an eine andere Person

Bevor Sie die Buchhaltung an jemand anderen übergeben:

- Zeigen Sie die korrekte Buchhaltungsdatei für jeden Verein.
- Zeigen Sie, wie Fava gestartet wird.
- Zeigen Sie die letzte Saldenprüfung.
- Zeigen Sie, wie CSV-Importe in `Bank Dump` vorbereitet werden.
- Zeigen Sie, wo Belege gespeichert sind.
- Zeigen Sie ein Beispielprojekt von der Finanzierung bis zum endgültigen Abschluss.
- Verweisen Sie auf diesen Dokumentationsordner.
