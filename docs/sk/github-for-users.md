---
lang: sk
translation_id: github-for-users
publish: true
tags:
  - github
  - tutorial
created: 2025-01-18 23:14:04
update: 2026-06-12 18:26:00
title: GitHub - priama spolupráca v repozitári
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/github-for-users.md
translation_source_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-12T17:32:00+00:00
translation_source_body_hash: 8125fe4a8331e806a2b0d103dd38dbfda6e82793ffa37265095b73ad0217bdf2
translation_source_metadata_hash: ac5f43c5c49905b729ab3c3f288e96be0cf997b5a5f1e94ca4f7eb6a77c1686f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-12T17:32:00+00:00
---
> [!info] Stručne povedané
> Táto stránka je určená pre ľudí, ktorí chcú priamo pracovať s Markdown súbormi CircusWiki. Pre bežné príspevky tento spôsob nepotrebujete: materiál môžete jednoducho poslať aj e-mailom.

Priama spolupráca cez GitHub je praktická, ak chcete pravidelne opravovať stránky, vytvárať nové Markdown súbory alebo pracovať s vaultom CircusWiki v editore ako Obsidian.

Ak chcete prispieť iba hrou, metódou, PDF-kom, odkazom alebo opravou, jednoduchší spôsob je zvyčajne lepší:

[Späť na Prispieť](mitmachen.md){ .md-button }

## Čo potrebujete

- bezplatný účet na GitHub: [https://github.com/join](https://github.com/join)
- voliteľne GitHub Desktop: [https://desktop.github.com/](https://desktop.github.com/)
- textový editor pre Markdown súbory, napríklad Obsidian, VS Code alebo jednoduchý editor

GitHub Desktop nie je povinný, ale pre mnohých ľudí je jednoduchší ako príkazový riadok.

## Nájsť repozitár

Verejný repozitár sa nachádza tu:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Tam sa nachádzajú samotné Markdown súbory, obrázky, preklady a nástroje, z ktorých sa webová stránka zostavuje.

## Pracovný postup v skratke

Typický postup je:

1. Vytvoriť fork repozitára na GitHub.
2. Naklonovať svoju kópiu na vlastný počítač.
3. Vykonávať zmeny v novom branche.
4. Upraviť súbory alebo vytvoriť nové Markdown súbory.
5. Committnúť zmeny.
6. Nahrať branch na GitHub.
7. Otvoriť Pull Request, aby bolo možné zmenu skontrolovať a prijať.

## Krok za krokom s GitHub Desktop

### 1. Vytvoriť fork repozitára

Otvorte repozitár CircusWiki na GitHub:

[https://github.com/nica-ev/circuswiki](https://github.com/nica-ev/circuswiki)

Kliknite na `Fork`. Tým sa vytvorí vlastná kópia repozitára vo vašom účte na GitHub. V tejto kópii môžete pracovať bez priameho zásahu do hlavného projektu.

### 2. Naklonovať repozitár

Otvorte GitHub Desktop a vyberte:

```text
File -> Clone repository...
```

Vyberte svoj fork `nica-ev/circuswiki` a určite priečinok na svojom počítači.

Potom budete mať lokálnu kópiu súborov.

### 3. Vytvoriť branch

Pre svoju zmenu je najlepšie vytvoriť vlastný branch, napríklad:

```text
pridat-popis-hry
opravit-odkaz
nova-metoda-balancovanie
```

Branch udržuje vašu prácu oddelene od hlavného stavu. To uľahčuje neskoršiu kontrolu.

### 4. Upraviť súbory

Verejný obsah sa nachádza predovšetkým v jazykových priečinkoch pod `docs/`:

```text
docs/de/
docs/en/
docs/es/
docs/pl/
...
docs/img/
```

Všetky jazyky sú rovnocenné. Neexistuje žiadny hlavný jazyk, v ktorom by sa mali prednostne vytvárať nové obsahy.

Ak vytvárate novú pôvodnú stránku, umiestnite ju do jazykového priečinka, v ktorom je text napísaný. Napríklad španielsky pôvodný text patrí do `docs/es/`, nemecký do `docs/de/`, anglický do `docs/en/`.

Dôležité je frontmatter na začiatku súboru. Tam musí byť zrejmé, že stránka je originál, napríklad:

```yaml
translation_status: original
translation_source_lang: es
```

`translation_source_lang` zodpovedá jazyku pôvodného textu. Z tohto originálu sa neskôr môžu automaticky generovať preklady do všetkých podporovaných jazykov.

Pri úprave si všímajte nasledovné:

- Nezabudnite na začiatku súboru frontmatter.
- Pri nových pôvodných stránkach nastavte `translation_status: original` a príslušný `translation_source_lang`.
- Existujúce odkazy zachovajte, ak je to možné.
- Nezverejňujte žiadne súkromné údaje, API kľúče ani interné poznámky.
- Obrázky používajte len vtedy, ak sú licenčné práva jasné.
- Radšej robte malé, jasné zmeny ako veľmi veľké zmiešané zmeny.

### 5. Committnúť zmeny

V GitHub Desktop vidíte svoje zmenené súbory v sekcii `Changes`.

Napíšte krátke zhrnutie, napríklad:

```text
Opraviť zoznam materiálu v pohybovej hre
Doplniť bezpečnostné upozornenie k Beigoma
Pridať nový popis hry
```

Potom kliknite na `Commit to <branch-name>`.

### 6. Nahrať zmeny

Kliknite na `Push origin`, aby ste nahrali svoj branch na GitHub.

### 7. Otvoriť Pull Request

GitHub Desktop alebo GitHub v prehliadači potom ponúkne možnosť vytvoriť Pull Request.

Pull Request znamená: navrhujete svoju zmenu pre hlavný repozitár. Zmena sa skontroluje, prípadne okomentuje a potom sa prijme alebo ďalej upraví.

## Základy Markdown

Markdown je jednoduchý textový formát. Najdôležitejšie znaky postačujú pre väčšinu príspevkov:

```markdown
# Veľký nadpis
## Podnadpis sekcie

Bežný text s **tučnou časťou** a *kurzívnou časťou*.

- Bod zoznamu
- Ďalší bod zoznamu

[Text odkazu](https://www.example.com)
```

## Ak je niečo nejasné

Priamu spoluprácu cez GitHub nemusíte hneď dokonale ovládať. Ak otvoríte Pull Request a niečo ešte nie je v poriadku, dá sa to vyjasniť v revízii.

Ak chcete prispieť iba obsahom a technický postup sa vám zdá príliš náročný, jednoducho použite e-mail na [stránke Prispieť](mitmachen.md).
