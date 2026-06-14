---
lang: pl
translation_id: doc-sys-2
publish: true
tags: 
created: 2025-01-20 02:58:43
update: 2025-04-13 21:47:35
title: System dokumentacji
authors:
  - Marc Bielert
description:
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/doc-sys-2.md
translation_source_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T20:11:33+00:00
translation_source_body_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_source_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:47:07+00:00
translation_source_localized_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_source_structural_metadata_hash: 12f0cb572b5daceba17f262576f82a2900f2588e247dd6c9743ac6c09aba134f
---
[Manifest](doc-sys-manifest.md){ .md-button }
[Obsidian Setup](Obsidian%20Setup.md){ .md-button }
## Architektura systemu

Ogólna idea
> [!info] Przegląd architektury
>
> Oto graficzna reprezentacja architektury systemu:
>```mermaid
>flowchart LR
>A(Treści) --> B(Kontrola wersji)
>C(Oprogramowanie do edycji) --> A
>A --> D(Udostępnianie online)
>```

Szczegółowo:

> [!info] Przegląd architektury
>```mermaid
>flowchart LR
>A[Obsidian] <--> B{Pliki}
>B <--> C(Github Desktop)
>C <--> D{Github}
>B <--> E(MkDocs)
>D --> F(Github Pages)
>G(Motyw: MkDocs-Material) --> E
>H(MkDocs-Publisher) --> E
>E --> D
>```
>
> *   **Obsidian:** Opcjonalny, ale zalecany przeze mnie edytor tekstu do edycji plików Markdown.
> *   **Pliki:** Pliki Markdown zawierające treść mojej dokumentacji.
> *   **Github Desktop:** Narzędzie do łatwego zarządzania moimi repozytoriami Git.
> *   **Github:** Usługa online do kontroli wersji i współpracy.
> *   **Github Pages:** Bezpłatna usługa do publikowania mojej strony internetowej.
> *   **MkDocs:** Narzędzie do automatycznego tworzenia strony internetowej z moich plików Markdown.
> *   **MkDocs-Material:** Motyw dla MkDocs, który zapewnia nowoczesny i atrakcyjny wygląd.
> *   **MkDocs-Publisher**: Zbiór wtyczek ułatwiających współpracę z Obsidianem i oferujących dodatkowe funkcje.

## Komponenty w szczegółach

### 1. Markdown

> [!info] Markdown jako podstawa
> Używam [formatu Markdown](Markdown.md) do mojej dokumentacji. Markdown to prosty język znaczników, który pozwala mi na dodawanie prostych formatowań do tekstu (np. nagłówków, list, linków).

**Zalety:**

*   Jest łatwy do nauczenia i użycia, co pozwala mi skupić się na treści.
*   Jest niezależny od platformy, dzięki czemu mogę kontynuować pracę na dowolnym urządzeniu.
*   Jest idealny do kontroli wersji, co pozwala mi śledzić i zarządzać zmianami.
*   Jest przyszłościowy i nie jest zastrzeżony, co daje mi pewność, że moja praca pozostanie dostępna w dłuższej perspektywie.

[Markdown](Markdown.md){ .md-buttons }

### 2. Obsidian

> [!info] Obsidian jako edytor tekstu
> [Obsidian](Obsidian%20Setup.md) to opcjonalny, ale zalecany przeze mnie edytor tekstu. Oferuje mi następujące korzyści:

*   Mogę przechowywać moje dane lokalnie i edytować je offline, co daje mi elastyczność i kontrolę.
*   Mogę łatwo linkować i łączyć pliki ze sobą, co pomaga mi organizować złożone informacje.
*   Mogę dodawać tagi do plików i łatwo nimi zarządzać, co daje mi dodatkowy wymiar organizacji.
*   Mogę wizualizować moje dane graficznie, co pomaga mi dostrzegać wzorce i relacje.
*   Mogę rozszerzać funkcjonalność Obsidian za pomocą wtyczek, co pozwala mi dostosować narzędzie do moich specyficznych potrzeb.

### 3. Git i Github

> [!info] Git do kontroli wersji
> [Git](https://git-scm.com/) to system kontroli wersji, który pozwala mi śledzić i zarządzać zmianami w dokumentacji. [Github](https://github.com/) to usługa online, która pozwala mi przechowywać moje repozytoria Git i współpracować z innymi.

**Zalety:**

*   Kontrola wersji: Każda zmiana jest dokumentowana i może być śledzona w dowolnym momencie, co pomaga mi unikać błędów i zachować porządek.
*   Współpraca: Wiele osób może jednocześnie pracować nad dokumentacją, co daje mi możliwość integracji informacji zwrotnych i wkładu od innych.
*   Kopia zapasowa: Moja dokumentacja jest bezpieczna i regularnie tworzone są jej kopie zapasowe, co daje mi pewność, że moja praca nie zostanie utracona.

### 4. Github Desktop

> [!info] Github Desktop jako narzędzie
> [Github Desktop](../_inbox/Github%20Desktop.md) to graficzny interfejs dla Git, który pozwala mi łatwo korzystać z Git bez użycia linii komend.

**Zalety:**

*   Łatwość obsługi, co ułatwia mi korzystanie z Git.
*   Nie wymaga znajomości linii komend, co oszczędza mi czas i wysiłek.
*   Upraszcza mój przepływ pracy, co pozwala mi skupić się na tworzeniu treści.

### 5. MkDocs

> [!info] MkDocs jako generator stron internetowych
> [MkDocs](https://mkdocs.org) to statyczny generator stron, który konwertuje moje pliki Markdown na statyczną stronę internetową.

**Zalety:**

*   Łatwe tworzenie stron internetowych, co pozwala mi szybko i łatwo publikować moją dokumentację.
*   Szybkie aktualizacje, co pozwala mi widzieć zmiany w czasie rzeczywistym.
*   Spójny układ, co zapewnia profesjonalny i jednolity wygląd mojej dokumentacji.
*   Podgląd offline, co pozwala mi sprawdzić moją dokumentację przed jej opublikowaniem.

### 6. Github Pages

> [!info] Github Pages do hostingu
> [Github Pages](../_inbox/Github%20Pages.md) to bezpłatna usługa hostingowa od Github, która pozwala mi łatwo publikować moją stronę internetową online.

**Zalety:**

*   Bezpłatny hosting, co pozwala mi publikować moją dokumentację bez dodatkowych kosztów.
*   Łatwe publikowanie, co zdejmuje ze mnie techniczne zadanie publikacji.
*   Niezawodność, co daje mi pewność, że moja dokumentacja jest zawsze dostępna.

### 7. MkDocs-Material

> [!info] MkDocs-Material jako motyw
> [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) to motyw dla MkDocs, który zapewnia nowoczesny i atrakcyjny wygląd.

**Zalety:**

*   Nowoczesny design, który sprawia, że moja dokumentacja wygląda profesjonalnie i nowocześnie.
*   Możliwość dostosowania, co pozwala mi dostosować układ do moich specyficznych potrzeb.
*   Przyjazny dla użytkownika, co ułatwia korzystanie z dokumentacji.

### 8. MkDocs-Publisher

> [!info] MkDocs-Publisher jako zbiór wtyczek
> [MkDocs-Publisher](https://github.com/mkdocs-publisher/mkdocs-publisher) to zbiór wtyczek MkDocs, które ułatwiają współpracę z Obsidianem i oferują dodatkowe funkcje.

**Zalety:**

- **Uproszczona integracja z Obsidianem:** Automatyczne dostosowywanie składni Markdown Obsidiana (wywołania, linki wiki itp.).
- **Rozszerzone metadane:** Integracja tagów i kategorii z frontmatter Obsidiana.

## Przepływ pracy

> [!info] Mój przepływ pracy
> Oto mój typowy przepływ pracy:

1.  Tworzę i edytuję pliki Markdown za pomocą edytora tekstu (opcjonalnie Obsidian).
2.  Zapisuję pliki Markdown lokalnie.
3.  Przesyłam moje zmiany do repozytorium Git za pomocą Github Desktop.
4.  Automatycznie generuję stronę internetową za pomocą MkDocs.
5.  Publikuję stronę internetową za pomocą Github Pages.

## System plików

> [!info] Struktura katalogów
> Oto struktura katalogów mojego systemu:
>
> ```
>/docs/     (Tutaj znajdują się moje pliki Markdown)
>/site/     (Tutaj generowana jest strona internetowa)
>license    (Informacje o licencji)
>mkdocs.yml (Plik konfiguracyjny dla MkDocs)
>readme.md  (Plik opisujący repozytorium)
>```

## Alternatywy dla tworzenia treści

> [!info] Alternatywy dla tworzenia treści
> Jestem świadomy, że nie każdy zna Markdown i Git. Dlatego oferuję następujące alternatywy:

1.  **Wordpress:** Treści można tworzyć w Wordpress jako strony.
2.  **Plik tekstowy, plik Word:** Treści można tworzyć jako plik tekstowy, plik Word (lub w innych typowych formatach).

W tych przypadkach mogę następnie zaimplementować treści w systemie.
