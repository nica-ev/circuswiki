---
lang: es
translation_id: frontmatter-properties
created: 2025-01-21 18:09:55
update: 2025-01-25 02:07:04
publish: true
tags: 
title: Propiedades de Frontmatter
description: Cómo usamos Frontmatter en los archivos Markdown
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Frontmatter Properties.md
translation_source_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T14:03:08+00:00
translation_source_body_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_source_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:50:16+00:00
translation_source_localized_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_source_structural_metadata_hash: 3adb19d9d9615179cd0c8ce86e9da32d59187adb8016b11a8c281dc68f9c4aad
---
Utilizamos el siguiente formato de metadatos (frontmatter):

| Propiedad | Tipo de dato | Predeterminado | Explicación                                                                                                                               |
| --------- | ------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| created   | Fecha y hora | automático     | Cuándo se creó el archivo.<br>Se introduce automáticamente.                                                                                |
| update    | Fecha y hora | automático     | Cuándo se modificó el archivo por última vez.<br>Se introduce automáticamente.                                                            |
| publish   | Booleano     | falso          | Decide si un archivo se publicará como parte de la página web.                                                                             |
| tags      | etiquetas    | -              | Las etiquetas definidas aquí también se mostrarán en la página web.                                                                       |
| title     | cadena       | -              | El título se mostrará en la página web como encabezado antes del contenido principal.                                                      |
| authors   | lista        | -              | Una lista de los autores del contenido de esta página.                                                                                    |
