---
lang: hu
translation_id: frontmatter-properties
created: 2025-01-21 18:09:55
update: 2025-01-25 02:07:04
publish: true
tags: 
title: Frontmatter Tulajdonságok
description: Hogyan használjuk a frontmattert a Markdown fájlokban
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Frontmatter Properties.md
translation_source_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T22:39:23+00:00
translation_source_body_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_source_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:50:13+00:00
translation_source_localized_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_source_structural_metadata_hash: 3adb19d9d9615179cd0c8ce86e9da32d59187adb8016b11a8c281dc68f9c4aad
---
A következő frontmatter formátumot használjuk:

| Tulajdonság | Adattípus   | Alapérték | Magyarázat                                                                                             |
| ----------- | ----------- | --------- | ------------------------------------------------------------------------------------------------------ |
| created     | Dátum + Idő | auto      | Mikor jött létre a fájl<br>automatikusan bejegyzésre kerül                                              |
| update      | Dátum + Idő | auto      | Mikor lett utoljára módosítva a fájl,<br>automatikusan bejegyzésre kerül                                 |
| publish     | Boolean     | false     | Eldönti, hogy egy fájl közzétételre kerül-e a weboldal részeként                                        |
| tags        | tagek       | -         | Az itt definiált tagek a weboldalon is megjelennek                                                    |
| title       | string      | -         | A cím a weboldalon címsorként jelenik meg a tényleges tartalom előtt,                                   |
| authors     | lista       | -         | az oldal tartalmának szerzői listája                                                                   |
