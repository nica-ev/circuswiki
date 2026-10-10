---
lang: cs
translation_id: beancount/11-regular-bookkeeping-routine
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Běžná účetní rutina
description: Praktický opakující se seznam úkolů pro udržování aktuálních účetních knih.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/11-regular-bookkeeping-routine.md
translation_source_body_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_source_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:12+00:00
translation_source_localized_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_source_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:12+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 11 – Pravidelná rutina účetnictví

Tato stránka popisuje praktickou rutinu pro udržování aktuálnosti účetních knih.

## Týdenní nebo čtrnáctidenní rutina

Použijte tuto rutinu, pokud dochází k pravidelným pohybům na bankovních účtech.

1. Otevřete příslušnou instanci Favy.
2. Zkontrolujte, zda Fava nehlásí chyby.
3. Najděte poslední kontrolu zůstatku.
4. Exportujte nová data CSV ze Sparkasse.
5. Převeďte CSV pomocí `csv2bean.py`.
6. Vložte nové položky do `Bank Dump`.
7. Klasifikujte položky do správných účtů.
8. Připojte nebo odkažte na účtenky, kde je to nutné.
9. Přidejte novou kontrolu zůstatku.
10. Znovu načtěte Favu a vyřešte chyby.
11. Zkontrolujte `Ausgaben:Sonstiges` (Výdaje:Různé) a `Einnahmen:Sonstiges` (Příjmy:Různé) a upravte položky, které by měly být specifičtější.

## Měsíční rutina

Na konci měsíce:

1. Proveďte odsouhlasení účtu Sparkasse.
2. Proveďte odsouhlasení PayPal, pokud je používán.
3. Proveďte odsouhlasení pokladny, pokud byla použita hotovost.
4. Zkontrolujte otevřené závazky vůči osobám.
5. Zkontrolujte zůstatky aktivních projektů.
6. Zkontrolujte neklasifikované položky v `Sonstiges` (Různé).
7. Zkontrolujte chybějící účtenky.
8. Zkontrolujte, zda by měl být některý dokončený projekt připraven k uzavření.

## Rutina pro projektové vykazování

Před přípravou projektové zprávy nebo vyúčtování (Verwendungsnachweis):

1. Otevřete stránky projektového účtu ve Favě.
2. Exportujte nebo zkontrolujte veškeré příjmy a výdaje projektu.
3. Potvrďte, že kategorie odpovídají rozpočtovým položkám poskytovatele financí.
4. Potvrďte, že existují všechny účtenky a dokumenty o honorářích.
5. Zkontrolujte, zda jsou vrácené platby, zrušení a proplacení zaúčtovány jako opravy, nikoli jako falešné příjmy.
6. Potvrďte, že zůstatek aktiv projektu je vysvětlitelný.
7. Pokud je projekt dokončen, správně převeďte zbývající peníze a uzavřete projektové účty.

## Roční rutina

Na konci roku:

1. Proveďte odsouhlasení všech bankovních účtů.
2. Proveďte odsouhlasení PayPal.
3. Proveďte odsouhlasení pokladen.
4. Zkontrolujte závazky.
5. Zkontrolujte otevřené zůstatky projektů.
6. Zajistěte, aby byly všechny účtenky uloženy a propojeny nebo dohledatelné.
7. Zkontrolujte kategorie příjmů a výdajů.
8. Přidejte konečné kontroly zůstatků.
9. Připravte zprávy z Favy.
10. Archivujte exportované CSV soubory a podpůrné dokumenty.

## Kontroly kvality

Účetní kniha je v dobrém stavu, pokud:

- Fava se otevře bez chyb.
- Poslední kontrola zůstatku ze Sparkasse odpovídá stavu na bankovním účtu.
- Jsou kontrolovány zůstatky PayPal a hotovosti, kde je to relevantní.
- Zůstatky projektů jsou záměrné a vysvětlitelné.
- Uzavřené projekty mají nulový zůstatek aktiv.
- Účty `Sonstiges` (Různé) neobsahují zbytečné nezařazené položky.
- Lze nalézt účtenky k výdajům.
- Komentáře vysvětlují neobvyklé opravy nebo předpoklady.

## Kontrolní seznam pro předání jiné osobě

Před předáním účetnictví jiné osobě:

- Ukažte jí správný soubor účetní knihy pro každé sdružení.
- Ukažte jí, jak spustit Favu.
- Ukažte jí poslední kontrolu zůstatku.
- Ukažte jí, jak jsou importy CSV připravovány v `Bank Dump`.
- Ukažte jí, kde jsou uloženy účtenky.
- Ukažte jí jeden příklad projektu od příjmu financování až po konečné uzavření.
- Odkazujte ji na tuto složku s dokumentací.
