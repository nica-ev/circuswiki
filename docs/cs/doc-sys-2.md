---
lang: cs
translation_id: doc-sys-2
publish: true
tags: 
created: 2025-01-20 02:58:43
update: 2025-04-13 21:47:35
title: Dokumentační systém
authors:
  - Marc Bielert
description:
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/doc-sys-2.md
translation_source_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T18:38:32+00:00
translation_source_body_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_source_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:47:12+00:00
translation_source_localized_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_source_structural_metadata_hash: 12f0cb572b5daceba17f262576f82a2900f2588e247dd6c9743ac6c09aba134f
---
[Manifest](doc-sys-manifest.md){ .md-button }
[Obsidian Setup](Obsidian%20Setup.md){ .md-button }
## Architektura systému

Obecná myšlenka

> [!info] Přehled architektury
>
> Zde je grafické znázornění architektury systému:
>```mermaid
>flowchart LR
>A(Obsah) --> B(Správa verzí)
>C(Editační software) --> A
>A --> D(Zpřístupnění online)
>```

Podrobněji:

> [!info] Přehled architektury
>```mermaid
>flowchart LR
>A[Obsidian] <--> B{Soubory}
>B <--> C(Github Desktop)
>C <--> D{Github}
>B <--> E(MkDocs)
>D --> F(Github Pages)
>G(Theme: MkDocs-Material) --> E
>H(MkDocs-Publisher) --> E
>E --> D
>```
>
> *   **Obsidian:** Volitelný, ale mnou doporučený textový editor pro úpravu souborů Markdown.
> *   **Soubory:** Soubory Markdown obsahující obsah mé dokumentace.
> *   **Github Desktop:** Nástroj pro snadnou správu mých Git repozitářů.
> *   **Github:** Online služba pro správu verzí a spolupráci.
> *   **Github Pages:** Bezplatná služba pro publikování mé webové stránky.
> *   **MkDocs:** Nástroj pro automatické generování webové stránky z mých souborů Markdown.
> *   **MkDocs-Material:** Téma pro MkDocs, které poskytuje moderní a atraktivní rozložení.
> *   **MkDocs-Publisher:** Kolekce pluginů, které usnadňují spolupráci s Obsidianem a poskytují další funkce.

## Komponenty podrobně

### 1. Markdown

> [!info] Markdown jako základ
> Pro svou dokumentaci používám [formát Markdown](Markdown.md). Markdown je jednoduchý značkovací jazyk, který mi umožňuje formátovat text pomocí jednoduchých značek (např. nadpisy, seznamy, odkazy).

**Výhody:**

*   Snadno se učí a používá, což mi umožňuje soustředit se na obsah.
*   Je nezávislý na platformě, takže mohu svou práci pokračovat na jakémkoli zařízení.
*   Je ideální pro správu verzí, což mi umožňuje sledovat a spravovat změny.
*   Je dlouhodobě udržitelný a není proprietární, což mi dává jistotu, že má práce zůstane dlouhodobě přístupná.

[Markdown](Markdown.md){ .md-buttons }

### 2. Obsidian

> [!info] Obsidian jako textový editor
> [Obsidian](Obsidian%20Setup.md) je volitelný, ale mnou doporučený textový editor. Nabízí mi následující výhody:

*   Mohu svá data ukládat lokálně a upravovat je offline, což mi dává flexibilitu a kontrolu.
*   Mohu snadno propojovat soubory a vytvářet mezi nimi vazby, což mi pomáhá organizovat složité informace.
*   Mohu soubory označovat štítky a snadno je spravovat, což mi poskytuje další rozměr organizace.
*   Mohu svá data vizualizovat, což mi pomáhá rozpoznávat vzorce a vztahy.
*   Mohu rozšířit funkčnost Obsidianu pomocí pluginů, což mi umožňuje přizpůsobit nástroj svým specifickým potřebám.

### 3. Git a Github

> [!info] Git pro správu verzí
> [Git](https://git-scm.com/) je systém pro správu verzí, který mi umožňuje sledovat a spravovat změny v dokumentaci. [Github](https://github.com/) je online služba, která mi umožňuje ukládat mé Git repozitáře a spolupracovat s ostatními.

**Výhody:**

*   Správa verzí: Každá změna je zdokumentována a lze ji kdykoli zpětně dohledat, což mi pomáhá předcházet chybám a udržovat si přehled.
*   Spolupráce: Více lidí může na dokumentaci pracovat současně, což mi umožňuje integrovat zpětnou vazbu a příspěvky od ostatních.
*   Záloha: Moje dokumentace je v bezpečí a je pravidelně zálohována, což mi dává jistotu, že má práce nebude ztracena.

### 4. Github Desktop

> [!info] Github Desktop jako nástroj
> [Github Desktop](../_inbox/Github%20Desktop.md) je grafické rozhraní pro Git, které mi umožňuje snadno používat Git bez příkazového řádku.

**Výhody:**

*   Snadné použití, což mi usnadňuje práci s Gitem.
*   Není nutná znalost příkazového řádku, což mi šetří čas a úsilí.
*   Zjednodušuje můj pracovní postup, což mi umožňuje soustředit se na tvorbu obsahu.

### 5. MkDocs

> [!info] MkDocs jako generátor webových stránek
> [MkDocs](https://mkdocs.org) je generátor statických stránek, který převádí mé soubory Markdown do statické webové stránky.

**Výhody:**

*   Snadné vytváření webových stránek, což mi umožňuje rychle a snadno publikovat svou dokumentaci.
*   Rychlá aktualizace, což mi umožňuje vidět změny v reálném čase.
*   Konzistentní rozložení, které zajišťuje profesionální a jednotný vzhled mé dokumentace.
*   Offline náhled, který mi umožňuje zkontrolovat svou dokumentaci před jejím publikováním.

### 6. Github Pages

> [!info] Github Pages pro hosting
> [Github Pages](../_inbox/Github%20Pages.md) je bezplatná hostingová služba od Githubu, která mi umožňuje snadno publikovat svou webovou stránku online.

**Výhody:**

*   Bezplatný hosting, což mi umožňuje publikovat svou dokumentaci bez dalších nákladů.
*   Snadné publikování, což mi odstraňuje technické provedení publikování.
*   Spolehlivost, což mi dává jistotu, že má dokumentace je kdykoli dostupná.

### 7. MkDocs-Material

> [!info] MkDocs-Material jako téma
> [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) je téma pro MkDocs, které nabízí moderní a atraktivní rozložení.

**Výhody:**

*   Moderní design, díky kterému má dokumentace vypadá profesionálně a aktuálně.
*   Přizpůsobitelnost, což mi umožňuje přizpůsobit rozložení svým specifickým potřebám.
*   Uživatelská přívětivost, což mi usnadňuje používání dokumentace.

### 8. MkDocs-Publisher

> [!info] MkDocs-Publisher jako kolekce pluginů
> [MkDocs-Publisher](https://github.com/mkdocs-publisher/mkdocs-publisher) je kolekce pluginů pro MkDocs, které zjednodušují spolupráci s Obsidianem a nabízejí další funkce.

**Výhody:**

*   **Zjednodušená integrace s Obsidianem:** Automatické přizpůsobení syntaxe Markdown v Obsidianu (Callouts, Wikilinks atd.).
*   **Rozšířená metadata:** Integrace štítků a kategorií z frontmatteru Obsidianu.

## Pracovní postup

> [!info] Můj pracovní postup
> Zde je můj typický pracovní postup:

1.  Vytvářím a upravuji soubory Markdown pomocí textového editoru (volitelně Obsidian).
2.  Soubory Markdown ukládám lokálně.
3.  Přenesu své změny do Git repozitáře pomocí Github Desktop.
4.  Automaticky nechám vygenerovat webovou stránku pomocí MkDocs.
5.  Publikuji webovou stránku pomocí Github Pages.

## Souborový systém

> [!info] Struktura adresářů
> Zde je struktura adresářů mého systému:
>
> ```
>/docs/     (Zde jsou mé soubory Markdown)
>/site/     (Zde se generuje webová stránka)
>license    (Informace o licenci)
>mkdocs.yml (Konfigurační soubor pro MkDocs)
>readme.md  (Soubor s popisem repozitáře)
>```

## Alternativy pro tvorbu obsahu

> [!info] Alternativy pro tvorbu obsahu
> Jsem si vědom, že ne každý je obeznámen s Markdownem a Gitem. Proto nabízím následující alternativy:

1.  **Wordpress:** Obsah lze vytvořit ve Wordpresu jako stránku.
2.  **Textový soubor, Word soubor:** Obsah lze vytvořit jako textový soubor, Word soubor (nebo v jiných běžných formátech).

V těchto případech mohu obsah následně do systému začlenit.
