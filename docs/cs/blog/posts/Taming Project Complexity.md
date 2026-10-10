---
lang: cs
translation_id: blog/posts/taming-project-complexity
created: 2025-05-02 04:37:37
update: 2026-10-10 20:09:23
date: 2025-05-03T11:00:00
publish: true
tags: 
title: Zvládnutí složitosti projektu - Sága
description: Cesta k efektivní správě verzí složitého vývojového prostředí bez znečištění hlavního repozitáře projektu.
authors:
  - Marc Bielert
categories: 
  - development
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/blog/posts/Taming Project Complexity.md
translation_source_hash: 15300a3605c6b0a1fbd64d24db3d47f664d6814dc7ad022e57bdace07abf1462
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-10-10T20:55:37+00:00
translation_source_body_hash: 15300a3605c6b0a1fbd64d24db3d47f664d6814dc7ad022e57bdace07abf1462
translation_source_metadata_hash: 326d746cf3f5ea2edc1d4adef6bfcba4e454202b335675ecfc6d363623d01f6b
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-10-10T20:55:37+00:00
translation_source_localized_metadata_hash: 326d746cf3f5ea2edc1d4adef6bfcba4e454202b335675ecfc6d363623d01f6b
translation_source_structural_metadata_hash: e3d56cc63df642dafa063d27bdc292098f6ac52159e83b1249537b0aebc40ffb
---
# Zkrocení složitosti projektu – Sága
**Správa verzí vývojového prostředí bez znečištění vašeho hlavního repozitáře**

Jak projekty rostou, zejména znalostní báze nebo dokumentační weby zahrnující více nástrojů, jako je MkDocs, Obsidian, vlastní skripty a specializovaná IDE jako Cursor, složitost přirozeně narůstá. Integrace těchto nástrojů vytváří výkonné pracovní postupy, ale také přináší novou výzvu: správu rostoucího počtu konfiguračních souborů, konceptů, skriptů a plánovacích dokumentů, které podporují hlavní projekt.
<!-- more -->
## Bolavé místo: Když `.gitignore` nestačí

Nedávno jsem narazil na bolestivý milník, který zažívá mnoho vývojářů: **ztrátu několika hodin práce**. Viník? Soubory klíčové pro můj vývojový pracovní postup nebyly pod správou verzí.

Stejně jako mnozí, i já jsem chtěl udržet svůj veřejný repozitář na GitHubu čistý. Pro tento projekt to znamenalo nahrávat pouze základní obsah ve formátu Markdown a nezbytné soubory MkDocs potřebné k sestavení webu. Vše ostatní – konfigurace mého trezoru Obsidian, nastavení Cursoru, koncepty překladových skriptů, poznámky k plánování úkolů – bylo pečlivě uvedeno v `.gitignore`. To udržovalo hlavní repozitář uklizený, ale ponechalo mou životně důležitou vývojovou infrastrukturu nechráněnou.

Toto probuzení se naštěstí odehrálo relativně brzy. Při práci na integraci překladových nástrojů a plánování pracovního postupu pomocí poznámek v rámci struktury projektu došlo k nehodě, která přepsala značnou část plánovací práce. Frustrující, ano, ale cenná lekce naučená dříve, než se sázky zvýšily.

## Hledání řešení: Neúspěšné pokusy

Mé počáteční nápady se točily kolem chytřejšího využití samotného Gitu, ale narazil jsem na překážky.

### Pokus 1: Vnořené repozitáře – Noční můra přepínání větví

Můj první nápad byl prozkoumat způsoby, jak mít v rámci stejného adresáře projektu více historií Gitu, možná pomocí vnořených repozitářů. Myšlenka byla mít "dev" repozitář nejvyšší úrovně sledující *všechno* (nastavení IDE, koncepty, soubory vnitřního repozitáře), zatímco vnitřní "veřejný" repozitář by obsahoval pouze čisté, nasaditelné soubory projektu. Vnější repozitář by ignoroval adresář `.git` vnitřního repozitáře.

Teoreticky to znělo jako elegantní vrstvený přístup. Když jsem se to však pokusil nastavit, velmi rychle jsem si uvědomil, že to nefunguje. Především Git ve skutečnosti nepodporuje vnořené repozitáře, přinejmenším ne tak, jak jsem si to představoval. A dává to smysl. Existuje však výhrada, o které jsem nepřemýšlel: Řekněme, že pracuji ve vnitřním repozitáři (`docs-nica`) a přepnu na jinou větev. Nyní se všechny soubory v tomto adresáři změní (aby odrážely větev) – ale vnější repozitář (`docs-nica-dev`) je stále na své hlavní větvi. Vnější repozitář nyní vidí všechny tyto změny souborů a myslí si, že jsou to změny *jeho* hlavní větve... Je jasně vidět, proč je to problém. Dobře, takže tento přístup nefungoval.

### Pokus 2: Oddělené repozitáře + Git hooky – Katastrofa kopírování

Zpět na rýsovací prkno. Můj další nápad byl mít dva zcela oddělené repozitáře. Jeden `dev`, který obsahuje vše, co potřebuji (skripty, poznámky, konfigurace *a* základní soubory projektu). A jeden `public`, který obsahuje pouze obsah ve formátu Markdown a nastavení MkDocs – jen holé základy, tak, jak je zamýšleno pro nasazení.

Ale zde přichází háček: pokud něco změníme ve `public` repozitáři (možná rychlou opravu přímo tam, nebo stažení změn od spolupracovníků), jak by se o tom měl `dev` repozitář dozvědět? A častěji, jak se změny v `dev` projeví v `public`? Potřebujeme nějaký způsob, jak je propojit.

První nápad byl použít GitHub hooky (nebo lokální Git hooky). Ty vám umožňují definovat příkazy, které se spustí po určitých akcích Gitu, jako je commit. Nastavil jsem hook, který po commitu v `dev` repozitáři v podstatě jen zkopíruje relevantní soubory (adresář `docs/`, `mkdocs.yml` atd.) do adresáře `public` repozitáře.

Na první pohled to fungovalo, ale tento přístup měl dva hlavní problémy:

1.  **Nepřehledná historie:** Hook zkopíroval *všechny* relevantní soubory při *každém* commitu. To znamenalo, že `public` repozitář si vždy myslel, že se změnil *veškerý* jeho obsah. I když to technicky nic neporušovalo, historie commitů se stala méně užitečnou, zobrazovala stovky (nebo tisíce) změněných souborů při každém jednotlivém commitu, což znemožňovalo okamžitě identifikovat, které *obsahy* souborů se skutečně změnily.
2.  **Neviditelnost smazání:** Skript soubory pouze *kopíroval*. Pokud jsem v `dev` repozitáři smazal soubor nebo adresář, tato změna se v `public` repozitáři neprojevila. Starý soubor tam prostě zůstal.

Sakra, už jsem na tom strávil hodiny – a stále žádné funkční řešení.

## Průlom: Oddělené repozitáře + synchronizace souborů

Pak jsem si vzpomněl na open-source software, který jsem kdysi dávno testoval pro synchronizaci lokálních složek: **FreeFileSync**. I když je nešťastné přidávat další sadu nástrojů/softwaru do zásobníku, který je potřeba, ve skutečnosti to splnilo přesně to, co jsem chtěl.

Nastavení nyní zahrnuje:

1.  Dva oddělené Git repozitáře: `docs-nica-dev` (obsahující vše) a `docs-nica` (čistá, veřejná verze).
2.  **FreeFileSync:** Používá se k definování pravidel pro synchronizaci konkrétních složek (jako `docs/`, soubory motivu, `mkdocs.yml`) mezi umístěními obou repozitářů. Dokáže zvládnout obousměrnou synchronizaci, zrcadlení a co je nejdůležitější, správně propagovat smazání.
3.  **RealTimeSync (součást FreeFileSync):** Používá se ke sledování definovaných složek na změny a automatickému spouštění synchronizace na základě pravidel FreeFileSync.

Tato kombinace konečně efektivně překlenuje propast mezi oběma repozitáři. Změny provedené v základních obsahových složkách `dev` repozitáře jsou zrcadleny do `public` repozitáře a naopak, pokud je to nutné (i když můj primární tok je dev -> public). Smazání jsou správně zpracována a protože synchronizuje pouze *změněné* soubory, historie commitů v `public` repozitáři přesně odráží skutečné úpravy.

## Zbývající háček: Načasování synchronizace vs. commitu

Stále však existuje jeden nevýhoda. Když změním soubor v `dev` repozitáři a RealTimeSync běží, tyto změny jsou synchronizovány do adresáře `public` repozitáře *okamžitě*, i když ještě nejsou v `dev` repozitáři commitnuty. Řešení synchronizace je odděleno od Gitu.

Není to velký problém, ale vyžaduje to trochu větší opatrnost při skutečném commitování a pushování změn. V podstatě, když pracuji na `dev` repozitáři, musím se ujistit, že tam všechno commitnu *předtím*, než přesunu pozornost na `public` repozitář, abych commitnul a pushnul. Také to posiluje zvyk *skutečně zkontrolovat změny* připravené ke commitu v `public` repozitáři, než je skutečně commitnu a pushnu, jen abych se ujistil, že stav je přesně takový, jaký zamýšlím.

## Pro koho to je? (Důležité upřesnění)

Počkejte, než si budete myslet, že celé toto nastavení je povinné jen pro práci s wiki, dovolte mi objasnit. **Všechna tato složitost? Není *potřebná*, pokud chcete pracovat pouze se základním obsahem.** Hlavní vstupní bod je stále super jednoduchý: naklonujte veřejný `docs-nica` repozitář (který má jen soubory Markdown a nastavení MkDocs) a použijte jakékoli nástroje, které *vy* preferujete. To je vše.

Proč jsem se tedy s tím vším trápil? Toto poměrně složité vývojové nastavení slouží *mně* dvěma hlavním účelům:

1.  **Moje osobní záchranná síť:** Je to klíčová správa verzí pro *všechny* mé vývojové drobnosti a kousky – konfigurace, nedokončené skripty, plánovací poznámky – věci, které si nemohu dovolit znovu ztratit.
2.  **Sdílení mého přesného pracovního postupu (volitelně):** Pokud někdo *chce* replikovat mé specifické prostředí, může naklonovat `docs-nica-dev` repozitář. Získá kompletní nastavení Obsidianu (pluginy, nastavení, záložky, vyhledávání, všechno!), potenciálně nastavení Cursoru a jakékoli další integrované nástroje, které jsem nakonfiguroval. Je to způsob, jak sdílet připravené základní nastavení.

Základní myšlenka se však nezměnila: rozhodně si můžete vzít jen veřejný repozitář a kolem něj si postavit vlastní pracovní postup s vašimi oblíbenými nástroji. Tento propracovaný tanec je o správě *mého* vývojového chaosu a nabídce plánu pro ty, kteří ho chtějí.

## Závěr: Těžce vybojované řešení

Celkově jsem rád, že jsem nyní našel řešení problému – i když mě to stálo asi dva dny zkoušení, chyb a frustrace. Ale správné nastavení tohoto pracovního postupu bylo klíčové, abych se vyhnul dalším problémům v budoucnu, zajistil jak čistý veřejný repozitář, tak plně verzovaný vývojový prostředí.

Je toto nastavení dokonalé? Vyžaduje správu dvou repozitářů a externího nástroje pro synchronizaci, plus vědomý pracovní postup pro commitování. Přímo však řeší kritický problém verzování *všeho*, co je nezbytné pro složitý vývojový proces, aniž by došlo ke kompromisu v čistotě hlavního repozitáře projektu nebo k boji s omezeními Gitu u vnořených struktur. Pro projekty, které přerostou jednoduché strategie `.gitignore`, tento přístup nabízí pragmatickou cestu vpřed, poskytující bezpečnost a strukturu pro nevyhnutelnou, nepořádnou realitu vývojové práce.
