---
lang: cs
translation_id: frontmatter-properties
created: 2025-01-21 18:09:55
update: 2025-01-25 02:07:04
publish: true
tags: 
title: Vlastnosti frontmatteru
description: Jak používáme frontmatter v souborech Markdown
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Frontmatter Properties.md
translation_source_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T18:45:37+00:00
translation_source_body_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_source_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:50:18+00:00
translation_source_localized_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_source_structural_metadata_hash: 3adb19d9d9615179cd0c8ce86e9da32d59187adb8016b11a8c281dc68f9c4aad
---
Používáme následující formát frontmatteru

| Vlastnost | Datový typ    | Výchozí hodnota | Vysvětlení                                                                                             |
| ----------- | ----------- | --------------- | ------------------------------------------------------------------------------------------------------ |
| created     | Datum a čas | automaticky     | Kdy byl soubor vytvořen<br>se zadává automaticky                                                       |
| update      | Datum a čas | automaticky     | Kdy byl soubor naposledy změněn,<br>se zadává automaticky                                              |
| publish     | Boolean     | false           | Rozhoduje, zda bude soubor publikován jako součást webu                                                |
| tags        | tagy        | -               | Zde definované tagy se zobrazí i na webu                                                               |
| title       | string      | -               | Název se na webu zobrazí jako nadpis před vlastním obsahem                                            |
| authors     | seznam      | -               | seznam autorů obsahu této stránky                                                                       |
