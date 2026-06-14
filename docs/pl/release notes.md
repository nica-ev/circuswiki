---
lang: pl
translation_id: release-notes
created: 2025-01-21 18:09:55
update: 2026-06-10 03:32:50
publish: true
tags: 
title: Notatki o wydaniu
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/release notes.md
translation_source_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:13:44+00:00
translation_source_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:17:00+00:00
translation_source_body_hash: 552574cc7eff1d5231818697f3e13c12302de19018f1a7f60a17252b52a71edd
translation_source_localized_metadata_hash: 7734b65772c8a40de5532cb66e4cf3344f2cc24a1de710397aaeb6ce14d0f822
translation_source_structural_metadata_hash: 48054209deb2d49a5f3283cd38424c2fba59ca058c0dd085323a92f8ef336177
---
>[!info]
>Niniejsze uwagi do wydania zawierają jedynie ogólny przegląd. Drobne zmiany (takie jak pojedyncze nowe strony czy modyfikacje istniejących treści) nie są tutaj wyszczególnione. Można je jednak dokładnie prześledzić w historii repozytorium.

>[!info]- **Wersja:** v0.04 - **Data wydania**: 9 czerwca 2026
>**Treść**
>- Znacznie rozszerzono treści wielojęzyczne: treści są teraz strukturalnie umieszczone w katalogu `docs/<język>`.
>- Dodano nowe i zaktualizowane tłumaczenia wielu opisów gier i stron projektów.
>- Zaimportowano polskie materiały warsztatowe i zintegrowano je z wielojęzyczną strukturą treści.
>- Dalsza unifikacja struktury metadanych i treści dla gier.
>
>**Techniczne**
>- Generator stron internetowych przeniesiono z MkDocs/MkDocs Material na Zensical.
>- Wprowadzono nową, wielojęzyczną strukturę budowania i stagingu.
>- Język niemiecki pozostaje językiem domyślnym bez prefiksu językowego; inne języki będą publikowane pod kodami językowymi, np. `/en/`, `/pl/`, `/es/`.
>- Wprowadzono centralną konfigurację językową za pomocą `tools/config/languages.json`.
>- Zaktualizowano wdrożenie GitHub Pages dla nowej struktury Zensical.
>- Znacznie rozszerzono lokalne narzędzia do tłumaczenia i konsolę deweloperską: kontrola poprawności, planowanie wsadowe, status tłumaczeń, widoki grafów, narzędzia nawigacyjne, przepływy pracy naprawy linków i czyszczenia.
>- Dodano przełącznik języków, wskaźniki statusu tłumaczeń i strony awaryjne dla brakujących tłumaczeń.
>- Ulepszono tabele w finalnym wyniku strony: sortowane tabele, lepsze wyświetlanie gęstych tabel i opcjonalnie zwijane sekcje stron.
>
>**Naprawiono**
>- Wewnętrzne linki i linki Markdown na przetłumaczonych stronach są zachowywane i naprawiane z większą niezawodnością.
>- Wielojęzyczna nawigacja i struktura adresów URL zostały ustabilizowane.
>- Poprawiono responsywność nawigacji, szczególnie w połączeniu z mobilnym menu hamburgerowym Zensical.

>[!info]- **Wersja:** v0.03 - **Data wydania**: 11 marca 2025
>**Treść**
>- Dodano brakujące opisy gier.
>
>**Techniczne**
>- Dodano favicon i logo.
>- Przeprojektowano interfejs użytkownika.
>- Nawigacja pierwszego poziomu znajduje się teraz w nagłówku strony, podczas gdy prawy pasek nawigacyjny jest dostosowywany kontekstowo.
>- Tabele można sortować, klikając na nagłówki.
>
>**Naprawiono**
>- Tagowanie działa ponownie.

>[!info]- **Wersja:** v0.02 - **Data wydania**: 26 lutego 2025
>**Techniczne**
>- Funkcja bloga.
>- Analityka (Google).
>- Baner dotyczący plików cookie.
>- Widżet opinii (na dole każdej strony).

>[!info]- **Wersja:** v0.01 - **Data wydania** 15 stycznia 2025
>**Treść**
>- Dodano 150 opisów gier.
>- Podstawowy opis dokumentacji.
>
>**Techniczne**
>- Podstawowa konfiguracja dla MkDocs i MkDocs-materials.
>- Wsparcie dla Obsidian z MkDocs-publisher (umożliwia korzystanie z Markdown Obsidian, takich jak linki Markdown, pola wywołań).
