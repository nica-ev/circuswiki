---
lang: cs
translation_id: translating-pdf-documents
created: 2025-05-03 21:32:10
update: 2025-05-03 22:24:12
publish: true
tags:
  - tutorial
title: Překlad PDF dokumentů pomocí velkých jazykových modelů
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Translating PDF Documents.md
translation_source_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-14T19:34:06+00:00
translation_source_body_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_source_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T19:34:06+00:00
translation_source_localized_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_source_structural_metadata_hash: 2b0fe62dfc02049e3f55e308c77f83a911789c48b0827769d60d3f00737d38b6
---
# Návod: Překlad PDF dokumentů pomocí velkých jazykových modelů

## Úvod

Tento návod popisuje postup pro překlad obsahu PDF dokumentů, zejména těch, které obsahují text založený na obrázcích a nelze jej vybírat, pomocí velkých jazykových modelů (LLM). Pracovní postup zahrnuje optimalizaci PDF, extrakci textu pomocí optického rozpoznávání znaků (OCR), překlad textu a nakonec přeformátování překladu do PDF.

**Předpoklady:**

*   Účet Google (pro přístup do Google AI Studia).
*   Volitelné: Software pro optimalizaci PDF (např. pdf24 Creator).
*   Volitelné: Textový editor nebo procesor schopný zpracovat Markdown a exportovat do PDF (např. Obsidian, Microsoft Word).

## Krok 1: Příprava PDF dokumentu

**Cíl:** Snížit velikost souboru PDF pro optimalizaci zpracování LLM při zachování čitelnosti textu. LLM mají často omezení vstupní velikosti a menší soubory se zpracovávají efektivněji.

**Důležité aspekty:**

*   **PDF založené na textu:** Pokud lze text v PDF vybírat (tj. je elektronicky vložen), snížení velikosti souboru je obvykle snazší a lze dosáhnout menších velikostí bez ztráty kvality.
*   **PDF založené na obrázcích:** Pokud jsou stránky PDF obrázky textu (text nelze vybírat jednotlivě), snížení velikosti zahrnuje kompresi obrazu. Je třeba dbát na to, aby se kvalita nesnížila natolik, že se text stane pro OCR nečitelným.

**Postup (příklad s pdf24):**

1.  Otevřete svůj PDF dokument v nástroji, jako je pdf24 Creator ([https://www.pdf24.org/](https://www.pdf24.org/)).
2.  Využijte funkce komprese nebo snížení velikosti. Běžná efektivní nastavení zahrnují:
    *   Povolení optimalizace pro web.
    *   Převod barev do odstínů šedi.
3.  Experimentujte s úrovněmi komprese a snažte se dosáhnout velikosti souboru pod **5 MB**, přičemž zajistěte, aby text zůstal jasný a čitelný.
4.  Uložte optimalizovaný soubor PDF.

## Krok 2: Extrakce textu pomocí Google AI Studia (Přepis/OCR)

**Cíl:** Využít multimodální schopnosti LLM k provedení OCR na připraveném PDF a extrakci textového obsahu ve strukturovaném formátu.

**Postup:**

1.  Přejděte do **Google AI Studia** ([https://aistudio.google.com/](https://aistudio.google.com/)) a přihlaste se pomocí svého účtu Google. Poznámka: AI Studio je primárně nástroj pro experimentování s modely a prompty.
2.  Spusťte novou relaci nebo chat.
3.  Připojte optimalizovaný soubor PDF k relaci (např. pomocí tlačítka pro přílohu nebo přetažením).
4.  Do pole pro zprávu uživatele zadejte následující prompt:
    ```
    Prosím, přepište přiložené PDF. Obsahuje obrázky s textem, což vyžaduje OCR. Výstup přepisu proveďte ve správném formátu Markdown, s využitím nadpisů a seznamů k vytvoření struktury, která co nejvěrněji napodobuje rozložení původního dokumentu.
    ```
5.  Nakonfigurujte nastavení modelu:
    *   Ponechte výchozí nastavení, pokud nemáte specifické požadavky.
    *   Nastavte **Teplotu** na **0.1**. Nižší teplota podporuje determinističtější a méně kreativní výstup, což je vhodné pro přesný přepis.
6.  Odešlete prompt. Proces přepisu může trvat několik minut (potenciálně 4–6 minut nebo déle, v závislosti na velikosti a složitosti PDF).
7.  Po dokončení generování zkopírujte výsledný text ve formátu Markdown.
    *   *Metoda 1:* Použijte možnost kopírování, která je často k dispozici v rozhraní (např. prostřednictvím nabídky spojené s odpovědí).
    *   *Metoda 2:* Ručně vyberte veškerý vygenerovaný text a zkopírujte jej (Ctrl+C nebo pravé kliknutí -> Kopírovat).
8.  Zkopírovaný text ve formátu Markdown vložte do jednoduchého textového editoru (jako Poznámkový blok, VS Code, Obsidian atd.).
9.  Uložte tento obsah jako prostý textový soubor. Doporučuje se použít přípony `.txt` nebo `.md` (Markdown). Formátování Markdown pomáhá zachovat strukturu dokumentu (nadpisy, seznamy).

![Google AI Studio - Snímek obrazovky Přepis](../img/Screenshot-Google-AiStudio-Transcription.png){ width=600 }

## Krok 3: Překlad extrahovaného textu pomocí Google AI Studia

**Cíl:** Přeložit extrahovaný text ve formátu Markdown do požadovaného cílového jazyka při zachování původní struktury a formátování.

**Postup:**

1.  V **Google AI Studiu** spusťte **nový chat**, abyste zajistili čistý kontext pro úlohu překladu.
2.  Připojte uložený soubor `.txt` nebo `.md` obsahující extrahovaný text ve formátu Markdown.
3.  Zadejte překladový prompt, specifikující zdrojový a cílový jazyk. Příklad pro angličtinu do italštiny:
    ```
    Prosím, přeložte přiložený soubor Markdown (angličtina) do italštiny. Zachovejte přesně původní strukturu, formátování, tón a styl řeči.
    ```
    *   **Upravte prompt** podle vašich specifických zdrojových a cílových jazyků (např. „...přeložte přiložený soubor Markdown (němčina) do španělštiny...“). Kvalita překladu se může lišit v závislosti na jazykovém páru.
4.  Nakonfigurujte nastavení modelu:
    *   Ujistěte se, že výchozí nastavení jsou vhodná.
    *   Nastavte **Teplotu** na **0.1**, abyste podpořili věrnost zdrojovému textu a struktuře během překladu.
5.  Odešlete prompt. Překlad může také trvat několik minut, srovnatelně s časem přepisu.
6.  Po vygenerování zkopírujte přeložený text ve formátu Markdown pomocí metod popsaných v Kroku 2 (tlačítko pro kopírování v rozhraní nebo ruční výběr).

![Google AI Studio - Snímek obrazovky Překlad](../img/Screenshot-Google-AiStudio-Translation.png){ width=600 }

## Krok 4: Přeformátování přeloženého textu do PDF dokumentu

**Cíl:** Převést zkopírovaný přeložený text ve formátu Markdown zpět do PDF dokumentu pro sdílení nebo archivaci.

**Postup:**

1.  Zkopírovaný přeložený text ve formátu Markdown vložte do vhodného softwaru.
2.  **Doporučeno:** Použijte textový editor nebo procesor dokumentů, který rozumí formátování Markdown, abyste zachovali strukturu (nadpisy, seznamy atd.).
    *   **Obsidian** ([https://obsidian.md/](https://obsidian.md/)) je bezplatný nástroj, který dobře funguje se soubory Markdown a často má možnosti exportu do PDF (přímo nebo prostřednictvím pluginů).
    *   Moderní procesory dokumentů (jako Microsoft Word) mohou také importovat nebo vkládat Markdown a umožňují ukládat/exportovat jako PDF, ačkoli věrnost formátování se může lišit.
    *   Specializované převodníky Markdown na PDF jsou také k dispozici online nebo jako instalovatelný software.
3.  Použijte funkci aplikace „Exportovat do PDF“ nebo „Uložit jako PDF“.
4.  Zkontrolujte výsledné PDF, abyste se ujistili, že formátování a obsah odpovídají očekávání.

## Závěr

Tento návod demonstroval pracovní postup pro využití Google AI Studia k přepisu a překladu PDF dokumentů, včetně těch, které vyžadují OCR. Přípravou PDF, extrakcí textu pomocí nakonfigurovaného LLM, překladem výsledku a jeho přeformátováním mohou uživatelé získat přeložené verze svých dokumentů. Ačkoli tato metoda nabízí bezplatné nebo nízkonákladové řešení, uživatelé by měli mít na paměti potenciální rozdíly v přesnosti OCR a kvalitě překladu, zejména u složitých rozložení nebo méně běžných jazyků. Doba zpracování významně závisí na velikosti dokumentu a zatížení serveru.
