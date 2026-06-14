---
lang: sk
translation_id: blog/posts/zettelkasten-wiki-and-beyond
created: 2025-01-21 18:09:55
update: 2025-05-03 22:54:11
date: 2025-02-25T02:14:00
publish: true
tags: 
title: Zettelkasten, Wiki a ďalej
description: 
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Zettelkasten, Wiki, and Beyond.md
translation_source_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T18:30:44+00:00
translation_source_body_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_source_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:15+00:00
translation_source_localized_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_source_structural_metadata_hash: 954fd44b41e05f58bf1c8770aa83d64e0e9940b99ea04fb9e455b64f3667247b
---
# **Zettelkasten, Wiki a ešte ďalej**
**Prečo som začal tento projekt, aké sú jeho myšlienky a kam by mohol viesť.**

V roku 2013 som pracoval ako projektový manažér pre mládežnícky cirkus. Tréneri sa ma často pýtali, či nepoznám iné hry, metódy alebo triky. V tom čase som mal množstvo zdrojov – kníh, časopisov, poznámok z workshopov – ale všetko bolo neusporiadané a sotva digitalizované.
<!-- more -->
Môj prvý pokus o sprístupnenie týchto zdrojov trénerom bol klasický wiki. Mnohé z popisov hier, ktoré dnes vidíte, pochádzajú z toho obdobia. Súčasne som začal digitalizovať svoje zdroje. Objavil som metódu *Zettelkasten* (kartotéka) od Niklasa Luhmanna a začal som svoje dáta organizovať podľa jej princípov.

Wiki bolo neúspešné. Bola tam malá interakcia; tréneri ho použili párkrát a rýchlo naň zabudli. Moja osobná Zettelkastenová zbierka však začala rásť. Hoci som spočiatku používal špecializovaný softvér, čoskoro som začal premýšľať, ako túto čoraz cennejšiu zbierku zabezpečiť do budúcnosti.

Čo to znamená? Prvé prebudenie prišlo, keď som si uvedomil, že softvér, ktorý som používal, sa už nevyvíja. Musel som nájsť nový softvér – a zistiť, ako doň migrovať svoje dáta. Vtedy som objavil Markdown.

Markdown je jednoduchý formát súboru – v podstate obyčajný textový súbor – navrhnutý tak, aby fungoval nezávisle od akéhokoľvek konkrétneho softvéru. Inými slovami, je to široko prijatý štandard, ktorý sa dá čítať a upravovať pomocou najzákladnejších nástrojov.

Formát podporoval všetko, čo som potreboval: základné formátovanie textu, odkazy, značky a metadata (napr. názov, autor, popis atď.). Našiel som nový softvér, ktorý používal Markdown, a pokračoval som v budovaní svojej Zettelkastenovej zbierky. V tom čase som mal asi 600 poznámok (alebo súborov/stránok). Neskôr som opäť zmenil softvér a prechod bol bezproblémový.

>[!info] Kľúčové poznanie
>Zabezpečenie vašich dát do budúcnosti znamená používanie jednoduchého, široko prijatého formátu, ktorý je nezávislý od konkrétneho softvéru.

## Spolupráca a zdieľanie

Môj prvý pokus s wiki nefungoval – čiastočne preto, že sa mi nepodarilo inšpirovať ostatných, aby prispievali. Počas rokov moja osobná Zettelkastenová zbierka narástla na viac ako 3 000 poznámok, mnohé z nich na témy ako cirkusová pedagogika, hry, žonglovanie a ďalšie.

Istý čas som ju jednoducho sprístupnil online, ale okrem pár ľudí, ktorí o nej vedeli a občas si vyhľadali opisy hier, nebola žiadna skutočná spolupráca ani širšie zdieľanie.

Teraz, asi 12 rokov po začatí svojej Zettelkastenovej zbierky, to skúšam znova. Cieľom je vytvoriť zdieľanú znalostnú bázu pre témy ako cirkusová a pohybová pedagogika, cirkusové umenie a ďalej.

### Kľúčové úvahy a otázky
- **Nezávislosť od konkrétnych systémov**
- **Jednoduchý, ľahko zrozumiteľný formát dát**
- **Použiteľnosť a cieľová skupina**
- **Štruktúrované dáta**

Tradičný wiki softvér (alebo platformy ako WordPress) boli vylúčené, pretože vytvárajú závislosť od jedného systému. Hoci to môže fungovať v krátkodobom alebo strednodobom horizonte, z dlhodobého hľadiska je to jasná slabina.

Namiesto toho spravujem dáta (ako súbory Markdown a obrázky) nezávisle od toho, ako sú nakoniec prezentované. To zaisťuje, že aj o 20 rokov budú dáta použiteľné. Spôsob, akým sa zobrazujú alebo upravujú, sa môže drasticky zmeniť, ale základné dáta zostanú rovnaké.

Existuje nespočetné množstvo spôsobov, ako dáta prezentovať: ako webovú stránku, e-knihu, PDF alebo dokonca aplikáciu. Môže sa zabaliť do súboru a čítať alebo upravovať offline pomocou jednoduchého textového editora. Ak ju chcete zobraziť ako webovú stránku WordPress alebo wiki, je to len otázka importu dát – keďže sú štruktúrované a ľahko čitateľné, je relatívne jednoduché ich implementovať (s potrebnými znalosťami).

## Moje súčasné riešenie pre webovú stránku

Používam MkDocs a tému MkDocs-Material na generovanie statickej webovej stránky. Existuje mnoho programov, ktoré vytvárajú statické HTML súbory z Markdownu, ale MkDocs je špeciálne navrhnutý pre dokumentáciu. Mnoho funkcií, ktoré generuje – ako je vyhľadávanie v celom texte a navigácia – je neuveriteľne užitočných.

MkDocs je tiež široko používané open-source riešenie podporované veľkými spoločnosťami, čo zaisťuje, že zostane funkčné aspoň v strednodobom horizonte.

## Spolupráca

Ďalším krokom je urobiť z toho spoločné úsilie. Skúmam spôsoby, ako pozvať ostatných, aby prispeli, či už pridaním nového obsahu, vylepšením existujúcich záznamov alebo navrhnutím zlepšení. Cieľom je vytvoriť živý, vyvíjajúci sa zdroj, ktorý ťaží z kolektívnych vedomostí a odborných znalostí.
