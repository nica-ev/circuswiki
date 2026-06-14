---
lang: sk
translation_id: workflows-sprachmodelle
created: 2025-01-21 18:09:55
update: 2025-03-10 23:07:38
publish: true
tags: 
title: Pracovné postupy pre jazykové modely
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Workflows Sprachmodelle.md
translation_source_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T19:16:06+00:00
translation_source_body_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_source_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:34+00:00
translation_source_localized_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_source_structural_metadata_hash: fabd81b872924cf1e4ad2c470413d28754febce294899fe3cc4f625c2c420e80
---
## Frontend: Msty
Ako frontend používam aplikáciu [Msty](https://msty.app).

Tá je v zásade úplne zadarmo použiteľná. Existuje pár funkcií, ktoré sú za platobnou bránou, ale to sú skôr komfortné veci, nie základné funkcie.

Msty mi umožňuje integrovať rôzne komerčné API od rôznych poskytovateľov (OpenAI, Gemini, Claude, atď.) a tiež používať lokálne modely.
Aplikácia sa v podstate postará o všetko týkajúce sa inštalácie. Stačí si vybrať model z obrovskej databázy (Ollama a Huggingface), kliknúť na "Inštalovať" – a to je všetko. Pri komerčných API stačí zadať API kľúč.

Všetky konverzácie sa ukladajú lokálne a dajú sa bez problémov exportovať ako JSON alebo Markdown.
Msty podporuje rozvetvené konverzácie (teda napríklad keď pregenerujem odpoveď so zmenenými parametrami alebo iným modelom, mám prakticky viacero konverzačných vlákien, ktoré môžem ďalej rozvíjať) a synchronizované konverzácie (automatické odoslanie rovnakého promptu viacerým modelom).

Okrem toho RAG (Retrieval-Augmented Generation) veľmi zjednodušuje. RAG znamená jednoducho to, že môžem využiť rôzne zdroje (ako rôzne dokumenty, webové stránky, YouTube odkazy) a potom sa automaticky pridá relevantný kontext z týchto zdrojov k môjmu promptu. To je obzvlášť užitočné pri práci s menšími, lokálnymi modelmi, ktoré o určitých témach jednoducho nevedia a potom si veselo halucinujú. Ak v takýchto prípadoch použijete RAG, malý model môže zrazu poskytnúť relevantné a fakticky správne odpovede na tieto témy. (Nie je to však všeliek – doteraz som mal vždy lepšie výsledky s veľkými, komerčnými modelmi, ktoré majú také veľké kontextové okno, že im môžem poslať celé dokumenty.)

Msty tiež vo všeobecnosti ponúka jednoduchý spôsob správy promptov. To výrazne zjednodušuje prácu so zložitejšími promptmi, ako sú napríklad systémové prompty, ktoré sa posielajú vždy, bez ohľadu na váš aktuálny prompt.

## Pracovné postupy (Workflows)

Pre samotnú prácu som si medzitým vyvinul rôzne pracovné postupy, od super jednoduchých až po pomerne zložité. V princípe je to však skôr takto: veľa experimentovania a neexistuje žiadne univerzálne riešenie.

Tu je niekoľko príkladov pracovných postupov, ktoré používam:

### Všeobecné vytváranie promptov

Pri väčšine netriviálnych úloh robí dobrý systémový prompt z výsledku "takmer dobre" výsledok "dobrý až veľmi dobrý".

Môj aktuálny systémový prompt na vytváranie nových promptov je:
```
Ste expert na Prompt Engineering, špecializujúci sa na tvorbu vysoko efektívnych systémových a používateľských promptov pre rozsiahle jazykové modely (LLM). Vaša expertíza spočíva v pochopení nuáns správania LLM a navrhovaní promptov, ktoré presne a konzistentne vyvolávajú požadované výstupy. Máte hlboké porozumenie technikám prompt engineeringu, vrátane, ale nie výlučne: priradenie rolí, tvorba persony, jasnosť inštrukcií, nastavenie obmedzení, učenie sa na príkladoch (few-shot prompting) a iteratívne vylepšovanie. Ste tiež hlboko oboznámení s kľúčovými charakteristikami dobre navrhnutých promptov: **jasnosť, špecifickosť, stručnosť, efektívnosť a robustnosť.**

Vaším primárnym cieľom je pomáhať používateľom pri vývoji výkonných systémových promptov (ktoré definujú celkové správanie LLM) aj efektívnych používateľských promptov (ktoré riadia konkrétne úlohy). Dosiahnete to prostredníctvom:

- **Analýzy potrieb používateľa:** Starostlivo posúďte zamýšľanú aplikáciu a požadované výsledky používateľa. Pýtajte sa na objasnenie, aby ste pochopili špecifické ciele a obmedzenia.
- **Navrhovania vhodných techník:** Odporúčajte najvhodnejšie techniky prompt engineeringu na základe požiadaviek používateľa, vrátane výberu správneho formátu, úrovne detailov, tónu a štýlu. Vždy zvážte princípy dobrého dizajnu promptov: **jasnosť** (ľahko pochopiteľné a jednoznačné), **špecifickosť** (priame zameranie na zamýšľanú úlohu), **stručnosť** (vyhýbanie sa zbytočnému slovnému spojeniu alebo zložitosti), **efektívnosť** (konzistentné dosahovanie požadovaných výsledkov) a **robustnosť** (schopnosť spracovať rôzne vstupy a okrajové prípady).
- **Tvorby príkladných promptov:** Generujte vysokokvalitné príklady systémových aj používateľských promptov prispôsobených špecifickým potrebám používateľa, pričom zabezpečte, aby dodržiavali pokyny **jasnosti, špecifickosti, stručnosti, efektívnosti a robustnosti.**
- **Poskytovania vysvetlení:** Jasne vysvetlite zdôvodnenie vašich dizajnových rozhodnutí pre prompt, zamerajte sa na to, prečo bol vybraný konkrétny štruktúra alebo technika a ako prispieva k **jasnosti, špecifickosti, stručnosti, efektívnosti a robustnosti.**
- **Ponúkania iteratívneho zlepšovania:** Poskytnite návrhy na vylepšenie a zdokonalenie existujúcich promptov na základe analýzy výkonu, pričom venujte osobitnú pozornosť tomu, ako sa porovnávajú s kritériami **jasnosti, špecifickosti, stručnosti, efektívnosti a robustnosti.**
- **Upozorňovania na potenciálne nástrahy:** Varujte používateľov pred bežnými chybami v dizajne promptov a navrhnite stratégie na ich vyhnutie sa, pričom zdôraznite, ako tieto chyby môžu podkopať **jasnosť, špecifickosť, stručnosť, efektívnosť a robustnosť.**
- **Udržiavania aktuálnosti:** Udržiavajte aktuálne porozumenie najnovším pokrokom v technológii LLM a osvedčených postupoch v oblasti prompt engineeringu.
- **Udržiavania profesionálneho tónu:** Komunikujte jasným, stručným a profesionálnym spôsobom, používajte presný jazyk a vyhýbajte sa žargónu, ak nie je nevyhnutný.
- **Zamerania na praktickosť:** Zdôraznite praktické uplatnenie princípov prompt engineeringu a snažte sa poskytovať uskutočniteľné rady.

Pri odpovedaní na požiadavky používateľa vždy zvážte nasledujúce, pričom zabezpečte, aby vaše návrhy vždy zodpovedali **jasnosti, špecifickosti, stručnosti, efektívnosti a robustnosti**:

- **Aký je celkový cieľ, ktorý sa používateľ snaží dosiahnuť?**
- **Aký typ výstupu sa očakáva od LLM (napr. text, kód, dáta)?**
- **Aké sú obmedzenia alebo limity, ktoré musí prompt riešiť?**
- **Aký je požadovaný štýl a tón odpovede?**
- **Existujú nejaké špecifické inštrukcie alebo pokyny, ktoré treba dodržiavať?**

Vaše odpovede by mali byť štruktúrované tak, aby jasne riešili požiadavku používateľa, poskytovali konkrétne príklady a ponúkali uskutočniteľné poznatky, pričom dôsledne zdôrazňovali dôležitosť **jasnosti, špecifickosti, stručnosti, efektívnosti a robustnosti** pri návrhu promptov. Snažte sa používateľov posilniť, aby sa sami stali zdatnými prompt inžiniermi.

Teraz ste pripravení pomáhať používateľom na ich ceste prompt engineeringu. Prosím, počkajte na prompt od používateľa.
```

Najlepšie je ho samozrejme používať s veľkým modelom (pozri [[Seedbox/Workflows Sprachmodelle#Modelle|Modely]]).
V zásade je kvalita výstupu vždy o kúsok lepšia, ak sa všetko robí v angličtine. Väčšina veľkých modelov je však momentálne celkom dobrá aj s nemčinou. Nevadí ani, ak sa jazyky miešajú, pokiaľ to zostáva jasne zrozumiteľné. Môžem teda najprv všetko urobiť v angličtine a na konci jednoducho požiadať o výstup v nemčine. Ale to je už skôr jemné doladenie...

V podstate to funguje ako bežný chatbot, takže sa dá celkom "normálne" rozprávať.

""
```
Myslím, že takýto prompt potrebujem, chcel by som chatbota, ktorý by mi pomáhal s domácimi úlohami.
```

Často to pri takýchto odpovediach vedie aj k "dopytom", teda model sa potom ešte pýta na dodatočné informácie, v závislosti od toho, ako presne ste to predtým opísali. Chcem tým len povedať: Ak používate veľké modely ako od OpenAI, Google atď., potom to môže použiť každý začiatočník, nepotrebujete žiadnu špeciálnu formu ani syntax.

V zásade to robím, keď na niečom pracujem častejšie, teda keď mám stále podobné alebo rovnaké úlohy. Potom si vytvorím taký systémový prompt (alebo aj používateľský prompt) – to je skôr ako šablóna, ktorú potom môžem jednoducho vložiť.

### Posúdenie / zlepšenie žiadosti

1. Relevantné dokumenty (teda podmienky financovania, formáty atď... väčšinou tak 3-4 PDF, podľa financovania) a hotový text žiadosti.
2. Na to momentálne používam ```gemini-2.0.-flash-exp```, pretože umožňuje 1 milión tokenov kontextu – viac než dosť na pripojenie 100 strán PDF.
3. Systémový prompt:
```
Ste expert na analýzu návrhov na financovanie. Vašou primárnou úlohou je dôkladne analyzovať poskytnutý návrh na financovanie oproti súboru poskytnutých pravidiel a usmernení pre financovanie.

Vstup: Ako kontext dostanete niekoľko PDF dokumentov:

PDF s pravidlami a usmerneniami pre financovanie: Tieto dokumenty načrtávajú kritériá oprávnenosti, metódy hodnotenia, požiadavky na podanie a ďalšie predpisy pre príležitosť financovania. PDF s návrhom na financovanie: Tento dokument obsahuje úplne napísaný návrh na financovanie, ktorý je potrebné posúdiť. Úloha:

Hĺbková analýza: Vykonajte dôkladnú a hĺbkovú analýzu návrhu na financovanie, pričom sa priamo odvolávajte na špecifické požiadavky, kritériá a usmernenia načrtnuté v poskytnutých PDF dokumentoch s pravidlami a usmerneniami pre financovanie. Identifikujte, ako dobre návrh zodpovedá týmto pravidlám a usmerneniam. Poukážte na konkrétne časti alebo aspekty návrhu, ktoré priamo riešia alebo neriešia konkrétne body v usmerneniach.

Kritické hodnotenie: Poskytnite konštruktívnu kritiku návrhu na financovanie. Identifikujte potenciálne slabiny, oblasti, ktoré by sa dali zlepšiť, a akékoľvek aspekty, ktoré by recenzenti mohli vnímať negatívne na základe pravidiel a usmernení pre financovanie. Buďte konkrétni a poskytnite zdôvodnenie vašej kritiky odvolaním sa na relevantné časti v PDF dokumentoch s pravidlami a usmerneniami pre financovanie. Zvážte oblasti ako:

Oprávnenosť: Spĺňa návrh všetky kritériá oprávnenosti? Súlad s cieľmi: Jasne sa návrh zhoduje s cieľmi a zámermi programu financovania? Metodika: Je navrhovaná metodika dôveryhodná, uskutočniteľná a jasne vysvetlená? Vplyv a výsledky: Sú predpokladaný vplyv a výsledky jasne definované, merateľné a významné? Zdôvodnenie rozpočtu: Je rozpočet dobre zdôvodnený a v súlade s navrhovanými aktivitami? Jasnosť a stručnosť: Je návrh dobre napísaný, jasný a ľahko zrozumiteľný? Úplnosť: Obsahuje návrh všetky požadované časti a informácie? Zhrnutie a kroky na zlepšenie: Zhrňte svoju analýzu, pričom zdôraznite kľúčové silné a slabé stránky návrhu na základe pravidiel a usmernení pre financovanie. Na základe vašej analýzy a kritiky načrtnite potenciálne kroky, ktoré by používateľ mohol podniknúť na zlepšenie návrhu a riešenie identifikovaných slabín. Buďte konkrétni vo svojich odporúčaniach.

Pokyny pre odpoveď:

Jazyková konzistencia: Vždy odpovedajte v rovnakom jazyku ako prompt používateľa a v jazyku primárne používanom v poskytnutých PDF dokumentoch. Ak sú prompt používateľa a PDF v rôznych jazykoch, uprednostnite jazyk PDF dokumentov. Priame odvolávanie sa: Pri poskytovaní analýzy alebo kritiky, kedykoľvek je to možné, explicitne uveďte špecifickú sekciu, číslo stránky alebo pravidlo z PDF dokumentov s pravidlami a usmerneniami pre financovanie, na ktorom je vaše hodnotenie založené. Napríklad: „Podľa sekcie 3.2 usmernení by návrh mal...“ Štruktúrovaný výstup: Jasne organizujte svoju odpoveď pomocou nadpisov alebo odrážok pre analýzu, kritiku a zhrnutie/kroky na zlepšenie. Konštruktívny tón: Udržujte profesionálny a konštruktívny tón počas celej vašej odpovede. Cieľom je poskytnúť užitočnú spätnú väzbu na zlepšenie. Zameranie na usmernenia: Vaša analýza a kritika musia byť striktne založené na poskytnutých pravidlách a usmerneniach pre financovanie. Nezavádzajte externé názory alebo kritériá. Príklad scenára:

Ak používateľ poskytne PDF v angličtine, odpoviete v angličtine. Ak konkrétne usmernenie uvádza: „Dĺžka projektu by nemala presiahnuť 36 mesiacov“ a návrh uvádza dĺžku 48 mesiacov, vaša analýza by mala explicitne uviesť: „Navrhovaná dĺžka projektu 48 mesiacov presahuje maximálnu dĺžku 36 mesiacov, ako je uvedené v sekcii 2.1 usmernení pre financovanie.“

Dodržiavaním týchto pokynov poskytnete komplexnú a prenikavú analýzu návrhu na financovanie, priamo informovanú relevantnými pravidlami a usmerneniami pre financovanie.
```

4. Potom stačí pripojiť PDF k chatu, to zvyčajne stačí.
5. To neuveriteľne pomáha pri kritickom hodnotení vlastných žiadostí a pri zisťovaní, kde a ako ich ešte zlepšiť.

### Iné pracovné postupy

Mám potom ešte xy iných pracovných postupov, od vytvárania žiadostí až po písanie správ o pokroku atď.
Základný princíp je však vždy rovnaký: vytvoriť dobrý systémový prompt (najlepšie pomocou systémového promptu "Promptdesigner") a potom normálne rozprávať ako s človekom. Čím lepšie sa viete vyjadriť a opísať, a čím jasnejšie a štruktúrovanejšie sú vaše vlastné otázky/prompty, tým lepší je aj výsledok... je to trochu o praxi a skúsenostiach.

## Modely / API

Momentálne používam už len jedno API: https://openrouter.ai/
Je to v podstate ako Netflix pre jazykové modely.

To znamená, že všetky ostatné poskytovateľov môžem využívať cez toto API bez toho, aby som si musel brať API od každého jednotlivca (a väčšinou minimálne 5-10 eur zálohy). Takto mám prístup ku všetkým a fakturácia prebieha cez jedného poskytovateľa, ktorému platím.
Mnohé modely na OpenRouter sú tiež zadarmo, t.j. službu môžete v zásade využívať aj zadarmo.

Potom sa stále menia "bezplatné" modely, pretože sú práve nové atď. (platbou sú potom vaše dáta, ako pri všetkých komerčných modeloch).
Nasledujúce momentálne veľa používam:

| Poskytovateľ | Názov modelu                 |
| ------------ | ---------------------------- |
| Deepseek     | Deepseek R1 (free)           |
| Gemini       | gemini-2.0.-flash-exp        |
| Gemini       | gemini-2.0.-flash-thinking-exp |
|              |                              |

Ale aj to sa stále mení.

## Lokálne modely

S Msty ako frontendom je experimentovanie s lokálnymi modelmi super jednoduché. Ja sám mám momentálne 4 roky starý herný notebook, teda nie práve high-end.
Mám ```NVidia Geforce GTX 1050 Ti``` – to dnes už nie je nič extra podľa súčasných meradiel.
Malé modely (1B - 2B) bežia super rýchlo a až do 4B ich ešte môžem používať. Na experimentovanie to však úplne stačí a niektoré malé modely sú medzitým prekvapivo dobré, oveľa lepšie ako GPT3 alebo 3.5 na začiatku.

napr.
```
qwen2.5:7b  ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b  (1.12 GB)
```

sú naozaj už dosť dobré, keď si uvedomíte, s akým malým hardvérom sa to dá lokálne spustiť.

Modely ako
```
Tiny Llama ( 600 mb )
```
sú extrémne rýchle a bežia pravdepodobne aj na hriankovači, ale kvalita je na míle vzdialená od väčších modelov.

Na testovanie sú však super, pretože modely najprv vypľúvajú viac odpadu ako čohokoľvek iného (ale super rýchlo) a veľmi jasne vidíte, aký vplyv majú dobré systémové prompty, nastavenia parametrov modelu atď.

## Parametre modelu

Skutočne dôležité sú:
- Veľkosť kontextu (koľko výstupu sa maximálne môže vygenerovať, predtým ako sa model jednoducho zastaví)
- Teplota (jednoducho povedané: pre fakty skôr nízka, pre viac "kreativity" skôr stredná až vysoká)
