---
lang: hu
translation_id: beancount/04-beancount-basics-for-users
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Beancount alapok felhasználóknak
description: Bemutatja a Beancount szöveges formátumot és a főkönyvekben használt tranzakciós mintákat.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/04-beancount-basics-for-users.md
translation_source_body_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_source_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:35:54+00:00
translation_source_localized_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_source_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:35:54+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 04 – Beancount alapok felhasználóknak

A Beancount a könyvelést olvasható szövegként tárolja. Minden tranzakció elmondja, mi történt, milyen dátumon, kik voltak érintettek, és mely számlák változtak.

## Alapvető tranzakciós forma

```beancount
2026-01-13 ! "Tragerwerk Soziale Dienste in Sachsen-Anhalt GmbH" "RgNr. T-2504"
  Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld  680.00 EUR
  Einnahmen:Sonstiges
```

| Rész | Jelentés |
| --- | --- |
| `2026-01-13` | A tranzakció dátuma. |
| `!` | Állapotjelző. Ebben a rendszerben gyakran használják importált vagy még nem véglegesen áttekintett bejegyzések jelölésére. |
| Első idézett szöveg | Kifizető vagy feladó. |
| Második idézett szöveg | A banktól származó leírás vagy könyvelési szöveg. |
| Első számlasor | Hova ment vagy honnan érkezett a pénz. |
| Második számlasor | Az ellentétes kategória. Ha nincs összeg megadva, a Beancount automatikusan kiszámítja. |

## Számlanevek

A számlaneveket kettőspontok választják el:

```text
Vermoegen:Bank:Sparkasse-NICA:Freies-Geld
```

Balról jobbra olvasva: eszközök, banki számla, NICA Sparkasse, szabadon felhasználható alapok.

## Az öt számlacsalád

| Család | Jelentés | Példa |
| --- | --- | --- |
| `Vermoegen` | Eszközök: bank, PayPal, készpénz, készletek. | `Vermoegen:Bank:Sparkasse-NICA` |
| `Verbindlichkeiten` | Kötelezettségek: pénz, amit másoknak vagy személyeknek tartozunk. | `Verbindlichkeiten:Person:Marc-Bielert` |
| `Equity` | Nyitó egyenlegek és kiegyenlítő bejegyzések. | `Equity:Opening-Balances` |
| `Einnahmen` | Jövedelem. | `Einnahmen:Vereinsbeitrag` |
| `Ausgaben` | Költségek. | `Ausgaben:Buero:Miete` |

## Jövedelem és költség előjelek

A Beancount jelentéseiben a jövedelem gyakran negatív előjellel, a költségek pedig pozitív előjellel jelennek meg belsőleg. A Fava és a műszerfalak gyakran felhasználóbarátabb módon jelenítik meg ezeket az értékeket. Ne változtass meg tranzakciókat csak azért, mert egy jövedelmi szám negatívnak tűnik egy nyers lekérdezésben.

## Egyenlegellenőrzések

Az egyenlegellenőrzés kimondja, hogy egy számlának egy adott dátumon meghatározott egyenleggel kell rendelkeznie:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Ha a Beancount nem tudja egyeztetni ezt az egyenleget az azt megelőző tranzakciókból, a Fava hibát jelez. Az egyenlegellenőrzések a fő minőségellenőrzési mechanizmus.

## Számlák nyitása és zárása

Mielőtt egy számlát használnánk, azt meg kell nyitni:

```beancount
2025-04-01 open Ausgaben:Projekt:25-ZGV:Honorar
```

Amikor egy projekt befejeződik, és a projekt számla nullára redukálódik, az lezárható:

```beancount
2026-02-27 close Ausgaben:Projekt:TOHUCON-25
```

A lezárt számlák általában nem kaphatnak új tranzakciókat.

## Megjegyzések és dokumentumok

A `;` jellel kezdődő sorok megjegyzések. Döntéseket vagy bizonytalan helyzeteket magyaráznak el, és nem befolyásolják a számokat.

A nyugták `document` sorokkal kapcsolhatók össze:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```
