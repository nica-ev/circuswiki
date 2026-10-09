---
lang: de
translation_id: beancount/04-beancount-basics-for-users
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Beancount Grundlagen für Anwender
description: Einführung in das Beancount-Textformat und die Transaktionsmuster, die in den Büchern verwendet werden.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/04-beancount-basics-for-users.md
translation_source_body_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_source_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:35:41+00:00
translation_source_localized_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_source_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:35:41+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 04 - Beancount-Grundlagen für Anwender

Beancount speichert Buchhaltung als lesbaren Text. Jede Transaktion gibt an, was wann passiert ist, wer beteiligt war und welche Konten sich geändert haben.

## Grundlegende Transaktionsstruktur

```beancount
2026-01-13 ! "Trägerwerk Soziale Dienste in Sachsen-Anhalt GmbH" "RgNr. T-2504"
  Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld  680.00 EUR
  Einnahmen:Sonstiges
```

| Teil | Bedeutung |
| --- | --- |
| `2026-01-13` | Datum der Transaktion. |
| `!` | Statuskennzeichen. In diesem System wird es üblicherweise für importierte oder noch nicht endgültig geprüfte Einträge verwendet. |
| Erster Anführungszeichen-Text | Zahlungsempfänger oder -sender. |
| Zweiter Anführungszeichen-Text | Beschreibung oder Buchungstext der Bank. |
| Erste Kontenzeile | Wohin das Geld geflossen ist oder woher es kam. |
| Zweite Kontenzeile | Die entgegengesetzte Kategorie. Wenn kein Betrag angegeben ist, berechnet Beancount ihn automatisch. |

## Kontonamen

Kontonamen sind durch Doppelpunkte getrennt:

```text
Vermoegen:Bank:Sparkasse-NICA:Freies-Geld
```

Lesen Sie es von links nach rechts: Vermögen, Bankkonto, NICA Sparkasse, frei verfügbare Mittel.

## Die fünf Kontofamilien

| Familie | Bedeutung | Beispiel |
| --- | --- | --- |
| `Vermoegen` | Vermögenswerte: Bank, PayPal, Bargeld, Inventar. | `Vermoegen:Bank:Sparkasse-NICA` |
| `Verbindlichkeiten` | Verbindlichkeiten: Geld, das Personen oder anderen geschuldet wird. | `Verbindlichkeiten:Person:Marc-Bielert` |
| `Equity` | Eröffnungsbilanzen und Ausgleichsbuchungen. | `Equity:Opening-Balances` |
| `Einnahmen` | Einnahmen. | `Einnahmen:Vereinsbeitrag` |
| `Ausgaben` | Ausgaben. | `Ausgaben:Buero:Miete` |

## Vorzeichen für Einnahmen und Ausgaben

In Beancount-Berichten erscheinen Einnahmen intern oft mit einem negativen Vorzeichen und Ausgaben mit einem positiven Vorzeichen. Fava und die Dashboards präsentieren diese Werte oft benutzerfreundlicher. Ändern Sie keine Transaktionen nur deshalb, weil eine Einnahmenzahl in einer Rohabfrage negativ erscheint.

## Saldenprüfungen

Eine Saldenprüfung besagt, dass ein Konto zu einem bestimmten Datum einen bestimmten Saldo haben muss:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Wenn Beancount diesen Saldo nicht aus den Transaktionen vor diesem Datum ermitteln kann, zeigt Fava einen Fehler an. Saldenprüfungen sind der wichtigste Mechanismus zur Qualitätskontrolle.

## Konten eröffnen und schließen

Bevor ein Konto verwendet wird, wird es eröffnet:

```beancount
2025-04-01 open Ausgaben:Projekt:25-ZGV:Honorar
```

Wenn ein Projekt abgeschlossen ist und das Projektkonto Null ist, kann es geschlossen werden:

```beancount
2026-02-27 close Ausgaben:Projekt:TOHUCON-25
```

Geschlossene Konten sollten normalerweise keine neuen Transaktionen mehr erhalten.

## Kommentare und Belege

Zeilen, die mit `;` beginnen, sind Kommentare. Sie erklären Entscheidungen oder unsichere Situationen und beeinflussen die Zahlen nicht.

Belege können mit `document`-Zeilen verknüpft werden:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```
