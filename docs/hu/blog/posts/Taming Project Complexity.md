---
lang: hu
translation_id: blog/posts/taming-project-complexity
created: 2025-05-02 04:37:37
update: 2026-10-10 20:09:23
date: 2025-05-03T11:00:00
publish: true
tags: 
title: A projektkomplexitás megszelídítése – A saga
description: Az utazás egy komplex fejlesztői környezet hatékony verziózásához anélkül, hogy a fő projekt adattárát szennyeznénk.
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Taming Project Complexity.md
translation_source_hash: 15300a3605c6b0a1fbd64d24db3d47f664d6814dc7ad022e57bdace07abf1462
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T20:54:31+00:00
translation_source_body_hash: 15300a3605c6b0a1fbd64d24db3d47f664d6814dc7ad022e57bdace07abf1462
translation_source_metadata_hash: 326d746cf3f5ea2edc1d4adef6bfcba4e454202b335675ecfc6d363623d01f6b
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T20:54:31+00:00
translation_source_localized_metadata_hash: 326d746cf3f5ea2edc1d4adef6bfcba4e454202b335675ecfc6d363623d01f6b
translation_source_structural_metadata_hash: e3d56cc63df642dafa063d27bdc292098f6ac52159e83b1249537b0aebc40ffb
---
# A Projektkomplexitás Megszelídítése – A Saga
**A fejlesztői környezet verziókezelése anélkül, hogy beszennyeznéd a fő adattáradat**

Ahogy a projektek fejlődnek, különösen az olyan tudásbázisok vagy dokumentációs oldalak, amelyek több eszközt is érintenek, mint például az MkDocs, az Obsidian, egyéni szkriptek és speciális IDE-k, mint a Cursor, a komplexitás természetesen növekszik. Ezeknek az eszközöknek az integrálása erőteljes munkafolyamatokat hoz létre, de egy új kihívást is jelent: a magprojektet támogató konfigurációs fájlok, piszkozatok, szkriptek és tervezési dokumentumok növekvő számának kezelése.
<!-- more -->
## A Fájdalom Pontja: Amikor a `.gitignore` Nem Elég

Nemrégiben elértem egy fájdalmas mérföldkövet, amellyel sok fejlesztő találkozik: **több órányi munkát veszítettem el**. A tettes? A fejlesztői munkafolyamatomhoz szükséges fájlok nem voltak verziókezelve.

Sokan közülünk szeretnénk tisztán tartani a nyilvánosan elérhető GitHub adattárunkat. Ehhez a projekthez ez azt jelentette, hogy csak a fő Markdown tartalmat és az alapvető MkDocs fájlokat rögzítettem, amelyek a weboldal felépítéséhez szükségesek. Minden más – az Obsidian tárolóm konfigurációja, a Cursor beállításai, a piszkozat fordítószkriptek, a feladattervezési jegyzetek – gondosan fel volt sorolva a `.gitignore`-ban. Ez tisztán tartotta a fő adattárat, de a létfontosságú fejlesztői támasztékomat védelem nélkül hagyta.

Ez a vészharang szerencsére viszonylag korán megszólalt. Miközben a fordítószkriptek integrálásán és a projektstruktúrán belüli jegyzetekkel történő munkafolyamat tervezésén dolgoztam, egy baleset jelentős tervezési munkát írt felül. Frusztráló, igen, de értékes lecke volt, mielőtt a tét magasabbra emelkedett volna.

## Megoldás Keresése: A Sikertelen Kísérletek

Kezdeti ötleteim a Git önmagában való okosabb használata körül forogtak, de elakadtam.

### 1. Kísérlet: Beágyazott Adattárak – Az Ágcserélgetés Éjszakája

Az első gondolatom az volt, hogy a Git-történetek több példányát vizsgáljam meg ugyanazon projektdirektóriumban, talán beágyazott adattárak használatával. Az ötlet az volt, hogy legyen egy legfelső szintű "dev" adattár, amely *mindent* követ (IDE beállítások, piszkozatok, a belső adattár fájljai), miközben a belső "public" adattár csak a tiszta, telepíthető projektfájlokat tartalmazza. A külső adattár figyelmen kívül hagyná a belső adattár `.git` könyvtárát.

Elméletben ez egy ügyes, rétegzett megközelítésnek tűnt. Azonban, amikor ténylegesen megpróbáltam ezt beállítani, nagyon hamar rájöttem, hogy ez nem működik. Először is, a Git nem igazán támogatja a beágyazott adattárakat, legalábbis nem úgy, ahogyan elképzeltem. És van értelme. Van egy figyelmen kívül hagyott tényező, amire nem gondoltam: Tegyük fel, hogy a belső adattárban (`docs-nica`) dolgozom, és átváltok egy másik ágra. Most az adott mappában lévő összes fájl megváltozik (hogy tükrözze az ágat) – de a külső adattár (`docs-nica-dev`) még mindig a fő ágán van. A külső adattár most látja ezeket a fájlváltozásokat, és azt gondolja, hogy ezek *annak* a fő ágának a változásai... Világosan látható, miért jelent ez problémát. Oké, tehát ez a megközelítés nem működött.

### 2. Kísérlet: Külön Adattárak + Git Hookok – A Másolási Katasztrófa

Vissza a rajztáblához. A következő ötletem két teljesen különálló adattár volt. Egy `dev` adattár, amely mindent tartalmaz, amire szükségem van (szkriptek, jegyzetek, konfigurációk, *és* a fő projektfájlok). És egy `public` adattár, amely csak a markdown tartalmat és az MkDocs beállítást tartalmazza – csak a lényeget, ahogy a telepítéshez szánták.

De itt jön a csapda: ha valamit megváltoztatunk a `public` adattárban (talán egy gyors javítás ott, vagy a közreműködők változásainak lehúzása), honnan tud róla a `dev` adattár? És gyakoribb esetben, hogyan tükröződnek a `dev` változásai a `public` adattárban? Szükségünk van valamilyen kapcsolatra.

Az első ötlet a GitHub hookok (vagy helyi Git hookok) használata volt. Ezek lehetővé teszik parancsok definiálását, amelyek bizonyos Git műveletek, például egy commit után futnak le. Beállítottam egy hookot, amely a `dev` adattárban történő commit után alapvetően csak átmásolta a releváns fájlokat (a `docs/` mappát, az `mkdocs.yml`-t stb.) a `public` adattár könyvtárába.

Első pillantásra úgy tűnt, hogy működik, de ennek a megközelítésnek két fő problémája volt:

1.  **Zajos Történet:** A hook *minden* releváns fájlt átmásolt *minden* commitnál. Ez azt jelentette, hogy a `public` adattár mindig azt gondolta, hogy *minden* tartalma megváltozott. Bár technikailag nem tört össze semmit, a commit története kevésbé lett hasznos, mivel minden egyes commitban több száz (vagy ezer) fájlt mutatott változásként, lehetetlenné téve annak azonnali beazonosítását, hogy mely fájlok *tartalma* változott valójában.
2.  **Törlés-Vakítás:** A szkript csak *másolt* fájlokat. Ha töröltem egy fájlt vagy mappát a `dev` adattárban, ez a változás nem tükröződött a `public` adattárban. A régi fájl csak ott maradt.

Átkozottul, már órákat töltöttem ezzel – és még mindig nincs működő megoldás.

## Az Áttörés: Külön Adattárak + Fájlszinkronizálás

Aztán eszembe jutott egy nyílt forráskódú szoftver, amelyet régen teszteltem helyi mappák szinkronizálására: **FreeFileSync**. Bár sajnálatos, hogy egy újabb eszközkészletet/szoftvert kell hozzáadni a szükségesekhez, ez valójában pontosan azt érte el, amit akartam.

A beállítás most magában foglalja:

1.  Két külön Git adattár: `docs-nica-dev` (minden tartalmaz) és `docs-nica` (a tiszta, nyilvános verzió).
2.  **FreeFileSync:** Használtam a szabályok meghatározására, hogyan szinkronizáljam a specifikus mappákat (mint a `docs/`, témájú fájlok, `mkdocs.yml`) a két adattár helyszíne között. Képes kezelni a kétirányú szinkronizálást, a tükrözést, és ami a legfontosabb, a törlések helyes továbbítását.
3.  **RealTimeSync (a FreeFileSync része):** Használtam a meghatározott mappák változásainak figyelésére és a szinkronizálás automatikus indítására a FreeFileSync szabályai alapján.

Ez a kombináció végre hatékonyan áthidalja a szakadékot a két adattár között. A `dev` adattár fő tartalommappáiban végrehajtott változások tükröződnek a `public` adattárban, és fordítva, ha szükséges (bár az elsődleges folyamatom a dev -> public). A törlések helyesen vannak kezelve, és mivel csak a *változott* fájlokat szinkronizálja, a `public` adattár commit története pontosan tükrözi a tényleges módosításokat.

## A Maradék Csapda: Szinkronizálás vs. Commit Időzítés

Van még egy hátránya. Amikor egy fájlt megváltoztatok a `dev` adattárban, és a RealTimeSync fut, ezek a változások *azonnal* szinkronizálódnak a `public` adattár könyvtárába, még akkor is, ha még nem commitáltam a `dev` adattárban. A szinkronizálási megoldás független a Git-től.

Ez nem egy nagy probléma, de egy kis óvatosságot igényel, amikor ténylegesen commitáljuk és feltoljuk a változásokat. Alapvetően, amikor a `dev` adattárral dolgozom, biztosítanom kell, hogy mindent ott commitálok, *mielőtt* a figyelmemet a `public` adattárra fordítanám a commit és push érdekében. Emellett megerősíti azt a szokást, hogy *valóban átnézzük a változásokat*, amelyeket a `public` adattárban a commitra jelöltünk, mielőtt ténylegesen commitálnánk és feltolnánk, csak hogy biztosak legyünk abban, hogy az állapot pontosan az, amit szándékozunk.

## Kinek Szól Ez? (Fontos Tisztázás)

Várjunk csak – mielőtt azt gondolnád, hogy ez a teljes beállítás kötelező csak a wiki használatához, hadd tisztázzam. **Mindez a komplexitás? Nem szükséges, ha csak a fő tartalommal akarsz dolgozni.** A fő belépési pont továbbra is szuper egyszerű: klónozd a nyilvános `docs-nica` adattárat (amely csak a Markdown fájlokat és az MkDocs beállítást tartalmazza), és használd azokat az eszközöket, amelyeket *te* preferálsz. Ennyi.

Tehát, miért mentem keresztül mindezen a bajlódáson? Ez a meglehetősen összetett fejlesztői beállítás két fő célt szolgál *számomra*:

1.  **Személyes Biztonsági Hálóm:** Létfontosságú verziókezelés *minden* fejlesztési apróságomhoz és darabomhoz – a konfigurációk, a félkész szkriptek, a tervezési jegyzetek – olyan dolgok, amelyeket nem engedhetek meg magamnak, hogy újra elveszítsek.
2.  **Pontos Munkafolyamatom Megosztása (Opcionálisan):** Ha valaki *szeretné* megismételni a specifikus környezetemet, klónozhatja a `docs-nica-dev` adattárat. Megkapja a teljes Obsidian beállításomat (bővítmények, beállítások, könyvjelzők, keresések, minden!), esetleg a Cursor beállításokat, és bármilyen más integrált eszközt, amit konfiguráltam. Ez egy kész, használatra kész alapbeállítás megosztásának módja.

De az alapvető ötlet nem változott: abszolút megkaphatod csak a nyilvános adattárat, és felépítheted a saját munkafolyamatodat a kedvenc eszközeiddel. Ez az el elaborate tánc az *én* fejlesztői káoszom kezeléséről szól, és egy tervrajzot kínál azoknak, akik akarják.

## Következtetés: Egy Nehezen Megszerzett Megoldás

Összességében örülök, hogy most megtaláltam a megoldást a problémára – még akkor is, ha ez körülbelül két napnyi próbálkozást, hibát és frusztrációt vett igénybe. De a munkafolyamat helyes kialakítása kulcsfontosságú volt a további problémák elkerülése érdekében, biztosítva mind a tiszta nyilvános adattárat, mind a teljes verziókezelésű fejlesztői környezetet.

Tökéletes ez a beállítás? Két adattár és egy külső szinkronizáló eszköz kezelését igényli, plusz egy tudatos munkafolyamatot a commitokhoz. Azonban közvetlenül megoldja a kritikus problémát, hogy *mindent* verziókezelni kell, ami egy komplex fejlesztési folyamathoz szükséges, anélkül, hogy veszélyeztetnénk a fő projekt adattárának tisztaságát, vagy a Git korlátaival küzdenénk a beágyazott struktúrákkal. Azoknak a projekteknek, amelyek kinövik az egyszerű `.gitignore` stratégiákat, ez a megközelítés pragmatikus utat kínál előre, biztonságot és struktúrát nyújtva a fejlesztői munka elkerülhetetlen, rendetlen valóságához.
