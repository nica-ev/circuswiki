---
lang: it
translation_id: release-notes
created: 2025-01-21 18:09:55
update: 2026-06-10 03:32:50
publish: true
tags: 
title: Note di rilascio
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/release notes.md
translation_source_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:13:53+00:00
translation_source_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:17:01+00:00
translation_source_body_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_source_localized_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_source_structural_metadata_hash: 48054209deb2d49a5f3283cd38424c2fba59ca058c0dd085323a92f8ef336177
---
>[!info]
>Queste note di rilascio forniscono solo una panoramica generale; piccole modifiche (come singole nuove pagine, modifiche a contenuti esistenti) non sono tutte elencate. Tuttavia, queste possono essere tracciate in dettaglio nella cronologia del repository.

>[!info]- **Versione:** v0.04 - **Data di rilascio**: 9 giugno 2026
>**Contenuti**
>- Contenuti multilingue notevolmente ampliati: i contenuti sono ora strutturati sotto `docs/<lingua>`.
>- Aggiunte traduzioni nuove e aggiornate per molte descrizioni di giochi e pagine di progetto.
>- Importati materiali di workshop in polacco e integrati nella struttura dei contenuti multilingue.
>- Struttura dei contenuti e dei metadati per i giochi ulteriormente unificata.
>
>**Tecnico**
>- Generatore di siti web modificato da MkDocs/MkDocs Material a Zensical.
>- Introdotta nuova struttura multilingue per build e staging.
>- Il tedesco rimane la lingua predefinita senza prefisso linguistico; altre lingue saranno pubblicate sotto codici linguistici, ad es. `/en/`, `/pl/`, `/es/`.
>- Introdotta configurazione linguistica centrale tramite `tools/config/languages.json`.
>- Aggiornato il deployment di GitHub Pages per la nuova struttura Zensical.
>- Strumenti di traduzione locali e console di sviluppo notevolmente ampliati: controlli di integrità, pianificazione batch, stato delle traduzioni, viste grafiche, strumenti di navigazione, riparazione link e flussi di lavoro di pulizia.
>- Aggiunti selettore di lingua, indicatori di stato della traduzione e pagine di fallback per traduzioni mancanti.
>- Tabelle migliorate nell'output finale del sito: tabelle ordinabili, migliore visualizzazione di tabelle dense e aree di pagina opzionalmente comprimibili.
>
>**Corretti**
>- Link interni e link Markdown nelle pagine tradotte vengono mantenuti e riparati in modo più affidabile.
>- Navigazione multilingue e struttura URL stabilizzate.
>- Comportamento responsive della navigazione migliorato, in particolare in combinazione con il menu hamburger mobile di Zensical.

>[!info]- **Versione:** v0.03 - **Data di rilascio**: 11 marzo 2025
>**Contenuti**
>- Aggiunte descrizioni di giochi mancanti
>
>**Tecnico**
>- Aggiunti favicon + logo
>- Redesign UI
>- La navigazione di primo livello è ora nell'header della pagina, mentre la barra di navigazione destra viene adattata in modo contestuale
>- Le tabelle possono essere ordinate cliccando sugli header
>
>**Corretti**
>- I tag funzionano di nuovo

>[!info]- **Versione:** v0.02 - **Data di rilascio**: 26 febbraio 2025
>**Tecnico**
>- Funzione blog
>- Analytics (Google)
>- Banner cookie
>- Widget di feedback (in fondo a ogni pagina)

>[!info]- **Versione:** v0.01 - **Data di rilascio** 15 gennaio 2025
>**Contenuti**
>- Aggiunte 150 descrizioni di giochi
>- Descrizione di base della documentazione
>
>**Tecnico**
>- Setup di base per Mkdocs e Mkdocs-materials
>- Supporto Obsidian con Mkdocs-publisher (consente l'uso di Markdown Obsidian come link Markdown, Callout Boxes)
