---
lang: pl
translation_id: translating-pdf-documents
created: 2025-05-03 21:32:10
update: 2025-05-03 22:24:12
publish: true
tags:
  - tutorial
title: Tłumaczenie dokumentów PDF za pomocą dużych modeli językowych
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Translating PDF Documents.md
translation_source_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-14T19:33:09+00:00
translation_source_body_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_source_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T19:33:09+00:00
translation_source_localized_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_source_structural_metadata_hash: 2b0fe62dfc02049e3f55e308c77f83a911789c48b0827769d60d3f00737d38b6
---
# Samouczek: Tłumaczenie dokumentów PDF za pomocą dużych modeli językowych

## Wprowadzenie

Niniejszy samouczek przedstawia proces tłumaczenia zawartości dokumentów PDF, szczególnie tych zawierających tekst oparty na obrazach, który nie podlega zaznaczeniu, przy użyciu dużych modeli językowych (LLM). Przepływ pracy obejmuje optymalizację PDF, ekstrakcję tekstu za pomocą optycznego rozpoznawania znaków (OCR), tłumaczenie tekstu, a na końcu ponowne formatowanie tłumaczenia do postaci PDF.

**Wymagania wstępne:**

*   Konto Google (do dostępu do Google AI Studio).
*   Opcjonalnie: Oprogramowanie do optymalizacji PDF (np. pdf24 Creator).
*   Opcjonalnie: Edytor tekstu lub procesor tekstu zdolny do obsługi Markdown i eksportu do PDF (np. Obsidian, Microsoft Word).

## Krok 1: Przygotowanie dokumentu PDF

**Cel:** Zmniejszenie rozmiaru pliku PDF w celu optymalizacji jego przetwarzania przez LLM przy jednoczesnym zachowaniu czytelności tekstu. LLM często mają ograniczenia dotyczące rozmiaru wejściowego, a mniejsze pliki przetwarzają się wydajniej.

**Uwagi:**

*   **PDF-y tekstowe:** Jeśli tekst w pliku PDF można zaznaczyć (co oznacza, że jest osadzony elektronicznie), zmniejszenie rozmiaru pliku jest zazwyczaj łatwiejsze i można osiągnąć mniejsze rozmiary bez utraty jakości.
*   **PDF-y oparte na obrazach:** Jeśli strony PDF są obrazami tekstu (tekstu nie można zaznaczyć indywidualnie), zmniejszenie rozmiaru obejmuje kompresję obrazu. Należy uważać, aby nie zmniejszyć jakości na tyle, aby tekst stał się nieczytelny dla OCR.

**Procedura (Przykład z użyciem pdf24):**

1.  Otwórz dokument PDF w narzędziu takim jak pdf24 Creator ([https://www.pdf24.org/](https://www.pdf24.org/)).
2.  Skorzystaj z funkcji kompresji lub zmniejszania rozmiaru. Typowe skuteczne ustawienia obejmują:
    *   Włączenie optymalizacji internetowej.
    *   Konwersja kolorów do skali szarości.
3.  Eksperymentuj z poziomami kompresji, dążąc do rozmiaru pliku poniżej **5 MB**, jednocześnie upewniając się, że tekst pozostaje jasny i czytelny.
4.  Zapisz zoptymalizowany plik PDF.

## Krok 2: Ekstrakcja tekstu za pomocą Google AI Studio (Transkrypcja/OCR)

**Cel:** Wykorzystanie możliwości multimodalnych LLM do wykonania OCR na przygotowanym pliku PDF i ekstrakcji zawartości tekstowej w ustrukturyzowanym formacie.

**Procedura:**

1.  Przejdź do **Google AI Studio** ([https://aistudio.google.com/](https://aistudio.google.com/)) i zaloguj się przy użyciu swojego konta Google. Uwaga: AI Studio jest przede wszystkim narzędziem do eksperymentowania z modelami i podpowiedziami.
2.  Rozpocznij nową sesję lub czat.
3.  Dołącz zoptymalizowany plik PDF do swojej sesji (np. za pomocą przycisku dołączania lub przeciągania i upuszczania).
4.  Wpisz następującą podpowiedź w obszarze wiadomości użytkownika:
    ```
    Proszę przepisać załączony plik PDF. Zawiera obrazy z tekstem, wymagające OCR. Wygeneruj transkrypcję w poprawnym formacie Markdown, wykorzystując nagłówki i listy, aby stworzyć strukturę jak najbardziej zbliżoną do układu oryginalnego dokumentu.
    ```
5.  Skonfiguruj ustawienia modelu:
    *   Zachowaj domyślne ustawienia, chyba że masz specyficzne wymagania.
    *   Ustaw **Temperaturę** na **0.1**. Niższa temperatura sprzyja bardziej deterministycznym i mniej kreatywnym wynikom, co jest odpowiednie do dokładnej transkrypcji.
6.  Wyślij podpowiedź. Proces transkrypcji może potrwać kilka minut (potencjalnie 4-6 minut lub dłużej, w zależności od rozmiaru i złożoności pliku PDF).
7.  Po zakończeniu generowania skopiuj wynikowy tekst Markdown.
    *   *Metoda 1:* Użyj opcji kopiowania często dostępnej w interfejsie (np. za pomocą menu związanego z odpowiedzią).
    *   *Metoda 2:* Ręcznie zaznacz cały wygenerowany tekst i skopiuj go (Ctrl+C lub kliknij prawym przyciskiem myszy -> Kopiuj).
8.  Wklej skopiowany tekst Markdown do edytora zwykłego tekstu (takiego jak Notatnik, VS Code, Obsidian itp.).
9.  Zapisz tę zawartość jako plik zwykłego tekstu. Zalecane jest użycie rozszerzeń `.txt` lub `.md` (Markdown). Formatowanie Markdown pomaga zachować strukturę dokumentu (nagłówki, listy).

![Google AI Studio - Zrzut ekranu Transkrypcja](../img/Screenshot-Google-AiStudio-Transcription.png){ width=600 }

## Krok 3: Tłumaczenie wyekstrahowanego tekstu za pomocą Google AI Studio

**Cel:** Przetłumaczenie wyekstrahowanego tekstu Markdown na pożądany język docelowy, zachowując oryginalną strukturę i formatowanie.

**Procedura:**

1.  W **Google AI Studio** rozpocznij **nowy czat**, aby zapewnić świeży kontekst dla zadania tłumaczenia.
2.  Dołącz zapisany plik `.txt` lub `.md` zawierający wyekstrahowany tekst Markdown.
3.  Wpisz podpowiedź tłumaczeniową, określając języki źródłowy i docelowy. Przykład z angielskiego na włoski:
    ```
    Proszę przetłumaczyć załączony plik Markdown (angielski) na język włoski. Zachowaj dokładnie oryginalną strukturę, formatowanie, ton i styl wypowiedzi.
    ```
    *   **Zmodyfikuj podpowiedź** zgodnie z konkretnymi językami źródłowymi i docelowymi (np. „...przetłumacz załączony plik Markdown (niemiecki) na hiszpański...”). Jakość tłumaczenia może się różnić w zależności od pary językowej.
4.  Skonfiguruj ustawienia modelu:
    *   Upewnij się, że ustawienia domyślne są odpowiednie.
    *   Ustaw **Temperaturę** na **0.1**, aby promować wierność tekstowi źródłowemu i strukturze podczas tłumaczenia.
5.  Wyślij podpowiedź. Tłumaczenie może również potrwać kilka minut, porównywalnie do czasu transkrypcji.
6.  Po wygenerowaniu skopiuj przetłumaczony tekst Markdown, używając metod opisanych w Kroku 2 (przycisk kopiowania w interfejsie lub ręczne zaznaczenie).

![Google AI Studio - Zrzut ekranu Tłumaczenie](../img/Screenshot-Google-AiStudio-Translation.png){ width=600 }

## Krok 4: Ponowne formatowanie przetłumaczonego tekstu do dokumentu PDF

**Cel:** Konwersja przetłumaczonego tekstu Markdown z powrotem do dokumentu PDF w celu udostępnienia lub archiwizacji.

**Procedura:**

1.  Wklej skopiowany przetłumaczony tekst Markdown do odpowiedniej aplikacji.
2.  **Zalecane:** Użyj edytora tekstu lub procesora dokumentów, który rozumie formatowanie Markdown, aby zachować strukturę (nagłówki, listy itp.).
    *   **Obsidian** ([https://obsidian.md/](https://obsidian.md/)) to darmowe narzędzie, które dobrze współpracuje z plikami Markdown i często posiada możliwości eksportu do PDF (bezpośrednio lub za pomocą wtyczek).
    *   Nowoczesne procesory tekstu (takie jak Microsoft Word) mogą również importować lub wklejać Markdown i pozwalać na zapis/eksport do PDF, chociaż wierność formatowania może się różnić.
    *   Dedykowane konwertery Markdown do PDF są również dostępne online lub jako oprogramowanie do instalacji.
3.  Użyj funkcji „Eksportuj do PDF” lub „Zapisz jako PDF” aplikacji.
4.  Przejrzyj wynikowy plik PDF, aby upewnić się, że formatowanie i treść wyglądają zgodnie z oczekiwaniami.

## Wnioski

Niniejszy samouczek zademonstrował przepływ pracy polegający na wykorzystaniu Google AI Studio do transkrypcji i tłumaczenia dokumentów PDF, w tym tych wymagających OCR. Poprzez przygotowanie pliku PDF, ekstrakcję tekstu za pomocą skonfigurowanego LLM, tłumaczenie wyniku i jego ponowne formatowanie, użytkownicy mogą uzyskać przetłumaczone wersje swoich dokumentów. Chociaż ta metoda oferuje darmowe lub tanie rozwiązanie, użytkownicy powinni być świadomi potencjalnych różnic w dokładności OCR i jakości tłumaczenia, szczególnie w przypadku złożonych układów lub mniej popularnych języków. Czas przetwarzania zależy w dużej mierze od rozmiaru dokumentu i obciążenia serwera.
