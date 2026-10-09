---
lang: hu
translation_id: beancount/06-entering-and-editing-transactions
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Tranzakciók rögzítése és szerkesztése
description: Leírja, hogyan tekinthetik át, osztályozhatják, javíthatják és rögzíthetik a felhasználók a könyvelési tranzakciókat.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/06-entering-and-editing-transactions.md
translation_source_body_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_source_hash: 7d239c8f3b4e3960fc2144b3abb0294d0ac9bcae86ac11d7be9625fabda81548
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-07-01T14:38:09+00:00
translation_source_localized_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_source_metadata_hash: 8519f0ee188c08a631101627e7f8e6f2a8bdc660286dbb4e363ab012ac9166a9
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-07-01T14:38:09+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 06 – Tranzakciók rögzítése és szerkesztése

A legtöbb bejegyzés importált banki adatokból származik, de a felhasználóknak továbbra is át kell tekinteniük, osztályozniuk, javítaniuk és néha manuálisan kell rögzíteniük a tranzakciókat.

## Tranzakció állapota

A főkönyvek általában az `!` jelet használják az importált tranzakcióknál:

```beancount
2026-03-12 ! "Kedvezményezett" "Banki szöveg"
```

Ezt használd alapértelmezett jelölőként, hacsak a csapat nem dönt szigorúbb státuszkonvenció mellett.

## Alapvető bevételi tétel

```beancount
2026-01-15 ! "Max Mustermann" "Tagdíj 2026"
  Vagyon:Bank:Sparkasse-NICA:Szabad-pénz  60.00 EUR
  Bevételek:Egyesületi-hozzájárulás
```

## Alapvető kiadási tétel

```beancount
2026-01-20 ! "Szolgáltató neve" "Számla 123"
  Kiadások:Iroda:Egyéb  25.00 EUR
  Vagyon:Bank:Sparkasse-NICA
```

## Projektbevétel

```beancount
2026-02-10 ! "Támogató szerv" "Támogatási kifizetés 25-ZGV projekt"
  Vagyon:Bank:Sparkasse-NICA:25-ZGV  5000.00 EUR
  Bevételek:Projekt:25-ZGV:Anyagi-javak
```

## Projektkiadás

```beancount
2026-02-15 ! "Személy neve" "Díj 25-ZGV projekt"
  Kiadások:Projekt:25-ZGV:Díj  450.00 EUR
  Vagyon:Bank:Sparkasse-NICA:25-ZGV
```

## Belső mozgás projekt- és szabad alapok között

Néha egy tranzakciónak a banki pénzt egy projektspecifikus eszközszámla és a szabad alapok között kell elszámolnia. A tényleges bankszámla egy fizikai Sparkasse számla, de a főkönyv külön követi a belső projektmérlegeket.

```beancount
2026-02-20 ! "Belső elszámolás" "Megmaradt projektforrások átcsoportosítása szabad pénzre"
  Vagyon:Bank:Sparkasse-NICA:Szabad-pénz  100.00 EUR
  Vagyon:Bank:Sparkasse-NICA:25-ZGV      -100.00 EUR
```

Csak akkor végezz belső átutalásokat, ha megérted, miért kell megváltoztatni a belső projektmérleget.

## Visszatérítések személyeknek

Ha valaki magánúton fizetett, és később visszatérítést kap, a tiszta módszer általában az, hogy a kiadást egy kötelezettség ellenében rögzítjük, majd a kötelezettséget a banki kifizetéssel rendezzük.

```beancount
2026-03-01 ! "Bolt" "Marc által vásárolt anyag"
  Kiadások:Projekt:25-ZGV:Anyagi-javak  35.00 EUR
  Kötelezettségek:Személy:Marc-Bielert
```

```beancount
2026-03-05 ! "Marc Bielert" "Anyag visszatérítése"
  Kötelezettségek:Személy:Marc-Bielert  35.00 EUR
  Vagyon:Bank:Sparkasse-NICA
```

## Megjegyzések tisztázatlan döntésekhez

```beancount
; Nem világos, hogy ez a CEDU-25-höz vagy a szabad egyesületi alapokhoz tartozik-e. Ellenőrizd a számlát.
2026-03-10 ! "Eladó" "Számla 456"
  Kiadások:Egyéb  120.00 EUR
  Vagyon:Bank:Sparkasse-Tohuwabohu
```

## Biztonságos szerkesztés

Szerkesztés előtt ellenőrizd:

- A megfelelő egyesületi főkönyvben vagy.
- Nem a generált import kimenetet szerkeszted úgy, mintha az lenne a végleges főkönyv.
- A tranzakció dátuma helyes.
- Az összeg tizedesvesszőként pontot használ, például `12.50 EUR`.
- A számlanevek pontosan úgy vannak írva, mint a meglévő számlák.
- A projekttel kapcsolatos tranzakciók következetesen használják a projekt eszközszámlát és a projekt bevételi/kiadási kategóriát.

Szerkesztés után mentsd el a fájlt, töltsd be újra a Favát, ellenőrizd a hibákat, és tekintsd meg a releváns számlát.
