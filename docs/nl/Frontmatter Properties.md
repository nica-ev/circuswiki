---
lang: nl
translation_id: frontmatter-properties
created: 2025-01-21 18:09:55
update: 2025-01-25 02:07:04
publish: true
tags: 
title: Frontmatter-eigenschappen
description: Hoe we frontmatter gebruiken in Markdown-bestanden
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Frontmatter Properties.md
translation_source_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T23:15:47+00:00
translation_source_body_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_source_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:50:15+00:00
translation_source_localized_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_source_structural_metadata_hash: 3adb19d9d9615179cd0c8ce86e9da32d59187adb8016b11a8c281dc68f9c4aad
---
We gebruiken het volgende frontmatter-formaat

| Eigenschap | Datatype    | Standaard | Uitleg                                                                                             |
| ---------- | ----------- | --------- | -------------------------------------------------------------------------------------------------- |
| created    | Datum + Tijd | auto      | Wanneer het bestand is aangemaakt<br>wordt automatisch ingevuld                                    |
| update     | Datum + Tijd | auto      | Wanneer het bestand voor het laatst is gewijzigd,<br>wordt automatisch ingevuld                   |
| publish    | Boolean     | false     | Bepaalt of een bestand wordt gepubliceerd als onderdeel van de website                              |
| tags       | tags        | -         | Hier gedefinieerde tags worden ook op de website weergegeven                                       |
| title      | string      | -         | De titel wordt op de website als kop boven de eigenlijke inhoud weergegeven,                     |
| authors    | lijst       | -         | een lijst van de makers van de inhoud van deze pagina                                              |
