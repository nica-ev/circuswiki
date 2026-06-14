---
lang: sk
translation_id: blog/posts/games-the-data-side
created: 2025-01-21 18:09:55
update: 2026-06-09 17:06:42
date: 2025-03-18T02:14:00
publish: true
tags: 
title: Hry - Dátová stránka
description: Ako boli popisy hier štandardizované a dynamickejšie pomocou metadát a pluginov Obsidian.
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Games - The Data Side.md
translation_source_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:01:27+00:00
translation_source_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:40:59+00:00
translation_source_body_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_source_localized_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_source_structural_metadata_hash: 6d067079ae1d1598e9306f517260d15351df3045ab315112fd921ab0e185903b
---
# **Hry – Dátová stránka**
**Ako boli popisy hier štandardizované a dynamickejšie vďaka metadátam a pluginom Obsidianu.**

Pokiaľ ide o správu obsahu, kľúčová je konzistencia. Pre prvú hlavnú časť tohto projektu som sa pustil do hier – približne 170 z nich, každá s vlastným jedinečným formátom, štýlom a prístupnosťou. Problém? Mnohé z týchto popisov sa spoliehali na pevne zakódované, statické odkazy, čo sťažovalo pridávanie nových hier alebo úpravu štruktúry.

Tak som si vyhrnul rukávy a pustil sa do práce.
<!-- more -->
## Krok 1: Jednotný formát
Prvou úlohou bolo stanoviť jednotný formát pre všetky popisy hier. Inšpiráciu som čerpal z „Tasifan Spielebuch“ (Kniha hier Tasifan), dobre organizovaného zdroja popisov hier. Aby boli veci ešte užívateľsky prívetivejšie, pridal som krátke zhrnutia, aby boli všetky podstatné detaily viditeľné na prvý pohľad – dokonca aj v náhľade.

Ale skutočnou zmenou hry? Metadáta.

## Krok 2: Kúzlo metadát
Teraz sú všetky kľúčové informácie – veľkosť skupiny, materiály, trvanie a ďalšie – uložené ako metadáta v hornej časti každého súboru Markdown vo formáte nazývanom YAML (alebo frontmatter). To nielen udržuje veci organizované, ale tiež umožňuje opätovné použitie dát v celom systéme.

Aby bolo vyhľadávanie správnej hry jednoduchšie, implementoval som jednoduchú, ale účinnú logiku:
1. **Vyberte kategóriu**: Aký typ hry hľadáte? Hru na upokojenie? Hru na naháňanie? Niečo na budovanie tímu? Na začiatok som vytvoril súbor kategórií, ale tieto sa dajú podľa potreby upraviť alebo rozšíriť.
2. **Prezrite si tabuľku**: Keď si vyberiete kategóriu, zobrazí sa vám tabuľka so všetkými hrami, ktoré zodpovedajú. Tabuľka je zoraditeľná – stačí kliknúť na hlavičky, aby ste ju usporiadali podľa trvania, obtiažnosti alebo iných kritérií.

A tu je to najlepšie: mnohé hry sa objavujú vo viacerých kategóriách, takže nikdy nie ste obmedzený len na jeden spôsob vyhľadávania toho, čo potrebujete.

## Nie celkom dynamické tabuľky
Skutočné kúzlo sa deje s dvoma pluginmi Obsidianu: **Dataview** a **Dataview Serializer**.

Dataview mi umožňuje vytvárať dynamické zoznamy a tabuľky pomocou dotazov podobných databázam. Háčik? Tieto tabuľky fungujú iba v rámci Obsidianu, pretože podkladové súbory Markdown sa nemenia.

Vstupuje Dataview Serializer. Tento plugin konvertuje tieto dynamické tabuľky do statického formátu Markdown a zapisuje ich priamo do súboru. Keď sa stránka zostavuje pomocou MkDocs, tabuľky sú statické, ale boli v podstate dynamicky generované offline.

Tieto dotazy môžu byť dosť zložité, čo mi umožňuje vyhľadávať alebo zobrazovať konkrétne časti wiki – ako sú všetky popisy hier alebo články napísané konkrétnym autorom. A pretože sa automaticky aktualizujú (prostredníctvom kroku serializácie), pridávanie nových informácií a budovanie navigovateľnej štruktúry je hračka.

Ale nie je to všetko len slnko a dúha. Proces nie je plne automatický. Dataview Serializer môže prepísať súbor iba vtedy, ak je otvorený v Obsidian. Zatiaľ je to zvládnuteľné – označil som každú stránku dynamickou tabuľkou alebo zoznamom, čo uľahčuje ich prechádzanie. Ale ak počet týchto stránok výrazne narastie, možno budem musieť prehodnotiť prístup.

## Nástroje a jazykové modely
Pôvodné popisy hier boli zmiešaninou z hľadiska formátovania a kvality. Na zefektívnenie procesu som sa obrátil na jazykové modely (LLM). Vytvoril som špecifický prompt, doplnený o príklady formátovania, aby som zabezpečil, že samotný obsah nebude zmenený (žiadne zbytočné prepisovanie). Napriek tomu som každú výsledok manuálne skontroloval a v prípade potreby vykonal malé úpravy.

Tu je záver: pri správnom použití sú tieto nástroje *neuveriteľne* výkonné. Kľúčom je byť presný a zámerný v tom, ako formulujete svoje úlohy.

Konečné zmeny sa týkajú hlavne formátovania – ako sú prezentované informácie a popisy hier. Metadáta však boli všetky zadané manuálne. Keďže som aj tak musel všetko dvakrát skontrolovať, v tomto prípade bolo ručné vykonanie rýchlejšie.

Je to však pomalý proces. Pracujem na tom popri práci a zvládam asi 10-15 hier denne. Pokrok je stály, ale bude to chvíľu trvať.

## Výzvy vpred
Jednou z potenciálnych prekážok sú preklady. Vyhľadávacie dotazy by bolo potrebné prispôsobiť na vyhľadávanie jazykovo špecifických verzií hier alebo značiek. Zatiaľ sa to dá zvládnuť manuálne, ale ak systém narastie, môže byť potrebná automatizácia.

Preklad je zložitá téma a podrobnejšie sa jej budem venovať inokedy.

## Prečo sa s tým trápiť?
Krátka odpoveď? Škálovateľnosť.

Tento systém je navrhnutý tak, aby rástol. Štandardizáciou formátu, využitím metadát a použitím dynamických nástrojov som vytvoril základ, ktorý zvládne viac obsahu bez toho, aby sa stal neovládateľným.

## Čo je ešte nové?
Funkcia vyhľadávania dostala niekoľko vylepšení:
- **Automatické dopĺňanie**: Keď píšete, vyhľadávanie navrhuje dotazy, ktoré poskytujú najviac výsledkov. Toto nie je založené na správaní používateľa – nesledujeme vyhľadávania – ale na statickom vyhľadávacom indexe generovanom pri zostavovaní stránky.
- **Uložené vyhľadávania**: Kliknite na malú ikonu vedľa vyhľadávacieho poľa a váš dotaz (a výsledky) sa uložia do URL. Uložte si ju do záložiek a vždy dostanete rovnaké výsledky.

Je to malá funkcia, ale môže sa stať neuveriteľne užitočnou, keď wiki rastie a pokrýva rozmanitejšie témy.
