---
lang: pl
translation_id: github-for-users
publish: true
tags:
  - github
  - tutorial
created: 2025-01-18 23:14:04
update: 2026-06-12 18:26:00
title: Współpraca bezpośrednio w repozytorium GitHub
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/github-for-users.md
translation_source_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-12T17:31:04+00:00
translation_source_body_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_source_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:51:15+00:00
translation_source_localized_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_source_structural_metadata_hash: 69966c4b32b093dc5fdaa8e7127a710d8477892c36f2859ba38215866bb73327
---
> [!info] Krótko mówiąc
> Ta strona jest przeznaczona dla osób, które chcą bezpośrednio pracować z plikami Markdown w CircusWiki. Do zwykłego dodawania treści nie potrzebujesz tej ścieżki: materiały możesz po prostu wysłać e-mailem.

Bezpośrednia współpraca przez GitHub jest praktyczna, jeśli chcesz regularnie poprawiać strony, tworzyć nowe pliki Markdown lub pracować z repozytorium CircusWiki w edytorze takim jak Obsidian.

Jeśli chcesz dodać tylko grę, metodę, plik PDF, link lub poprawkę, prostsza droga jest zazwyczaj lepsza:

[Powrót do „Jak pomóc”](mitmachen.md){ .md-button }

## Czego potrzebujesz

- Darmowe konto GitHub: [https://github.com/join](https://github.com/join)
- Opcjonalnie GitHub Desktop: [https://desktop.github.com/](https://desktop.github.com/)
- Edytor tekstu dla plików Markdown, na przykład Obsidian, VS Code lub prosty edytor

GitHub Desktop nie jest obowiązkowy, ale dla wielu osób jest łatwiejszy niż wiersz poleceń.

## Znajdź repozytorium

Publiczne repozytorium znajduje się tutaj:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Znajdują się tam właściwe pliki Markdown, obrazy, tłumaczenia i narzędzia, z których budowana jest strona internetowa.

## Sposób pracy w skrócie

Typowy przebieg wygląda następująco:

1. Sklonuj repozytorium na GitHubie.
2. Skopiuj swoje repozytorium na własny komputer.
3. Wprowadź zmiany w nowej gałęzi (branch).
4. Edytuj pliki lub twórz nowe pliki Markdown.
5. Zatwierdź zmiany (commit).
6. Prześlij gałąź do GitHub.
7. Otwórz Pull Request, aby zmiana mogła zostać sprawdzona i zaakceptowana.

## Krok po kroku z GitHub Desktop

### 1. Sklonuj repozytorium

Otwórz repozytorium CircusWiki na GitHubie:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Kliknij `Fork`. Spowoduje to utworzenie własnej kopii repozytorium na Twoim koncie GitHub. W tej kopii możesz pracować, nie modyfikując bezpośrednio głównego projektu.

### 2. Skopiuj repozytorium

Otwórz GitHub Desktop i wybierz:

```text
File -> Clone repository...
```

Wybierz swój fork `nica-ev/circuswiki` i określ folder na swoim komputerze.

Następnie będziesz mieć lokalną kopię plików.

### 3. Utwórz gałąź (branch)

Dla swojej zmiany najlepiej utwórz osobną gałąź, na przykład:

```text
opis-gry-dodaj
popraw-link
nowa-metoda-balansowanie
```

Gałąź utrzymuje Twoją pracę oddzielnie od głównego stanu. Ułatwia to późniejsze przeglądanie.

### 4. Edytuj pliki

Publiczne treści znajdują się głównie w folderach językowych pod `docs/`:

```text
docs/de/
docs/en/
docs/es/
docs/pl/
...
docs/img/
```

Wszystkie języki są równoważne. Nie ma głównego języka, w którym treści muszą być tworzone od podstaw.

Jeśli tworzysz nową oryginalną stronę, umieść ją w folderze językowym, w którym napisany jest tekst. Na przykład hiszpański tekst oryginalny należy do `docs/es/`, niemiecki do `docs/de/`, a angielski do `docs/en/`.

Ważne jest „frontmatter” na początku pliku. Tam musi być widoczne, że strona jest oryginalna, na przykład:

```yaml
translation_status: original
translation_source_lang: es
```

`translation_source_lang` odpowiada językowi tekstu oryginalnego. Z tego oryginału można później automatycznie generować tłumaczenia na wszystkie obsługiwane języki.

Podczas edycji zwróć uwagę na następujące kwestie:

- Nie usuwaj „frontmatter” na początku pliku.
- W przypadku nowych oryginalnych stron ustaw `translation_status: original` i odpowiedni `translation_source_lang`.
- W miarę możliwości zachowaj istniejące linki.
- Nie publikuj danych osobowych, kluczy API ani notatek wewnętrznych.
- Używaj obrazów tylko wtedy, gdy prawa do ich wykorzystania są jasne.
- Lepiej wprowadzać małe, jasne zmiany niż bardzo duże, mieszane zmiany.

### 5. Zatwierdź zmiany (commit)

W GitHub Desktop zobaczysz swoje zmienione pliki w sekcji `Changes`.

Napisz krótkie podsumowanie, na przykład:

```text
Poprawiono listę materiałów w grze ruchowej
Dodano wskazówkę bezpieczeństwa do Beigoma
Dodano nowy opis gry
```

Następnie kliknij `Commit to <branch-name>`.

### 6. Prześlij zmiany

Kliknij `Push origin`, aby przesłać swoją gałąź do GitHub.

### 7. Otwórz Pull Request

GitHub Desktop lub GitHub w przeglądarce zaproponuje następnie utworzenie Pull Request.

Pull Request oznacza: proponujesz swoją zmianę do głównego repozytorium. Zmiana zostanie sprawdzona, ewentualnie skomentowana, a następnie zaakceptowana lub dalej rozwijana.

## Podstawy Markdown

Markdown to prosty format tekstowy. Najważniejsze znaki wystarczą do większości wpisów:

```markdown
# Duży nagłówek
## Podtytuł sekcji

Zwykły tekst z **pogrubieniem** i *kursywą*.

- Punkt listy
- Kolejny punkt listy

[Tekst linku](https://www.example.com)
```

## Jeśli coś jest niejasne

Nie musisz od razu perfekcyjnie znać bezpośredniej współpracy przez GitHub. Jeśli otworzysz Pull Request, a coś jeszcze nie jest poprawne, można to wyjaśnić w przeglądzie.

Jeśli chcesz tylko dodać treść, a droga techniczna wydaje się zbyt skomplikowana, po prostu skorzystaj z adresu e-mail na [stronie „Jak pomóc”](mitmachen.md).
