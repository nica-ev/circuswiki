---
lang: it
translation_id: frontmatter-properties
created: 2025-01-21 18:09:55
update: 2025-01-25 02:07:04
publish: true
tags: 
title: Proprietà del Frontmatter
description: Come utilizziamo il frontmatter nei file Markdown
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Frontmatter Properties.md
translation_source_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T23:01:25+00:00
translation_source_body_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_source_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:50:14+00:00
translation_source_localized_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_source_structural_metadata_hash: 3adb19d9d9615179cd0c8ce86e9da32d59187adb8016b11a8c281dc68f9c4aad
---
Utilizziamo il seguente formato di frontmatter

| Proprietà | Tipo di dato | Predefinito | Spiegazione                                                                                                                               |
| --------- | ------------ | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| created   | Data e ora   | auto        | Quando il file è stato creato<br>viene inserito automaticamente                                                                            |
| update    | Data e ora   | auto        | Quando il file è stato modificato l'ultima volta,<br>viene inserito automaticamente                                                        |
| publish   | Booleano     | false       | Decide se un file deve essere pubblicato come parte del sito web                                                                           |
| tags      | tag          | -           | I tag definiti qui verranno visualizzati anche sul sito web                                                                               |
| title     | string       | -           | Il titolo viene visualizzato sul sito web come intestazione prima del contenuto effettivo,                                                |
| authors   | lista        | -           | un elenco degli autori del contenuto di questa pagina                                                                                     |
