---
lang: en
translation_id: frontmatter-properties
created: 2025-01-21 18:09:55
update: 2025-01-25 02:07:04
publish: true
tags: 
title: Frontmatter Properties
description: How to use frontmatter in Markdown files
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Frontmatter Properties.md
translation_source_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T19:22:58+00:00
translation_source_body_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_source_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:50:12+00:00
translation_source_localized_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_source_structural_metadata_hash: 3adb19d9d9615179cd0c8ce86e9da32d59187adb8016b11a8c281dc68f9c4aad
---
We use the following frontmatter format:

| Property | Data Type   | Default | Explanation                                                                                             |
| -------- | ----------- | ------- | ------------------------------------------------------------------------------------------------------- |
| created  | Date + Time | auto    | When the file was created<br>automatically entered                                                      |
| update   | Date + Time | auto    | When the file was last modified,<br>automatically entered                                               |
| publish  | Boolean     | false   | Determines whether a file is published as part of the website                                           |
| tags     | tags        | -       | Tags defined here will also be displayed on the website                                                 |
| title    | string      | -       | The title will be displayed on the website as a heading before the actual content,                      |
| authors  | list        | -       | a list of the creators of the content on this page                                                      |
