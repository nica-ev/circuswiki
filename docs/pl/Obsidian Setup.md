---
lang: pl
translation_id: obsidian-setup
publish: true
tags: 
title: Konfiguracja Obsidian
created: 2025-01-23 01:38:52
update: 2026-06-06 21:43:04
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Obsidian Setup.md
translation_source_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T20:21:46+00:00
translation_source_body_hash: bf9ce19d8ada1591527eaab93d628ac5f52f6502ff79e986249b1b03be05d9b0
translation_source_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:14:19+00:00
translation_source_localized_metadata_hash: eee2750242d12c0698089fdccf01158f1f5419251afe57cf80738860f2bf9d11
translation_source_structural_metadata_hash: 6eec0b8a6b7772bab240bcedda44bfa18061f6163b3b9475217ace91bcc065ea
---
Obsidian jest niezwykle konfigurowalny, co może stanowić wyzwanie dla nowych użytkowników.
Dostarczamy gotowy zestaw, który można od razu wykorzystać, zawierający wtyczki i motywy, a także ich dopracowane ustawienia.
Jest to podstawowy zestaw, który można dalej dostosować do indywidualnych preferencji.
Oferujemy gotowe rozwiązanie – które udokumentujemy i wyjaśnimy tutaj.

## Używane terminy
**Repozytorium (Vault)** – zbiór plików markdown i obrazów tworzących bazę wiedzy.

## Wtyczki

- Advanced Canvas
- BRAT
- Better Wordcount
- Clear unused Images
- Dataview
- Dataview Serializer
- Emoji Toolbar
- Linter
- Note Toolbar
- Tag Wrangler
- Templater
- Beautitab
- Omnisearch
- Status Bar Organizer
- Workspaces Plus
- Sortable

### Advanced Canvas
Zapewnia dostęp do wielu nowych funkcji i opcji stylizacji dla Canvas.

### BRAT
Potrzebna do instalacji nieoficjalnych wtyczek / wtyczek niezarejestrowanych w ekosystemie Obsidiana, a mianowicie:
- Dataview Serializer
- Sortable

### Better Word Count
Głównie używana ze względu na możliwość wyświetlania liczby słów/znaków w zaznaczonym tekście.
Widoczna na pasku stanu.

### Beautitab
Czysto kosmetyczna, zapewnia konfigurowalną stronę "pustej nowej karty".

### Clear unused Images
Jak sama nazwa wskazuje, pomaga w organizacji repozytorium poprzez identyfikację nieużywanych obrazów.

❗Wykluczyłem podfolder ```/site/```, aby nie usuwać zawsze obrazów z zbudowanej strony internetowej (co nie jest problemem, a raczej irytacją).

❗Zachowaj ostrożność podczas korzystania z polecenia czyszczenia załączników – spowoduje ono zawsze usunięcie ```mkdocs.yml``` oraz ```license.``` --> jeśli się to zdarzy, pliki znajdują się w folderze .trash i można je odzyskać. Ale łatwo je przeoczyć.

### Dataview
Umożliwia wykonywanie zapytań podobnych do SQL na repozytorium.

### Dataview Serializer
Konwertuje wyniki Dataview na markdown.
Pomaga w ponownym wykorzystaniu wyników zapytań Dataview w rzeczywistych notatkach.

### Emoji Toolbar
Cóż, zapewnia łatwy dostęp do emotikonów.
**Skrót ustawiony na: ALT-E**
😍

### Linter
Czyści pliki markdown i dane frontmatter.
Pomaga w utrzymaniu spójnej formy.

### Note Toolbar
Umożliwia tworzenie konfigurowalnych pasków narzędzi na górze notatki, które można zdefiniować na poziomie folderu/pliku.

### Tag Wrangler
Zapewnia dodatkowe opcje pracy z tagami.
- Zmiana nazw tagów
Pomaga w organizacji repozytorium.

### Templater
Pozwala na tworzenie niestandardowych szablonów, które można wstawiać ręcznie lub warunkowo (np. podczas tworzenia notatki).

### Status Bar Organizer
Pozwala na ukrywanie elementów na pasku stanu.

### Sortable
Umożliwia sortowanie tabel (zarówno markdown, jak i tabel Dataview) poprzez kliknięcie ich nagłówków.

### Workspaces Plus
Umożliwia łatwe szybkie przełączanie z paska stanu.

## System plików repozytorium

[System plików repozytorium](Vault%20File%20System.md){ .md-button }
