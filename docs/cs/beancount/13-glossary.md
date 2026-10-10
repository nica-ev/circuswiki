---
lang: cs
translation_id: beancount/13-glossary
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Slovníček
description: Definice účetních, Beancount, Fava a projektových účetních termínů použitých v této dokumentaci.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/13-glossary.md
translation_source_body_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_source_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:21+00:00
translation_source_localized_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_source_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:21+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 13 – Slovníček pojmů

## Účet

Pojmenované místo, kde Beancount zaznamenává peníze nebo hodnotu. Příklad: `Ausgaben:Buero:Miete`.

## Aktivum

Něco, co sdružení vlastní nebo kontroluje, jako jsou peníze na bankovním účtu, zůstatek na PayPal, hotovost nebo zásoby. V tomto systému jsou aktiva pod účty `Vermoegen`.

## Kontrola zůstatku

Řádek, který potvrzuje, že účet má k určitému datu konkrétní zůstatek. Kontroly zůstatku slouží k ověření, že účetní kniha odpovídá záznamům banky, PayPalu nebo hotovosti.

## Bankovní výpis (Bank Dump)

Průchozí sekce v dolní části účetní knihy, kam se nejprve vloží importované bankovní transakce, než jsou plně zařazeny.

## Beancount

Formát účetnictví v prostém textu, který slouží jako zdroj pravdy pro systém.

## CSV

Exportovaný soubor podobný tabulce. Sparkasse exportuje soubory CSV, které se převádějí na transakce Beancount.

## Vlastní kapitál (Equity)

Rodina účtů Beancount používaná pro počáteční stavy a vyrovnání historických výchozích bodů.

## Fava

Rozhraní prohlížeče pro prohlížení a práci s účetními knihami Beancount.

## Fava Dashboards

Rozšíření, které přidává vlastní stránky s přehledy do Favě.

## Freies-Geld (Volné peníze)

Volné nebo neomezené peníze, které nejsou přiděleny omezenému projektovému rozpočtu.

## Příjem

Přijaté peníze. V tomto systému účty příjmů začínají na `Einnahmen`.

## Účetní kniha (Ledger)

Účetní soubor obsahující účty, transakce, kontroly zůstatků a dokumenty. Hlavními účetními knihami jsou `nica.beancount` a `2023.beancount`.

## Závazek (Liability)

Peníze dlužné někomu jinému. V tomto systému jsou závazky pod účty `Verbindlichkeiten`.

## Příjemce platby (Payee)

Osoba nebo organizace uvedená v transakci.

## Projektový účet

Účet používaný ke sledování peněz pro konkrétní projekt odděleně od obecných peněz sdružení.

## Rekonciliace (Smíření)

Proces kontroly, zda Beancount a skutečný zůstatek na bankovním účtu nebo PayPalu odpovídají.

## Potvrzení o platbě (Receipt)

Dokument prokazující výdaj, jako je faktura, smlouva nebo účtenka.

## Sonstiges (Různé)

Německy „různé“ nebo „ostatní“. Užitečné jako dočasné řešení, ale pro konečné účetnictví jsou lepší konkrétní kategorie.

## Transakce

Datovaný účetní záznam popisující jednu finanční událost.

## Verwendungsnachweis (Doklad o použití prostředků)

Zpráva pro poskytovatele projektu vysvětlující, jak byly poskytnuté peníze použity.
