---
lang: sk
translation_id: beancount/04-beancount-basics-for-users
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Základy Beancount pre používateľov
description: Predstavuje textový formát Beancount a vzory transakcií používané v účtovných knihách.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/04-beancount-basics-for-users.md
translation_source_body_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_source_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:36:40+00:00
translation_source_localized_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_source_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:36:40+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 04 - Základy Beancount pre používateľov

Beancount ukladá účtovníctvo ako čitateľný text. Každá transakcia uvádza, čo sa stalo, kedy, kto bol zapojený a ktoré účty sa zmenili.

## Základný tvar transakcie

```beancount
2026-01-13 ! "Tragerwerk Soziale Dienste in Sachsen-Anhalt GmbH" "RgNr. T-2504"
  Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld  680.00 EUR
  Einnahmen:Sonstiges
```

| Časť | Význam |
| --- | --- |
| `2026-01-13` | Dátum transakcie. |
| `!` | Označenie stavu. V tomto systéme sa bežne používa pre importované alebo ešte nie definitívne skontrolované záznamy. |
| Prvý text v úvodzovkách | Príjemca alebo odosielateľ. |
| Druhý text v úvodzovkách | Popis alebo text bankového výpisu. |
| Prvý riadok účtu | Kam peniaze išli alebo odkiaľ prišli. |
| Druhý riadok účtu | Opačná kategória. Ak nie je uvedená žiadna suma, Beancount ju vypočíta automaticky. |

## Názvy účtov

Názvy účtov sú oddelené dvojbodkami:

```text
Vermoegen:Bank:Sparkasse-NICA:Freies-Geld
```

Čítajte sprava doľava: majetok, bankový účet, Sparkasse NICA, voľné prostriedky.

## Päť rodín účtov

| Rodina | Význam | Príklad |
| --- | --- | --- |
| `Vermoegen` | Majetok: banka, PayPal, hotovosť, zásoby. | `Vermoegen:Bank:Sparkasse-NICA` |
| `Verbindlichkeiten` | Záväzky: peniaze dlžné ľuďom alebo iným. | `Verbindlichkeiten:Person:Marc-Bielert` |
| `Equity` | Počiatočné zostatky a vyrovnávacie položky. | `Equity:Opening-Balances` |
| `Einnahmen` | Príjmy. | `Einnahmen:Vereinsbeitrag` |
| `Ausgaben` | Výdavky. | `Ausgaben:Buero:Miete` |

## Znamienka príjmov a výdavkov

V reportoch Beancount sa príjmy často interne zobrazujú so záporným znamienkom a výdavky s kladným znamienkom. Fava a dashboardy často prezentujú tieto hodnoty používateľsky prívetivejším spôsobom. Nemodifikujte transakcie len preto, že číslo príjmu vyzerá v surovom dopyte záporne.

## Kontroly zostatkov

Kontrola zostatku uvádza, že účet musí mať k určitému dátumu špecifický zostatok:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Ak Beancount nemôže zosúladiť tento zostatok s transakciami pred týmto dátumom, Fava zobrazí chybu. Kontroly zostatkov sú hlavným mechanizmom kontroly kvality.

## Otváranie a zatváranie účtov

Pred použitím účtu sa otvorí:

```beancount
2025-04-01 open Ausgaben:Projekt:25-ZGV:Honorar
```

Keď je projekt dokončený a projektový účet je nulový, môže byť zatvorený:

```beancount
2026-02-27 close Ausgaben:Projekt:TOHUCON-25
```

Uzavreté účty by normálne nemali prijímať nové transakcie.

## Komentáre a dokumenty

Riadky začínajúce na `;` sú komentáre. Vysvetľujú rozhodnutia alebo neisté situácie a neovplyvňujú čísla.

Príjmy je možné pripojiť pomocou riadkov `document`:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```
