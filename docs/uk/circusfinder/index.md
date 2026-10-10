---
lang: uk
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-10 00:00:00
publish: true
tags:
  - moc
  - circusfinder
title: CircusFinder
description: Інтерактивний прототип для пошуку та дослідження циркових місць і мереж з даних CircusWiki.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/circusfinder/index.md
translation_source_body_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_source_hash: f4fbf5645cb1e6a8cbd48a59ccd871eb1a077f9e8ede8d95987812535a2e15db
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:39+00:00
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:39+00:00
translation_source_structural_metadata_hash: 20e821b79875446bc7befb339dc882993110dc1e540ed70cb31b6ea3b9663186
---
# CircusFinder

<div class="cw-finder" data-circusfinder>
  <p class="cw-finder__loading">CircusFinder завантажується…</p>
</div>

> [!info] Точні місця та приблизні позиції мережі
> Сині маркери базуються на опублікованих адресах. Помаранчеві маркери імпортованих мережевих контактів, навпаки, показують лише центри міст або регіонів. Будь ласка, перевіряйте інформацію, залежну від часу, як-от дати курсів та тренувань, на пов'язаному вебсайті перед відвідуванням.

<noscript>
CircusFinder потребує JavaScript для карти та фільтрів. Окремі записи залишаються доступними як звичайні сторінки Wiki.
</noscript>

## Що тестує цей прототип

Дані походять з файлів Markdown з метаданими YAML. Під час збірки Zensical вони перевіряються та експортуються як JSON. Ця сторінка завантажує виключно цей експорт і не знає про вихідні файли Markdown.

- Повнотекстовий пошук за назвою, описом, місцем та пропозиціями
- Фільтрація за типом запису
- Маркери на карті з інформацією у спливаючих вікнах
- Сині маркери для опублікованих, точних адрес
- Помаранчеві маркери для приблизних позицій міст або регіонів
- Добровільний пошук у радіусі за допомогою геолокації браузера
- Записи без географічної точки, наприклад, міжнародні мережі
