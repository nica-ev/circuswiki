---
lang: uk
translation_id: beancount/06-entering-and-editing-transactions
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Введення та редагування транзакцій
description: Описує, як користувачі переглядають, класифікують, виправляють та вводять бухгалтерські транзакції.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/06-entering-and-editing-transactions.md
translation_source_body_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_source_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:53:39+00:00
translation_source_localized_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_source_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:53:39+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 06 - Введення та редагування транзакцій

Більшість записів надходять з імпортованих банківських даних, але користувачам все одно потрібно переглядати, класифікувати, виправляти, а іноді й вручну вводити транзакції.

## Статус транзакції

У записах часто використовується `!` для імпортованих транзакцій:

```beancount
2026-03-12 ! "Отримувач" "Банківський текст"
```

Використовуйте цей маркер як стандартний, якщо команда не вирішить запровадити суворішу конвенцію щодо статусів.

## Базове введення доходу

```beancount
2026-01-15 ! "Макс Мустерманн" "Членський внесок 2026"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  60.00 EUR
  Einnahmen:Vereinsbeitrag
```

## Базове введення витрат

```beancount
2026-01-20 ! "Назва постачальника" "Рахунок 123"
  Ausgaben:Buero:Sonstiges  25.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Дохід за проєктом

```beancount
2026-02-10 ! "Орган фінансування" "Грантова виплата проєкт 25-ZGV"
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV  5000.00 EUR
  Einnahmen:Projekt:25-ZGV:Sachmittel
```

## Витрати за проєктом

```beancount
2026-02-15 ! "Ім'я особи" "Гонорар проєкт 25-ZGV"
  Ausgaben:Projekt:25-ZGV:Honorar  450.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV
```

## Внутрішній рух коштів між проєктом та вільними фондами

Іноді транзакція повинна розподіляти банківські кошти між специфічним для проєкту рахунком активів та вільними фондами. Реальний банківський рахунок є одним фізичним рахунком Sparkasse, але в записах баланси проєкту відстежуються окремо.

```beancount
2026-02-20 ! "Внутрішній розподіл" "Переведення залишку коштів проєкту на вільні гроші"
  Vermoegen:Bank:Sparkasse-NICA:Freies-Geld  100.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:25-ZGV      -100.00 EUR
```

Здійснюйте внутрішні перекази лише тоді, коли ви розумієте, чому має змінитися баланс проєкту.

## Відшкодування особам

Якщо хтось оплатив щось з власної кишені, а потім йому відшкодовують, чистий шаблон зазвичай полягає в тому, щоб записати витрати проти зобов'язання, а потім погасити зобов'язання банківським платежем.

```beancount
2026-03-01 ! "Магазин" "Матеріали, придбані Марком"
  Ausgaben:Projekt:25-ZGV:Sachmittel  35.00 EUR
  Verbindlichkeiten:Person:Marc-Bielert
```

```beancount
2026-03-05 ! "Марк Білерт" "Відшкодування за матеріали"
  Verbindlichkeiten:Person:Marc-Bielert  35.00 EUR
  Vermoegen:Bank:Sparkasse-NICA
```

## Коментарі до незрозумілих рішень

```beancount
; Незрозуміло, чи це належить до CEDU-25, чи до фондів вільної асоціації. Перевірити рахунок-фактуру.
2026-03-10 ! "Постачальник" "Рахунок 456"
  Ausgaben:Sonstiges  120.00 EUR
  Vermoegen:Bank:Sparkasse-Tohuwabohu
```

## Безпечне редагування

Перед редагуванням перевірте:

- Ви перебуваєте в правильному реєстрі асоціації.
- Ви не редагуєте згенерований вивід імпорту так, ніби це остаточний реєстр.
- Дата транзакції правильна.
- У сумі використовується крапка як десятковий роздільник, наприклад `12.50 EUR`.
- Назви рахунків написані точно так само, як існуючі рахунки.
- Транзакції за проєктами послідовно використовують рахунок активів проєкту та категорію доходів/витрат проєкту.

Після редагування збережіть файл, перезавантажте Fava, перевірте на наявність помилок та перегляньте відповідну сторінку рахунку.
