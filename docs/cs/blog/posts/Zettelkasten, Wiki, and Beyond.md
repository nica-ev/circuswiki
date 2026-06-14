---
lang: cs
translation_id: blog/posts/zettelkasten-wiki-and-beyond
created: 2025-01-21 18:09:55
update: 2025-05-03 22:54:11
date: 2025-02-25T02:14:00
publish: true
tags: 
title: Zettelkasten, Wiki a dál
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
translation_updated: 2026-06-07T18:30:38+00:00
translation_source_body_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_source_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:14+00:00
translation_source_localized_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_source_structural_metadata_hash: 954fd44b41e05f58bf1c8770aa83d64e0e9940b99ea04fb9e455b64f3667247b
---
# **Zettelkasten, Wiki a dál**  
**Proč jsem tento projekt začal, jaké jsou jeho myšlenky a kam by mohl směřovat.**

V roce 2013 jsem pracoval jako projektový manažer pro mládežnický cirkus. Trenéři se na mě často obraceli s dotazy, zda neznám jiné hry, metody nebo triky. V té době jsem měl spoustu zdrojů – knihy, časopisy, poznámky z workshopů – ale vše bylo neuspořádané a sotva digitalizované.  
<!-- more -->
Můj první pokus, jak tyto zdroje zpřístupnit trenérům, byl klasický wiki. Mnoho popisů her, které dnes vidíte, pochází z té doby. Současně jsem začal digitalizovat své zdroje. Objevil jsem metodu *Zettelkasten* (systém lístků) od Niklase Luhmanna a začal jsem svá data organizovat podle jejích principů.  

Wiki se ukázalo jako neúspěšné. Byla tam malá interakce; trenéři ho použili párkrát a rychle na něj zapomněli. Můj osobní Zettelkasten však začal růst. Ačkoli jsem zpočátku používal specializovaný software, brzy jsem začal přemýšlet, jak tuto stále cennější sbírku zajistit pro budoucnost.  

Co to znamená? První probuzení přišlo, když jsem si uvědomil, že software, který používám, se již nevyvíjí. Musel jsem najít nový software – a zjistit, jak do něj svá data migrovat. Tehdy jsem objevil Markdown.  

Markdown je jednoduchý formát souboru – v podstatě prostý textový soubor – navržený tak, aby fungoval nezávisle na jakémkoli konkrétním softwaru. Jinými slovy, je to široce přijímaný standard, který lze číst a upravovat pomocí nejzákladnějších nástrojů.  

Formát podporoval vše, co jsem potřeboval: základní formátování textu, odkazy, štítky a metadata (např. název, autor, popis atd.). Našel jsem nový software, který používal Markdown, a pokračoval jsem v budování svého Zettelkastenu. V té době jsem měl asi 600 poznámek (nebo souborů/stránek). Později jsem znovu změnil software a přechod byl bezproblémový.  

>[!info]  Klíčové poznatky
>Zajištění dat pro budoucnost znamená použití jednoduchého, široce přijímaného formátu, který je nezávislý na konkrétním softwaru.  

## Spolupráce a sdílení  

Můj první pokus s wiki nefungoval – částečně proto, že se mi nepodařilo inspirovat ostatní ke spolupráci. Během let můj osobní Zettelkasten narostl na více než 3 000 poznámek, z nichž mnohé se týkaly témat jako cirkusová pedagogika, hry, žonglování a další.  

Po nějakou dobu jsem jej jednoduše zpřístupnil online, ale kromě několika lidí, kteří o něm věděli a občas si vyhledávali popisy her, neprobíhala žádná skutečná spolupráce ani širší sdílení.  

Nyní, asi 12 let po zahájení svého Zettelkastenu, to zkouším znovu. Cílem je vytvořit sdílenou znalostní bázi pro témata jako cirkusová a pohybová pedagogika, cirkusové umění a další.  

### Klíčové aspekty a otázky  
- **Nezávislost na konkrétních systémech**  
- **Jednoduchý, snadno pochopitelný datový formát**  
- **Užitečnost a cílové publikum**  
- **Strukturovaná data**  

Tradiční wiki software (nebo platformy jako WordPress) nepřipadaly v úvahu, protože vytvářejí závislost na jednom systému. Ačkoli to může fungovat krátkodobě nebo střednědobě, z dlouhodobého hlediska je to jasná slabina.  

Místo toho spravuji data (jako soubory Markdown a obrázky) nezávisle na tom, jak jsou nakonec prezentována. To zajišťuje, že i za 20 let budou data použitelná. Způsob jejich zobrazení nebo úpravy se může drasticky změnit, ale základní data zůstanou stejná.  

Existuje nespočet způsobů, jak data prezentovat: jako webovou stránku, e-knihu, PDF nebo dokonce aplikaci. Lze je zabalit do souboru a číst nebo upravovat offline pomocí jednoduchého textového editoru. Pokud je chcete zobrazit jako webovou stránku WordPress nebo wiki, je to jen otázka importu dat – protože jsou strukturovaná a snadno čitelná, je relativně snadné je implementovat (s patřičnými znalostmi).  

## Moje současné řešení pro webové stránky  

Používám MkDocs a motiv MkDocs-Material k vygenerování statické webové stránky. Existuje mnoho programů, které vytvářejí statické HTML soubory z Markdownu, ale MkDocs je speciálně navržen pro dokumentaci. Mnoho funkcí, které generuje – jako je fulltextové vyhledávání a navigace – je neuvěřitelně užitečných.  

MkDocs je také široce používané open-source řešení podporované velkými společnostmi, což zajišťuje, že zůstane funkční alespoň ve střednědobém horizontu.  

## Spolupráce  

Dalším krokem je, aby se z toho stal společný projekt. Zkoumám způsoby, jak pozvat ostatní ke spolupráci, ať už přidáváním nového obsahu, vylepšováním stávajících záznamů nebo navrhováním zlepšení. Cílem je vytvořit živý, vyvíjející se zdroj, který těží z kolektivních znalostí a odborných znalostí.
