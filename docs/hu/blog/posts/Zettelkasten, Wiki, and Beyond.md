---
lang: hu
translation_id: blog/posts/zettelkasten-wiki-and-beyond
created: 2025-01-21 18:09:55
update: 2025-05-03 22:54:11
date: 2025-02-25T02:14:00
publish: true
tags: 
title: Zettelkasten, Wiki és azon túl
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
translation_updated: 2026-06-06T22:34:54+00:00
translation_source_body_hash: 7962c1d3def8449dd725f1045c0e2fc9e6f0b9cb5aa662c2ef6ecd76aa114186
translation_source_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:10+00:00
translation_source_localized_metadata_hash: d1fdf486731057ba36e38856452394aa4294072211fe8a1ebd4de6c5ba53ba51
translation_source_structural_metadata_hash: 954fd44b41e05f58bf1c8770aa83d64e0e9940b99ea04fb9e455b64f3667247b
---
# **Zettelkasten, Wiki és a jövő**
**Miért indítottam ezt a projektet, az ötletek mögötte, és hová vezethet.**

2013-ban egy ifjúsági cirkusznál dolgoztam projektvezetőként. Az edzők gyakran kerestek meg azzal a kérdéssel, hogy ismerek-e más játékokat, módszereket vagy trükköket. Abban az időben rengeteg forrásom volt – könyvek, magazinok, workshopokról származó jegyzetek –, de minden rendszerezetlen volt és alig volt digitalizálva.
<!-- more -->
Az első kísérletem, hogy ezeket az erőforrásokat hozzáférhetővé tegyem az edzők számára, egy klasszikus wiki volt. Sok, ma is látható játékleírás ebből az időszakból származik. Ezzel párhuzamosan elkezdtem digitalizálni a forrásaimat. Felfedeztem Niklas Luhmann *Zettelkasten* (jegyzetdoboz) módszerét, és elkezdtem az adataimat az elvei szerint rendezni.

A wiki kudarc volt. Kevés volt az interakció; az edzők néhányszor használták, majd gyorsan elfelejtették. A személyes Zettelkastenom azonban növekedni kezdett. Bár kezdetben speciális szoftvert használtam, hamarosan azon kezdtem gondolkodni, hogyan tehetném jövőbiztossá ezt az egyre értékesebb gyűjteményt.

Mit jelent ez? Az első figyelmeztető jel akkor jött, amikor rájöttem, hogy a használt szoftvert már nem fejlesztik. Új szoftvert kellett találnom – és ki kellett találnom, hogyan migrálhatom bele az adataimat. Ekkor fedeztem fel a Markdown-t.

A Markdown egy egyszerű fájlformátum – lényegében egy sima szöveges fájl –, amelyet úgy terveztek, hogy ne legyen szoftverfüggő. Más szóval, egy széles körben elfogadott szabvány, amely a legegyszerűbb eszközökkel is olvasható és szerkeszthető.

A formátum mindent támogatott, amire szükségem volt: alapvető szövegformázást, hivatkozásokat, címkéket és metaadatokat (pl. cím, szerző, leírás stb.). Találtam új szoftvert, amely használta a Markdown-t, és folytattam a Zettelkastenem építését. Akkoriban körülbelül 600 jegyzetem (vagy fájlom/oldalam) volt. Később ismét szoftvert váltottam, és az átállás zökkenőmentes volt.

>[!info]  Kulcsfontosságú tanulság
>Az adatok jövőbiztossá tétele azt jelenti, hogy egy egyszerű, széles körben elfogadott, szoftverfüggetlen formátumot használunk.

## Együttműködés és megosztás

Az első wiki próbálkozásom nem sikerült – részben azért, mert nem sikerült másokat inspirálnom a közreműködésre. Az évek során a személyes Zettelkastenom több mint 3000 jegyzetté nőtte ki magát, sokuk olyan témákban, mint a cirkuszi pedagógia, játékok, zsonglőrködés és még sok más.

Egy ideig egyszerűen online elérhetővé tettem, de néhány emberen kívül, akik tudtak róla, és alkalmanként megnézték a játékleírásokat, nem volt valódi együttműködés vagy szélesebb körű megosztás.

Most, körülbelül 12 évvel a Zettelkastenem elindítása után, ismét megpróbálkozom. A cél egy közös tudásbázis létrehozása olyan témákban, mint a cirkusz- és mozgáspedagógia, a cirkuszművészetek és azon túl.

### Főbb szempontok és kérdések
- **Rendszerfüggetlenség**
- **Egyszerű, könnyen érthető adatformátum**
- **Használhatóság és célközönség**
- **Strukturált adatok**

A hagyományos wiki szoftverek (vagy olyan platformok, mint a WordPress) szóba sem jöhettek, mert egyetlen rendszerhez való függőséget teremtenek. Ez rövid vagy középtávon működhet, de hosszú távon egyértelmű gyengeség.

Ehelyett az adatokat (Markdown és képfájlok formájában) a megjelenítésüktől függetlenül kezelem. Ez biztosítja, hogy még 20 év múlva is használhatóak maradjanak az adatok. A megjelenítés vagy szerkesztés módja drasztikusan változhat, de az alapul szolgáló adatok változatlanok maradnak.

Az adatok megjelenítésére számtalan mód létezik: weboldalként, e-könyvként, PDF-ként vagy akár alkalmazásként. Becsomagolható egy fájlba, és offline is olvasható vagy szerkeszthető egy egyszerű szövegszerkesztővel. Ha WordPress-webhelyként vagy wikiként szeretné megjeleníteni, az csak az adatok importálásának kérdése – mivel strukturált és könnyen olvasható, viszonylag egyszerűen megvalósítható (a megfelelő szaktudással).

## Jelenlegi megoldásom a weboldalhoz

Az MkDocs és az MkDocs-Material témát használom egy statikus weboldal generálásához. Számos program létezik, amelyek statikus HTML fájlokat hoznak létre Markdownból, de az MkDocs kifejezetten dokumentációhoz készült. Számos funkciója – mint a teljes szöveges keresés és a navigáció – hihetetlenül hasznos.

Az MkDocs egy széles körben használt, nyílt forráskódú megoldás is, amelyet nagyvállalatok támogatnak, ami biztosítja, hogy legalább középtávon működőképes maradjon.

## Együttműködés

A következő lépés az, hogy ezt közös erőfeszítéssé tegyük. Vizsgálom azokat a módokat, amelyekkel másokat is meghívhatok a közreműködésre, akár új tartalom hozzáadásával, meglévő bejegyzések finomításával vagy fejlesztési javaslatokkal. A cél egy élő, fejlődő erőforrás létrehozása, amely a kollektív tudásból és szakértelemből profitál.
