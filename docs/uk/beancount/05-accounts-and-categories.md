---
lang: uk
translation_id: beancount/05-accounts-and-categories
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Рахунки та категорії
description: Пояснює німецьку структуру рахунків та угоди щодо категорій, що використовуються в регістрах.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/05-accounts-and-categories.md
translation_source_body_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_source_hash: 6f562333b2c1021f7336e3dc41da20ec1484a3fc3e0863800bb0d8a5f3b7a003
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:37:25+00:00
translation_source_localized_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_source_metadata_hash: f376b9be0067b295b4c3cf49f12cb423a17243cba8ba3a6edc4ca9109f20f465
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:37:25+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 05 - Рахунки та категорії

Ця сторінка пояснює структуру рахунків, що використовуються в облікових регістрах.

## Мова найменувань

Назви рахунків — німецькою мовою. Продовжуйте використовувати наявні назви рахунків, щоб забезпечити послідовність звітів.

| Німецька | Англійське значення |
| --- | --- |
| `Vermoegen` | Активи |
| `Verbindlichkeiten` | Зобов'язання |
| `Einnahmen` | Доходи |
| `Ausgaben` | Витрати |
| `Buero` | Офіс |
| `Verein` | Асоціація/загальна діяльність асоціації |
| `Projekt` | Проєкт |
| `Barkasse` | Готівка в касі |
| `Freies-Geld` | Вільні/необмежені кошти |

## Рахунки активів

Приклади NICA:

- `Vermoegen:Bank:Sparkasse-NICA`
- `Vermoegen:Bank:Sparkasse-NICA:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:NICA:Barkasse`
- `Vermoegen:Inventar`

Приклади Tohuwabohu:

- `Vermoegen:Bank:Sparkasse-Tohuwabohu`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld`
- `Vermoegen:PayPal`
- `Vermoegen:Tohuwabohu:Barkasse`

## Загальні рахунки доходів

| Рахунок | Використання |
| --- | --- |
| `Einnahmen:Vereinsbeitrag` | Членські внески. |
| `Einnahmen:Spende` | Пожертви. |
| `Einnahmen:Verleih` | Дохід від оренди або позики. |
| `Einnahmen:Sonstiges` | Інші доходи, які не підходять до інших категорій. |

## Загальні рахунки витрат

| Рахунок | Використання |
| --- | --- |
| `Ausgaben:Buero:Miete` | Оренда офісу або приміщення. |
| `Ausgaben:Buero:Internet` | Інтернет та цифрові послуги. |
| `Ausgaben:Buero:Sonstiges` | Інші офісні витрати. |
| `Ausgaben:Verein:Versicherung` | Страхування асоціації. |
| `Ausgaben:Verein:Ehrenamt` | Компенсації волонтерам або витрати на волонтерську діяльність асоціації. |
| `Ausgaben:Essen` | Витрати на харчування поза межами конкретного проєкту. |
| `Ausgaben:Sonstiges` | Тимчасовий резерв для незрозумілих витрат. |

`Ausgaben:Sonstiges` та `Einnahmen:Sonstiges` корисні під час імпорту, але не повинні ставати остаточною категорією, якщо існує більш точна.

## Рахунки проєктів

Рахунки проєктів відповідають такому шаблону:

```text
Vermoegen:Bank:Sparkasse-ASSOCIATION:PROJECT
Ausgaben:Projekt:PROJECT
Einnahmen:Projekt:PROJECT
```

Приклади:

- `Vermoegen:Bank:Sparkasse-NICA:25-ZGV`
- `Ausgaben:Projekt:25-ZGV:Honorar`
- `Einnahmen:Projekt:25-ZGV:Sachmittel`
- `Vermoegen:Bank:Sparkasse-Tohuwabohu:TOHUCON-25`
- `Ausgaben:Projekt:TOHUCON-25:Essen`
- `Einnahmen:Projekt:TOHUCON-25:ConTickets`

## Типові підкатегорії проєктів

| Підкатегорія | Значення |
| --- | --- |
| `Honorar` | Плата, виплачена особам або отримана за роботу. |
| `Aufwand` | Витрати або компенсація витрат. |
| `Sachmittel` | Матеріали та витратні матеріали. |
| `Sonstiges` | Інші витрати або доходи проєкту. |
| `Pauschale` / `Pauschalen` | Фіксований бюджет проєкту або погодинна оплата. |

## Зобов'язання перед особами

Рахунки зобов'язань відстежують гроші, які винні особам або які повертаються особам. Приклади включають `Verbindlichkeiten:Person:Marc-Bielert`, `Verbindlichkeiten:Person:Peter-Huhndorf` та `Verbindlichkeiten:Person:Charleen-Hoffmann`.

## Вибір правильного рахунку

1. Це рівень асоціації чи рівень проєкту?
2. Якщо рівень проєкту, якому проєкту належать кошти?
3. Це дохід, витрата, рух активів чи погашення зобов'язання?
4. Чи існує вже точна категорія?
5. Якщо немає відповідної категорії, тимчасово використовуйте `Sonstiges` і додайте коментар.
