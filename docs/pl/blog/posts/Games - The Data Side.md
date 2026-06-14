---
lang: pl
translation_id: blog/posts/games-the-data-side
created: 2025-01-21 18:09:55
update: 2026-06-09 17:06:42
date: 2025-03-18T02:14:00
publish: true
tags: 
title: Gry - Strona danych
description: Jak opisy gier zostały znormalizowane i uczynione bardziej dynamicznymi przy użyciu metadanych i wtyczek Obsidian.
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Games - The Data Side.md
translation_source_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-10T20:00:26+00:00
translation_source_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:40:53+00:00
translation_source_body_hash: b13a5e3bb0cc33ef0b3c6817aeb5e20eca7fb6f23d360373ed8cf7c5631dcff0
translation_source_localized_metadata_hash: 262d87a742385ccade0b7f56eef78a0bd97b6bb6b9bb2f05168393c72df587fb
translation_source_structural_metadata_hash: 6d067079ae1d1598e9306f517260d15351df3045ab315112fd921ab0e185903b
---
# **Gry – Aspekt danych**
**Jak opisy gier zostały ustandaryzowane i uczynione bardziej dynamicznymi dzięki metadanym i wtyczkom Obsidian.**

Jeśli chodzi o zarządzanie treścią, kluczowa jest spójność. W pierwszej dużej części tego projektu zająłem się grami – około 170 z nich, każda z własnym, unikalnym formatem, stylem i dostępnością. Problem? Wiele z tych opisów opierało się na zakodowanych na stałe, statycznych linkach, co sprawiało, że dodawanie nowych gier lub dostosowywanie struktury było koszmarem.

Więc podwinąłem rękawy i zabrałem się do pracy.
<!-- more -->
## Krok 1: Jednolity format
Pierwszym zadaniem było ustanowienie spójnego formatu dla wszystkich opisów gier. Zainspirowałem się „Tasifan Spielebuch” (Księga Gier Tasifan), dobrze zorganizowanym źródłem opisów gier. Aby uczynić rzeczy jeszcze bardziej przyjaznymi dla użytkownika, dodałem krótkie podsumowania, dzięki czemu wszystkie kluczowe szczegóły są widoczne na pierwszy rzut oka – nawet w podglądzie.

Ale prawdziwą rewolucją? Metadane.

## Krok 2: Magia metadanych
Teraz wszystkie kluczowe informacje – liczba graczy, materiały, czas trwania i inne – są przechowywane jako metadane na górze każdego pliku Markdown w formacie zwanym YAML (lub frontmatter). To nie tylko utrzymuje porządek, ale także sprawia, że dane są wielokrotnego użytku w całym systemie.

Aby ułatwić znalezienie odpowiedniej gry, wdrożyłem prostą, ale skuteczną logikę:
1. **Wybierz kategorię**: Jakiego rodzaju gry szukasz? Gra wyciszająca? Gra w berka? Coś do budowania zespołu? Stworzyłem zestaw kategorii na początek, ale można je dostosowywać lub rozszerzać w miarę potrzeb.
2. **Przeglądaj tabelę**: Po wybraniu kategorii zobaczysz tabelę zawierającą wszystkie pasujące gry. Tabela jest sortowalna – wystarczy kliknąć nagłówki, aby uporządkować według czasu trwania, trudności lub innych kryteriów.

A oto najlepsze: wiele gier pojawia się w wielu kategoriach, więc nigdy nie jesteś ograniczony tylko do jednego sposobu znalezienia tego, czego potrzebujesz.

## Tabele nie do końca dynamiczne
Prawdziwa magia dzieje się dzięki dwóm wtyczkom Obsidian: **Dataview** i **Dataview Serializer**.

Dataview pozwala mi tworzyć dynamiczne listy i tabele za pomocą zapytań podobnych do bazodanowych. Haczyk? Te tabele działają tylko w Obsidian, ponieważ bazowe pliki Markdown nie są modyfikowane.

Wchodzi Dataview Serializer. Ta wtyczka konwertuje te dynamiczne tabele do statycznego formatu Markdown i zapisuje je bezpośrednio w pliku. Kiedy strona jest budowana za pomocą MkDocs, tabele są statyczne, ale zostały zasadniczo wygenerowane dynamicznie offline.

Te zapytania mogą być dość złożone, pozwalając mi wyszukiwać lub wyświetlać określone części wiki – takie jak wszystkie opisy gier lub artykuły napisane przez konkretnego autora. A ponieważ aktualizują się automatycznie (poprzez krok serializacji), dodawanie nowych informacji i budowanie nawigacyjnej struktury jest dziecinnie proste.

Ale nie wszystko jest idealne. Proces nie jest w pełni automatyczny. Dataview Serializer może nadpisać plik tylko wtedy, gdy jest on otwarty w Obsidian. Na razie jest to wykonalne – oznaczyłem każdą stronę z dynamiczną tabelą lub listą, co ułatwia ich przeglądanie. Ale jeśli liczba tych stron znacznie wzrośnie, być może będę musiał przemyśleć podejście.

## Narzędzia i modele językowe
Oryginalne opisy gier były mieszanką pod względem formatowania i jakości. Aby usprawnić proces, zwróciłem się do modeli językowych (LLM). Stworzyłem specyficzny prompt, wraz z przykładowym formatowaniem, aby zapewnić, że sama treść nie zostanie zmieniona (bez niepotrzebnych przepisów). Mimo to, ręcznie przeglądałem każdy wynik i dokonywałem drobnych korekt tam, gdzie było to potrzebne.

Oto wnioski: przy prawidłowym użyciu te narzędzia są *niezwykle* potężne. Kluczem jest precyzja i celowość w sposobie formułowania zadań.

Ostateczne zmiany dotyczą głównie formatowania – sposobu prezentacji informacji i opisów gier. Metadane jednak zostały wprowadzone ręcznie. Ponieważ i tak musiałem wszystko dwukrotnie sprawdzić, zrobienie tego ręcznie było w tym przypadku szybsze.

Jest to jednak powolny proces. Pracując w niepełnym wymiarze godzin, udaje mi się przetworzyć około 10-15 gier dziennie. Postęp jest stały, ale zajmie to trochę czasu.

## Wyzwania na przyszłość
Jedną z potencjalnych przeszkód są tłumaczenia. Zapytania wyszukiwania musiałyby zostać dostosowane, aby znaleźć wersje gier lub tagów specyficzne dla danego języka. Na razie można sobie z tym poradzić ręcznie, ale jeśli system się rozrośnie, automatyzacja może być konieczna.

Tłumaczenie to złożony temat, do którego wrócę innym razem.

## Po co się w to bawić?
Krótka odpowiedź? Skalowalność.

Ten system jest zaprojektowany do rozwoju. Standaryzując format, wykorzystując metadane i stosując dynamiczne narzędzia, stworzyłem fundament, który może obsłużyć więcej treści, nie stając się nieporęcznym.

## Co jeszcze nowego?
Funkcja wyszukiwania doczekała się kilku ulepszeń:
- **Autouzupełnianie**: Podczas pisania wyszukiwanie sugeruje zapytania, które dają najwięcej trafień. Nie opiera się to na zachowaniu użytkownika – nie śledzimy wyszukiwań – ale na statycznym indeksie wyszukiwania generowanym podczas budowania strony.
- **Zapisane wyszukiwania**: Kliknij małą ikonę obok paska wyszukiwania, a Twoje zapytanie (i wyniki) zostaną zapisane w adresie URL. Dodaj go do zakładek, a za każdym razem uzyskasz te same wyniki.

To mała funkcja, ale może okazać się niezwykle przydatna w miarę rozwoju wiki i obejmowania przez nią coraz bardziej zróżnicowanych tematów.
