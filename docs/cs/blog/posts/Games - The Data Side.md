---
lang: cs
translation_id: blog/posts/games-the-data-side
created: 2025-01-21 18:09:55
update: 2026-06-09 17:06:42
date: 2025-03-18T02:14:00
publish: true
tags: 
title: Hry – Datová strana
description: Jak byly popisy her standardizovány a zefektivněny pomocí metadat a pluginů Obsidian.
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Games - The Data Side.md
translation_source_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:01:19+00:00
translation_source_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:40:58+00:00
translation_source_body_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_source_localized_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_source_structural_metadata_hash: 6d067079ae1d1598e9306f517260d15351df3045ab315112fd921ab0e185903b
---
# **Hry – Datová stránka**
**Jak byly popisy her standardizovány a zefektivněny pomocí metadat a pluginů Obsidianu.**

Pokud jde o správu obsahu, klíčová je konzistence. Pro první velkou část tohoto projektu jsem se pustil do her – asi 170 z nich, každá s vlastním jedinečným formátem, stylem a přístupností. Problém? Mnoho z těchto popisů spoléhalo na pevně zakódované, statické odkazy, což ztěžovalo přidávání nových her nebo úpravu struktury.

Tak jsem si vyhrnul rukávy a pustil se do práce.
<!-- more -->
## Krok 1: Sjednocený formát
Prvním úkolem bylo stanovit jednotný formát pro všechny popisy her. Inspiraci jsem čerpal z „Tasifan Spielebuch“ (Kniha her Tasifan), dobře uspořádaného zdroje popisů her. Aby byly věci ještě uživatelsky přívětivější, přidal jsem krátká shrnutí, takže všechny podstatné detaily jsou viditelné na první pohled – i v náhledu.

Ale skutečná změna hry? Metadata.

## Krok 2: Kouzlo metadat
Nyní jsou všechny klíčové informace – velikost skupiny, materiály, doba trvání a další – uloženy jako metadata v horní části každého souboru Markdown ve formátu nazývaném YAML (nebo frontmatter). To nejen udržuje věci uspořádané, ale také umožňuje opakované použití dat v celém systému.

Aby bylo snazší najít tu správnou hru, implementoval jsem jednoduchou, ale účinnou logiku:
1. **Vyberte kategorii**: Jaký typ hry hledáte? Hru na zklidnění? Hru na honičku? Něco pro budování týmu? Vytvořil jsem sadu kategorií pro začátek, ale tyto lze podle potřeby upravit nebo rozšířit.
2. **Prohlédněte si tabulku**: Jakmile si vyberete kategorii, zobrazí se tabulka se všemi hrami, které do ní spadají. Tabulka je řaditelná – stačí kliknout na záhlaví a uspořádat podle délky trvání, obtížnosti nebo jiných kritérií.

A tady je to nejlepší: mnoho her se objevuje ve více kategoriích, takže nikdy nejste omezeni pouze na jeden způsob, jak najít to, co potřebujete.

## Ne úplně dynamické tabulky
Skutečné kouzlo se odehrává se dvěma pluginy Obsidianu: **Dataview** a **Dataview Serializer**.

Dataview mi umožňuje vytvářet dynamické seznamy a tabulky pomocí dotazů podobných databázím. Háček? Tyto tabulky fungují pouze v Obsidianu, protože podkladové soubory Markdown nejsou upravovány.

Vstupuje Dataview Serializer. Tento plugin převádí tyto dynamické tabulky do statického formátu Markdown a zapisuje je přímo do souboru. Když je web sestaven pomocí MkDocs, tabulky jsou statické, ale byly v podstatě generovány dynamicky offline.

Tyto dotazy mohou být poměrně složité a umožňují mi vyhledávat nebo zobrazovat konkrétní části wiki – jako jsou všechny popisy her nebo články napsané konkrétním autorem. A protože se automaticky aktualizují (prostřednictvím kroku serializace), přidávání nových informací a budování navigovatelné struktury je hračka.

Ale není to všechno slunce a duha. Proces není plně automatický. Dataview Serializer může přepsat soubor pouze v případě, že je otevřen v Obsidianu. Prozatím je to zvládnutelné – označil jsem každou stránku dynamickou tabulkou nebo seznamem, což usnadňuje jejich procházení. Ale pokud se počet těchto stránek výrazně zvýší, možná budu muset přehodnotit přístup.

## Nástroje a jazykové modely
Původní popisy her byly směsicí z hlediska formátování a kvality. Abych zjednodušil proces, obrátil jsem se na jazykové modely (LLM). Vytvořil jsem specifický prompt, doplněný o příklady formátování, abych zajistil, že samotný obsah nebude změněn (žádné zbytečné přepisování). Přesto jsem každý výsledek ručně zkontroloval a provedl drobné úpravy tam, kde to bylo nutné.

Zde je ponaučení: při správném použití jsou tyto nástroje *neuvěřitelně* mocné. Klíčem je být přesný a záměrný v tom, jak formulujete své úkoly.

Finální změny se týkají především formátování – jak jsou informace a popisy her prezentovány. Metadata však byla zadána ručně. Jelikož jsem stejně musel vše dvakrát zkontrolovat, ruční provedení bylo v tomto případě rychlejší.

Je to však pomalý proces. Při práci na částečný úvazek zvládnu asi 10–15 her denně. Pokrok je stálý, ale bude to chvíli trvat.

## Výzvy před námi
Jednou z možných překážek jsou překlady. Vyhledávací dotazy by musely být upraveny tak, aby našly jazykově specifické verze her nebo značek. Prozatím to lze řešit ručně, ale pokud se systém rozšíří, může být nutná automatizace.

Překlad je složité téma a budu se mu věnovat podrobněji jindy.

## Proč se namáhat?
Krátká odpověď? Škálovatelnost.

Tento systém je navržen tak, aby rostl. Standardizací formátu, využitím metadat a použitím dynamických nástrojů jsem vytvořil základ, který zvládne více obsahu, aniž by se stal neohrabaným.

## Co je ještě nového?
Funkce vyhledávání dostala několik vylepšení:
- **Automatické doplňování**: Při psaní vyhledávání navrhuje dotazy, které vracejí nejvíce výsledků. To není založeno na chování uživatelů – nesledujeme vyhledávání – ale na statickém vyhledávacím indexu vygenerovaném při sestavování webu.
- **Uložená vyhledávání**: Kliknutím na malou ikonu vedle vyhledávacího pole se váš dotaz (a výsledky) uloží do adresy URL. Uložte si ji do záložek a pokaždé získáte stejné výsledky.

Je to malá funkce, ale může se stát neuvěřitelně užitečnou, jak se wiki rozrůstá a pokrývá rozmanitější témata.
