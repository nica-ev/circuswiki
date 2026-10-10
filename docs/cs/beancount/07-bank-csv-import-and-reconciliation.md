---
lang: cs
translation_id: beancount/07-bank-csv-import-and-reconciliation
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Import a výpořet bankovních CSV
description: Pracovní postup pro import dat CSV ze Sparkasse a vyrovnání bankovních zůstatků.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/07-bank-csv-import-and-reconciliation.md
translation_source_body_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_source_hash: 7dd13868d2b7a7d5a8d26bde46c89e3e3f14edfd6d202ae3eb18dc793e3bc9f4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:05:45+00:00
translation_source_localized_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_source_metadata_hash: 3a464794d1427ecf69a508497b69a8933ba1084ec0747ba2a04cd409ce50284f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:05:45+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 07 - Import CSV z banky a párování

Tento pracovní postup přináší nové transakce ze Sparkasse do Beancountu a potvrzuje, že účetní kniha stále odpovídá skutečnému bankovnímu účtu.

## Kde probíhají importy

| Sdružení | Importní složka | Skript | Výstupní soubor |
| --- | --- | --- | --- |
| NICA | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/test` | `csv2bean.py` | `beancount_file.beancount` |
| Tohuwabohu | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/test` | `csv2bean.py` | `beancount_file.beancount` |

## Před exportem ze Sparkasse

1. Otevřete správný soubor účetní knihy.
2. Najděte sekci `Balance Checks`.
3. Najděte nejnovější datum zůstatku pro účet Sparkasse.
4. Zkontrolujte také sekci `Bank Dump` ve spodní části pro datum posledního importu.
5. Použijte pozdější z těchto dat jako výchozí bod.

Tím se předejde vynechání transakcí nebo dvojímu importu stejného období.

## Export ze Sparkasse

1. Otevřete přehled účtu.
2. Filtrujte podle rozsahu dat.
3. Začněte od posledního zkontrolovaného nebo importovaného data.
4. Ukončete dneškem nebo požadovaným datem párování.
5. Exportujte jako `Excel (CSV-CAMT V2)`.
6. Zkopírujte stažený CSV soubor do správné složky `test`.

Skripty očekávají formát Sparkasse CSV-CAMT-V2 se sloupci oddělenými středníkem.

## Konverze CSV

Otevřete terminál ve správné složce `test` a spusťte:

```powershell
python csv2bean.py "NAZEV-STAZENEHO-SOUBORU.CSV"
```

Příklad:

```powershell
python csv2bean.py "20260312-1894137139-umsatz.CSV"
```

Pokud to funguje, skript vypíše `Process finished.` a vytvoří nebo přepíše soubor `beancount_file.beancount`.

## Co konvertor dělá

Konvertor vytváří základní záznamy Beancount:

- Příchozí částky jdou na účet aktiv Sparkasse a ve výchozím nastavení na `Einnahmen:Sonstiges`.
- Odchozí částky jdou ve výchozím nastavení na `Ausgaben:Sonstiges` a na účet aktiv Sparkasse.
- Některé popisy příjmů jsou automaticky klasifikovány jako `Einnahmen:Vereinsbeitrag`.
- Některý text související s Tohuwabohu může být klasifikován jako projektový účet příjmů.

Konvertor je pouze první průchod. Neví konečný účetní význam každé transakce.

## Kopírování do hlavní účetní knihy

1. Otevřete `test/beancount_file.beancount`.
2. Ignorujte vygenerovaný hlavičkový soubor s možnostmi.
3. Zkopírujte pouze transakce.
4. Vložte je nejprve do hlavní účetní knihy pod `Bank Dump`.
5. V případě potřeby přidejte oddělovač s datem pro datum importu.

```beancount
****************************************************************************
** 2026-01-13
****************************************************************************
```

`Bank Dump` je přechodná oblast. Importované transakce lze později přesunout do správné tematické nebo projektové sekce.

## Klasifikace importovaných záznamů

Pro každou importovanou transakci rozhodněte:

- Je na úrovni sdružení nebo projektu?
- Jedná se o příjem nebo výdaj?
- Jedná se o vrácení peněz nebo splátku závazku?
- Patří do `Freies-Geld` nebo na projektový specifický účet aktiv?
- Existuje k tomu potvrzení nebo faktura k přiložení?

Nahraďte obecné záložní účty, jako je `Ausgaben:Sonstiges`, pokud existuje přesnější účet.

## Přidání kontroly zůstatku

Příklad NICA:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Příklad Tohuwabohu:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-Tohuwabohu 2345.67 EUR
```

Použijte zůstatek zobrazený Sparkasse k přesnému datu.

## Ověření ve Favě

1. Uložte soubor účetní knihy.
2. Znovu načtěte Favau.
3. Zkontrolujte chyby v horní části stránky Favy.
4. Otevřete stránku účtu Sparkasse.
5. Potvrďte průběžný zůstatek a nejnovější transakce.
6. Zkontrolujte rozvahu.
7. Zkontrolujte projektové dashboardy, pokud byly ovlivněny projektové účty.

## Pokud kontrola zůstatku selže

Běžné příčiny:

- CSV export vynechal jeden den na začátku nebo na konci.
- Transakce byla importována dvakrát.
- Transakce byla vložena do nesprávné účetní knihy sdružení.
- Číslo bylo nesprávně upraveno.
- Projektový split použil nesprávné znaménko.
- Pohyby PayPal nebo hotovosti nebyly také zaznamenány.

Neodstraňujte kontrolu zůstatku jen proto, abyste odstranili chybu. Opravte základní rozdíl v transakcích.
