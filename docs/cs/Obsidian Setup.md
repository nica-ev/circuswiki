---
lang: cs
translation_id: obsidian-setup
publish: true
tags: 
title: Nastavení Obsidianu
created: 2025-01-23 01:38:52
update: 2026-06-06 21:43:04
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Obsidian Setup.md
translation_source_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T19:07:07+00:00
translation_source_body_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_source_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:14:24+00:00
translation_source_localized_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_source_structural_metadata_hash: 6eec0b8a6b7772bab240bcedda44bfa18061f6163b3b9475217ace91bcc065ea
---
Obsidian je extrémně přizpůsobitelný, což může být pro nováčky problém.
Poskytujeme základní nastavení, které lze použít tak, jak je, včetně pluginů a motivů, a také jejich jemně doladěná nastavení.
Jedná se o základní nastavení, které lze dále upravit podle osobních preferencí každého.
Poskytujeme pouze funkční řešení – které zde zdokumentujeme a vysvětlíme.

## Použité termíny
**Trezor (Vault)** – kolekce markdown souborů a obrázků, které tvoří znalostní bázi

## Pluginy

- Advanced Canvas
- BRAT
- Better Wordcount
- Clear Unused Images
- Dataview
- Dataview Serializer
- Emoji Toolbar
- Linter
- Note Toolbar
- Tag Wrangler
- Templater
- Beautitab
- Omnisearch
- Status Bar Organizer
- Workspaces Plus
- Sortable

### Advanced Canvas
Poskytuje přístup k mnoha novým funkcím a možnostem stylizace pro Canvas.

### BRAT
Potřebný k instalaci neoficiálních pluginů / pluginů, které nejsou registrovány v ekosystému Obsidianu, konkrétně:
- Dataview Serializer
- Sortable

### Better Word Count
Používá se hlavně pro svou schopnost zobrazit počet slov/znaků v označeném textu.
Je viditelný ve stavovém řádku.

### Beautitab
Čistě kosmetický, poskytuje přizpůsobitelnou stránku "prázdného nového panelu".

### Clear unused Images
Jak název napovídá, pomáhá s organizací trezoru identifikací nepoužívaných obrázků.

❗Vyloučil jsem podsložku ```/site/```, aby se ne vždy mazaly obrázky z vytvořené webové stránky (což není problém, spíše nepříjemnost).

❗Buďte opatrní při používání příkazu pro vymazání příloh – ten vždy smaže ```mkdocs.yml``` a ```license.``` --> pokud se to stane, soubory jsou ve složce .trash a lze je obnovit. Ale je snadné to přehlédnout.

### Dataview
Umožňuje dotazy podobné SQL na trezoru.

### Dataview Serializer
Převádí výsledky Dataview na markdown.
Pomáhá s opětovným použitím výsledků dotazů Dataview v samotných poznámkách.

### Emoji Toolbar
No, poskytuje snadný přístup k emotikonům.
**Klávesová zkratka nastavena na: ALT-E**
😍

### Linter
Čistí markdown soubory a data frontmatter.
Pomáhá udržovat konzistentní formu.

### Note Toolbar
Umožňuje přizpůsobitelné panely nástrojů v horní části poznámky, které lze definovat na úrovni složky/souboru.

### Tag Wrangler
Poskytuje další možnosti pro práci se značkami.
- přejmenování značek
Pomáhá s organizací trezoru.

### Templater
Umožňuje přizpůsobitelné šablony, které lze vložit ručně nebo na základě podmínek (např. při vytváření poznámky).

### Status Bar Organizer
Umožňuje skrýt položky ze stavového řádku.

### Sortable
Umožňuje řazení tabulek (jak markdown, tak dataview tabulek) kliknutím na jejich záhlaví.

### Workspaces Plus
Umožňuje snadné rychlé přepínání ze stavového řádku.

## Souborový systém trezoru

[Souborový systém trezoru](Vault%20File%20System.md){ .md-button }
