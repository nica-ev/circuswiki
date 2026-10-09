---
lang: uk
translation_id: beancount/03-folder-and-file-map
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Карта папок і файлів
description: Відображає важливі бухгалтерські папки, файли журналів, панелі інструментів та допоміжні файли.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/03-folder-and-file-map.md
translation_source_body_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_source_hash: cf477654bf1aa178745e737465d6aae9dae4d99d7443eb01772ad88b1db509fb
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:35:21+00:00
translation_source_localized_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_source_metadata_hash: 4aee259bbdfab5e0381231dba7af82d7ee0a7eaecdcc840f2a797b99da226344
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:35:21+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 03 - Структура папок та файлів

Ця сторінка пояснює, де зберігаються важливі бухгалтерські файли.

## Основна папка бухгалтерії

```text
1. Vereinsverwaltung/Buchhaltung
```

Ця папка містить реєстри, файли панелей інструментів, супровідні документи та допоміжні папки.

## Важливі файли верхнього рівня

| Файл | Призначення |
| --- | --- |
| `Buchhaltung Home.md` | Вхідна сторінка Obsidian з кнопками та короткими примітками щодо робочого процесу. |
| `all.beancount` | Експериментальний об'єднаний реєстр, що включає NICA та Tohuwabohu. |
| `dashboards.yaml` | Визначення панелей інструментів для панелей Fava на спільному рівні. |

## Структура NICA

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA
```

| Шлях | Призначення |
| --- | --- |
| `2023/nica.beancount` | Основний реєстр NICA. Це файл, який зазвичай редагується. |
| `2023/dashboards.yaml` | Конфігурація панелей інструментів для реєстру NICA. |
| `2023/Buchhaltung NICA eV.md` | Допоміжна нотатка Obsidian для відкриття бухгалтерії NICA. |
| `2023/CSV/` | Збережені експорти CSV. |
| `test/csv2bean.py` | Конвертує CSV Sparkasse у тимчасові записи Beancount. |
| `test/beancount_file.beancount` | Згенерований вивід з конвертації CSV. |
| `test/paypal2bean.py` | Допоміжний інструмент для імпорту CSV з PayPal. |
| `test/output_file_paypal.beancount` | Згенерований вихідний файл PayPal. |
| `test/old files/` | Старіші CSV та згенеровані файли. |

## Структура Tohuwabohu

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu
```

| Шлях | Призначення |
| --- | --- |
| `2023/2023.beancount` | Основний реєстр Tohuwabohu. Це файл, який зазвичай редагується. |
| `2021/2021.beancount` | Старіші дані реєстру, включені через `all.beancount`. |
| `all.beancount` | Об'єднаний файл Tohuwabohu, що включає файли реєстрів за 2021 та 2023 роки. |
| `2023/dashboards.yaml` | Конфігурація панелей інструментів для реєстру Tohuwabohu. |
| `2023/Buchhaltung Tohuwabohu Halle eV.md` | Допоміжна нотатка Obsidian. |
| `2023/Belege Ausgaben/` | Квитанції та супровідні документи для витрат. |
| `2023/Belege Ausgaben/Eingetragen/` | Квитанції, вже внесені до реєстру. |
| `test/csv2bean.py` | Конвертує CSV Sparkasse у тимчасові записи Beancount. |
| `test/beancount_file.beancount` | Згенерований вивід з конвертації CSV. |
| `test/paypal2bean.py` | Допоміжний інструмент для імпорту CSV з PayPal. |
| `test/output_file_paypal.beancount` | Згенерований вихідний файл PayPal. |
| `test/CSV - old files/` | Старіші CSV та згенеровані файли. |

## Принцип найменування файлів

Папки все ще містять історичні назви, такі як `2023`, навіть якщо вони також містять пізнішу активність з 2024, 2025 та 2026 років. Розглядайте поточні основні файли реєстрів як активні, якщо структура не змінена навмисно.

## Де редагувати

| Асоціація | Редагувати цей файл |
| --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` |

Не редагуйте згенеровані вихідні файли як постійний запис. Це тимчасові проміжні файли.
