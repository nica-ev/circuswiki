---
lang: pl
translation_id: beancount/09-receipts-and-documents
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Potwierdzenia i dokumenty
description: Wyjaśnia, gdzie przechowywane są dokumenty potwierdzające i jak transakcje odnoszą się do potwierdzeń.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/09-receipts-and-documents.md
translation_source_body_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_source_hash: 0eb7db344a083d1e3f8e7330c51d40fa2989b80ac511578eff6f61b20688ad57
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:06:32+00:00
translation_source_localized_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_source_metadata_hash: bee9c73fae5bfce616ba94ee5316a128ff29b317389294613f79d6fd77c016c4
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:06:32+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 09 - Potwierdzenia i dokumenty

Potwierdzenia, faktury, umowy i inne dokumenty źródłowe sprawiają, że transakcje są możliwe do zweryfikowania. Rejestr powinien umożliwiać odnalezienie dokumentu stojącego za wydatkiem.

## Gdzie przechowywane są dokumenty

Tohuwabohu ma obecnie przejrzysty folder na potwierdzenia:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben
```

Potwierdzenia, które zostały już wprowadzone do rejestru, znajdują się często w:

```text
1. Vereinsverwaltung/Buchhaltung/Buchhaltung-Tohuwabohu/2023/Belege Ausgaben/Eingetragen
```

NICA używa plików pomocniczych w swoim folderze księgowym i folderach projektowych. Jeśli w przyszłości zostanie wprowadzony spójny folder na potwierdzenia NICA, należy to udokumentować tutaj i stosować konsekwentnie.

## Wpisy `document`

Wpis `document` łączy plik z kontem i datą:

```beancount
2025-10-02 document Ausgaben:Projekt:TOHUCON-25:Essen "Belege Ausgaben/Quittung-Tohu25-001.pdf"
```

Ścieżka do pliku jest względna w stosunku do folderu zawierającego plik rejestru.

## Powiązania dokumentów z tagami

Niektóre starsze wpisy zawierają tagi dokumentów, takie jak:

```beancount
2023-01-05 document Ausgaben:Buero:Sonstiges "Belege Ausgaben/Eingetragen/2023_001.jpg" ^2023_001
```

Część `^2023_001` to powiązanie Beancount. Może ono połączyć potwierdzenie z powiązaną transakcją, jeśli użyto tam tego samego powiązania.

## Znaczenie `scanned`

Komentarze w rejestrach definiują konwencję dotyczącą zeskanowanych potwierdzeń. Gdy używany jest tag `scanned`, oznacza to:

- Potwierdzenie zostało zeskanowane lub zdigitalizowane.
- Obraz został zmniejszony i zoptymalizowany, na przykład za pomocą TinyPNG.
- Plik został zapisany zgodnie ze wzorem roku i numeru, na przykład `2023_002.jpg`.
- Numer jest odniesieniem w powiązanej pozycji rejestru.

## Dobre nazwy plików

Dobre nazwy plików potwierdzeń są stabilne i czytelne:

```text
2026_001.jpg
2026_002.pdf
Quittung-Tohu25-001.pdf
Invoice406-Schwarze_Risse-marc-bielert.pdf
```

Unikaj nazw takich jak `scan.jpg`, `image1.jpg` czy `download.pdf`.

## Przepływ pracy dla nowego potwierdzenia

1. Zapisz potwierdzenie w odpowiednim folderze potwierdzeń.
2. Zmień jego nazwę, aby można je było rozpoznać później.
3. Wprowadź lub znajdź powiązaną transakcję.
4. Dodaj linię `document` lub metadane powiązania, jeśli jest to przydatne.
5. Jeśli potwierdzenie zostało przetworzone, przenieś je do `Eingetragen`, jeśli taka jest konwencja folderu.
6. Przeładuj Fava i sprawdź, czy powiązanie dokumentu działa.

## Gdy brakuje potwierdzenia

Jeśli potwierdzenie brakuje, dodaj komentarz w pobliżu transakcji:

```beancount
; Receipt missing. Ask responsible person.
```

Nie udawaj, że dokument istnieje, jeśli go nie ma.

## Umowy i dokumenty honorariów

Umowy i faktury honorariów powinny być przechowywane w pobliżu powiązanego projektu lub folderu księgowego i jasno odwoływane. W przypadku audytów projektów ważne jest nie tylko to, czy transakcja istnieje, ale także to, czy dokument potwierdzający wydatek można szybko znaleźć.
