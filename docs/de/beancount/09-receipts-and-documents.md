---
lang: de
translation_id: beancount/09-receipts-and-documents
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Belege und Dokumente
description: Erklärt, wo Belege aufbewahrt werden und wie Transaktionen auf Belege verweisen.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/09-receipts-and-documents.md
translation_source_body_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_source_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_model: openai/codex
translation_updated: 2026-10-10T00:00:00+00:00
translation_source_localized_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_source_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T15:14:00+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 09 - Belege und Dokumente

Belege, Rechnungen, Verträge und andere unterstützende Dokumente machen Buchungen nachvollziehbar. Das Buchungsjournal sollte es ermöglichen, den Beleg hinter einer Ausgabe zu finden.

## Wo Dokumente gespeichert werden

Tohuwabohu verfügt derzeit über einen klar definierten Belegordner:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben
```

Bereits in das Journal eingetragene Belege befinden sich häufig in:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben/Eingetragen
```

NICA speichert zugehörige Dateien im Buchhaltungsordner und in den Projektordnern. Falls später ein einheitlicher NICA-Belegordner eingeführt wird, sollte er hier dokumentiert und konsequent verwendet werden.

## `document`-Einträge

Ein `document`-Eintrag verknüpft eine Datei mit einem Konto und einem Datum:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```

Der Dateipfad ist relativ zum Ordner, in dem sich die Buchungsdatei befindet.

## Dokumentverknüpfungen mit Tags

Einige ältere Einträge enthalten Dokument-Tags wie:

```beancount
2023-01-05 document Ausgaben:Buero:Sonstiges "Belege Ausgaben/Eingetragen/2023_001.jpg" ^2023_001
```

Der Teil `^2023_001` ist eine Beancount-Verknüpfung. Er kann einen Beleg mit der zugehörigen Buchung verbinden, wenn dort dieselbe Verknüpfung verwendet wird.

## Bedeutung von `scanned`

Kommentare in den Buchungsdateien definieren die Konvention für gescannte Belege. Wenn das Tag `scanned` verwendet wird, bedeutet das:

- Der Beleg wurde gescannt oder digitalisiert.
- Das Bild wurde verkleinert und optimiert, beispielsweise mit TinyPNG.
- Die Datei wurde nach einem Jahres- und Nummernschema gespeichert, beispielsweise `2023_002.jpg`.
- Die Nummer wird im zugehörigen Journaleintrag referenziert.

## Gute Dateinamen

Gute Belegdateinamen sind dauerhaft und verständlich:

```text
2026_001.jpg
2026_002.pdf
Quittung-Tohu25-001.pdf
Invoice406-Schwarze_Risse-marc-bielert.pdf
```

Vermeiden Sie Namen wie `scan.jpg`, `image1.jpg` oder `download.pdf`.

## Arbeitsablauf für einen neuen Beleg

1. Speichern Sie den Beleg im richtigen Belegordner.
2. Benennen Sie ihn so um, dass er später eindeutig erkannt werden kann.
3. Tragen Sie die zugehörige Buchung ein oder suchen Sie diese.
4. Ergänzen Sie bei Bedarf eine `document`-Zeile oder Link-Metadaten.
5. Verschieben Sie den verarbeiteten Beleg nach `Eingetragen`, sofern dies der verwendeten Ordnerkonvention entspricht.
6. Laden Sie Fava neu und prüfen Sie, ob die Dokumentverknüpfung funktioniert.

## Wenn ein Beleg fehlt

Wenn ein Beleg fehlt, ergänzen Sie einen Kommentar bei der Buchung:

```beancount
; Beleg fehlt. Verantwortliche Person fragen.
```

Geben Sie nicht vor, dass ein Dokument vorhanden ist, wenn es nicht verfügbar ist.

## Verträge und Honorarunterlagen

Verträge und Honorarrechnungen sollten in der Nähe des zugehörigen Projekt- oder Buchhaltungsordners gespeichert und eindeutig referenziert werden. Bei einer Projektprüfung ist nicht nur wichtig, dass die Buchung existiert, sondern auch, dass der Nachweis für die Ausgabe schnell gefunden werden kann.
