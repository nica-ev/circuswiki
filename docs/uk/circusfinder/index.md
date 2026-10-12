---
lang: uk
translation_id: circusfinder/index
created: 2026-10-09 00:00:00
update: 2026-10-11 02:44:56
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
translation_source_body_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_source_hash: 8b966c09580440aa5f2aa3c5cce7df402e5f379da6d8a1544a80e6804812124c
translation_model: google/gemini-2.5-flash-lite
translation_updated: "2026-10-11T20:10:53+00:00"
translation_source_localized_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_source_metadata_hash: 658f97fdd64c5d89452b98e35083d80e2e92529566d5157dab6cec469e95c453
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: "2026-10-11T20:10:53+00:00"
translation_source_structural_metadata_hash: 3c8e9a99c2102ebe9c7bd993f9672df51a21bd43f42f25fb7e56ae5ca962728e
---
# CircusFinder

<div class="cw-finder" data-circusfinder aria-busy="true">
  <div class="cw-finder__layout">
    <div class="cw-finder__map-column">
      <div class="cw-finder__map cw-finder__map--loading" role="region" aria-label="CircusFinder">
        <div class="cw-finder__map-placeholder" role="status">
          <img src="../images/circusfinder-map-placeholder.svg" alt="" width="1200" height="560">
          <span>Завантаження CircusFinder…</span>
        </div>
      </div>
    </div>
    <section class="cw-finder__results" aria-hidden="true"></section>
  </div>
</div>

> [!info] Точні місця та приблизні позиції мережі
> Сині маркери базуються на опублікованих адресах. Помаранчеві маркери імпортованих мережевих контактів показують лише центри міст або регіонів. Будь ласка, перевіряйте актуальну інформацію, як-от розклад занять та тренувань, на пов'язаному вебсайті перед відвідуванням.

<noscript>
CircusFinder потребує JavaScript для роботи карти та фільтрів. Окремі записи залишаються доступними як звичайні сторінки Wiki.
</noscript>

## Що тестує цей прототип

Дані надходять із файлів Markdown з метаданими YAML. Під час збірки Zensical вони перевіряються та експортуються як JSON. Ця сторінка завантажує виключно цей експорт і не знає про вихідні файли Markdown.

- Повнотекстовий пошук за назвою, описом, місцем розташування та пропозиціями
- Фільтрація за типом запису
- Маркери на карті з інформацією у спливаючих вікнах
- Сині маркери для опублікованих, точних адрес
- Помаранчеві маркери для приблизних позицій міст або регіонів
- Добровільний пошук у радіусі за допомогою геолокації браузера
- Записи без географічної точки, наприклад, міжнародні мережі
