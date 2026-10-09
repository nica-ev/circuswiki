---
lang: pl
translation_id: beancount/04-beancount-basics-for-users
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Podstawy Beancount dla użytkowników
description: Wprowadzenie do formatu tekstowego Beancount i wzorców transakcji używanych w księgach.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/04-beancount-basics-for-users.md
translation_source_body_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_source_hash: 58d98cd465879b982a68fc0bd2e47a0655c4f65bf1b7b7b0add5c529be8962b4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:35:49+00:00
translation_source_localized_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_source_metadata_hash: 4a8690c7cf2155515e8fc2b879e86e67bdd013e0fcf37e4bce4cf777d8522105
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:35:49+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 04 - Podstawy Beancount dla użytkowników

Beancount przechowuje księgowość w postaci czytelnego tekstu. Każda transakcja informuje, co się wydarzyło, kiedy, kto był zaangażowany i które konta się zmieniły.

## Podstawowy format transakcji

```beancount
2026-01-13 ! "Tragerwerk Soziale Dienste in Sachsen-Anhalt GmbH" "RgNr. T-2504"
  Vermoegen:Bank:Sparkasse-Tohuwabohu:Freies-Geld  680.00 EUR
  Einnahmen:Sonstiges
```

| Część | Znaczenie |
| --- | --- |
| `2026-01-13` | Data transakcji. |
| `!` | Znacznik statusu. W tym systemie jest powszechnie używany dla wpisów zaimportowanych lub jeszcze nieostatecznie przejrzanych. |
| Pierwszy tekst w cudzysłowie | Odbiorca lub nadawca. |
| Drugi tekst w cudzysłowie | Opis lub tekst księgowy z banku. |
| Pierwsza linia konta | Miejsce, skąd pieniądze przyszły lub dokąd poszły. |
| Druga linia konta | Przeciwstawna kategoria. Jeśli nie podano kwoty, Beancount oblicza ją automatycznie. |

## Nazwy kont

Nazwy kont są oddzielone dwukropkami:

```text
Vermoegen:Bank:Sparkasse-NICA:Freies-Geld
```

Czytaj od lewej do prawej: aktywa, konto bankowe, Sparkasse NICA, wolne środki.

## Pięć rodzin kont

| Rodzina | Znaczenie | Przykład |
| --- | --- | --- |
| `Vermoegen` | Aktywa: bank, PayPal, gotówka, zapasy. | `Vermoegen:Bank:Sparkasse-NICA` |
| `Verbindlichkeiten` | Zobowiązania: pieniądze należne ludziom lub innym. | `Verbindlichkeiten:Person:Marc-Bielert` |
| `Equity` | Salda początkowe i wpisy wyrównujące. | `Equity:Opening-Balances` |
| `Einnahmen` | Przychody. | `Einnahmen:Vereinsbeitrag` |
| `Ausgaben` | Wydatki. | `Ausgaben:Buero:Miete` |

## Znaki przychodów i wydatków

W raportach Beancount przychody często pojawiają się wewnętrznie ze znakiem ujemnym, a wydatki ze znakiem dodatnim. Fava i pulpity nawigacyjne często prezentują te wartości w sposób bardziej przyjazny dla użytkownika. Nie zmieniaj transakcji tylko dlatego, że liczba przychodów wygląda na ujemną w surowym zapytaniu.

## Sprawdzanie salda

Sprawdzenie salda stwierdza, że konto musi mieć określone saldo w danym dniu:

```beancount
2026-03-13 balance Vermoegen:Bank:Sparkasse-NICA 1234.56 EUR
```

Jeśli Beancount nie może dopasować tego salda z transakcji sprzed tej daty, Fava wyświetli błąd. Sprawdzanie salda jest głównym mechanizmem kontroli jakości.

## Otwieranie i zamykanie kont

Zanim konto zostanie użyte, jest otwierane:

```beancount
2025-04-01 open Ausgaben:Projekt:25-ZGV:Honorar
```

Gdy projekt zostanie zakończony, a konto projektu będzie miało saldo zero, można je zamknąć:

```beancount
2026-02-27 close Ausgaben:Projekt:TOHUCON-25
```

Zamknięte konta zazwyczaj nie powinny otrzymywać nowych transakcji.

## Komentarze i dokumenty

Linie zaczynające się od `;` to komentarze. Wyjaśniają one decyzje lub niepewne sytuacje i nie wpływają na liczby.

Potwierdzenia można powiązać za pomocą linii `document`:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```
