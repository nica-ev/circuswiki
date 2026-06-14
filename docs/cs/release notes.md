---
lang: cs
translation_id: release-notes
created: 2025-01-21 18:09:55
update: 2026-06-10 03:32:50
publish: true
tags: 
title: Poznámky k vydání
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/release notes.md
translation_source_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:14:19+00:00
translation_source_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:17:05+00:00
translation_source_body_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_source_localized_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_source_structural_metadata_hash: 48054209deb2d49a5f3283cd38424c2fba59ca058c0dd085323a92f8ef336177
---
>[!info]
>Tyto poznámky k vydání poskytují pouze hrubý přehled, drobné změny (jako jsou jednotlivé nové stránky, úpravy stávajícího obsahu) nejsou všechny uvedeny. Tyto lze však přesně sledovat v historii repozitáře.

>[!info]- **Verze:** v0.04 - **Datum vydání**: 9. června 2026
>**Obsah**
>- Výrazně rozšířen vícejazyčný obsah: obsah je nyní strukturován pod `docs/<jazyk>`.
>- Přidány nové a aktualizované překlady pro mnoho popisů her a projektových stránek.
>- Importovány polské workshopové materiály a integrovány do vícejazyčné struktury obsahu.
>- Další sjednocení struktury obsahu a metadat pro hry.
>
>**Technické**
>- Generátor webu převeden z MkDocs/MkDocs Material na Zensical.
>- Zavedena nová vícejazyčná struktura pro sestavení a staging.
>- Němčina zůstává výchozím jazykem bez předpony jazyka; další jazyky budou publikovány pod jazykovými kódy, např. `/en/`, `/pl/`, `/es/`.
>- Zavedena centrální konfigurace jazyků prostřednictvím `tools/config/languages.json`.
>- Aktualizováno nasazení GitHub Pages pro novou strukturu Zensical.
>- Výrazně rozšířeny lokální překladové nástroje a vývojová konzole: kontroly stavu, dávkové plánování, stav překladu, grafické zobrazení, navigační nástroje, workflow pro opravu odkazů a čištění.
>- Doplněn přepínač jazyků, indikátory stavu překladu a záložní stránky pro chybějící překlady.
>- Vylepšeny tabulky ve finálním výstupu webu: řaditelné tabulky, lepší zobrazení hustých tabulek a volitelně rozbalitelné sekce stránek.
>
>**Opraveno**
>- Interní odkazy a odkazy v Markdownu na přeložených stránkách jsou spolehlivěji zachovány a opraveny.
>- Stabilizována vícejazyčná navigace a struktura URL.
>- Vylepšeno responzivní chování navigace, zejména ve spojení s mobilní hamburgerovou nabídkou Zensical.

>[!info]- **Verze:** v0.03 - **Datum vydání**: 11. března 2025
>**Obsah**
>- Přidány chybějící popisy her
>
>**Technické**
>- Přidán favicon + logo
>- Redesign UI
>- Navigace první úrovně je nyní v záhlaví stránky, zatímco kontextově se přizpůsobuje pravý navigační panel
>- Tabulky lze řadit kliknutím na záhlaví
>
>**Opraveno**
>- Značky opět fungují

>[!info]- **Verze:** v0.02 - **Datum vydání**: 26. února 2025
>**Technické**
>- Funkce blogu
>- Analytika (Google)
>- Banner pro cookies
>- Widget pro zpětnou vazbu (v dolní části každé stránky)

>[!info]- **Verze:** v0.01 - **Datum vydání** 15. ledna 2025
>**Obsah**
>- Přidáno 150 popisů her
>- Základní popis dokumentace
>
>**Technické**
>- Základní nastavení pro Mkdocs a Mkdocs-materials
>- Podpora Obsidianu s Mkdocs-publisher (umožňuje použití Obsidian Markdown, jako jsou Markdown odkazy, Callout Boxes)
