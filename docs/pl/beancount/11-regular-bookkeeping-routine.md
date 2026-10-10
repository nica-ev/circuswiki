---
lang: pl
translation_id: beancount/11-regular-bookkeeping-routine
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Regularna Rutyna Księgowa
description: Praktyczna, powtarzalna lista kontrolna do bieżącego prowadzenia ksiąg.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/11-regular-bookkeeping-routine.md
translation_source_body_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_source_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:43+00:00
translation_source_localized_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_source_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:43+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 11 - Regularna rutyna księgowa

Ta strona opisuje praktyczną rutynę prowadzenia bieżących ksiąg rachunkowych.

## Tygodniowa lub dwutygodniowa rutyna

Używaj tej rutyny, gdy występują regularne ruchy na koncie bankowym.

1. Otwórz odpowiednią instancję Fava.
2. Sprawdź, czy Fava nie wyświetla błędów.
3. Znajdź ostatnie sprawdzenie salda.
4. Wyeksportuj nowe dane CSV z Sparkasse.
5. Przekonwertuj CSV za pomocą `csv2bean.py`.
6. Wklej nowe wpisy do `Bank Dump`.
7. Przypisz wpisy do odpowiednich kont.
8. Dołącz lub odwołaj się do dowodów księgowych tam, gdzie jest to potrzebne.
9. Dodaj nowe sprawdzenie salda.
10. Przeładuj Fava i rozwiąż błędy.
11. Przejrzyj `Ausgaben:Sonstiges` (Wydatki:Inne) i `Einnahmen:Sonstiges` (Przychody:Inne) w poszukiwaniu wpisów, które powinny być bardziej szczegółowe.

## Miesięczna rutyna

Na koniec miesiąca:

1. Uzgodnij saldo konta Sparkasse.
2. Uzgodnij saldo PayPal, jeśli jest używane.
3. Uzgodnij saldo kasy, jeśli używano gotówki.
4. Sprawdź otwarte zobowiązania wobec osób.
5. Sprawdź salda aktywnych projektów.
6. Przejrzyj nieprzypisane wpisy w `Sonstiges`.
7. Sprawdź brakujące dowody księgowe.
8. Sprawdź, czy jakieś zakończone projekty powinny zostać przygotowane do zamknięcia.

## Rutyna raportowania projektów

Przed przygotowaniem raportu projektowego lub sprawozdania z wykorzystania środków (Verwendungsnachweis):

1. Otwórz strony kont projektowych w Fava.
2. Wyeksportuj lub przejrzyj wszystkie przychody i wydatki projektu.
3. Potwierdź, że kategorie odpowiadają liniom budżetowym fundatora.
4. Potwierdź, że wszystkie dowody księgowe i dokumenty dotyczące honorariów są dostępne.
5. Sprawdź, czy zwroty, anulowania i refundacje są księgowane jako korekty, a nie jako fałszywe przychody.
6. Potwierdź, że saldo aktywów projektu jest zrozumiałe.
7. Jeśli projekt został zakończony, prawidłowo przenieś pozostałe środki i zamknij konta projektowe.

## Roczna rutyna

Na koniec roku:

1. Uzgodnij wszystkie konta bankowe.
2. Uzgodnij saldo PayPal.
3. Uzgodnij salda kas.
4. Sprawdź zobowiązania.
5. Sprawdź otwarte salda projektów.
6. Upewnij się, że wszystkie dowody księgowe są przechowywane i powiązane lub możliwe do odnalezienia.
7. Przejrzyj kategorie przychodów i wydatków.
8. Dodaj końcowe sprawdzenia salda.
9. Przygotuj raporty z Fava.
10. Zarchiwizuj wyeksportowane pliki CSV i dokumenty pomocnicze.

## Kontrole jakości

Księgi rachunkowe są w dobrym stanie, gdy:

- Fava otwiera się bez błędów.
- Ostatnie sprawdzenie salda Sparkasse zgadza się z bankiem.
- Salda PayPal i kasy są sprawdzane tam, gdzie ma to zastosowanie.
- Salda projektów są zamierzone i zrozumiałe.
- Zamknięte projekty mają zerowe saldo aktywów.
- Konta `Sonstiges` nie zawierają możliwych do uniknięcia niekategoryzowanych wpisów.
- Dowody księgowe dla wydatków można znaleźć.
- Komentarze wyjaśniają nietypowe korekty lub założenia.

## Lista kontrolna przekazania innej osobie

Przed przekazaniem księgowości innej osobie:

- Pokaż jej odpowiedni plik księgowy dla każdego stowarzyszenia.
- Pokaż jej, jak uruchomić Fava.
- Pokaż jej ostatnie sprawdzenie salda.
- Pokaż jej, jak importowane są pliki CSV w `Bank Dump`.
- Pokaż jej, gdzie przechowywane są dowody księgowe.
- Pokaż jej jeden przykładowy projekt od przychodów z finansowania do ostatecznego zamknięcia.
- Wskaż jej folder z tą dokumentacją.
