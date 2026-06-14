---
lang: sk
translation_id: doc-sys-2
publish: true
tags: 
created: 2025-01-20 02:58:43
update: 2025-04-13 21:47:35
title: Systém dokumentácie
authors:
  - Marc Bielert
description:
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/doc-sys-2.md
translation_source_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T18:38:39+00:00
translation_source_body_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_source_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:47:13+00:00
translation_source_localized_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_source_structural_metadata_hash: 12f0cb572b5daceba17f262576f82a2900f2588e247dd6c9743ac6c09aba134f
---
[Manifest](doc-sys-manifest.md){ .md-button }
[Obsidian Setup](Obsidian%20Setup.md){ .md-button }
## Architektúra systému

Všeobecná myšlienka
> [!info] Prehľad architektúry
>
> Tu je grafické znázornenie architektúry systému:
>```mermaid
>flowchart LR
>A(Obsah) --> B(Správa verzií)
>C(Softvér na úpravu) --> A
>A --> D(Sprístupniť online)
>```

Podrobnejšie:

> [!info] Prehľad architektúry
>```mermaid
>flowchart LR
>A[Obsidian] <--> B{Súbory}
>B <--> C(Github Desktop)
>C <--> D{Github}
>B <--> E(MkDocs)
>D --> F(Github Pages)
>G(Téma: MkDocs-Material) --> E
>H(MkDocs-Publisher) --> E
>E --> D
>```
>
> *   **Obsidian:** Voliteľný, ale mnou odporúčaný textový editor na úpravu súborov Markdown.
> *   **Súbory:** Súbory Markdown, ktoré obsahujú obsah mojej dokumentácie.
> *   **Github Desktop:** Nástroj na jednoduchú správu mojich Git repozitárov.
> *   **Github:** Online služba na správu verzií a spoluprácu.
> *   **Github Pages:** Bezplatná služba na publikovanie mojej webovej stránky.
> *   **MkDocs:** Nástroj na automatické generovanie webovej stránky z mojich súborov Markdown.
> *   **MkDocs-Material:** Téma pre MkDocs, ktorá poskytuje moderné a atraktívne rozloženie.
> *   **MkDocs-Publisher**: Súbor pluginov, ktoré zjednodušujú spoluprácu s Obsidianom a poskytujú dodatočnú funkcionalitu.

## Komponenty podrobnejšie

### 1. Markdown

> [!info] Markdown ako základ
> Pre svoju dokumentáciu používam [formát Markdown](Markdown.md). Markdown je jednoduchý značkovací jazyk, ktorý mi umožňuje formátovať text pomocou jednoduchých značiek (napr. nadpisy, zoznamy, odkazy).

**Výhody:**

*   Ľahko sa učí a používa, čo mi umožňuje sústrediť sa na obsah.
*   Je nezávislý od platformy, takže svoju prácu môžem pokračovať na akomkoľvek zariadení.
*   Je ideálny na správu verzií, čo mi umožňuje sledovať a spravovať zmeny.
*   Je odolný voči budúcnosti a nie je proprietárny, čo mi dáva istotu, že moja práca zostane dlhodobo prístupná.

[Markdown](Markdown.md){ .md-buttons }

### 2. Obsidian

> [!info] Obsidian ako textový editor
> [Obsidian](Obsidian%20Setup.md) je voliteľný, ale mnou odporúčaný textový editor. Ponúka mi nasledujúce výhody:

*   Svoje údaje môžem ukladať lokálne a upravovať ich offline, čo mi dáva flexibilitu a kontrolu.
*   Súbory môžem ľahko prepojiť a navzájom prepojiť, čo mi pomáha organizovať zložité informácie.
*   Súbory môžem označiť značkami a ľahko ich spravovať, čo mi poskytuje ďalšiu dimenziu organizácie.
*   Svoje údaje môžem vizualizovať, čo mi pomáha rozpoznávať vzory a vzťahy.
*   Funkcionalitu Obsidianu môžem rozšíriť pomocou pluginov, čo mi umožňuje prispôsobiť si nástroj mojim špecifickým potrebám.

### 3. Git a Github

> [!info] Git na správu verzií
> [Git](https://git-scm.com/) je systém na správu verzií, ktorý mi umožňuje sledovať a spravovať zmeny v dokumentácii. [Github](https://github.com/) je online služba, ktorá mi umožňuje ukladať moje Git repozitáre a spolupracovať s ostatnými.

**Výhody:**

*   Správa verzií: Každá zmena je zdokumentovaná a dá sa kedykoľvek spätne dohľadať, čo mi pomáha predchádzať chybám a udržať si prehľad.
*   Spolupráca: Viacero ľudí môže na dokumentácii pracovať súčasne, čo mi dáva možnosť integrovať spätnú väzbu a príspevky od ostatných.
*   Zálohovanie: Moja dokumentácia je v bezpečí a pravidelne sa zálohuje, čo mi dáva istotu, že moja práca nebude stratená.

### 4. Github Desktop

> [!info] Github Desktop ako nástroj
> [Github Desktop](../_inbox/Github%20Desktop.md) je grafické rozhranie pre Git, ktoré mi umožňuje používať Git jednoducho a bez príkazového riadka.

**Výhody:**

*   Jednoduché použitie, čo mi uľahčuje používanie Gitu.
*   Nie sú potrebné žiadne znalosti príkazového riadka, čo mi šetrí čas a námahu.
*   Zjednodušuje môj pracovný postup, čo mi umožňuje sústrediť sa na tvorbu obsahu.

### 5. MkDocs

> [!info] MkDocs ako generátor webových stránok
> [MkDocs](https://mkdocs.org) je generátor statických stránok, ktorý premieňa moje súbory Markdown na statickú webovú stránku.

**Výhody:**

*   Jednoduché vytváranie webových stránok, čo mi umožňuje rýchlo a ľahko publikovať moju dokumentáciu.
*   Rýchla aktualizácia, čo mi umožňuje vidieť zmeny v reálnom čase.
*   Konzistentné rozloženie, ktoré zabezpečuje profesionálne a jednotné zobrazenie mojej dokumentácie.
*   Offline náhľad, ktorý mi umožňuje skontrolovať moju dokumentáciu pred jej publikovaním.

### 6. Github Pages

> [!info] Github Pages na hostovanie
> [Github Pages](../_inbox/Github%20Pages.md) je bezplatná hostingová služba od Githubu, ktorá mi umožňuje jednoducho publikovať moju webovú stránku online.

**Výhody:**

*   Bezplatné hostovanie, čo mi umožňuje publikovať moju dokumentáciu bez dodatočných nákladov.
*   Jednoduché publikovanie, čo mi odbremeňuje technickú realizáciu publikovania.
*   Spoľahlivé, čo mi dáva istotu, že moja dokumentácia je kedykoľvek dostupná.

### 7. MkDocs-Material

> [!info] MkDocs-Material ako téma
> [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) je téma pre MkDocs, ktorá poskytuje moderné a atraktívne rozloženie.

**Výhody:**

*   Moderný dizajn, vďaka ktorému moja dokumentácia vyzerá profesionálne a aktuálne.
*   Prispôsobiteľné, čo mi umožňuje prispôsobiť rozloženie mojim špecifickým potrebám.
*   Užívateľsky prívetivé, čo mi uľahčuje používanie dokumentácie.

### 8. MkDocs-Publisher

> [!info] MkDocs-Publisher ako kolekcia pluginov
> [MkDocs-Publisher](https://github.com/mkdocs-publisher/mkdocs-publisher) je kolekcia pluginov MkDocs, ktoré zjednodušujú spoluprácu s Obsidianom a poskytujú dodatočné funkcie.

**Výhody:**

- **Zjednodušená integrácia s Obsidianom:** Automatické prispôsobenie syntaxe Markdownu Obsidianu (Callouts, Wikilinks atď.).
- **Rozšírené metaúdaje:** Integrácia značiek a kategórií z frontmatteru Obsidianu.

## Pracovný postup

> [!info] Môj pracovný postup
> Tu je môj typický pracovný postup:

1.  Vytváram a upravujem súbory Markdown pomocou textového editora (voliteľne Obsidian).
2.  Súbory Markdown ukladám lokálne.
3.  Svoje zmeny prenášam do Git repozitára pomocou Github Desktop.
4.  Automaticky nechám vygenerovať webovú stránku pomocou MkDocs.
5.  Webovú stránku publikujem pomocou Github Pages.

## Súborový systém

> [!info] Štruktúra adresárov
> Tu je štruktúra adresárov môjho systému:
>
> ```
>/docs/     (Tu sú moje súbory Markdown)
>/site/     (Tu sa generuje webová stránka)
>license    (Informácie o licencii)
>mkdocs.yml (Konfiguračný súbor pre MkDocs)
>readme.md  (Súbor s popisom repozitára)
>```

## Alternatívy na tvorbu obsahu

> [!info] Alternatívy na tvorbu obsahu
> Som si vedomý, že nie každý je oboznámený s Markdownom a Gitom. Preto ponúkam nasledujúce alternatívy:

1.  **Wordpress:** Obsah je možné vytvoriť vo Wordpresse ako stránku.
2.  **Textový súbor, Word dokument:** Obsah je možné vytvoriť ako textový súbor, Word dokument (alebo v iných bežných formátoch).

V týchto prípadoch môžem obsah následne vložiť do systému.
