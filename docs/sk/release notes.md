---
lang: sk
translation_id: release-notes
created: 2025-01-21 18:09:55
update: 2026-06-10 03:32:50
publish: true
tags: 
title: Poznámky k vydaniu
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/release notes.md
translation_source_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:14:24+00:00
translation_source_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:17:06+00:00
translation_source_body_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_source_localized_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_source_structural_metadata_hash: 48054209deb2d49a5f3283cd38424c2fba59ca058c0dd085323a92f8ef336177
---
>[!info]
>Tieto poznámky k vydaniu poskytujú len hrubý prehľad, malé zmeny (ako napríklad jednotlivé nové stránky, úpravy existujúceho obsahu) nie sú všetky uvedené. Tie sa však dajú presne sledovať v histórii úložiska.

>[!info]- **Verzia:** v0.04 - **Dátum vydania**: 9. júna 2026
>**Obsah**
>- Viacjazyčný obsah bol výrazne rozšírený: obsah je teraz štruktúrovaný pod adresárom `docs/<jazyk>`.
>- Pridané nové a aktualizované preklady pre mnohé popisy hier a projektové stránky.
>- Poľské workshopové materiály boli importované a integrované do viacjazyčnej štruktúry obsahu.
>- Štruktúra obsahu a metadát pre hry bola ďalej zjednotená.
>
>**Technické aspekty**
>- Generátor webových stránok bol prepnutý z MkDocs/MkDocs Material na Zensical.
>- Zaviedla sa nová viacjazyčná štruktúra zostavenia a staging.
>- Nemčina zostáva predvoleným jazykom bez predpony jazyka; ďalšie jazyky budú publikované pod jazykovými kódmi, napr. `/en/`, `/pl/`, `/es/`.
>- Zaviedla sa centrálna konfigurácia jazykov cez `tools/config/languages.json`.
>- Nasadenie GitHub Pages bolo aktualizované pre novú štruktúru Zensical.
>- Lokálne nástroje na preklad a vývojová konzola boli výrazne rozšírené: kontroly stavu, dávkové plánovanie, stav prekladov, grafické zobrazenia, navigačné nástroje, oprava odkazov a čistiace pracovné postupy.
>- Pridaný prepínač jazykov, indikátory stavu prekladov a záložné stránky pre chýbajúce preklady.
>- Tabuľky vo finálnom výstupe stránky boli vylepšené: triediteľné tabuľky, lepšie zobrazenie hustých tabuliek a voliteľné zbaliteľné sekcie stránok.
>
>**Opravené**
>- Interné odkazy a odkazy v Markdown na preložených stránkach sú spoľahlivejšie zachované a opravené.
>- Viacjazyčná navigácia a štruktúra URL boli stabilizované.
>- Responzívne správanie navigácie bolo vylepšené, najmä v súčinnosti s mobilnou hamburgerovou ponukou Zensical.

>[!info]- **Verzia:** v0.03 - **Dátum vydania**: 11. marca 2025
>**Obsah**
>- Pridané chýbajúce popisy hier
>
>**Technické aspekty**
>- Pridané favicon + logo
>- Redizajn používateľského rozhrania
>- Navigácia prvej úrovne je teraz v hlavičke stránky, zatiaľ čo kontextovo závislý pravý navigačný panel sa prispôsobuje
>- Tabuľky je možné triediť kliknutím na hlavičky
>
>**Opravené**
>- Značky (tagy) opäť fungujú

>[!info]- **Verzia:** v0.02 - **Dátum vydania**: 26. februára 2025
>**Technické aspekty**
>- Funkcia blogu
>- Analytika (Google)
>- Banner na súbory cookie
>- Widget na spätnú väzbu (v spodnej časti každej stránky)

>[!info]- **Verzia:** v0.01 - **Dátum vydania** 15. januára 2025
>**Obsah**
>- Pridaných 150 popisov hier
>- Základný popis dokumentácie
>
>**Technické aspekty**
>- Základné nastavenie pre Mkdocs a Mkdocs-materials
>- Podpora Obsidian s Mkdocs-publisher (umožňuje používať Obsidian Markdown, ako napríklad Markdown odkazy, Callout Boxes)
