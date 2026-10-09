---
lang: de
translation_id: beancount/01-system-overview
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Systemübersicht
description: Erläutert den Zweck, die Komponenten und den normalen Benutzerablauf des Buchhaltungssystems.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/01-system-overview.md
translation_source_body_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_source_hash: 4470d0cc26952bfa78d3d570da387af93c6d407d46dc06543ca9b2a2e69e4b65
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:32:13+00:00
translation_source_localized_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_source_metadata_hash: 3863961c2f755b8d4df8bb269c2bba03cb2b98c5777689de151d93930256390e
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:32:13+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 01 - Systemübersicht

## Zweck

Das Buchhaltungssystem erfasst alle finanziellen Aktivitäten der Vereine auf strukturierte und nachprüfbare Weise. Es ist darauf ausgelegt, übliche Buchführungsfragen zu beantworten:

- Wie viel Geld ist aktuell verfügbar?
- Welche Einnahmen und Ausgaben gehören zum Verein selbst?
- Welche Einnahmen und Ausgaben gehören zu einem bestimmten Projekt?
- Stimmen die Kontostände von Sparkasse, PayPal und Bargeld?
- Welche Belege und Dokumente gehören zu welchen Transaktionen?
- Welche Projekte sind aktiv, in Bearbeitung oder bereits abgeschlossen?

## Hauptkomponenten

| Komponente | Was sie tut |
| --- | --- |
| Beancount | Das Format für die Buchhaltungsdaten. Transaktionen werden in Klartextdateien geschrieben. |
| Fava | Die Browser-Oberfläche zur Anzeige und Filterung der Beancount-Daten. |
| Fava Dashboards | Benutzerdefinierte Dashboard-Seiten innerhalb von Fava für den Management-Überblick und Projektansichten. |
| Obsidian | Das Notizsystem, aus dem die Buchhaltung über Schaltflächen geöffnet werden kann. |
| CSV-Import-Skripte | Hilfsskripte, die Sparkassen-CSV-Exporte in Beancount-Einträge umwandeln. |

## Wie die Teile zusammenpassen

1. Bank- oder PayPal-Daten werden als CSV exportiert.
2. Die CSV wird in temporäre Beancount-Einträge umgewandelt.
3. Die neuen Einträge werden in die richtige Hauptbuchdatei kopiert.
4. Der Benutzer prüft, klassifiziert und korrigiert die Einträge.
5. Saldenprüfungen bestätigen, dass das Hauptbuch mit dem Bank- oder PayPal-Saldo übereinstimmt.
6. Fava zeigt Berichte, Kontoseiten, Gewinn- und Verlustrechnungen, Bilanzen und Dashboards an.

## Zwei getrennte Vereine

| Verein | Hauptbuch | Typischer Kontopräfix |
| --- | --- | --- |
| NICA e.V. | `nica.beancount` | `Sparkasse-NICA`, `NICA` |
| Tohuwabohu Halle e.V. | `2023.beancount` | `Sparkasse-Tohuwabohu`, `Tohuwabohu` |

Es gibt auch eine experimentelle kombinierte Datei: `1. Vereinsverwaltung/Buchhaltung/all.beancount`. Die normale tägliche Arbeit sollte im individuellen Hauptbuch des jeweiligen Vereins stattfinden.

## Grundlegender Arbeitsablauf

1. Die richtige Fava-Instanz öffnen.
2. Die letzte abgeschlossene Saldenprüfung finden.
3. Neue Banktransaktionen von der Sparkasse ab dem letzten geprüften Datum exportieren.
4. Die CSV in das Beancount-Format konvertieren.
5. Die generierten Einträge zuerst in den Abschnitt `Bank Dump` einfügen.
6. Einträge in die richtigen Vereins- oder Projektbereiche verschieben oder klassifizieren.
7. Bei Bedarf Belege, Links, Kommentare oder Tags hinzufügen.
8. Eine neue Saldenprüfung hinzufügen.
9. Fava neu laden und überprüfen, ob keine Fehler vorhanden sind.

## Was ein neuer Benutzer zuerst lernen sollte

1. [Fava öffnen](02-opening-fava.md)
2. [Beancount-Grundlagen für Benutzer](04-beancount-basics-for-users.md)
3. [Bank-CSV-Import und Abgleich](07-bank-csv-import-and-reconciliation.md)
4. [Konten und Kategorien](05-accounts-and-categories.md)
5. [Projekte und zweckgebundene Mittel](08-projects-and-restricted-funds.md)
