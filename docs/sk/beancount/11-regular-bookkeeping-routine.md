---
lang: sk
translation_id: beancount/11-regular-bookkeeping-routine
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Pravidelná účtovná rutina
description: Praktický opakujúci sa zoznam úloh na udržiavanie aktuálnych kníh.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/11-regular-bookkeeping-routine.md
translation_source_body_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_source_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:17+00:00
translation_source_localized_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_source_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:17+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 11 – Pravidelná účtovná rutina

Táto stránka opisuje praktickú rutinu na udržiavanie aktuálnosti účtovných kníh.

## Týždenná alebo dvojtýždenná rutina

Použite ju v prípade pravidelných bankových pohybov.

1. Otvorte správnu inštanciu Favy.
2. Skontrolujte, či Fava nehlási chyby.
3. Nájdite poslednú kontrolu zostatku.
4. Exportujte nové CSV dáta zo Sparkasse.
5. Preveďte CSV pomocou `csv2bean.py`.
6. Vlozte nové záznamy do `Bank Dump`.
7. Klasifikujte záznamy do správnych účtov.
8. Priložte alebo odkazujte príjmové doklady podľa potreby.
9. Pridajte novú kontrolu zostatku.
10. Znova načítajte Favu a odstráňte chyby.
11. Skontrolujte `Ausgaben:Sonstiges` (Výdavky:Rôzne) a `Einnahmen:Sonstiges` (Príjmy:Rôzne) na záznamy, ktoré by mali byť konkrétnejšie.

## Mesačná rutina

Na konci mesiaca:

1. Vykonajte zúčtovanie Sparkasse.
2. Vykonajte zúčtovanie PayPal, ak sa používa.
3. Vykonajte zúčtovanie pokladnice, ak sa používala hotovosť.
4. Skontrolujte otvorené záväzky voči osobám.
5. Skontrolujte zostatky aktívnych projektov.
6. Skontrolujte neklasifikované záznamy v `Sonstiges` (Rôzne).
7. Skontrolujte chýbajúce príjmové doklady.
8. Skontrolujte, či by mal byť nejaký dokončený projekt pripravený na uzatvorenie.

## Rutina projektového vykazovania

Pred prípravou projektovej správy alebo vyúčtovania (Verwendungsnachweis):

1. Otvorte stránky projektového účtu vo Fave.
2. Exportujte alebo skontrolujte všetky projektové príjmy a výdavky.
3. Potvrďte, že kategórie zodpovedajú rozpočtovým riadkom poskytovateľa financovania.
4. Potvrďte, že existujú všetky príjmové doklady a dokumenty o honorároch.
5. Skontrolujte, či sú vrátené platby, zrušenia a refundácie zaúčtované ako opravy, nie ako falošné príjmy.
6. Potvrďte, že zostatok projektového majetku je vysvetliteľný.
7. Ak je projekt dokončený, správne presuňte zostávajúce peniaze a uzatvorte projektové účty.

## Ročná rutina

Na konci roka:

1. Vykonajte zúčtovanie všetkých bankových účtov.
2. Vykonajte zúčtovanie PayPal.
3. Vykonajte zúčtovanie pokladníc.
4. Skontrolujte záväzky.
5. Skontrolujte otvorené projektové zostatky.
6. Zabezpečte, aby boli všetky príjmové doklady uložené a prepojené alebo dohľadateľné.
7. Skontrolujte kategórie príjmov a výdavkov.
8. Pridajte konečné kontroly zostatkov.
9. Pripravte správy z Favy.
10. Archivujte exportované CSV súbory a podporné dokumenty.

## Kontroly kvality

Účtovná kniha je v dobrom stave, keď:

- Fava sa otvorí bez chýb.
- Posledná kontrola zostatku Sparkasse zodpovedá banke.
- Zostatky PayPal a hotovosti sú skontrolované tam, kde je to relevantné.
- Projektové zostatky sú zámerné a vysvetliteľné.
- Uzatvorené projekty majú nulový zostatok majetku.
- Účty `Sonstiges` (Rôzne) neobsahujú zbytočné nekategorizované záznamy.
- Príjmové doklady k výdavkom sú dohľadateľné.
- Komentáre vysvetľujú neobvyklé opravy alebo predpoklady.

## Kontrolný zoznam odovzdania inej osobe

Pred odovzdaním účtovníctva niekomu inému:

- Ukážte im správny súbor účtovnej knihy pre každé združenie.
- Ukážte im, ako spustiť Favu.
- Ukážte im poslednú kontrolu zostatku.
- Ukážte im, ako sa importy CSV organizujú v `Bank Dump`.
- Ukážte im, kde sú uložené príjmové doklady.
- Ukážte im jeden príklad projektu od príjmu financovania až po konečné uzatvorenie.
- Nasmerujte ich do tohto priečinka s dokumentáciou.
