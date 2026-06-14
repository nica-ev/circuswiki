---
lang: uk
translation_id: obsidian-setup
publish: true
tags: 
title: Налаштування Obsidian
created: 2025-01-23 01:38:52
update: 2026-06-06 21:43:04
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Obsidian Setup.md
translation_source_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T14:30:33+00:00
translation_source_body_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_source_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:14:23+00:00
translation_source_localized_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_source_structural_metadata_hash: 6eec0b8a6b7772bab240bcedda44bfa18061f6163b3b9475217ace91bcc065ea
---
Obsidian надзвичайно гнучкий, що може стати проблемою для новачків.
Ми надаємо базове налаштування, яке можна використовувати як є, включно з плагінами та темами, а також їхніми тонкими налаштуваннями.
Це базове налаштування, яке можна далі доопрацювати відповідно до особистих уподобань кожного.
Ми надаємо лише робоче рішення, яке ми документуємо та пояснюємо тут.

## Використовувані терміни
**Сховище (Vault)** — колекція файлів Markdown та зображень, що формують базу знань.

## Плагіни

- Advanced Canvas
- BRAT
- Better Wordcount
- Clear unused Images
- Dataview
- Dataview Serializer
- Emoji Toolbar
- Linter
- Note Toolbar
- Tag Wrangler
- Templater
- Beautitab
- Omnisearch
- Status Bar Organizer
- Workspaces Plus
- Sortable

### Advanced Canvas
Надає доступ до багатьох нових функцій та опцій стилізації для Canvas.

### BRAT
Необхідний для встановлення неофіційних плагінів / плагінів, не зареєстрованих в екосистемі Obsidian, а саме:
- Dataview Serializer
- Sortable

### Better Word Count
В основному використовується завдяки можливості показувати кількість слів/символів у виділеному тексті.
Відображається у рядку стану.

### Beautitab
Суто косметичний, надає настроювану сторінку "порожньої нової вкладки".

### Clear unused Images
Як випливає з назви, допомагає організувати сховище, ідентифікуючи невикористані зображення.

❗Я виключив підпапку ```/site/```, щоб не видаляти завжди зображення з зібраного вебсайту (що не є проблемою, радше дратівливою дрібницею).

❗Будьте обережні з командою очищення вкладень (clear attachments), оскільки вона завжди видалятиме ```mkdocs.yml``` та ```license.``` --> якщо це станеться, файли будуть у папці ```.trash``` і їх можна буде відновити. Але це легко пропустити.

### Dataview
Дозволяє виконувати запити, подібні до SQL, до сховища.

### Dataview Serializer
Перетворює результати Dataview на Markdown.
Допомагає повторно використовувати результати запитів Dataview у фактичних нотатках.

### Emoji Toolbar
Надає легкий доступ до емодзі.
**Гаряча клавіша встановлена на: ALT-E**
😍

### Linter
Очищає файли Markdown та дані фронтматера.
Допомагає підтримувати послідовну форму.

### Note Toolbar
Надає настроювані панелі інструментів у верхній частині нотатки, які можна визначати на рівні папки/файлу.

### Tag Wrangler
Надає додаткові опції для роботи з тегами.
- перейменування тегів
Допомагає організувати сховище.

### Templater
Дозволяє створювати настроювані шаблони, які можна вставляти вручну або на основі умов (наприклад, при створенні нотатки).

### Status Bar Organizer
Дозволяє приховувати елементи з рядка стану.

### Sortable
Дозволяє сортувати таблиці (як Markdown, так і таблиці Dataview), натискаючи на їхні заголовки.

### Workspaces Plus
Дозволяє швидко перемикатися між робочими областями з рядка стану.

## Файлова система сховища

[Файлова система сховища](Vault%20File%20System.md){ .md-button }
