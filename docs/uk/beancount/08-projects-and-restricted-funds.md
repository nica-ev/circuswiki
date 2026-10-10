---
lang: uk
translation_id: beancount/08-projects-and-restricted-funds
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Проекти та цільові фонди
description: Пояснює, як представляються та перевіряються кошти проектів та цільові фонди.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/08-projects-and-restricted-funds.md
translation_source_body_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_source_hash: 5e72121bb5522d74478e3b413a2d2e8f50da60457105cfabd83badca9f466eea
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:18+00:00
translation_source_localized_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_source_metadata_hash: 50d470a00bfd4d1f33b31629ae6820d2e3ad09a9942d1b8a8bbbd2155b90d3bb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:18+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 08 - Проєкти та цільові кошти

Проєкти є центральним елементом цієї системи обліку. Багато грантів та видів діяльності потребують окремого відстеження від коштів вільної асоціації.

## Що означає проєкт у бухгалтерському обліку

| Тип рахунку | Приклад | Призначення |
| --- | --- | --- |
| Активи проєкту | `Vermoegen:Bank:Sparkasse-NICA:25-ZGV` | Внутрішній баланс коштів проєкту. |
| Доходи проєкту | `Einnahmen:Projekt:25-ZGV:Sachmittel` | Фінансування проєкту або доходи проєкту. |
| Витрати проєкту | `Ausgaben:Projekt:25-ZGV:Sachmittel` | Витрати проєкту. |

Реальний банківський рахунок може бути одним рахунком Sparkasse, але облік розділяє внутрішні баланси проєктів, щоб команда могла бачити, що належить до кожного проєкту.

## Активні та закриті проєкти

Активні проєкти мають відкриті рахунки та відповідні баланси. Закриті проєкти зазвичай мають перевірку кінцевого балансу `0.00 EUR` та директиви `close` для рахунків активів, доходів та витрат проєкту.

Не проводьте нові операції за закритими проєктами, якщо ви свідомо не відкриваєте їх знову або не виправляєте історичні дані.

## Поточні приклади в NICA

- `26-JEP-Buehnenreif`
- `25-ZGV`
- `25-CircusWiki`
- `25-Machen-UnitedAges`
- `25-Erasmus`
- закриті проєкти 2024 року, такі як `24-AWO`, `24-HONY`, `24-Peter`

## Поточні приклади в Tohuwabohu

- `VHS-TOHU-25`
- `ZMS-TOHU-25`
- `CEDU-25`
- `TOHUCON-25`
- закриті проєкти, такі як `Revierpionier-25`, `OAC-25`, `TohuCon2024`, `ZGV-TOHU-24`, `TohuCon2023`

## Створення нового проєкту

Для нового проєкту зазвичай потрібно відкрити рахунки перед введенням операцій.

```beancount
2026-01-01 open Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject
2026-01-01 open Ausgaben:Projekt:26-NewProject:Honorar
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sachmittel
2026-01-01 open Ausgaben:Projekt:26-NewProject:Aufwand
2026-01-01 open Ausgaben:Projekt:26-NewProject:Sonstiges
2026-01-01 open Einnahmen:Projekt:26-NewProject
2026-01-01 open Einnahmen:Projekt:26-NewProject:Honorar
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sachmittel
2026-01-01 open Einnahmen:Projekt:26-NewProject:Aufwand
2026-01-01 open Einnahmen:Projekt:26-NewProject:Sonstiges
```

Відкривайте лише ті категорії, які дійсно корисні для проєкту.

## Облік фінансування проєкту

```beancount
2026-02-01 ! "Funding Body" "First payment NewProject"
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject  3000.00 EUR
  Einnahmen:Projekt:26-NewProject:Sachmittel
```

## Облік витрат проєкту

```beancount
2026-02-10 ! "Supplier" "Project material"
  Ausgaben:Projekt:26-NewProject:Sachmittel  250.00 EUR
  Vermoegen:Bank:Sparkasse-NICA:26-NewProject
```

## Розуміння балансів проєктів

Позитивний баланс активів проєкту означає, що кошти ще виділені на цей проєкт. Нульовий баланс активів проєкту означає, що проєкт не має внутрішнього банківського залишку. Від'ємний баланс активів проєкту зазвичай означає, що проєкт витратив більше, ніж виділені кошти, або відсутнє виділення коштів.

## Закриття проєкту

Перед закриттям проєкту необхідно ввести всі доходи та витрати, забезпечити можливість знайти квитанції, баланс рахунку активів проєкту має бути рівно нуль, а будь-які залишки коштів мають бути коректно переведені або повернуті.

```beancount
2026-12-31 balance Vermoegen:Bank:Sparkasse-NICA:26-NewProject 0.00 EUR
2026-12-31 close Vermoegen:Bank:Sparkasse-NICA:26-NewProject
2026-12-31 close Ausgaben:Projekt:26-NewProject
2026-12-31 close Einnahmen:Projekt:26-NewProject
```

Закривайте також субрахунки, якщо вони були відкриті окремо.
