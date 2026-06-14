---
lang: uk
translation_id: frontmatter-properties
created: 2025-01-21 18:09:55
update: 2025-01-25 02:07:04
publish: true
tags: 
title: Властивості Frontmatter
description: Як використовувати Frontmatter у файлах Markdown
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Frontmatter Properties.md
translation_source_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T14:22:25+00:00
translation_source_body_hash: 2e30831383593168acdb0184b17d6967214f93b5e052c4e649cbab6fd46ba0aa
translation_source_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:50:16+00:00
translation_source_localized_metadata_hash: d83f0b9f04363f25d81155e86a0379f5d491b0786760c44ff11a50b17b319883
translation_source_structural_metadata_hash: 3adb19d9d9615179cd0c8ce86e9da32d59187adb8016b11a8c281dc68f9c4aad
---
Ми використовуємо такий формат фронтматеру:

| Властивість | Тип даних   | За замовчуванням | Пояснення                                                                                                                               |
| ----------- | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| created     | Дата + час  | авто             | Коли файл було створено<br>заповнюється автоматично                                                                                    |
| update      | Дата + час  | авто             | Коли файл було востаннє змінено,<br>заповнюється автоматично                                                                            |
| publish     | Булевий     | false            | Визначає, чи буде файл опубліковано як частину вебсайту                                                                                 |
| tags        | теги        | -                | Теги, визначені тут, також відображатимуться на вебсайті                                                                                |
| title       | рядок       | -                | Заголовок відображатиметься на вебсайті як основний заголовок перед фактичним вмістом                                                  |
| authors     | список      | -                | Список авторів вмісту цієї сторінки                                                                                                     |
