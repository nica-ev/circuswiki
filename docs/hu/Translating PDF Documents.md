---
lang: hu
translation_id: translating-pdf-documents
created: 2025-05-03 21:32:10
update: 2025-05-03 22:24:12
publish: true
tags:
  - tutorial
title: PDF-dokumentumok fordítása nagyméretű nyelvi modellekkel
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Translating PDF Documents.md
translation_source_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-14T19:33:20+00:00
translation_source_body_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_source_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T19:33:20+00:00
translation_source_localized_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_source_structural_metadata_hash: 2b0fe62dfc02049e3f55e308c77f83a911789c48b0827769d60d3f00737d38b6
---
# Útmutató: PDF dokumentumok fordítása nagyméretű nyelvi modellek (LLM) segítségével

## Bevezetés

Ez az útmutató egy olyan folyamatot ismertet, amellyel PDF dokumentumok tartalmát lehet lefordítani, különös tekintettel azokra, amelyek nem választható, kép alapú szöveget tartalmaznak, nagyméretű nyelvi modellek (LLM) segítségével. A munkafolyamat magában foglalja a PDF optimalizálását, a szöveg kinyerését optikai karakterfelismeréssel (OCR), a szöveg fordítását, és végül a fordítás újbóli PDF formátumba rendezését.

**Előfeltételek:**

*   Google-fiók (a Google AI Studio eléréséhez).
*   Opcionális: PDF optimalizáló szoftver (pl. pdf24 Creator).
*   Opcionális: Markdown és PDF exportálására alkalmas szövegszerkesztő vagy kiadványszerkesztő (pl. Obsidian, Microsoft Word).

## 1. lépés: A PDF dokumentum előkészítése

**Cél:** A PDF fájlméretének csökkentése az LLM általi feldolgozás optimalizálása érdekében, miközben megőrizzük a szöveg olvashatóságát. Az LLM-ek gyakran rendelkeznek bemeneti méretkorlátokkal, és a kisebb fájlok hatékonyabban dolgozhatók fel.

**Megfontolások:**

*   **Szövegalapú PDF-ek:** Ha a PDF-en belüli szöveg kiválasztható (azaz elektronikusan beágyazott), a fájlméret csökkentése általában könnyebb, és kisebb méreteket érhet el minőségvesztés nélkül.
*   **Kép alapú PDF-ek:** Ha a PDF oldalai szöveget tartalmazó képek (a szöveg nem választható ki egyenként), a méretcsökkentés képtömörítést foglal magában. Óvatosan kell eljárni, hogy ne csökkentsük annyira a minőséget, hogy a szöveg olvashatatlanná váljon az OCR számára.

**Eljárás (Példa a pdf24 használatával):**

1.  Nyissa meg a PDF dokumentumot egy olyan eszközzel, mint a pdf24 Creator ([https://www.pdf24.org/](https://www.pdf24.org/)).
2.  Használja a tömörítési vagy méretcsökkentési funkciókat. A gyakran hatékony beállítások közé tartoznak:
    *   A webes optimalizálás engedélyezése.
    *   A színek szürkeárnyalatosra konvertálása.
3.  Kísérletezzen a tömörítési szintekkel, célozva egy **5 MB** alatti fájlméretre, miközben biztosítja, hogy a szöveg tiszta és olvasható maradjon.
4.  Mentse el az optimalizált PDF fájlt.

## 2. lépés: Szöveg kinyerése a Google AI Studio segítségével (Átírás/OCR)

**Cél:** Az LLM multimodális képességeinek használata az OCR elvégzésére az előkészített PDF-en, és a szöveges tartalom strukturált formátumban történő kinyerése.

**Eljárás:**

1.  Lépjen a **Google AI Studio** oldalára ([https://aistudio.google.com/](https://aistudio.google.com/)) és jelentkezzen be Google-fiókjával. Megjegyzés: Az AI Studio elsősorban modellekkel és promptokkal való kísérletezésre szolgáló eszköz.
2.  Indítson új munkamenetet vagy csevegést.
3.  Csatolja az optimalizált PDF fájlt a munkamenethez (pl. a csatolás gomb vagy húzd és ejtsd funkció használatával).
4.  Írja be a következő promptot a felhasználói üzenet mezőbe:
    ```
    Kérem, írja át a csatolt PDF-et. Képeket tartalmaz szöveggel, ami OCR-t igényel. Adja meg az átírást megfelelő Markdown formátumban, fejlécet és listákat használva, hogy olyan struktúrát hozzon létre, amely szorosan tükrözi az eredeti dokumentum elrendezését.
    ```
5.  Konfigurálja a modell beállításait:
    *   Tartsa meg az alapértelmezett beállításokat, hacsak nincsenek speciális követelményei.
    *   Állítsa a **Hőmérsékletet** **0.1**-re. Az alacsonyabb hőmérséklet determinisztikusabb és kevésbé kreatív kimenetet ösztönöz, ami alkalmas a pontos átíráshoz.
6.  Küldje el a promptot. Az átírási folyamat több percig is eltarthat (potenciálisan 4-6 perc vagy hosszabb, a PDF méretétől és összetettségétől függően).
7.  Miután a generálás befejeződött, másolja ki a kapott Markdown szöveget.
    *   *1. módszer:* Használja a felületen gyakran elérhető másolási opciót (pl. a válaszhoz kapcsolódó menün keresztül).
    *   *2. módszer:* Manuálisan jelölje ki az összes generált szöveget, és másolja ki (Ctrl+C vagy jobb egérgomb -> Másolás).
8.  Illessze be a kimásolt Markdown szöveget egy egyszerű szövegszerkesztőbe (mint a Jegyzettömb, VS Code, Obsidian stb.).
9.  Mentse el ezt a tartalmat egyszerű szöveges fájlként. Ajánlott a `.txt` vagy `.md` (Markdown) kiterjesztések használata. A Markdown formázás segít megőrizni a dokumentum struktúráját (fejlécek, listák).

![Google AI Studio - Képernyőkép átírás](../img/Screenshot-Google-AiStudio-Transcription.png){ width=600 }

## 3. lépés: A kinyert szöveg fordítása a Google AI Studio segítségével

**Cél:** A kinyert Markdown szöveg lefordítása a kívánt célnyelvre, megőrizve az eredeti struktúrát és formázást.

**Eljárás:**

1.  A **Google AI Studio**-ban indítson egy **új csevegést** a friss kontextus biztosítása érdekében a fordítási feladathoz.
2.  Csatolja a mentett `.txt` vagy `.md` fájlt, amely a kinyert Markdown szöveget tartalmazza.
3.  Írjon be egy fordítási promptot, megadva a forrás- és célnyelvet. Példa angolról olaszra:
    ```
    Kérem, fordítsa le a csatolt Markdown fájlt (angol) olaszra. Tartsa meg pontosan az eredeti struktúrát, formázást, hangnemet és beszédstílust.
    ```
    *   **Módosítsa a promptot** az Ön specifikus forrás- és célnyelveinek megfelelően (pl. "...fordítsa le a csatolt Markdown fájlt (német) spanyolra..."). A fordítás minősége változhat a nyelvpárostól függően.
4.  Konfigurálja a modell beállításait:
    *   Győződjön meg arról, hogy az alapértelmezett beállítások megfelelőek.
    *   Állítsa a **Hőmérsékletet** **0.1**-re, hogy elősegítse a forrásszöveghez és struktúrához való hűséget a fordítás során.
5.  Küldje el a promptot. A fordítás is több percig tarthat, hasonlóan az átírási időhöz.
6.  A generálás után másolja ki a lefordított Markdown szöveget a 2. lépésben leírt módszerekkel (felület másolás gomb vagy manuális kijelölés).

![Google AI Studio - Képernyőkép fordítás](../img/Screenshot-Google-AiStudio-Translation.png){ width=600 }

## 4. lépés: A lefordított szöveg újbóli PDF dokumentummá rendezése

**Cél:** A lefordított Markdown szöveg konvertálása PDF dokumentummá megosztás vagy archiválás céljából.

**Eljárás:**

1.  Illessze be a kimásolt lefordított Markdown szöveget egy megfelelő alkalmazásba.
2.  **Ajánlott:** Használjon egy szövegszerkesztőt vagy kiadványszerkesztőt, amely érti a Markdown formázást a struktúra megőrzése érdekében (fejlécek, listák stb.).
    *   Az **Obsidian** ([https://obsidian.md/](https://obsidian.md/)) egy ingyenes eszköz, amely jól működik Markdown fájlokkal, és gyakran rendelkezik PDF exportálási képességekkel (közvetlenül vagy bővítményeken keresztül).
    *   Modern kiadványszerkesztők (mint a Microsoft Word) is képesek lehetnek Markdown importálására vagy beillesztésére, és PDF-ként menthetők/exportálhatók, bár a formázási hűség változhat.
    *   Dedikált Markdown-PDF konverterek is elérhetők online vagy telepíthető szoftverként.
3.  Használja az alkalmazás "Exportálás PDF-be" vagy "Mentés másként PDF" funkcióját.
4.  Tekintse át a keletkezett PDF-et, hogy megbizonyosodjon arról, hogy a formázás és a tartalom a vártnak megfelelően jelenik meg.

## Következtetés

Ez az útmutató bemutatott egy munkafolyamatot a Google AI Studio kihasználására PDF dokumentumok átírására és fordítására, beleértve azokat is, amelyek OCR-t igényelnek. A PDF előkészítésével, a szöveg kinyerésével egy konfigurált LLM segítségével, az eredmény fordításával és újbóli formázásával a felhasználók a dokumentumaik lefordított változatait kaphatják meg. Bár ez a módszer ingyenes vagy alacsony költségű megoldást kínál, a felhasználóknak tisztában kell lenniük az OCR pontosságának és a fordítás minőségének lehetséges eltéréseivel, különösen összetett elrendezések vagy kevésbé elterjedt nyelvek esetén. A feldolgozási idők jelentősen függnek a dokumentum méretétől és a szerver terhelésétől.
