---
lang: de
translation_id: beancount/08-projects-and-restricted-funds
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Projekte und zweckgebundene Mittel
description: Erklärt, wie Projektgelder und zweckgebundene Mittel dargestellt und geprüft werden.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/08-projects-and-restricted-funds.md
translation_source_body_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_source_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T15:13:57+00:00
translation_source_localized_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_source_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T15:13:57+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 08 - Projekte und zweckgebundene Gelder

Projekte sind zentral für dieses Buchhaltungssystem. Viele Zuschüsse und Aktivitäten müssen getrennt vom Geld der freien Vereinigung verbucht werden.

## Was ein Projekt im Buchungssystem bedeutet

| Kontotyp | Beispiel | Zweck |
| --- | --- | --- |
| Projektvermögen | `Vermoegen:Bank:Sparkasse-NICA:25-ZGV` | Interner Saldo von Projektgeldern. |
| Projekterträge | `Einnahmen:Projekt:25-ZGV:Sachmittel` | Projektfinanzierung oder Projekterträge. |
| Projektausgaben | `Ausgaben:Projekt:25-ZGV:Sachmittel` | Projektausgaben. |

Das eigentliche Bankkonto kann ein Sparkassenkonto sein, aber das Buchungssystem trennt interne Projektbudgets, damit das Team sehen kann, was zu jedem Projekt gehört.

## Aktive und abgeschlossene Projekte

Aktive Projekte haben offene Konten und relevante Salden. Abgeschlossene Projekte haben normalerweise eine abschließende Saldenprüfung von `0,00 EUR` und `close`-Anweisungen für die Projektvermögens-, Ertrags- und Ausgabenkonten.

Buchen Sie keine neuen Transaktionen in abgeschlossene Projekte, es sei denn, Sie eröffnen sie absichtlich neu oder korrigieren historische Daten.

## Aktuelle Beispiele bei NICA

- `26-JEP-Buehnenreif`
- `25-ZGV`
- `25-CircusWiki`
- `25-Machen-UnitedAges`
- `25-Erasmus`
- abgeschlossene Projekte von 2024 wie `24-AWO`, `24-HONY`, `24-Peter`

## Aktuelle Beispiele bei Tohuwabohu

- `VHS-TOHU-25`
- `ZMS-TOHU-25`
- `CEDU-25`
- `TOHUCON-25`
- abgeschlossene Projekte wie `Revierpionier-25`, `OAC-25`, `TohuCon2024`, `ZGV-TOHU-24`, `TohuCon2023`

## Ein neues Projekt erstellen

Ein neues Projekt erfordert normalerweise die Eröffnung von Konten, bevor Transaktionen eingegeben werden.

```beancount
2026-01-01 open Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject:Honorar
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sachmittel
2026-01-01 open Ausgaben:Projekt:26-NewProject:Aufwand
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sonstiges
2026-01-01 open Einnahmen:Projekt:26-NewProject
2026-01-01 open Einnahmen:Projekt:26-NewProject:Honorar
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sachmittel
2026-01-01 open Einnahmen:Projekt:26-NewProject:Aufwand
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sonstiges
```

Eröffnen Sie nur Kategorien, die für das Projekt tatsächlich nützlich sind.

## Projektfinanzierung buchen

```beancount
2026-02-01 ! "Fördergeber" "Erste Zahlung NewProject"
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject  3000.00 EUR
  Einnahmen:Projekt:26-NewProject:Sachmittel
```

## Projektausgaben buchen

```beancount
2026-02-10 ! "Lieferant" "Projektmaterial"
  Ausgaben:Projekt:26-NewProject:Sachmittel  250.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject
```

## Projektbudgets verstehen

Ein positiver Projektvermögenssaldo bedeutet, dass dem Projekt noch Geld zugewiesen ist. Ein Projektvermögenssaldo von Null bedeutet, dass das Projekt kein verbleibendes internes Bankguthaben hat. Ein negativer Projektvermögenssaldo bedeutet normalerweise, dass das Projekt mehr ausgegeben hat, als ihm zugewiesen wurde, oder dass eine Zuweisung fehlt.

## Ein Projekt abschließen

Bevor ein Projekt abgeschlossen wird, müssen alle Einnahmen und Ausgaben erfasst, Belege auffindbar sein, das Projektvermögenskonto muss exakt Null betragen und verbleibendes Geld muss korrekt verschoben oder zurückgegeben werden.

```beancount
2026-12-31 balance Vermoegen:Bank:Sparkasse-NICA:26-NewProject 0.00 EUR
2026-12-31 close Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-12-31 close Ausgaben:Projekt:26-NewProject
2026-12-31 close Einnahmen:Projekt:26-NewProject
```

Schließen Sie auch Unterkonten, wenn diese separat eröffnet wurden.
