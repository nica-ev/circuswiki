---
lang: uk
translation_id: beancount/09-receipts-and-documents
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Квитанції та документи
description: Пояснює, де зберігаються підтверджуючі документи та як транзакції посилаються на квитанції.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/09-receipts-and-documents.md
translation_source_body_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_source_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:53+00:00
translation_source_localized_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_source_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:53+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 09 - Квитанції та документи

Квитанції, рахунки-фактури, договори та інші підтверджуючі документи роблять транзакції аудитованими. Реєстр (ledger) має дозволяти знаходити документ, що стоїть за витратою.

## Де зберігаються документи

Наразі Tohuwabohu має чітку папку для квитанцій:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben
```

Квитанції, які вже внесені до реєстру, часто знаходяться в:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben/Eingetragen
```

NICA використовує підтверджуючі файли у своїй папці для бухгалтерського обліку та проєктних папках. Якщо пізніше буде впроваджено єдину папку для квитанцій NICA, задокументуйте це тут і використовуйте її послідовно.

## Записи `document`

Запис `document` пов'язує файл з рахунком та датою:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```

Шлях до файлу є відносним до папки, що містить файл реєстру.

## Посилання на документи з тегами

Деякі старі записи містять теги документів, такі як:

```beancount
2023-01-05 document Ausgaben:Buero:Sonstiges "Belege Ausgaben/Eingetragen/2023_001.jpg" ^2023_001
```

Частина `^2023_001` є посиланням Beancount. Вона може пов'язати квитанцію з відповідною транзакцією, якщо там використовується те саме посилання.

## Значення `scanned`

Коментарі в реєстрах визначають угоду щодо відсканованих квитанцій. Коли використовується тег `scanned`, це означає:

- Квитанцію було відскановано або оцифровано.
- Зображення було зменшено та оптимізовано, наприклад, за допомогою TinyPNG.
- Файл було збережено за шаблоном "рік і номер", наприклад `2023_002.jpg`.
- Номер згадується у відповідному записі реєстру.

## Гарні назви файлів

Гарні назви файлів квитанцій є стабільними та читабельними:

```text
2026_001.jpg
2026_002.pdf
Quittung-Tohu25-001.pdf
Invoice406-Schwarze_Risse-marc-bielert.pdf
```

Уникайте назв на кшталт `scan.jpg`, `image1.jpg` або `download.pdf`.

## Робочий процес для нової квитанції

1. Збережіть квитанцію у відповідну папку для квитанцій.
2. Перейменуйте її, щоб її можна було розпізнати пізніше.
3. Внесіть або знайдіть відповідну транзакцію.
4. Додайте рядок `document` або метадані посилання, якщо це корисно.
5. Якщо квитанцію оброблено, перемістіть її до `Eingetragen`, якщо це така угода щодо папок.
6. Перезавантажте Fava та перевірте, чи працює посилання на документ.

## Коли квитанція відсутня

Якщо квитанція відсутня, додайте коментар біля транзакції:

```beancount
; Receipt missing. Ask responsible person.
```

Не вдавайте, що документ існує, якщо його немає.

## Договори та документи про гонорари

Договори та рахунки-фактури про гонорари слід зберігати поблизу відповідного проєкту або папки бухгалтерського обліку та чітко посилатися на них. Для аудиту проєкту важливим є не лише наявність транзакції, а й можливість швидко знайти документ, що підтверджує витрату.
