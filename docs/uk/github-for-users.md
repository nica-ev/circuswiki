---
lang: uk
translation_id: github-for-users
publish: true
tags:
  - github
  - tutorial
created: 2025-01-18 23:14:04
update: 2026-06-12 18:26:00
title: Співпраця безпосередньо у репозиторії GitHub
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/github-for-users.md
translation_source_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-12T17:31:42+00:00
translation_source_body_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_source_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:51:19+00:00
translation_source_localized_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_source_structural_metadata_hash: 69966c4b32b093dc5fdaa8e7127a710d8477892c36f2859ba38215866bb73327
---
> [!info] Коротко кажучи
> Ця сторінка призначена для тих, хто хоче безпосередньо працювати з Markdown-файлами CircusWiki. Для звичайних внесків цей шлях не потрібен: ви можете просто надіслати матеріал електронною поштою.

Пряма співпраця через GitHub зручна, якщо ви хочете регулярно виправляти сторінки, створювати нові Markdown-файли або працювати з сховищем CircusWiki в редакторі на кшталт Obsidian.

Якщо ви хочете додати лише гру, метод, PDF, посилання або виправлення, простіший шлях зазвичай кращий:

[Назад до "Долучитися"](mitmachen.md){ .md-button }

## Що вам знадобиться

- безкоштовний обліковий запис GitHub: [https://github.com/join](https://github.com/join)
- необов'язково GitHub Desktop: [https://desktop.github.com/](https://desktop.github.com/)
- текстовий редактор для Markdown-файлів, наприклад Obsidian, VS Code або простий редактор

GitHub Desktop не є обов'язковим, але для багатьох людей він простіший за командний рядок.

## Знайти репозиторій

Публічний репозиторій знаходиться тут:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Там зберігаються фактичні Markdown-файли, зображення, переклади та інструменти, з яких будується вебсайт.

## Робота в короткій формі

Типовий процес виглядає так:

1. Створити форк репозиторію на GitHub.
2. Клонувати свою копію на власний комп'ютер.
3. Вносити зміни в новому гілці.
4. Редагувати файли або створювати нові Markdown-файли.
5. Зробити коміт змін.
6. Завантажити гілку на GitHub.
7. Відкрити Pull Request, щоб зміну можна було перевірити та прийняти.

## Крок за кроком з GitHub Desktop

### 1. Створити форк репозиторію

Відкрийте репозиторій CircusWiki на GitHub:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Натисніть `Fork`. Це створить власну копію репозиторію у вашому обліковому записі GitHub. У цій копії ви можете працювати, не змінюючи безпосередньо основний проєкт.

### 2. Клонувати репозиторій

Відкрийте GitHub Desktop і виберіть:

```text
File -> Clone repository...
```

Виберіть свій форк `nica-ev/circuswiki` і вкажіть папку на своєму комп'ютері.

Після цього у вас буде локальна копія файлів.

### 3. Створити гілку

Для вашої зміни найкраще створити окрему гілку, наприклад:

```text
spiel-beschreibung-ergaenzen
link-korrigieren
neue-methode-balancieren
```

Гілка зберігає вашу роботу окремо від основного стану. Це полегшує подальшу перевірку.

### 4. Редагувати файли

Публічний контент переважно знаходиться в мовних папках під `docs/`:

```text
docs/de/
docs/en/
docs/es/
docs/pl/
...
docs/img/
```

Усі мови є рівноцінними. Немає основної мови, якою б створювався новий контент.

Якщо ви створюєте нову оригінальну сторінку, розмістіть її в мовній папці, мовою якої написаний текст. Наприклад, оригінальний іспанський текст належить до `docs/es/`, німецький — до `docs/de/`, англійський — до `docs/en/`.

Важливим є Frontmatter на початку файлу. Там має бути зазначено, що сторінка є оригіналом, наприклад:

```yaml
translation_status: original
translation_source_lang: es
```

`translation_source_lang` відповідає мові оригінального тексту. З цього оригіналу пізніше можна автоматично генерувати переклади всіма підтримуваними мовами.

Під час редагування зверніть увагу на наступне:

- Не видаляйте Frontmatter на початку файлу.
- Для нових оригінальних сторінок встановіть `translation_status: original` та відповідний `translation_source_lang`.
- За можливості зберігайте існуючі посилання.
- Не публікуйте приватні дані, ключі API або внутрішні нотатки.
- Використовуйте зображення лише тоді, коли права на використання чіткі.
- Краще робити невеликі, чіткі зміни, ніж дуже великі змішані зміни.

### 5. Зробити коміт змін

У GitHub Desktop ви побачите змінені файли в розділі `Changes`.

Напишіть короткий опис, наприклад:

```text
Korrigiere Materialliste im Bewegungsspiel
Ergänze Sicherheitshinweis zu Beigoma
Füge neue Spielbeschreibung hinzu
```

Потім натисніть `Commit to <branch-name>`.

### 6. Завантажити зміни

Натисніть `Push origin`, щоб завантажити свою гілку на GitHub.

### 7. Відкрити Pull Request

GitHub Desktop або GitHub у браузері запропонують створити Pull Request.

Pull Request означає: ви пропонуєте свою зміну для основного репозиторію. Зміна буде перевірена, можливо, прокоментована, а потім прийнята або доопрацьована.

## Основи Markdown

Markdown — це простий текстовий формат. Найважливіших символів достатньо для більшості внесків:

```markdown
# Великий заголовок
## Заголовок розділу

Звичайний текст із **жирним виділенням** та *курсивним виділенням*.

- Пункт списку
- Ще один пункт списку

[Текст посилання](https://www.example.com)
```

## Якщо щось незрозуміло

Не обов'язково одразу досконало вміти працювати з GitHub. Якщо ви відкриєте Pull Request, а щось ще не так, це можна буде з'ясувати під час перегляду.

Якщо ви хочете лише додати контент, а технічний шлях здається занадто складним, просто скористайтеся електронною поштою на [сторінці "Долучитися"](mitmachen.md).
