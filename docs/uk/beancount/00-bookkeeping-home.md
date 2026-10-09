---
lang: uk
translation_id: beancount/00-bookkeeping-home
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Документація системи бухгалтерського обліку
description: Огляд та початкова точка для документації бухгалтерського обліку Beancount для NICA e.V. та Tohuwabohu Halle e.V.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/00-bookkeeping-home.md
translation_source_body_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_source_hash: 84895e9f27f1d3b8cbf965fab1ab1bbaa35b84d9e02adf47cfb6547e4c0067f3
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:31:47+00:00
translation_source_localized_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_source_metadata_hash: 109fa3341d28b0e47f31a3f9130fbe6f6f7e3e579076c39bbfcbca54ac1fbec7
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:31:47+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# Документація системи бухгалтерського обліку

Ця документація пояснює, як працює система бухгалтерського обліку для NICA e.V. та Tohuwabohu Halle e.V. з точки зору звичайного користувача.

Система використовує файли обліку у форматі простого тексту Beancount та браузерний інтерфейс Fava. Вам не потрібно розуміти програмування, щоб користуватися нею, але ви повинні ретельно дотримуватися робочого процесу обліку: імпортувати банківські дані, класифікувати транзакції, додавати квитанції за потреби та перевіряти баланси.

## Почніть тут

- [01 - Огляд системи](01-system-overview.md)
- [02 - Відкриття Fava](02-opening-fava.md)
- [03 - Карта папок і файлів](03-folder-and-file-map.md)
- [04 - Основи Beancount для користувачів](04-beancount-basics-for-users.md)
- [05 - Рахунки та категорії](05-accounts-and-categories.md)
- [06 - Введення та редагування транзакцій](06-entering-and-editing-transactions.md)
- [07 - Імпорт CSV з банку та звірка](07-bank-csv-import-and-reconciliation.md)
- [08 - Проєкти та цільові фонди](08-projects-and-restricted-funds.md)
- [09 - Квитанції та документи](09-receipts-and-documents.md)
- [10 - Панелі інструментів та звіти Fava](10-fava-dashboards-and-reports.md)
- [11 - Регулярна рутина обліку](11-regular-bookkeeping-routine.md)
- [12 - Вирішення проблем](12-troubleshooting.md)
- [13 - Глосарій](13-glossary.md)

## Найважливіше правило

Обліковий файл є джерелом правди. Fava відображає лише те, що записано у файлах `.beancount`. Якщо щось виглядає неправильно у Fava, виправте запис у Beancount та перезавантажте Fava.

## Поточні книги

| Організація | Основний файл | Адреса Fava | Порт |
| --- | --- | --- | --- |
| NICA e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023/nica.beancount` | `http://127.0.0.1:4998/` | `4998` |
| Tohuwabohu Halle e.V. | `1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/2023.beancount` | `http://127.0.0.1:4999/` | `4999` |

## Чим ця документація не є

Це не юридична чи податкова консультація. Вона описує, як організована ця конкретна місцева система бухгалтерського обліку та як користувачі повинні послідовно з нею працювати.
