---
lang: sk
translation_id: beancount/07-bank-csv-import-and-reconciliation
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Import a výkaz CSV banky
description: Pracovný postup na import údajov CSV Sparkasse a výkaz bankových zostatkov.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/07-bank-csv-import-and-reconciliation.md
translation_source_body_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_source_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:05:51+00:00
translation_source_localized_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_source_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:05:51+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 07 - Import CSV z banky a párovanie

Tento pracovný postup prináša nové transakcie Sparkasse do Beancountu a potvrdzuje, že účtovný denník stále zodpovedá skutočnému bankovému účtu.

## Kde prebiehajú importy

| Združenie | Importný priečinok | Skript | Výstupný súbor |
| --- | --- | --- | --- |
| NICA | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/test` | `csv2bean.py` | `beancount_file.beancount` |
| Tohuwabohu | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/test` | `csv2bean.py` | `beancount_file.beancount` |

## Pred exportom zo Sparkasse

1. Otvorte správny súbor účtovného denníka.
2. Nájdite sekciu `Balance Checks`.
3. Nájdite najnovší dátum zostatku pre účet Sparkasse.
4. Skontrolujte tiež sekciu `Bank Dump` v spodnej časti pre dátum posledného importu.
5. Použite neskorší z týchto dátumov ako východiskový bod.

Tým sa zabráni vynechaniu transakcií alebo dvojitému importu rovnakého obdobia.

## Export zo Sparkasse

1. Otvorte prehľad účtu.
2. Filtrujte podľa rozsahu dátumov.
3. Začnite od posledného skontrolovaného alebo importovaného dátumu.
4. Ukončite dnešným dňom alebo požadovaným dátumom párovania.
5. Exportujte ako `Excel (CSV-CAMT V2)`.
6. Skopírujte stiahnutý CSV do správneho priečinka `test`.

Skripty očakávajú formát Sparkasse CSV-CAMT-V2 so stĺpcami oddelenými bodkočiarkou.

## Konverzia CSV

Otvorte terminál v správnom priečinku `test` a spustite:

```powershell
python csv2bean.py "MENO-STIAHNUTEHO-SUBORU.CSV"
```

Príklad:

```powershell
python csv2bean.py "20260312-1894137139-umsatz.CSV"
```

Ak to funguje, skript vypíše `Process finished.` a vytvorí alebo prepíše súbor `beancount_file.beancount`.

## Čo robí konvertor

Konvertor vytvára základné záznamy Beancount:

- Prichádzajúce sumy smerujú na aktívny účet Sparkasse a predvolene na `Einnahmen:Sonstiges`.
- Odchádzajúce sumy smerujú predvolene na `Ausgaben:Sonstiges` a aktívny účet Sparkasse.
- Niektoré popisy príjmov sú automaticky klasifikované ako `Einnahmen:Vereinsbeitrag`.
- Niektorý text súvisiaci s Tohuwabohu môže byť klasifikovaný ako príjmový účet projektu.

Konvertor je len prvý krok. Nevie konečný účtovný význam každej transakcie.

## Kopírovanie do hlavného denníka

1. Otvorte `test/beancount_file.beancount`.
2. Ignorujte vygenerovaný hlavičkový súbor s možnosťami.
3. Skopírujte iba transakcie.
4. Najprv ich prilepte do hlavného denníka pod `Bank Dump`.
5. V prípade potreby pridajte dátumový oddeľovač pre dátum importu.

```beancount
****************************************************************************
** 2026-01-13
****************************************************************************
```

`Bank Dump` je dočasné úložisko. Importované transakcie sa môžu neskôr presunúť do správnej tematickej alebo projektovej sekcie.

## Klasifikácia importovaných záznamov

Pre každú importovanú transakciu sa rozhodnite:

- Je na úrovni združenia alebo projektu?
- Je to príjem alebo výdavok?
- Je to preplatenie alebo splatenie záväzku?
- Patrí to k účtu `Freies-Geld` alebo k špecifickému projektovému aktívu?
- Existuje k tomu príjmový doklad alebo faktúra na pripojenie?

Nahraďte široké záložné účty, ako napríklad `Ausgaben:Sonstiges`, keď existuje presnejší účet.

## Pridanie kontroly zostatku

Príklad NICA:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Príklad Tohuwabohu:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-Tohuwabohu 2345.67 EUR
```

Použite zostatok zobrazený Sparkasse k presnému dátumu.

## Overenie vo Fava

1. Uložte súbor denníka.
2. Znovu načítajte Fava.
3. Skontrolujte chyby v hornej časti stránky Fava.
4. Otvorte stránku účtu Sparkasse.
5. Potvrďte bežný zostatok a najnovšie transakcie.
6. Skontrolujte súvahu.
7. Skontrolujte dashboardy projektov, ak boli ovplyvnené projektové účty.

## Ak kontrola zostatku zlyhá

Bežné príčiny:

- Export CSV vynechal jeden deň na začiatku alebo na konci.
- Transakcia bola importovaná dvakrát.
- Transakcia bola prilepená do nesprávneho denníka združenia.
- Číslo bolo nesprávne upravené.
- Projektové rozdelenie použilo nesprávne znamienko.
- Pohyby PayPal alebo hotovosti neboli tiež zaznamenané.

Neodstraňujte kontrolu zostatku len preto, aby chyba zmizla. Opravte základný rozdiel v transakciách.
