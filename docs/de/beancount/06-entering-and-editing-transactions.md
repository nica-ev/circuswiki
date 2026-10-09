---
lang: de
translation_id: beancount/06-entering-and-editing-transactions
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Transaktionen eingeben und bearbeiten
description: Beschreibt, wie Benutzer Buchungstransaktionen überprüfen, klassifizieren, korrigieren und eingeben.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/06-entering-and-editing-transactions.md
translation_source_body_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_source_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:37:56+00:00
translation_source_localized_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_source_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:37:56+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 06 - Buchungen eingeben und bearbeiten

Die meisten Einträge stammen aus importierten Bankdaten, aber Benutzer müssen Transaktionen dennoch überprüfen, klassifizieren, korrigieren und manchmal manuell eingeben.

## Transaktionsstatus

Die Buchhaltungsdateien verwenden üblicherweise `!` bei importierten Transaktionen:

```beancount
2026-03-12 ! "Zahlungsempfänger" "Banktext"
```

Verwenden Sie dies als normalen Marker, es sei denn, das Team entscheidet sich für eine strengere Statuskonvention.

## Einfache Einnahmebuchung

```beancount
2026-01-15 ! "Max Mustermann" "Mitgliedsbeitrag 2026"
  Vermögen:Bank:Sparkasse-NICA:Freies-Geld  60.00 EUR
  Einnahmen:Vereinsbeitrag
```

## Einfache Ausgabe

```beancount
2026-01-20 ! "Anbietername" "Rechnung 123"
  Ausgaben:Büro:Sonstiges  25.00 EUR
  Vermögen:Bank:Sparkasse-NICA
```

## Projekteinnahmen

```beancount
2026-02-10 ! "Fördereinrichtung" "Zuschusszahlung Projekt 25-ZGV"
  Vermögen:Bank:Sparkasse-NICA:25-ZGV  5000.00 EUR
  Einnahmen:Projekt:25-ZGV:Sachmittel
```

## Projektausgaben

```beancount
2026-02-15 ! "Name der Person" "Honorar Projekt 25-ZGV"
  Ausgaben:Projekt:25-ZGV:Honorar  450.00 EUR
  Vermögen:Bank:Sparkasse-NICA:25-ZGV
```

## Interne Verrechnung zwischen Projekt- und freien Mitteln

Manchmal muss eine Transaktion Bankguthaben zwischen einem projektspezifischen Anlagekonto und freien Mitteln zuordnen. Das eigentliche Bankkonto ist ein physisches Sparkassenkonto, aber die Buchhaltungsdatei verfolgt die internen Projektguthaben separat.

```beancount
2026-02-20 ! "Interne Verrechnung" "Restliche Projektmittel auf freie Mittel übertragen"
  Vermögen:Bank:Sparkasse-NICA:Freies-Geld  100.00 EUR
  Vermögen:Bank:Sparkasse-NICA:25-ZGV      -100.00 EUR
```

Führen Sie interne Überweisungen nur durch, wenn Sie verstehen, warum sich das interne Projektguthaben ändern muss.

## Rückerstattungen an Personen

Wenn jemand privat bezahlt hat und später erstattet wird, ist das saubere Muster normalerweise, die Ausgabe gegen eine Verbindlichkeit zu verbuchen und dann die Verbindlichkeit mit der Bankzahlung auszugleichen.

```beancount
2026-03-01 ! "Geschäft" "Material von Marc gekauft"
  Ausgaben:Projekt:25-ZGV:Sachmittel  35.00 EUR
  Verbindlichkeiten:Person:Marc-Bielert
```

```beancount
2026-03-05 ! "Marc Bielert" "Rückerstattung Material"
  Verbindlichkeiten:Person:Marc-Bielert  35.00 EUR
  Vermögen:Bank:Sparkasse-NICA
```

## Kommentare für unklare Entscheidungen

```beancount
; Unklar, ob dies zu CEDU-25 oder zu Mitteln der freien Vereinigung gehört. Rechnung prüfen.
2026-03-10 ! "Lieferant" "Rechnung 456"
  Ausgaben:Sonstiges  120.00 EUR
  Vermögen:Bank:Sparkasse-Tohuwabohu
```

## Sicher bearbeiten

Überprüfen Sie vor der Bearbeitung:

- Sie befinden sich in der richtigen Vereinsbuchhaltung.
- Sie bearbeiten nicht die generierte Importausgabe, als wäre sie die endgültige Buchhaltung.
- Das Transaktionsdatum ist korrekt.
- Der Betrag verwendet einen Punkt als Dezimaltrennzeichen, z. B. `12.50 EUR`.
- Kontonamen sind exakt wie bestehende Konten geschrieben.
- Transaktionen für Projekte verwenden konsequent das projektspezifische Anlagekonto und die entsprechende Einnahmen-/Ausgabenkategorie.

Speichern Sie nach der Bearbeitung die Datei, laden Sie Fava neu, prüfen Sie auf Fehler und inspizieren Sie die entsprechende Kontoübersicht.
