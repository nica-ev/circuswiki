---
lang: hu
translation_id: github-for-users
publish: true
tags:
  - github
  - tutorial
created: 2025-01-18 23:14:04
update: 2026-06-12 18:26:00
title: Közvetlen együttműködés a GitHub repóban
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/github-for-users.md
translation_source_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-12T17:31:12+00:00
translation_source_body_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_source_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:51:16+00:00
translation_source_localized_metadata_hash: 2a66a70e78516539cd6e01bb623a9a0267cfab77111903ce6a9a9dd30aac506c
translation_source_structural_metadata_hash: 69966c4b32b093dc5fdaa8e7127a710d8477892c36f2859ba38215866bb73327
---
> [!info] Röviden
> Ez az oldal azoknak szól, akik közvetlenül a CircusWiki Markdown-fájljain szeretnének dolgozni. Normál hozzájárulásokhoz nincs szükséged erre az útvonalra: anyagokat e-mailben is egyszerűen elküldhetsz.

A közvetlen közreműködés a GitHubon keresztül praktikus, ha rendszeresen szeretnél oldalakat javítani, új Markdown-fájlokat létrehozni, vagy a CircusWiki-vaulttal dolgozni egy olyan szerkesztőben, mint az Obsidian.

Ha csak egy játékot, egy módszert, egy PDF-et, egy linket vagy egy javítást szeretnél hozzáadni, akkor általában az egyszerűbb út a jobb:

[Vissza a Közreműködéshez](mitmachen.md){ .md-button }

## Amire szükséged lesz

- egy ingyenes GitHub-fiók: [https://github.com/join](https://github.com/join)
- opcionálisan GitHub Desktop: [https://desktop.github.com/](https://desktop.github.com/)
- egy szövegszerkesztő Markdown-fájlokhoz, például Obsidian, VS Code vagy egy egyszerű szerkesztő

A GitHub Desktop nem kötelező, de sokak számára egyszerűbb, mint a parancssor.

## A tár (repository) megtalálása

A nyilvános tár itt található:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Ott találhatók a tényleges Markdown-fájlok, képek, fordítások és eszközök, amelyekből a weboldal felépül.

## Munkamenet röviden

A tipikus folyamat a következő:

1. A tár (repository) "forkolása" a GitHubon.
2. A saját másolat klónozása a saját számítógépre.
3. A változtatások végrehajtása egy új ágon (branch).
4. Fájlok szerkesztése vagy új Markdown-fájlok létrehozása.
5. A változtatások "commit"-olása.
6. Az ág (branch) feltöltése a GitHubra.
7. Pull Request (lekéréses kérelem) megnyitása, hogy a változtatást ellenőrizni és átvenni lehessen.

## Lépésről lépésre a GitHub Desktop segítségével

### 1. A tár (repository) "forkolása"

Nyisd meg a CircusWiki tárát (repository) a GitHubon:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Kattints a `Fork` gombra. Ez létrehoz egy saját másolatot a tárról a GitHub-fiókodban. Ebben a másolatban dolgozhatsz anélkül, hogy közvetlenül módosítanád a fő projektet.

### 2. A tár (repository) klónozása

Nyisd meg a GitHub Desktopot és válaszd a következőt:

```text
File -> Clone repository...
```

Válaszd ki a `nica-ev/circuswiki` "fork"-odat, és adj meg egy mappát a számítógépeden.

Ezután a fájlok helyi másolatával fogsz rendelkezni.

### 3. Egy új ág (branch) létrehozása

A legjobb, ha a változtatásaidhoz létrehozol egy saját ágat (branch), például:

```text
jatek-leiras-kiegeszitese
link-javitas
uj-modszer-balansz
```

Egy ág (branch) elkülönítve tartja a munkádat a fő állástól. Ez megkönnyíti a későbbi ellenőrzést.

### 4. Fájlok szerkesztése

A nyilvános tartalmak főként a nyelvi mappákban találhatók a `docs/` alatt:

```text
docs/de/
docs/en/
docs/es/
docs/pl/
...
docs/img/
```

Minden nyelv egyenértékű. Nincs fő nyelv, amelyben az új tartalmaknak alapvetően meg kellene születniük.

Ha új eredeti oldalt hozol létre, helyezd el a nyelvi mappában, amelyen a szöveget írod. Egy spanyol eredeti szöveg például a `docs/es/` mappába kerül, egy német a `docs/de/` mappába, egy angol a `docs/en/` mappába.

Fontos a fájl elején található "frontmatter". Ott fel kell ismerhetőnek lennie, hogy az oldal eredeti, például:

```yaml
translation_status: original
translation_source_lang: es
```

A `translation_source_lang` felel meg az eredeti szöveg nyelvét. Ebből az eredetiből később automatikusan fordítások hozhatók létre minden támogatott nyelvre.

Szerkesztéskor ügyelj a következőkre:

- Ne töröld a fájl elején lévő "frontmatter"-t.
- Új eredeti oldalak esetén állítsd be a `translation_status: original` és a megfelelő `translation_source_lang` értéket.
- Lehetőség szerint tartsd meg a meglévő linkeket.
- Ne publikálj privát adatokat, API-kulcsokat vagy belső jegyzeteket.
- Képeket csak akkor használj, ha a felhasználási jogok tiszták.
- Inkább kis, világos változtatásokat végezz, mint nagy, vegyes változtatásokat.

### 5. Változtatások "commit"-olása

A GitHub Desktopon a megváltozott fájlokat a `Changes` (Változtatások) részben láthatod.

Írj egy rövid összefoglalót, például:

```text
Javítom a mozgójáték anyaglistáját
Biztonsági figyelmeztetést egészítek ki a Beigomához
Új játékleírást adok hozzá
```

Ezután kattints a `Commit to <branch-name>` gombra.

### 6. Változtatások feltöltése

Kattints a `Push origin` gombra, hogy feltöltsd az ágat (branch) a GitHubra.

### 7. Pull Request (lekéréses kérelem) megnyitása

A GitHub Desktop vagy a GitHub böngészőben ezután felajánlja a Pull Request (lekéréses kérelem) létrehozását.

A Pull Request (lekéréses kérelem) azt jelenti: a te változtatásodat javaslod a fő tárhoz (repository). A változtatást ellenőrzik, esetleg kommentálják, majd átveszik vagy tovább dolgoznak rajta.

## Markdown alapok

A Markdown egy egyszerű szöveges formátum. A legfontosabb jelek elegendőek a legtöbb hozzájáruláshoz:

```markdown
# Nagy cím
## Szakaszcím

Normál szöveg **félkövérrel** és *dőlt betűkkel*.

- Listaelem
- Még egy listaelem

[Link szövege](https://www.example.com)
```

## Ha valami nem világos

A közvetlen közreműködés a GitHubon keresztül nem kell, hogy azonnal tökéletes legyen. Ha megnyitsz egy Pull Requestet (lekéréses kérelmet), és valami mégsem stimmel, azt az ellenőrzés során tisztázni lehet.

Ha csak tartalmat szeretnél hozzáadni, és a technikai út túl bonyolultnak tűnik, használd egyszerűen az e-mail címet a [Közreműködés oldalán](mitmachen.md).
