---
lang: uk
translation_id: beancount/04-beancount-basics-for-users
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Основи Beancount для користувачів
description: Ознайомлення з текстовим форматом Beancount та шаблонами транзакцій, що використовуються в облікових книгах.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/04-beancount-basics-for-users.md
translation_source_body_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_source_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:36:24+00:00
translation_source_localized_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_source_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:36:24+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 04 - Основи Beancount для користувачів

Beancount зберігає бухгалтерський облік у вигляді читабельного тексту. Кожна транзакція вказує, що сталося, коли, хто був залучений і які рахунки змінилися.

## Базова структура транзакції

```beancount
2026-01-13 ! "Tragerwerk Soziale Dienste in Sachsen-Anhalt GmbH" "RgNr. T-2504"
  Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld  680.00 EUR
  Einnahmen:Sonstiges
```

| Частина | Значення |
| --- | --- |
| `2026-01-13` | Дата транзакції. |
| `!` | Маркер статусу. У цій системі він зазвичай використовується для імпортованих або ще не остаточно перевірених записів. |
| Перший текст у лапках | Одержувач або відправник. |
| Другий текст у лапках | Опис або текст банківської виписки. |
| Перший рядок рахунку | Звідки надійшли або куди пішли гроші. |
| Другий рядок рахунку | Протилежна категорія. Якщо сума не вказана, Beancount розраховує її автоматично. |

## Назви рахунків

Назви рахунків розділені двокрапками:

```text
Vermoegen:Bank:Sparkasse-NICA:Freies-Geld
```

Читайте зліва направо: активи, банківський рахунок, Sparkasse-NICA, вільно доступні кошти.

## П'ять сімейств рахунків

| Сімейство | Значення | Приклад |
| --- | --- | --- |
| `Vermoegen` | Активи: банк, PayPal, готівка, запаси. | `Vermoegen:Bank:Sparkasse-NICA` |
| `Verbindlichkeiten` | Зобов'язання: гроші, винні людям або іншим. | `Verbindlichkeiten:Person:Marc-Bielert` |
| `Equity` | Початкові залишки та балансуючі записи. | `Equity:Opening-Balances` |
| `Einnahmen` | Доходи. | `Einnahmen:Vereinsbeitrag` |
| `Ausgaben` | Витрати. | `Ausgaben:Buero:Miete` |

## Знаки доходів та витрат

У звітах Beancount доходи часто відображаються з внутрішнім від'ємним знаком, а витрати — з додатним. Fava та панелі інструментів часто представляють ці значення у більш зручному для користувача форматі. Не змінюйте транзакції лише тому, що число доходу виглядає від'ємним у необробленому запиті.

## Перевірки балансу

Перевірка балансу стверджує, що рахунок повинен мати певний баланс на певну дату:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Якщо Beancount не може співставити цей баланс із транзакціями до цієї дати, Fava покаже помилку. Перевірки балансу є основним механізмом контролю якості.

## Відкриття та закриття рахунків

Перед використанням рахунок відкривається:

```beancount
2025-04-01 open Ausgaben:Projekt:25-ZGV:Honorar
```

Коли проект завершено, а баланс рахунку проекту дорівнює нулю, його можна закрити:

```beancount
2026-02-27 close Ausgaben:Projekt:TOHUCON-25
```

Закриті рахунки зазвичай не повинні отримувати нових транзакцій.

## Коментарі та документи

Рядки, що починаються з `;`, є коментарями. Вони пояснюють рішення або невизначені ситуації та не впливають на цифри.

Квитанції можна пов'язати за допомогою рядків `document`:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```
