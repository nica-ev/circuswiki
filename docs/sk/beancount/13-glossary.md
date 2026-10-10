---
lang: sk
translation_id: beancount/13-glossary
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Slovník
description: Definície účtovných, Beancount, Fava a projektových účtovných pojmov použitých v tejto dokumentácii.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/13-glossary.md
translation_source_body_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_source_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:24+00:00
translation_source_localized_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_source_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:24+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 13 – Slovník

## Účet

Názov miesta, kde Beancount zaznamenáva peniaze alebo hodnotu. Príklad: `Výdavky:Kancelária:Nájomné`.

## Aktíva

Niečo, čo združenie vlastní alebo kontroluje, napríklad peniaze na bankovom účte, zostatok na PayPal, hotovosť alebo zásoby. V tomto systéme sú aktíva pod položkou `Vermoegen` (Majetok).

## Kontrola zostatku

Riadok, ktorý potvrdzuje, že účet má na konkrétny dátum konkrétny zostatok. Kontroly zostatku sa používajú na overenie, či účtovná kniha zodpovedá záznamom banky, PayPalu alebo hotovosti.

## Bankový výpis (Bank Dump)

Prípravná sekcia v spodnej časti účtovnej knihy, kam sa najprv vkladajú importované bankové transakcie pred ich úplným zaradením.

## Beancount

Formát účtovníctva v čistom texte používaný ako zdroj pravdy systému.

## CSV

Exportovaný súbor podobný tabuľke. Sparkasse exportuje CSV súbory, ktoré sa prevádzajú na Beancount transakcie.

## Vlastný kapitál (Equity)

Rodina účtov v Beancount používaná pre otváracie zostatky a vyrovnanie historických východiskových bodov.

## Fava

Rozhranie prehliadača na prezeranie a prácu s Beancount účtovnými knihami.

## Fava Dashboards

Rozšírenie, ktoré pridáva vlastné stránky s prehľadmi do Favy.

## Freies-Geld (Voľné peniaze)

Voľné alebo neobmedzené peniaze, ktoré nie sú pridelené na rozpočet obmedzeného projektu.

## Príjem

Prijaté peniaze. V tomto systéme účty príjmov začínajú na `Einnahmen` (Príjmy).

## Účtovná kniha (Ledger)

Účtovný súbor obsahujúci účty, transakcie, kontroly zostatkov a dokumenty. Hlavné účtovné knihy sú `nica.beancount` a `2023.beancount`.

## Pasíva (Liability)

Peniaze dlžné niekomu inému. V tomto systéme sú pasíva pod položkou `Verbindlichkeiten` (Záväzky).

## Príjemca platby (Payee)

Osoba alebo organizácia uvedená v transakcii.

## Projektový účet

Účet používaný na sledovanie peňazí pre konkrétny projekt oddelene od všeobecných peňazí združenia.

## Zúčtovanie (Reconciliation)

Proces kontroly, či sa Beancount a skutočný bankový alebo PayPal zostatok zhodujú.

## Potvrdenie o platbe (Receipt)

Doklad preukazujúci výdavok, ako je faktúra, zmluva alebo potvrdenie o platbe v hotovosti.

## Sonstiges (Rôzne)

Nemčina pre „rôzne“ alebo „iné“. Užitočné ako dočasné riešenie, ale konkrétne kategórie sú pre konečné účtovníctvo lepšie.

## Transakcia

Dátumovaný účtovný záznam opisujúci jednu finančnú udalosť.

## Verwendungsnachweis (Doklad o použití prostriedkov)

Správa pre poskytovateľa projektu vysvetľujúca, ako boli pridelené peniaze použité.
