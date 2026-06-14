---
lang: sk
translation_id: translating-pdf-documents
created: 2025-05-03 21:32:10
update: 2025-05-03 22:24:12
publish: true
tags:
  - tutorial
title: Preklad PDF dokumentov pomocou veľkých jazykových modelov
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Translating PDF Documents.md
translation_source_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-14T19:34:14+00:00
translation_source_body_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_source_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T19:34:14+00:00
translation_source_localized_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_source_structural_metadata_hash: 2b0fe62dfc02049e3f55e308c77f83a911789c48b0827769d60d3f00737d38b6
---
# Tutoriál: Preklad PDF dokumentov pomocou veľkých jazykových modelov

## Úvod

Tento tutoriál načrtáva proces prekladu obsahu PDF dokumentov, najmä tých, ktoré obsahujú text založený na obrazoch, ktorý nie je možné vybrať, pomocou veľkých jazykových modelov (LLM). Pracovný postup zahŕňa optimalizáciu PDF, extrakciu textu pomocou optického rozpoznávania znakov (OCR), preklad textu a nakoniec preformátovanie prekladu do PDF.

**Predpoklady:**

*   Účet Google (na prístup k Google AI Studio).
*   Voliteľné: Softvér na optimalizáciu PDF (napr. pdf24 Creator).
*   Voliteľné: Textový editor alebo textový procesor schopný spracovať Markdown a exportovať do PDF (napr. Obsidian, Microsoft Word).

## Krok 1: Príprava PDF dokumentu

**Cieľ:** Znížiť veľkosť súboru PDF, aby sa optimalizoval na spracovanie LLM pri zachovaní čitateľnosti textu. LLM majú často obmedzenia vstupnej veľkosti a menšie súbory sa spracúvajú efektívnejšie.

**Úvahy:**

*   **PDF založené na texte:** Ak je text v PDF možné vybrať (čo znamená, že je elektronicky vložený), zmenšenie veľkosti súboru je zvyčajne jednoduchšie a možno dosiahnuť menšie veľkosti bez straty kvality.
*   **PDF založené na obrazoch:** Ak sú stránky PDF obrázkami textu (text nie je možné vybrať jednotlivo), zmenšenie veľkosti zahŕňa kompresiu obrazu. Je potrebné dbať na to, aby sa kvalita neznížila natoľko, že text bude pre OCR nečitateľný.

**Postup (Príklad pomocou pdf24):**

1.  Otvorte svoj PDF dokument v nástroji, ako je pdf24 Creator ([https://www.pdf24.org/](https://www.pdf24.org/)).
2.  Využite funkcie kompresie alebo zmenšenia veľkosti. Bežné efektívne nastavenia zahŕňajú:
    *   Povolenie webovej optimalizácie.
    *   Konverzia farieb na odtiene sivej.
3.  Experimentujte s úrovňami kompresie, pričom cieľom je veľkosť súboru pod **5 MB**, pričom sa zabezpečí, že text zostane jasný a čitateľný.
4.  Uložte optimalizovaný PDF súbor.

## Krok 2: Extrakcia textu pomocou Google AI Studio (Prepis/OCR)

**Cieľ:** Využiť multimodálne schopnosti LLM na vykonanie OCR na pripravenom PDF a extrahovanie textového obsahu v štruktúrovanom formáte.

**Postup:**

1.  Prejdite na **Google AI Studio** ([https://aistudio.google.com/](https://aistudio.google.com/)) a prihláste sa pomocou svojho účtu Google. Poznámka: AI Studio je primárne nástroj na experimentovanie s modelmi a promptami.
2.  Spustite novú reláciu alebo konverzáciu.
3.  Pripojte optimalizovaný PDF súbor k svojej relácii (napr. pomocou tlačidla prílohy alebo pretiahnutím).
4.  Do oblasti používateľskej správy zadajte nasledujúci prompt:
    ```
    Prosím, prepíš priložené PDF. Obsahuje obrázky s textom, ktorý vyžaduje OCR. Výstup prepisu poskytnite v správnom formáte Markdown, pričom použite hlavičky a zoznamy na vytvorenie štruktúry, ktorá čo najviac zodpovedá rozloženiu pôvodného dokumentu.
    ```
5.  Nakonfigurujte nastavenia modelu:
    *   Ponechajte predvolené nastavenia, pokiaľ nemáte špecifické požiadavky.
    *   Nastavte **Teplotu** na **0,1**. Nižšia teplota podporuje deterministickejší a menej kreatívny výstup, čo je vhodné pre presný prepis.
6.  Odošlite prompt. Proces prepisu môže trvať niekoľko minút (potenciálne 4-6 minút alebo dlhšie, v závislosti od veľkosti a zložitosti PDF).
7.  Po dokončení generovania skopírujte výsledný text vo formáte Markdown.
    *   *Metóda 1:* Použite možnosť kopírovania, ktorá je často k dispozícii v rozhraní (napr. prostredníctvom ponuky spojenej s odpoveďou).
    *   *Metóda 2:* Manuálne vyberte všetok vygenerovaný text a skopírujte ho (Ctrl+C alebo kliknite pravým tlačidlom myši -> Kopírovať).
8.  Skopírovaný text vo formáte Markdown prilepte do jednoduchého textového editora (ako Poznámkový blok, VS Code, Obsidian atď.).
9.  Uložte tento obsah ako súbor s čistým textom. Odporúča sa použiť prípony `.txt` alebo `.md` (Markdown). Formátovanie Markdown pomáha zachovať štruktúru dokumentu (hlavičky, zoznamy).

![Google AI Studio - Snímka obrazovky prepisu](../img/Screenshot-Google-AiStudio-Transcription.png){ width=600 }

## Krok 3: Preklad extrahovaného textu pomocou Google AI Studio

**Cieľ:** Preložiť extrahovaný text vo formáte Markdown do požadovaného cieľového jazyka pri zachovaní pôvodnej štruktúry a formátovania.

**Postup:**

1.  V **Google AI Studio** spustite **novú konverzáciu**, aby ste zabezpečili čerstvý kontext pre úlohu prekladu.
2.  Pripojte uložený súbor `.txt` alebo `.md` obsahujúci extrahovaný text vo formáte Markdown.
3.  Zadajte prekladový prompt, špecifikujte zdrojový a cieľový jazyk. Príklad pre angličtinu do taliančiny:
    ```
    Prosím, preložte priložený súbor Markdown (angličtina) do taliančiny. Presne zachovajte pôvodnú štruktúru, formátovanie, tón a štýl reči.
    ```
    *   **Upravte prompt** podľa vašich špecifických zdrojových a cieľových jazykov (napr. "...preložte priložený súbor Markdown (nemčina) do španielčiny..."). Kvalita prekladu sa môže líšiť v závislosti od jazykového páru.
4.  Nakonfigurujte nastavenia modelu:
    *   Uistite sa, že predvolené nastavenia sú vhodné.
    *   Nastavte **Teplotu** na **0,1**, aby ste podporili vernosť zdrojovému textu a štruktúre počas prekladu.
5.  Odošlite prompt. Preklad môže tiež trvať niekoľko minút, porovnateľne s časom prepisu.
6.  Po vygenerovaní skopírujte preložený text vo formáte Markdown pomocou metód opísaných v Kroku 2 (tlačidlo kopírovania v rozhraní alebo manuálny výber).

![Google AI Studio - Snímka obrazovky prekladu](../img/Screenshot-Google-AiStudio-Translation.png){ width=600 }

## Krok 4: Preformátovanie preloženého textu do PDF dokumentu

**Cieľ:** Konvertovať preložený text vo formáte Markdown späť do PDF dokumentu na zdieľanie alebo archiváciu.

**Postup:**

1.  Preložený text vo formáte Markdown skopírujte a prilepte do vhodnej aplikácie.
2.  **Odporúčané:** Použite textový editor alebo textový procesor, ktorý rozumie formátovaniu Markdown, aby ste zachovali štruktúru (hlavičky, zoznamy atď.).
    *   **Obsidian** ([https://obsidian.md/](https://obsidian.md/)) je bezplatný nástroj, ktorý dobre funguje so súbormi Markdown a často má možnosti exportu do PDF (priamo alebo prostredníctvom doplnkov).
    *   Moderné textové procesory (ako Microsoft Word) môžu tiež importovať alebo prilepovať Markdown a umožňovať ukladanie/exportovanie ako PDF, hoci vernosť formátovania sa môže líšiť.
    *   Špecializované konvertory Markdown do PDF sú tiež k dispozícii online alebo ako inštalovateľný softvér.
3.  Použite funkciu "Exportovať do PDF" alebo "Uložiť ako PDF" aplikácie.
4.  Skontrolujte výsledné PDF, aby ste sa uistili, že formátovanie a obsah zodpovedajú očakávaniam.

## Záver

Tento tutoriál demonštroval pracovný postup na využitie Google AI Studio na prepis a preklad PDF dokumentov, vrátane tých, ktoré vyžadujú OCR. Prípravou PDF, extrakciou textu pomocou nakonfigurovaného LLM, prekladom výsledku a jeho preformátovaním môžu používatelia získať preložené verzie svojich dokumentov. Hoci táto metóda ponúka bezplatné alebo nízkonákladové riešenie, používatelia by mali brať do úvahy potenciálne rozdiely v presnosti OCR a kvalite prekladu, najmä pri zložitých rozloženiach alebo menej bežných jazykoch. Časy spracovania výrazne závisia od veľkosti dokumentu a zaťaženia servera.
