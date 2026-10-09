---
lang: de
translation_id: beancount/13-glossary
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Glossar
description: Definitionen von Buchhaltungs-, Beancount-, Fava- und Projektbuchhaltungsbegriffen, die in dieser Dokumentation verwendet werden.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/13-glossary.md
translation_source_body_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_source_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T15:14:28+00:00
translation_source_localized_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_source_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T15:14:28+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 13 - Glossar

## Konto

Ein benannter Ort, an dem Beancount Geld oder Wert erfasst. Beispiel: `Ausgaben:Buero:Miete`.

## Vermögenswert

Etwas, das der Verein besitzt oder kontrolliert, wie z. B. Bankgeld, PayPal-Guthaben, Bargeld oder Inventar. In diesem System sind Vermögenswerte unter `Vermoegen` aufgeführt.

## Saldenprüfung

Eine Zeile, die bestätigt, dass ein Konto zu einem bestimmten Datum einen bestimmten Saldo aufweist. Saldenprüfungen werden verwendet, um zu überprüfen, ob das Hauptbuch mit den Bank-, PayPal- oder Bargeldaufzeichnungen übereinstimmt.

## Bank-Dump

Ein Staging-Bereich am unteren Ende des Hauptbuchs, in den importierte Banktransaktionen zuerst eingefügt werden, bevor sie vollständig klassifiziert sind.

## Beancount

Das Plaintext-Buchhaltungsformat, das als Quelle der Wahrheit für das System dient.

## CSV

Eine tabellenkalkulationsähnliche Exportdatei. Die Sparkasse exportiert CSV-Dateien, die in Beancount-Transaktionen umgewandelt werden.

## Eigenkapital

Beancount-Kontofamilie, die für Eröffnungsbilanzen und die Ausgleichung historischer Ausgangspunkte verwendet wird.

## Fava

Die Browser-Oberfläche zur Anzeige und Bearbeitung von Beancount-Hauptbüchern.

## Fava Dashboards

Eine Erweiterung, die benutzerdefinierte Dashboard-Seiten zu Fava hinzufügt.

## Freies Geld

Freies oder uneingeschränktes Geld, das keinem eingeschränkten Projektbudget zugeordnet ist.

## Einnahmen

Eingegangenes Geld. In diesem System beginnen Einnahmenkonten mit `Einnahmen`.

## Hauptbuch

Die Buchhaltungsdatei, die Konten, Transaktionen, Saldenprüfungen und Dokumente enthält. Die Haupt-Hauptbücher sind `nica.beancount` und `2023.beancount`.

## Verbindlichkeit

Geld, das jemand anderem geschuldet wird. In diesem System sind Verbindlichkeiten unter `Verbindlichkeiten` aufgeführt.

## Zahlungsempfänger

Die Person oder Organisation, die in einer Transaktion genannt wird.

## Projektkonto

Ein Konto, das verwendet wird, um Geld für ein bestimmtes Projekt getrennt vom allgemeinen Vereinsgeld zu verfolgen.

## Abgleich

Der Prozess der Überprüfung, ob Beancount und der tatsächliche Bank- oder PayPal-Saldo übereinstimmen.

## Beleg

Ein Dokument, das eine Ausgabe belegt, wie z. B. eine Rechnung, ein Vertrag oder ein Kassenbeleg.

## Sonstiges

Deutsch für „verschiedenes“ oder „anderes“. Nützlich als vorübergehender Fallback, aber spezifische Kategorien sind für die endgültige Buchführung besser geeignet.

## Transaktion

Ein datierter Buchhaltungseintrag, der ein finanzielles Ereignis beschreibt.

## Verwendungsnachweis

Ein Bericht eines Projektförderers, der erklärt, wie die gewährten Mittel verwendet wurden.
