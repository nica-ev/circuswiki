---
lang: pl
translation_id: blog/posts/zettelkasten-wiki-and-beyond
created: 2025-01-21 18:09:55
update: 2025-05-03 22:54:11
date: 2025-02-25T02:14:00
publish: true
tags: 
title: Zettelkasten, Wiki i dalej
description: 
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Zettelkasten, Wiki, and Beyond.md
translation_source_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T20:08:52+00:00
translation_source_body_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_source_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:09+00:00
translation_source_localized_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_source_structural_metadata_hash: 954fd44b41e05f58bf1c8770aa83d64e0e9940b99ea04fb9e455b64f3667247b
---
# **Zettelkasten, Wiki i Co Dalej**  
**Dlaczego rozpocząłem ten projekt, jakie idee za nim stoją i dokąd może on prowadzić.**

W 2013 roku pracowałem jako menedżer projektu w cyrku młodzieżowym. Trenerzy często przychodzili do mnie z pytaniami, czy znam inne gry, metody lub sztuczki. W tamtym czasie miałem mnóstwo zasobów – książek, czasopism, notatek z warsztatów – ale wszystko było nieuporządkowane i ledwo zdigitalizowane.  
<!-- more -->
Moją pierwszą próbą udostępnienia tych zasobów trenerom był klasyczny wiki. Wiele opisów gier, które dziś można znaleźć, pochodzi właśnie z tamtego okresu. Jednocześnie zacząłem digitalizować swoje źródła. Odkryłem metodę *Zettelkasten* (skrzynki na fiszki) Niklasa Luhmanna i zacząłem organizować swoje dane zgodnie z jej zasadami.  

Wiki okazało się porażką. Było mało interakcji; trenerzy użyli go kilka razy i szybko o nim zapomnieli. Moja osobista skrzynka Zettelkasten rosła jednak w siłę. Chociaż początkowo używałem specjalistycznego oprogramowania, wkrótce zacząłem zastanawiać się, jak zapewnić długoterminową użyteczność tej coraz cenniejszej kolekcji.  

Co to oznacza? Pierwszym sygnałem ostrzegawczym było uświadomienie sobie, że oprogramowanie, którego używałem, nie jest już rozwijane. Musiałem znaleźć nowe oprogramowanie – i dowiedzieć się, jak przenieść do niego moje dane. Wtedy odkryłem Markdown.  

Markdown to prosty format pliku – w zasadzie zwykły plik tekstowy – zaprojektowany tak, aby działać niezależnie od konkretnego oprogramowania. Innymi słowy, jest to powszechnie przyjęty standard, który można odczytywać i edytować za pomocą najprostszych narzędzi.  

Format ten obsługiwał wszystko, czego potrzebowałem: podstawowe formatowanie tekstu, linki, tagi i metadane (np. tytuł, autor, opis itp.). Znalazłem nowe oprogramowanie wykorzystujące Markdown i kontynuowałem budowanie mojego Zettelkasten. W tamtym momencie miałem około 600 notatek (czyli plików/stron). Później ponownie zmieniłem oprogramowanie, a przejście było bezproblemowe.  

>[!info]  Kluczowy Wniosek
>Zapewnienie długoterminowej użyteczności danych oznacza korzystanie z prostego, powszechnie przyjętego formatu, niezależnego od konkretnego oprogramowania.  

## Współpraca i Dzielenie się  

Moja pierwsza próba z wiki nie powiodła się – po części dlatego, że nie udało mi się zainspirować innych do współtworzenia. Przez lata mój osobisty Zettelkasten rozrósł się do ponad 3000 notatek, wiele z nich na tematy takie jak pedagogika cyrkowa, gry, żonglerka i inne.  

Przez pewien czas po prostu udostępniałem go online, ale poza kilkoma osobami, które o nim wiedziały i od czasu do czasu szukały opisów gier, nie było prawdziwej współpracy ani szerszego dzielenia się.  

Teraz, około 12 lat po rozpoczęciu mojego Zettelkasten, próbuję ponownie. Celem jest stworzenie wspólnej bazy wiedzy na tematy takie jak pedagogika cyrkowa i ruchowa, sztuka cyrkowa i nie tylko.  

### Kluczowe Kwestie i Pytania  
- **Niezależność od konkretnych systemów**  
- **Prosty, łatwy do zrozumienia format danych**  
- **Użyteczność i grupa docelowa**  
- **Strukturalizacja danych**  

Tradycyjne oprogramowanie wiki (lub platformy takie jak WordPress) były wykluczone, ponieważ tworzą zależność od jednego systemu. Chociaż może to działać w krótkim lub średnim okresie, w dłuższej perspektywie jest to wyraźna słabość.  

Zamiast tego zarządzam danymi (jako pliki Markdown i obrazy) niezależnie od sposobu ich ostatecznego prezentowania. Zapewnia to, że nawet za 20 lat dane pozostaną użyteczne. Sposób ich wyświetlania lub edycji może się drastycznie zmienić, ale podstawowe dane pozostaną te same.  

Istnieje niezliczona ilość sposobów prezentacji danych: jako strona internetowa, e-book, PDF, a nawet aplikacja. Można je spakować do pliku i odczytywać lub edytować offline za pomocą prostego edytora tekstu. Jeśli chcesz wyświetlić je jako stronę WordPress lub wiki, jest to po prostu kwestia importu danych – ponieważ są one ustrukturyzowane i łatwe do odczytania, ich implementacja jest stosunkowo prosta (przy odpowiedniej wiedzy).  

## Moje Obecne Rozwiązanie dla Strony Internetowej  

Używam MkDocs i motywu MkDocs-Material do generowania statycznej strony internetowej. Istnieje wiele programów, które tworzą statyczne pliki HTML z Markdown, ale MkDocs jest specjalnie zaprojektowany do dokumentacji. Wiele funkcji, które generuje – takich jak wyszukiwanie pełnotekstowe i nawigacja – jest niezwykle pomocnych.  

MkDocs jest również szeroko stosowanym rozwiązaniem open-source wspieranym przez duże firmy, co zapewnia, że pozostanie funkcjonalne przynajmniej w średnim okresie.  

## Współpraca  

Następnym krokiem jest uczynienie tego wysiłkiem zespołowym. Badam sposoby zapraszania innych do współtworzenia, czy to poprzez dodawanie nowej treści, ulepszanie istniejących wpisów, czy sugerowanie usprawnień. Celem jest stworzenie żywego, ewoluującego zasobu, który korzysta z wiedzy i doświadczenia zbiorowego.
