---
lang: uk
translation_id: beancount/02-opening-fava
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Відкриття Fava
description: Як запустити та відкрити локальний інтерфейс обліку Fava.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/02-opening-fava.md
translation_source_body_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_source_hash: 36fa0a4608e2081a8834edf1e2028a1f774f2309d650bd5bf875143e034549d6
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:04:12+00:00
translation_source_localized_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_source_metadata_hash: e7fd366f194b149f0afa5fdcdb8f3a7a415803f5ea46d3bc30d13c2152c94ddf
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:04:12+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 02 - Запуск Fava

Fava — це веб-інтерфейс для перегляду бухгалтерських записів. Він працює локально на комп'ютері та відкривається у браузері або веб-переглядачі Obsidian.

## Вимоги

На комп'ютері мають бути встановлені та доступні такі програми:

- Python
- Beancount
- Fava
- `fava-dashboards`, якщо потрібно відображати розширення панелі інструментів
- Obsidian, якщо використовуються кнопки Obsidian

## Відкриття з Obsidian

Нотатка `1. Vereinsverwaltung/Buchhaltung/Buchhaltung Home.md` містить кнопки для відкриття бухгалтерських записів. Ці кнопки запускають Fava через Obsidian Shell Commands, а потім відкривають локальну URL-адресу Fava.

| Кнопка | Відкриває |
| --- | --- |
| `NICA e.V. Buchhaltung` | NICA Fava на порту `4998` |
| `Tohuwabohu Halle Buchhaltung` | Tohuwabohu Fava на порту `4999` |

Не закривайте вікно терміналу, яке запускає Fava. Якщо термінал закрити, Fava зупиниться.

## Ручне відкриття

### NICA e.V.

Відкрийте термінал у каталозі:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-NICA/2023
```

Виконайте команду:

```powershell
fava nica.beancount --port 4998
```

Потім відкрийте `http://127.0.0.1:4998/`.

### Tohuwabohu Halle e.V.

Відкрийте термінал у каталозі:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023
```

Виконайте команду:

```powershell
fava 2023.beancount --port 4999
```

Потім відкрийте `http://127.0.0.1:4999/`.

## Скрипти запуску

| Файл | Призначення |
| --- | --- |
| `startup-nica.bat` | Запускає NICA Fava на порту `4998`. |
| `startup-tohu.bat` | Запускає Tohuwabohu Fava на порту `4999`. |
| `startup-all.bat` | Запускає Obsidian, кілька інструментів та обидва екземпляри Fava. |

## Важливі URL-адреси

| Перегляд | NICA | Tohuwabohu |
| --- | --- | --- |
| Головна | `http://127.0.0.1:4998/` | `http://127.0.0.1:4999/` |
| Панелі інструментів | `http://127.0.0.1:4998/nica-ev/extension/FavaDashboards/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/extension/FavaDashboards/` |
| Звіт про доходи | `http://127.0.0.1:4998/nica-ev/income_statement/` | `http://127.0.0.1:4999/tohuwabohu-halle-ev/income_statement/` |

## Якщо Fava вже запущено

Якщо Fava вже працює, достатньо відкрити URL-адресу. Якщо порт вже зайнятий і Fava не запускається, можливо, вже відкрито інший екземпляр Fava. Скористайтеся наявною сторінкою браузера або закрийте старе вікно терміналу та спробуйте знову.
