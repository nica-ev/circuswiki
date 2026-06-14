---
lang: sk
translation_id: blog/posts/taming-project-complexity
created: 2025-05-02 04:37:37
update: 2025-05-03 22:54:32
date: 2025-05-03T11:00:00
publish: true
tags: 
title: Zvládnutie zložitosti projektu - Sága
description: Cesta k efektívnemu verzovaniu komplexného vývojového prostredia bez znečistenia hlavného repozitára projektu.
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Taming Project Complexity.md
translation_source_hash: 40282a58c37a5a74d5d1057009bfb53d11f763e5c6ffb18bbe51adba7cee476a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T18:30:28+00:00
translation_source_body_hash: 40282a58c37a5a74d5d1057009bfb53d11f763e5c6ffb18bbe51adba7cee476a
translation_source_metadata_hash: 326d746cf3f5ea2edc1d4adef6bfcba4e454202b335675ecfc6d363623d01f6b
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:41:08+00:00
translation_source_localized_metadata_hash: 326d746cf3f5ea2edc1d4adef6bfcba4e454202b335675ecfc6d363623d01f6b
translation_source_structural_metadata_hash: 6be66a2d5c4cf84d2025d2de231c2a43257a55f773a5faa74703a0519f2b4c56
---
# Zvládanie zložitosti projektu – Ságá
**Správa verzií vývojového prostredia bez znečistenia vášho hlavného repozitára**

Ako projekty rastú, najmä vedomostné bázy alebo dokumentačné stránky, ktoré zahŕňajú viacero nástrojov ako MkDocs, Obsidian, vlastné skripty a špecializované IDE ako Cursor, prirodzene rastie aj ich zložitosť. Integrácia týchto nástrojov vytvára výkonné pracovné postupy, ale zároveň prináša novú výzvu: správu rastúceho počtu konfiguračných súborov, konceptov, skriptov a plánovacích dokumentov, ktoré podporujú hlavný projekt.
<!-- more -->
## Bolestivý bod: Keď `.gitignore` nestačí

Nedávno som narazil na bolestivý míľnik, s ktorým sa stretáva mnoho vývojárov: **stratu niekoľkých hodín práce**. Vinník? Súbory kľúčové pre môj vývojový pracovný postup neboli pod správou verzií.

Rovnako ako mnohí, aj ja som chcel udržať svoj verejne prístupný repozitár na GitHub čistý. Pre tento projekt to znamenalo nahrávanie iba základného obsahu v Markdown a nevyhnutných súborov MkDocs potrebných na zostavenie webovej stránky. Všetko ostatné – konfigurácia môjho Obsidian trezoru, nastavenia Cursoru, skripty na preklad konceptov, poznámky na plánovanie úloh – bolo starostlivo uvedené v `.gitignore`. Tým bol hlavný repozitár prehľadný, ale moja životne dôležitá vývojová infraštruktúra zostala nechránená.

Toto prebudenie prišlo, našťastie, pomerne skoro. Pri práci na integrácii prekladateľských nástrojov a plánovaní pracovného postupu pomocou poznámok v štruktúre projektu došlo k nehode, ktorá prepísala významnú časť plánovacej práce. Frustrujúce, áno, ale cenná lekcia naučená skôr, než sa vklady zvýšili.

## Hľadanie riešenia: Neúspešné pokusy

Moje počiatočné nápady sa sústredili na šikovnejšie využitie samotného Gitu, ale narazil som na prekážky.

### Pokus 1: Vnořené repozitáre – Nočná mora prepínania vetiev

Mojou prvou myšlienkou bolo preskúmať spôsoby, ako mať viacero histórií Gitu v tom istom adresári projektu, možno pomocou vnořených repozitárov. Myšlienka bola mať „dev“ repozitár na najvyššej úrovni sledujúci *všetko* (nastavenia IDE, koncepty, súbory vnútorného repozitára), zatiaľ čo vnútorný „verejný“ repozitár by obsahoval iba čisté, nasaditeľné súbory projektu. Vonkajší repozitár by ignoroval adresár `.git` vnútorného repozitára.

V teórii to znelo ako elegantný vrstvený prístup. Keď som sa to však pokúsil nastaviť, veľmi rýchlo som si uvedomil, že to nefunguje. Predovšetkým Git v skutočnosti nepodporuje vnořené repozitáre, aspoň nie tak, ako som si to predstavoval. A má to svoj dôvod. Existuje však jedna výhrada, o ktorej som nepremýšľal: Povedzme, že pracujem vo vnútornom repozitári (`docs-nica`) a prepnem na inú vetvu. Teraz sa všetky súbory v tomto priečinku zmenia (aby odrážali vetvu) – ale vonkajší repozitár (`docs-nica-dev`) je stále na svojej hlavnej vetve. Vonkajší repozitár teraz vidí všetky tieto zmeny súborov a myslí si, že sú to zmeny na *jeho* hlavnej vetve... Je jasné, prečo je to problém. Dobre, takže tento prístup nefungoval.

### Pokus 2: Samostatné repozitáre + Git háčiky – Katastrofa kopírovania

Späť k rysovacej doske. Mojou ďalšou myšlienkou bolo mať dva úplne oddelené repozitáre. Jeden „dev“, ktorý obsahuje všetko, čo potrebujem (skripty, poznámky, konfigurácie, *a tiež* základné súbory projektu). A jeden „public“, ktorý obsahuje iba obsah v Markdown a nastavenie MkDocs – len to najnutnejšie, tak ako je to určené na nasadenie.

Ale tu prichádza háčik: ak niečo zmeníme vo „public“ repozitári (možno rýchla oprava priamo tam, alebo stiahnutie zmien od spolupracovníkov), ako by to mal „dev“ repozitár vedieť? A častejšie, ako sa zmeny v „dev“ prejavia v „public“? Potrebujeme nejaký spôsob, ako ich prepojiť.

Prvou myšlienkou bolo použiť GitHub háčiky (alebo lokálne Git háčiky). Tieto umožňujú definovať príkazy, ktoré sa spustia po určitých akciách Gitu, ako je napríklad commit. Nastavil som háčik, ktorý po commite v „dev“ repozitári jednoducho skopíruje relevantné súbory (priečinok `docs/`, `mkdocs.yml` atď.) do adresára „public“ repozitára.

Na prvý pohľad sa to zdalo fungovať, ale tento prístup mal dva hlavné problémy:

1.  **Neprehľadná história:** Háčik kopíroval *všetky* relevantné súbory pri *každom* commite. To znamenalo, že „public“ repozitár si vždy myslel, že sa zmenil *všetok* jeho obsah. Aj keď to technicky nič neporušovalo, história commitov sa stala menej užitočnou, zobrazujúc stovky (alebo tisíce) zmien súborov pri každom jednom commite, čo znemožňovalo okamžite identifikovať, ktoré *obsahy* súborov sa skutočne zmenili.
2.  **Neviditeľnosť mazania:** Skript iba *kopíroval* súbory. Ak som v „dev“ repozitári zmazal súbor alebo priečinok, táto zmena sa neprejavila v „public“ repozitári. Starý súbor tam jednoducho zostal.

Prekliatie, už som na tom strávil hodiny – a stále žiadne funkčné riešenie.

## Prelom: Samostatné repozitáre + Synchronizácia súborov

Potom som si spomenul na open-source softvér, ktorý som dávno testoval na synchronizáciu lokálnych priečinkov: **FreeFileSync**. Aj keď je nešťastné pridať ďalšiu sadu nástrojov/softvéru do potrebného balíka, v skutočnosti to dosiahlo presne to, čo som chcel.

Nastavenie teraz zahŕňa:

1.  Dva samostatné Git repozitáre: `docs-nica-dev` (obsahujúci všetko) a `docs-nica` (čistá, verejná verzia).
2.  **FreeFileSync:** Používa sa na definovanie pravidiel pre synchronizáciu konkrétnych priečinkov (ako `docs/`, súbory tém, `mkdocs.yml`) medzi umiestneniami oboch repozitárov. Dokáže zvládnuť obojsmernú synchronizáciu, zrkadlenie a, čo je kľúčové, správne propagovať mazanie.
3.  **RealTimeSync (súčasť FreeFileSync):** Používa sa na monitorovanie definovaných priečinkov na zmeny a automatické spustenie synchronizácie na základe pravidiel FreeFileSync.

Táto kombinácia konečne efektívne premostila priepasť medzi dvoma repozitármi. Zmeny vykonané v základných priečinkoch obsahu „dev“ repozitára sa zrkadlia do „public“ repozitára a naopak, ak je to potrebné (aj keď môj primárny tok je dev -> public). Mazanie je spracované správne a pretože synchronizuje iba *zmenené* súbory, história commitov v „public“ repozitári presne odráža skutočné úpravy.

## Zostávajúci háčik: Načasovanie synchronizácie vs. commitu

Stále však existuje jeden nedostatok. Keď zmením súbor v „dev“ repozitári a RealTimeSync beží, tieto zmeny sa synchronizujú do adresára „public“ repozitára *okamžite*, aj keď ešte nie sú v „dev“ repozitári commitnuté. Riešenie synchronizácie je oddelené od Gitu.

Nie je to super veľký problém, ale vyžaduje si to trochu viac opatrnosti pri skutočnom committovaní a pushovaní zmien. V podstate, keď pracujem na „dev“ repozitári, musím sa uistiť, že tam všetko commitnem *predtým*, ako preorientujem pozornosť na „public“ repozitár na commit a push. Taktiež to posilňuje návyk *skutočne skontrolovať zmeny* pripravené na commit v „public“ repozitári pred ich skutočným committovaním a pushovaním, len aby som sa uistil, že stav je presne taký, aký zamýšľam.

## Pre koho je to určené? (Dôležité objasnenie)

Počkajte, predtým, než si budete myslieť, že celé toto nastavenie je povinné len na používanie wiki, dovoľte mi objasniť. **Všetka táto zložitosť? Nie je potrebná, ak chcete pracovať len so základným obsahom.** Hlavný vstupný bod je stále super jednoduchý: naklonujte verejný `docs-nica` repozitár (ktorý obsahuje len súbory v Markdown a nastavenie MkDocs) a používajte akékoľvek nástroje, ktoré *vy* preferujete. To je všetko.

Prečo som sa teda namáhal s týmto všetkým? Toto pomerne zložité vývojové nastavenie slúži *mnou* dvom hlavným účelom:

1.  **Moja osobná záchranná sieť:** Je to kľúčová správa verzií pre *všetky moje vývojové drobnosti a kúsky* – konfigurácie, nedokončené skripty, plánovacie poznámky – veci, ktoré si nemôžem dovoliť znova stratiť.
2.  **Zdieľanie môjho presného pracovného postupu (voliteľne):** Ak niekto *chce* replikovať moje špecifické prostredie, môže naklonovať `docs-nica-dev` repozitár. Dostane moje kompletné nastavenie Obsidian (pluginy, nastavenia, záložky, vyhľadávania, všetko!), potenciálne nastavenia Cursoru a akékoľvek iné integrované nástroje, ktoré som nakonfiguroval. Je to spôsob, ako zdieľať pripravené základné nastavenie.

Základná myšlienka sa však nezmenila: môžete si absolútne vziať len verejný repozitár a postaviť si okolo neho vlastný pracovný postup s vašimi obľúbenými nástrojmi. Tento prepracovaný tanec je o správe *môjho* vývojového chaosu a ponúka plán pre tých, ktorí ho chcú.

## Záver: Tvrdohlavo získané riešenie

Celkovo som rád, že som teraz našiel riešenie problému – aj keď ma to stálo asi dva dni skúšania, chýb a frustrácie. Ale správne nastavenie tohto pracovného postupu bolo kľúčové na zabránenie ďalším problémom v budúcnosti, čím sa zabezpečil čistý verejný repozitár aj plne spravované vývojové prostredie.

Je toto nastavenie dokonalé? Vyžaduje si správu dvoch repozitárov a externého synchronizačného nástroja, plus vedomý pracovný postup pre committovanie. Priamo však rieši kritický problém správy verzií *všetkého*, čo je potrebné pre komplexný vývojový proces, bez toho, aby sa ohrozila čistota hlavného repozitára projektu alebo bojovalo s obmedzeniami Gitu pri vnořených štruktúrach. Pre projekty, ktoré prerastú jednoduché stratégie `.gitignore`, tento prístup ponúka pragmatickú cestu vpred, poskytujúc bezpečnosť a štruktúru pre nevyhnutnú, chaotickú realitu vývojovej práce.
