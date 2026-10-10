---
lang: hu
translation_id: beancount/13-glossary
publish: true
tags:
  - accounting
  - beancount
created: 2026-07-01 00:00:00
update: 2026-07-01 00:00:00
title: Szószedet
description: A dokumentációban használt könyvelési, Beancount, Fava és projektkönyvelési kifejezések meghatározásai.
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: en
translation_source: docs/en/beancount/13-glossary.md
translation_source_body_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_source_hash: 531c271660b8cbd2a8eb2bdb0f6e6c0d196489c5fda53acf6e8d401e9b6d0cf4
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T00:09:00+00:00
translation_source_localized_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_source_metadata_hash: d5b05695f6ea58b307f91a90790b098b3926d34f0ccbc459ba21086855875867
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T00:09:00+00:00
translation_source_structural_metadata_hash: cca628ac4150320efe0a824be4b91d2a51fbd4e6b9175d13b08a1b1842607223
---
# 13. Szójegyzék

## Számla

Egy megnevezett hely, ahol a Beancount pénzt vagy értéket rögzít. Példa: `Ausgaben:Buero:Miete`.

## Eszközök

Minden, ami a szervezet tulajdonában vagy ellenőrzése alatt áll, például banki pénz, PayPal egyenleg, készpénz vagy leltár. Ebben a rendszerben az eszközök a `Vermoegen` alatt találhatók.

## Mérlegellenőrzés

Egy sor, amely megerősíti, hogy egy számlának egy adott dátumon egy meghatározott egyenlege van. A mérlegellenőrzéseket a főkönyv banki, PayPal vagy készpénz nyilvántartásokkal való egyeztetésére használják.

## Banki mentés

Egy ideiglenes szakasz a főkönyv alján, ahová az importált banki tranzakciókat először beillesztik, mielőtt teljesen besorolnák őket.

## Beancount

A szöveges könyvelési formátum, amelyet a rendszer „igazság forrásaként” használnak.

## CSV

Egy táblázatkezelőhöz hasonló export fájl. A Sparkasse CSV fájlokat exportál, amelyeket Beancount tranzakciókká alakítanak át.

## Saját tőke

A Beancount számlacsalád, amelyet a nyitó egyenlegekhez és a történelmi kiindulópontok kiegyenlítéséhez használnak.

## Fava

A Beancount főkönyvek megtekintésére és kezelésére szolgáló böngészőfelület.

## Fava irányítópultok

Egy bővítmény, amely egyéni irányítópult oldalakat ad a Favához.

## Freies-Geld (Szabad pénz)

Szabad vagy korlátozás nélküli pénz, amelyet nem rendeltek hozzá egy korlátozott projekt költségvetéséhez.

## Bevétel

Kapott pénz. Ebben a rendszerben a bevételi számlák az `Einnahmen` előtaggal kezdődnek.

## Főkönyv

A könyvelési fájl, amely számlákat, tranzakciókat, mérlegellenőrzéseket és dokumentumokat tartalmaz. A fő főkönyvek a `nica.beancount` és a `2023.beancount`.

## Kötelezettség

Másoknak tartozott pénz. Ebben a rendszerben a kötelezettségek a `Verbindlichkeiten` alatt találhatók.

## Kifizető

A tranzakcióban megnevezett személy vagy szervezet.

## Projekt számla

Egy számla, amelyet egy adott projekt pénzének elkülönített nyomon követésére használnak a szervezet általános pénzétől.

## Egyeztetés

Annak ellenőrzése, hogy a Beancount és a tényleges banki vagy PayPal egyenleg megegyezik-e.

## Nyugta

Egy kiadás igazolására szolgáló dokumentum, például számla, szerződés vagy pénztári nyugta.

## Sonstiges (Egyéb)

Németül: vegyes vagy egyéb. Hasznos ideiglenes megoldásként, de a végleges könyveléshez specifikus kategóriák javasoltak.

## Tranzakció

Egy dátummal ellátott könyvelési bejegyzés, amely egy pénzügyi eseményt ír le.

## Verwendungsnachweis (Felhasználási igazolás)

Egy projektfinanszírozó jelentése, amely elmagyarázza, hogyan használták fel az elnyert pénzt.
