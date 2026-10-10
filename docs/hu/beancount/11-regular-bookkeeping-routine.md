---
lang: hu
translation_id: beancount/11-regular-bookkeeping-routine
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Rendszeres könyvelési rutin
description: Gyakorlati, ismétlődő ellenőrzőlista a főkönyvek naprakészen tartásához.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/11-regular-bookkeeping-routine.md
translation_source_body_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_source_hash: f5d0598f906eace87f7f3b231481f82dcdcad6c1b23bde21e925b14e145bd4d4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:07:48+00:00
translation_source_localized_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_source_metadata_hash: 40dfea60b9872dfd45332129b6997d8f84322f9d8c85d8b1034b01e29b1ab840
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:07:48+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 11 - Rendszeres könyvelési rutin

Ez az oldal a főkönyvek naprakészen tartásának gyakorlati rutinját írja le.

## Heti vagy kétheti rutin

Akkor használd, ha rendszeres banki mozgások vannak.

1. Nyissuk meg a megfelelő Fava példányt.
2. Ellenőrizzük, hogy a Fava nem mutat-e hibákat.
3. Keressük meg a legfrissebb egyenleg-ellenőrzést.
4. Exportáljuk az új Sparkasse CSV adatokat.
5. Konvertáljuk a CSV-t a `csv2bean.py` segítségével.
6. Illesszük be az új tételeket a `Bank Dump` (Banki mentés) mappába.
7. Osztályozzuk a tételeket a megfelelő számlákra.
8. Csatoljunk vagy hivatkozzunk nyugtákra, ahol szükséges.
9. Adjunk hozzá egy új egyenleg-ellenőrzést.
10. Töltsük újra a Favát, és oldjuk meg a hibákat.
11. Tekintsük át a `Kiadások:Egyéb` és `Bevételek:Egyéb` kategóriákat, hogy az ott lévő tételeket pontosítsuk.

## Havi rutin

A hónap végén:

1. Egyeztesse a Sparkasse-t.
2. Egyeztesse a PayPal-t, ha használatban volt.
3. Egyeztesse a pénztárat, ha készpénzt használtak.
4. Ellenőrizze a fennálló tartozásokat magánszemélyek felé.
5. Ellenőrizze az aktív projektmérlegeket.
6. Tekintse át a besorolatlan `Egyéb` tételeket.
7. Ellenőrizze a hiányzó nyugtákat.
8. Ellenőrizze, hogy a befejezett projektek készen állnak-e a lezárásra.

## Projektjelentési rutin

Projektjelentés vagy felhasználási igazolás elkészítése előtt:

1. Nyissa meg a projekt számláit a Favában.
2. Exportálja vagy tekintse át az összes projekt bevételt és kiadást.
3. Győződjön meg arról, hogy a kategóriák megegyeznek a finanszírozó költségvetési sorain.
4. Győződjön meg arról, hogy minden nyugta és tiszteletdíj dokumentum rendelkezésre áll.
5. Ellenőrizze, hogy a visszatérítések, törlések és megtérítések helytelen bevételként, helyesbítő tételekként vannak-e könyvelve.
6. Győződjön meg arról, hogy a projekt eszközmérlege magyarázható.
7. Ha a projekt befejeződött, helyesen utalja át a fennmaradó pénzt, és zárja le a projekt számláit.

## Év végi rutin

Az év végén:

1. Egyeztesse az összes bankszámlát.
2. Egyeztesse a PayPal-t.
3. Egyeztesse a pénztárakat.
4. Ellenőrizze a tartozásokat.
5. Ellenőrizze a nyitott projektmérlegeket.
6. Győződjön meg arról, hogy minden nyugta tárolva és csatolva van, vagy megtalálható.
7. Tekintse át a bevételi és kiadási kategóriákat.
8. Adjon hozzá végső egyenleg-ellenőrzéseket.
9. Készítsen jelentéseket a Favából.
10. Archiválja az exportált CSV-ket és a támogató dokumentumokat.

## Minőségellenőrzések

Egy főkönyv akkor van jó állapotban, ha:

- A Fava hiba nélkül megnyílik.
- A legfrissebb Sparkasse egyenleg-ellenőrzés megegyezik a bankival.
- A PayPal és a pénztár egyenlegei ellenőrzésre kerültek, ahol releváns.
- A projektmérlegek szándékoltak és magyarázhatók.
- A lezárt projekteknek nulla az eszközmérlege.
- Az `Egyéb` számlák nem tartalmaznak elkerülhető, besorolatlan tételeket.
- A kiadásokhoz tartozó nyugták megtalálhatók.
- A megjegyzések magyarázzák a szokatlan korrekciókat vagy feltételezéseket.

## Átadási ellenőrzőlista egy másik személy számára

Mielőtt a könyvelést másra bízná:

- Mutassa meg neki a megfelelő főkönyvi fájlt minden egyesület számára.
- Mutassa meg neki, hogyan kell elindítani a Favát.
- Mutassa meg neki a legfrissebb egyenleg-ellenőrzést.
- Mutassa meg neki, hogyan kell a CSV importokat a `Bank Dump` (Banki mentés) mappában elhelyezni.
- Mutassa meg neki, hol tárolja a nyugtákat.
- Mutasson neki egy példaprojektet a finanszírozási bevételtől a végső lezárásig.
- Irányítsa őt erre a dokumentációs mappára.
