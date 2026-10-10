---
lang: pl
translation_id: beancount/13-glossary
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Słowniczek
description: Definicje terminów księgowych, Beancount, Fava i księgowości projektowej używanych w tej dokumentacji.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/13-glossary.md
translation_source_body_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_source_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:08:56+00:00
translation_source_localized_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_source_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:08:56+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 13 - Słowniczek

## Konto

Nazwane miejsce, w którym Beancount rejestruje pieniądze lub wartość. Przykład: `Ausgaben:Buero:Miete`.

## Aktywa

Coś, co stowarzyszenie posiada lub kontroluje, na przykład pieniądze na koncie bankowym, saldo PayPal, gotówka lub zapasy. W tym systemie aktywa znajdują się pod `Vermoegen`.

## Sprawdzenie salda

Linia potwierdzająca, że konto ma określone saldo w określonym dniu. Sprawdzenia salda służą do weryfikacji, czy księga rachunkowa zgadza się z zapisami bankowymi, PayPal lub gotówkowymi.

## Bank Dump

Obszar tymczasowy w dolnej części księgi, do którego najpierw wkleja się zaimportowane transakcje bankowe przed ich pełną klasyfikacją.

## Beancount

Format księgowości w postaci zwykłego tekstu, używany jako źródło prawdy w systemie.

## CSV

Plik eksportu przypominający arkusz kalkulacyjny. Sparkasse eksportuje pliki CSV, które są konwertowane na transakcje Beancount.

## Kapitał własny

Rodzina kont Beancount używana do sald początkowych i bilansowania historycznych punktów wyjścia.

## Fava

Interfejs przeglądarki do przeglądania i pracy z księgami Beancount.

## Pulpity Fava

Rozszerzenie dodające niestandardowe strony pulpitów nawigacyjnych do Fava.

## Freies-Geld

Wolne lub nieograniczone pieniądze, które nie są przypisane do budżetu ograniczonego projektu.

## Przychody

Otrzymane pieniądze. W tym systemie konta przychodów zaczynają się od `Einnahmen`.

## Księga rachunkowa

Plik księgowy zawierający konta, transakcje, sprawdzenia sald i dokumenty. Główne księgi to `nica.beancount` i `2023.beancount`.

## Zobowiązania

Pieniądze należne komuś innemu. W tym systemie zobowiązania znajdują się pod `Verbindlichkeiten`.

## Wystawca płatności

Osoba lub organizacja wymieniona w transakcji.

## Konto projektu

Konto używane do śledzenia pieniędzy na konkretny projekt, oddzielnie od ogólnych pieniędzy stowarzyszenia.

## Uzgodnienie

Proces sprawdzania, czy Beancount zgadza się z rzeczywistym saldem bankowym lub PayPal.

## Potwierdzenie płatności

Dokument potwierdzający wydatek, taki jak faktura, umowa lub paragon.

## Sonstiges

Niemieckie słowo oznaczające "różne" lub "inne". Przydatne jako tymczasowe rozwiązanie awaryjne, ale konkretne kategorie są lepsze do ostatecznego księgowania.

## Transakcja

Oznaczony datą wpis księgowy opisujący jedno zdarzenie finansowe.

## Verwendungsnachweis

Raport fundatora projektu wyjaśniający, jak zostały wykorzystane przyznane środki.
