---
lang: hu
translation_id: blog/posts/taming-project-complexity
created: 2025-05-02 04:37:37
update: 2025-05-03 22:54:32
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
translation_source_hash: 40282a58c37a5a74d5d1057009bfb53d11f763e5c6ffb18bbe51adba7cee476a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T22:34:46+00:00
translation_source_body_hash: 40282a58c37a5a74d5d1057009bfb53d11f763e5c6ffb18bbe51adba7cee476a
translation_source_metadata_hash: 326d746cf3f5ea2edc1d4adef6bfcba4e454202b335675ecfc6d363623d01f6b
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:01+00:00
translation_source_localized_metadata_hash: 326d746cf3f5ea2edc1d4adef6bfcba4e454202b335675ecfc6d363623d01f6b
translation_source_structural_metadata_hash: 6be66a2d5c4cf84d2025d2de231c2a43257a55f773a5faa74703a0519f2b4c56
---
# A projektkomplexitás megzabolázása – A saga
**A fejlesztői környezet verziókezelése anélkül, hogy beszennyeznéd a fő adattáradat**

Ahogy a projektek fejlődnek, különösen az olyan tudásbázisok vagy dokumentációs oldalak, amelyek több eszközt is érintenek, mint például az MkDocs, az Obsidian, egyéni szkriptek és speciális IDE-k, mint a Cursor, a komplexitás természetesen növekszik. Ezeknek az eszközöknek az integrálása erőteljes munkafolyamatokat hoz létre, de új kihívást is jelent: a magprojektet támogató konfigurációs fájlok, piszkozatok, szkriptek és tervezési dokumentumok növekvő számának kezelése.
<!-- more -->
## A fájó pont: Amikor a `.gitignore` már nem elég

Nemrégiben elértem egy fájdalmas mérföldkövet, amellyel sok fejlesztő találkozik: **több órányi munkát veszítettem el**. Az ok? A fejlesztői munkafolyamatomhoz szükséges fájlok nem voltak verziókezelés alatt.

Sokan közülünk szeretnénk tisztán tartani a nyilvános GitHub adattárunkat. Ehhez a projekthez ez azt jelentette, hogy csak a fő Markdown tartalmat és azokat az alapvető MkDocs fájlokat rögzítettem, amelyek a weboldal felépítéséhez szükségesek. Minden más – az Obsidian vault konfigurációja, a Cursor beállításai, a fordítási piszkozatok, a feladattervezési jegyzetek – gondosan fel volt sorolva a `.gitignore` fájlban. Ez tisztán tartotta a fő adattárat, de védtelenül hagyta az életfontosságú fejlesztői támasztékokat.

Ez a vészharang szerencsére viszonylag korán megszólalt. Miközben a fordítási eszközök integrálásán és a projektstruktúrán belüli jegyzetekkel történő munkafolyamat tervezésén dolgoztam, egy balszerencse jelentős tervezési munkát írt felül. Frusztráló volt, igen, de értékes lecke volt, mielőtt a tét magasabbra emelkedett volna.

## Megoldáskeresés: A sikertelen kísérletek

Kezdeti ötleteim a Git önmagában való okosabb használata körül forogtak, de elakadtam.

### 1. kísérlet: Beágyazott adattárak – Az ágváltás rémálma

Az első gondolatom az volt, hogy megvizsgálom a lehetőségeket, hogy több Git előzmény legyen ugyanazon projekten belül, talán beágyazott adattárak használatával. Az ötlet az volt, hogy legyen egy legfelső szintű "dev" adattár, amely *mindent* követ (IDE beállítások, piszkozatok, a belső adattár fájljai), míg a belső "public" adattár csak a tiszta, telepíthető projektfájlokat tartalmazza. A külső adattár figyelmen kívül hagyná a belső adattár `.git` könyvtárát.

Elméletben ez egy ügyes rétegezett megközelítésnek tűnt. Azonban, amikor ténylegesen megpróbáltam ezt beállítani, nagyon hamar rájöttem, hogy ez nem működik. Először is, a Git nem igazán támogatja a beágyazott adattárakat, legalábbis nem úgy, ahogyan elképzeltem. És van értelme. Van egy figyelmeztetés, amire nem gondoltam: Tegyük fel, hogy a belső adattárban (`docs-nica`) dolgozom, és átváltok egy másik ágra. Most az összes fájl abban a mappában megváltozik (hogy tükrözze az ágat) – de a külső adattár (`docs-nica-dev`) még mindig a fő ágán van. A külső adattár most látja ezeket a fájlváltozásokat, és azt gondolja, hogy ezek *annak* a fő ágának a változásai... Világosan látszik, miért jelent ez problémát. Oké, tehát ez a megközelítés nem működött.

### 2. kísérlet: Külön adattárak + Git hookok – A másolási katasztrófa

Vissza a rajzasztalhoz. A következő ötletem két teljesen különálló adattár volt. Egy `dev` adattár, amely mindent tartalmaz, amire szükségem van (szkriptek, jegyzetek, konfigurációk, *és* a fő projektfájlok). És egy `public` adattár, amely csak a markdown tartalmat és az MkDocs beállítást tartalmazza – csak a lényeget, ahogy a telepítéshez szánták.

De itt jön a csavar: ha valamit megváltoztatunk a `public` adattárban (talán egy gyors javítást ott, vagy a közreműködők változásainak lehúzását), honnan tud róla a `dev` adattár? És gyakoribb esetben, hogyan tükröződnek a `dev` változásai a `public` adattárban? Szükségünk van valamilyen kapcsolatra.

Az első ötlet a GitHub hookok (vagy helyi Git hookok) használata volt. Ezek lehetővé teszik parancsok definiálását, amelyek bizonyos Git műveletek után futnak le, például egy commit után. Beállítottam egy hookot, amely a `dev` adattárban történő commit után lényegében csak átmásolta a releváns fájlokat (a `docs/` mappát, az `mkdocs.yml`-t stb.) a `public` adattár könyvtárába.

Első pillantásra úgy tűnt, hogy működik, de ennek a megközelítésnek két fő problémája volt:

1.  **Zajos előzmények:** A hook minden commit után *minden* releváns fájlt lemásolt. Ez azt jelentette, hogy a `public` adattár mindig azt gondolta, hogy *minden* tartalma megváltozott. Bár technikailag nem tört össze semmit, a commit előzmények kevésbé hasznosak lettek, mivel minden egyes commitban több száz (vagy ezer) fájlt mutattak, lehetetlenné téve annak azonnali azonosítását, hogy mely fájlok *tartalma* változott valójában.
2.  **Törlés vakfolt:** A szkript csak *másolt* fájlokat. Ha töröltem egy fájlt vagy mappát a `dev` adattárban, ez a változás nem tükröződött a `public` adattárban. A régi fájl ott maradt volna.

Átkozottul, már órákat töltöttem ezzel – és még mindig nincs működő megoldás.

## Az áttörés: Külön adattárak + Fájlszinkronizálás

Aztán eszembe jutott egy nyílt forráskódú szoftver, amelyet régen teszteltem helyi mappák szinkronizálására: **FreeFileSync**. Bár sajnálatos, hogy egy újabb eszközkészletet/szoftvert kell hozzáadni a szükséges stack-hez, valójában pontosan azt érte el, amit akartam.

A beállítás most a következőket foglalja magában:

1.  Két külön Git adattár: `docs-nica-dev` (minden tartalmaz) és `docs-nica` (a tiszta, nyilvános verzió).
2.  **FreeFileSync:** Használtam a szabályok meghatározására, hogyan szinkronizáljuk a specifikus mappákat (mint a `docs/`, témájú fájlok, `mkdocs.yml`) a két adattár helyszínei között. Képes kezelni a kétirányú szinkronizálást, a tükrözést, és ami a legfontosabb, a törlések helyes továbbítását.
3.  **RealTimeSync (a FreeFileSync része):** Használtam a meghatározott mappák változásainak figyelésére és a szinkronizálás automatikus indítására a FreeFileSync szabályai alapján.

Ez a kombináció végre hatékonyan áthidalja a szakadékot a két adattár között. A `dev` adattár fő tartalommappáiban végrehajtott változások tükröződnek a `public` adattárban, és fordítva, ha szükséges (bár az elsődleges folyamatom a dev -> public). A törlések helyesen vannak kezelve, és mivel csak a *változott* fájlokat szinkronizálja, a `public` adattár commit előzményei pontosan tükrözik a tényleges módosításokat.

## A megmaradt csapda: Szinkronizálás vs. Commit időzítés

Van még egy hátránya. Amikor egy fájlt megváltoztatok a `dev` adattárban, és a RealTimeSync fut, ezek a változások *azonnal* szinkronizálódnak a `public` adattár könyvtárába, még akkor is, ha még nem commitáltam őket a `dev` adattárban. A szinkronizálási megoldás független a Git-től.

Ez nem egy nagy probléma, de egy kis óvatosságot igényel, amikor ténylegesen commitáljuk és feltoljuk a változásokat. Alapvetően, amikor a `dev` adattárral dolgozom, biztosítanom kell, hogy mindent ott commitáljak, *mielőtt* a figyelmemet a `public` adattárra váltanám a commit és push érdekében. Ezenkívül megerősíti azt a szokást, hogy *igazán átnézzem a változásokat*, amelyeket a `public` adattárban a commitra jelöltem, mielőtt ténylegesen commitálnám és feltolnám, csak hogy biztosítsam, hogy az állapot pontosan az, amit szándékozok.

## Kinek szól ez? (Fontos pontosítás)

Várjunk csak – mielőtt azt gondolnád, hogy ez a teljes beállítás kötelező csak a wiki használatához, hadd tisztázzam. **Mindez a komplexitás? *Nem* szükséges, ha csak a fő tartalommal akarsz dolgozni.** A fő belépési pont továbbra is szuper egyszerű: klónozd a nyilvános `docs-nica` adattárat (amely csak a Markdown fájlokat és az MkDocs beállítást tartalmazza), és használd azokat az eszközöket, amelyeket *te* preferálsz. Ennyi.

Tehát, miért mentem keresztül mindezen a bajlódáson? Ez a meglehetősen összetett fejlesztői beállítás két fő célt szolgál *számomra*:

1.  **Személyes biztonsági hálóm:** Ez létfontosságú verziókezelés *minden* fejlesztői apróságomhoz és darabomhoz – a konfigurációkhoz, a félkész szkriptekhez, a tervezési jegyzetekhez – olyan dolgokhoz, amelyeket nem engedhetek meg magamnak, hogy újra elveszítsek.
2.  **Pontos munkafolyamatom megosztása (opcionálisan):** Ha valaki *szeretné* megismételni a specifikus környezetemet, klónozhatja a `docs-nica-dev` adattárat. Megkapja a teljes Obsidian beállításomat (bővítmények, beállítások, könyvjelzők, keresések, minden!), esetleg a Cursor beállításokat, és bármely más integrált eszközt, amelyet konfiguráltam. Ez egy kész, használatra kész alapbeállítás megosztásának módja.

De az alapvető ötlet nem változott: abszolút megkaphatod csak a nyilvános adattárat, és felépítheted a saját munkafolyamatodat a kedvenc eszközeiddel. Ez az elborult tánc az *én* fejlesztői káoszom kezeléséről szól, és egy tervrajzot kínál azoknak, akik akarják.

## Következtetés: Egy nehezen megszerzett megoldás

Összességében örülök, hogy most megtaláltam a megoldást a problémára – még akkor is, ha ez körülbelül két napnyi próbálkozást, hibát és frusztrációt vett igénybe. De ennek a munkafolyamatnak a helyes beállítása kulcsfontosságú volt a további problémák elkerülése érdekében, biztosítva mind a tiszta nyilvános adattárat, mind a teljes verziókezelésű fejlesztői környezetet.

Tökéletes ez a beállítás? Két adattár és egy külső szinkronizáló eszköz kezelését igényli, plusz egy tudatos munkafolyamatot a commitokhoz. Azonban közvetlenül megoldja azt a kritikus problémát, hogy *mindent* verziókezelni lehessen, ami egy összetett fejlesztési folyamathoz szükséges, anélkül, hogy veszélyeztetnénk a fő projekt adattárának tisztaságát, vagy a Git korlátaival küzdenénk a beágyazott struktúrákkal. Azoknak a projekteknek, amelyek kinövik az egyszerű `.gitignore` stratégiákat, ez a megközelítés pragmatikus utat kínál előre, biztonságot és struktúrát nyújtva a fejlesztői munka elkerülhetetlen, rendetlen valóságához.
