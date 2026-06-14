---
lang: hu
translation_id: doc-sys-2
publish: true
tags: 
created: 2025-01-20 02:58:43
update: 2025-04-13 21:47:35
title: Dokumentációs Rendszer
authors:
  - Marc Bielert
description:
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/doc-sys-2.md
translation_source_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T22:38:28+00:00
translation_source_body_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_source_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:47:08+00:00
translation_source_localized_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_source_structural_metadata_hash: 12f0cb572b5daceba17f262576f82a2900f2588e247dd6c9743ac6c09aba134f
---
[Manifest](doc-sys-manifest.md){ .md-button }
[Obsidian beállítása](Obsidian%20Setup.md){ .md-button }
## Rendszerarchitektúra

Az általános elképzelés
> [!info] Az architektúra áttekintése
>
> Itt található a rendszerarchitektúra grafikus ábrázolása:
>```mermaid
>flowchart LR
>A(Tartalmak) --> B(Verziókezelés)
>C(Szerkesztőszoftver) --> A
>A --> D(Online elérhetővé tétel)
>```

Részletesen:

> [!info] Az architektúra áttekintése
>```mermaid
>flowchart LR
>A[Obsidian] <--> B{Fájlok}
>B <--> C(Github Desktop)
>C <--> D{Github}
>B <--> E(MkDocs)
>D --> F(Github Pages)
>G(Téma: MkDocs-Material) --> E
>H(MkDocs-Publisher) --> E
>E --> D
>```
>
> *   **Obsidian:** Egy opcionális, de általam ajánlott szövegszerkesztő a Markdown fájlok szerkesztéséhez.
> *   **Fájlok:** A dokumentációmat tartalmazó Markdown fájlok.
> *   **Github Desktop:** Egy eszköz a Git-repoim egyszerű kezeléséhez.
> *   **Github:** Egy online szolgáltatás a verziókezeléshez és az együttműködéshez.
> *   **Github Pages:** Egy ingyenes szolgáltatás a weboldalam közzétételéhez.
> *   **MkDocs:** Egy eszköz a weboldal automatikus létrehozásához a Markdown fájljaimból.
> *   **MkDocs-Material:** Egy téma az MkDocs-hoz, amely modern és vonzó elrendezést kínál.
> *   **MkDocs-Publisher**: Pluginok gyűjteménye, amelyek megkönnyítik az együttműködést az Obsidiannal, és további funkciókat kínálnak.

## Komponensek részletesen

### 1. Markdown

> [!info] Markdown mint alap
> A dokumentációmhoz a [Markdown formátumot](Markdown.md) használom. A Markdown egy egyszerű jelölőnyelv, amely lehetővé teszi számomra, hogy egyszerű formázással (pl. címek, listák, hivatkozások) lássam el a szöveget.

**Előnyök:**

*   Könnyen elsajátítható és használható, ami lehetővé teszi, hogy a tartalomra koncentráljak.
*   Platformfüggetlen, így bármilyen eszközön folytathatom a munkámat.
*   Ideális a verziókezeléshez, ami lehetővé teszi a változtatások nyomon követését és kezelését.
*   Jövőbiztos és nem szabadalmaztatott, ami biztosítékot ad arra, hogy a munkám hosszú távon hozzáférhető marad.

[Markdown](Markdown.md){ .md-buttons }

### 2. Obsidian

> [!info] Obsidian mint szövegszerkesztő
> Az [Obsidian](Obsidian%20Setup.md) egy opcionális, de általam ajánlott szövegszerkesztő. A következő előnyöket kínálja számomra:

*   Helyileg tárolhatom az adataimat és offline szerkeszthetem őket, ami rugalmasságot és kontrollt biztosít.
*   Könnyen összekapcsolhatom és hálózatba kapcsolhatom a fájlokat, ami segít a komplex információk rendszerezésében.
*   Címkézhetem és könnyen kezelhetem a fájlokat, ami további rendszerezési dimenziót ad.
*   Grafikusan ábrázolhatom az adataimat, ami segít a minták és kapcsolatok felismerésében.
*   A beépülő modulok segítségével bővíthetem az Obsidian funkcionalitását, ami lehetővé teszi az eszköz testreszabását az egyedi igényeimhez.

### 3. Git és Github

> [!info] Git a verziókezeléshez
> A [Git](https://git-scm.com/) egy verziókezelő rendszer, amely lehetővé teszi a dokumentáció változásainak nyomon követését és kezelését. A [Github](https://github.com/) egy online szolgáltatás, amely lehetővé teszi a Git-repoim tárolását és másokkal való együttműködést.

**Előnyök:**

*   Verziókezelés: Minden változás dokumentálva van, és bármikor nyomon követhető, ami segít a hibák elkerülésében és az áttekintés megőrzésében.
*   Együttműködés: Több személy dolgozhat egyszerre a dokumentáción, ami lehetővé teszi mások visszajelzéseinek és hozzájárulásainak integrálását.
*   Biztonsági mentés: A dokumentációm biztonságban van, és rendszeresen biztonsági mentést készítek róla, ami biztosítékot ad arra, hogy a munkám nem vész el.

### 4. Github Desktop

> [!info] Github Desktop mint eszköz
> A [Github Desktop](../_inbox/Github%20Desktop.md) egy grafikus felület a Git-hez, amely lehetővé teszi a Git egyszerű használatát parancssor nélkül.

**Előnyök:**

*   Egyszerű használat, ami megkönnyíti a Git használatát.
*   Nincs szükség parancssori ismeretekre, ami időt és erőfeszítést takarít meg.
*   Egyszerűsíti a munkafolyamatomat, ami lehetővé teszi, hogy a tartalom létrehozására koncentráljak.

### 5. MkDocs

> [!info] MkDocs mint weboldalgenerátor
> Az [MkDocs](https://mkdocs.org) egy statikus weboldalgenerátor, amely a Markdown fájljaimat statikus weboldallá alakítja.

**Előnyök:**

*   Egyszerű weboldalkészítés, ami lehetővé teszi a dokumentációm gyors és egyszerű közzétételét.
*   Gyors frissítés, ami lehetővé teszi a változtatások valós idejű megtekintését.
*   Konzisztens elrendezés, ami professzionális és egységes megjelenést biztosít a dokumentációm számára.
*   Offline előnézet, ami lehetővé teszi a dokumentációm ellenőrzését a közzététel előtt.

### 6. Github Pages

> [!info] Github Pages a tárhelyhez
> A [Github Pages](../_inbox/Github%20Pages.md) a Github ingyenes tárhelyszolgáltatása, amely lehetővé teszi a weboldalam egyszerű online közzétételét.

**Előnyök:**

*   Ingyenes tárhely, ami lehetővé teszi a dokumentációm további költségek nélküli közzétételét.
*   Egyszerű közzététel, ami leveszi a vállamról a közzététel technikai megvalósítását.
*   Megbízható, ami biztosítékot ad arra, hogy a dokumentációm mindig elérhető.

### 7. MkDocs-Material

> [!info] MkDocs-Material mint téma
> Az [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) egy téma az MkDocs-hoz, amely modern és vonzó elrendezést kínál.

**Előnyök:**

*   Modern dizájn, ami professzionálissá és naprakésszé teszi a dokumentációmat.
*   Testreszabható, ami lehetővé teszi az elrendezés testreszabását az egyedi igényeimhez.
*   Felhasználóbarát, ami megkönnyíti a dokumentáció használatát.

### 8. MkDocs-Publisher

> [!info] MkDocs-Publisher mint plugin gyűjtemény
> Az [MkDocs-Publisher](https://github.com/mkdocs-publisher/mkdocs-publisher) egy MkDocs plugin gyűjtemény, amely megkönnyíti az együttműködést az Obsidiannal és további funkciókat kínál.

**Előnyök:**

- **Egyszerűsített Obsidian integráció:** Az Obsidian Markdown szintaxisának automatikus igazítása (Callouts, Wikilinks stb.)
- **Bővített metaadatok:** Címkék és kategóriák integrálása az Obsidian frontmatter-jából.

## Munkafolyamat

> [!info] Az én munkafolyamatom
> Itt látható a tipikus munkafolyamatom:

1.  Markdown fájlokat hozok létre és szerkesztek egy szövegszerkesztővel (opcionálisan Obsidian).
2.  Helyileg mentem a Markdown fájlokat.
3.  A változtatásokat a Github Desktop segítségével feltöltöm a Git-repoimra.
4.  Automatikus weboldalgenerálást végzek az MkDocs segítségével.
5.  A weboldalt a Github Pages segítségével teszem közzé.

## Fájlrendszer

> [!info] Könyvtárstruktúra
> Itt látható a rendszerem könyvtárstruktúrája:
>
> ```
>/docs/     (Itt találhatók a Markdown fájljaim)
>/site/     (Itt generálódik a weboldal)
>license    (Licencinformációk)
>mkdocs.yml (Konfigurációs fájl az MkDocs-hoz)
>readme.md  (Fájl a repository leírásához)
>```

## Tartalomkészítési alternatívák

> [!info] Alternatívák a tartalomkészítéshez
> Tisztában vagyok vele, hogy nem mindenki ismeri a Markdown-t és a Git-et. Ezért a következő alternatívákat kínálom:

1.  **Wordpress:** A tartalmak Wordpress-ben oldalakként hozhatók létre.
2.  **Szöveges fájl, Word fájl:** A tartalmak szöveges fájlként, Word fájlként (vagy más tipikus formátumokban) hozhatók létre.

Ebben az esetben a tartalmakat be tudom építeni a rendszerbe.
