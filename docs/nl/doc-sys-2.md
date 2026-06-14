---
lang: nl
translation_id: doc-sys-2
publish: true
tags: 
created: 2025-01-20 02:58:43
update: 2025-04-13 21:47:35
title: Documentatiesysteem
authors:
  - Marc Bielert
description:
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/doc-sys-2.md
translation_source_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T23:14:56+00:00
translation_source_body_hash: abdfb6fee5c5acdbc79aba5e10b9842bc9bded85e1122eb2b3ee32e88e92a418
translation_source_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T15:47:09+00:00
translation_source_localized_metadata_hash: a179fe68c6936cefa174c900180989e826166a8bbd0fabe2751f7150a0ab3545
translation_source_structural_metadata_hash: 12f0cb572b5daceba17f262576f82a2900f2588e247dd6c9743ac6c09aba134f
---
[Manifest](doc-sys-manifest.md){ .md-button }
[Obsidian Setup](Obsidian%20Setup.md){ .md-button }
## Systeemarchitectuur

Het algemene idee
> [!info] Overzicht van de architectuur
>
> Hier is een grafische weergave van de systeemarchitectuur:
>```mermaid
>flowchart LR
>A(Inhoud) --> B(Versiebeheer)
>C(Bewerkingssoftware) --> A
>A --> D(Online toegankelijk maken)
>```

In detail:

> [!info] Overzicht van de architectuur
>```mermaid
>flowchart LR
>A[Obsidian] <--> B{Bestanden}
>B <--> C(Github Desktop)
>C <--> D{Github}
>B <--> E(MkDocs)
>D --> F(Github Pages)
>G(Thema: MkDocs-Material) --> E
>H(MkDocs-Publisher) --> E
>E --> D
>```
>
> *   **Obsidian:** Een optionele, maar door mij aanbevolen teksteditor voor het bewerken van Markdown-bestanden.
> *   **Bestanden:** De Markdown-bestanden die de inhoud van mijn documentatie bevatten.
> *   **Github Desktop:** Een tool voor eenvoudig beheer van mijn Git-repositories.
> *   **Github:** Een online dienst voor versiebeheer en samenwerking.
> *   **Github Pages:** Een gratis dienst voor het publiceren van mijn website.
> *   **MkDocs:** Een tool voor het automatisch genereren van de website uit mijn Markdown-bestanden.
> *   **MkDocs-Material:** Een thema voor MkDocs dat een moderne en aantrekkelijke lay-out biedt.
> *   **MkDocs-Publisher**: Een verzameling plugins die de samenwerking met Obsidian vereenvoudigen en extra functionaliteit bieden.

## Componenten in detail

### 1. Markdown

> [!info] Markdown als basis
> Ik gebruik het [Markdown-formaat](Markdown.md) voor mijn documentatie. Markdown is een eenvoudige opmaaktaal waarmee ik tekst kan voorzien van simpele opmaak (bijvoorbeeld koppen, lijsten, links).

**Voordelen:**

*   Het is eenvoudig te leren en te gebruiken, waardoor ik me kan concentreren op de inhoud.
*   Het is platformonafhankelijk, zodat ik mijn werk op elk apparaat kan voortzetten.
*   Het is ideaal voor versiebeheer, waardoor ik wijzigingen kan bijhouden en beheren.
*   Het is toekomstbestendig en niet-propriëtair, wat me de zekerheid geeft dat mijn werk toegankelijk blijft op de lange termijn.

[Markdown](Markdown.md){ .md-buttons }

### 2. Obsidian

> [!info] Obsidian als teksteditor
> [Obsidian](Obsidian%20Setup.md) is een optionele, maar door mij aanbevolen teksteditor. Het biedt mij de volgende voordelen:

*   Ik kan mijn gegevens lokaal opslaan en offline bewerken, wat me flexibiliteit en controle geeft.
*   Ik kan eenvoudig bestanden linken en met elkaar verbinden, wat me helpt complexe informatie te organiseren.
*   Ik kan bestanden van tags voorzien en eenvoudig beheren, wat me een extra dimensie van organisatie biedt.
*   Ik kan mijn gegevens grafisch weergeven, wat me helpt patronen en verbanden te herkennen.
*   Ik kan de functionaliteit van Obsidian uitbreiden met plugins, waardoor ik de tool kan aanpassen aan mijn specifieke behoeften.

### 3. Git en Github

> [!info] Git voor versiebeheer
> [Git](https://git-scm.com/) is een versiebeheersysteem waarmee ik wijzigingen in de documentatie kan bijhouden en beheren. [Github](https://github.com/) is een online dienst waarmee ik mijn Git-repositories kan opslaan en met anderen kan samenwerken.

**Voordelen:**

*   Versiebeheer: Elke wijziging wordt gedocumenteerd en kan op elk moment worden teruggezien, wat me helpt fouten te voorkomen en het overzicht te bewaren.
*   Samenwerking: Meerdere personen kunnen tegelijkertijd aan de documentatie werken, waardoor ik feedback en bijdragen van anderen kan integreren.
*   Back-up: Mijn documentatie is veilig en wordt regelmatig geback-upt, wat me de zekerheid geeft dat mijn werk niet verloren gaat.

### 4. Github Desktop

> [!info] Github Desktop als tool
> [Github Desktop](../_inbox/Github%20Desktop.md) is een grafische interface voor Git, waarmee ik Git eenvoudig en zonder commandoregel kan gebruiken.

**Voordelen:**

*   Eenvoudige bediening, wat het gebruik van Git voor mij vergemakkelijkt.
*   Geen kennis van de commandoregel nodig, wat me tijd en moeite bespaart.
*   Vereenvoudigt mijn workflow, waardoor ik me kan concentreren op het creëren van inhoud.

### 5. MkDocs

> [!info] MkDocs als websitegenerator
> [MkDocs](https://mkdocs.org) is een statische sitegenerator die mijn Markdown-bestanden omzet in een statische website.

**Voordelen:**

*   Eenvoudige websitecreatie, waardoor ik mijn documentatie snel en eenvoudig kan publiceren.
*   Snelle updates, waardoor ik wijzigingen in realtime kan zien.
*   Consistente lay-out, wat zorgt voor een professionele en uniforme weergave van mijn documentatie.
*   Offline preview, waardoor ik mijn documentatie kan controleren voordat ik deze publiceer.

### 6. Github Pages

> [!info] Github Pages voor hosting
> [Github Pages](../_inbox/Github%20Pages.md) is een gratis hostingdienst van Github, waarmee ik mijn website eenvoudig online kan publiceren.

**Voordelen:**

*   Gratis hosting, waardoor ik mijn documentatie zonder extra kosten kan publiceren.
*   Eenvoudige publicatie, wat de technische implementatie van de publicatie voor mij uit handen neemt.
*   Betrouwbaar, wat me de zekerheid geeft dat mijn documentatie te allen tijde beschikbaar is.

### 7. MkDocs-Material

> [!info] MkDocs-Material als thema
> [MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) is een thema voor MkDocs dat een moderne en aantrekkelijke lay-out biedt.

**Voordelen:**

*   Modern design, waardoor mijn documentatie er professioneel en eigentijds uitziet.
*   Aanpasbaar, waardoor ik de lay-out kan aanpassen aan mijn specifieke behoeften.
*   Gebruiksvriendelijk, wat het gebruik van de documentatie voor mij vergemakkelijkt.

### 8. MkDocs-Publisher

> [!info] MkDocs-Publisher als plugin-verzameling
> [MkDocs-Publisher](https://github.com/mkdocs-publisher/mkdocs-publisher) is een verzameling MkDocs plugins die de samenwerking met Obsidian vereenvoudigen en extra functies bieden.

**Voordelen:**

- **Vereenvoudigde Obsidian-integratie:** Automatische aanpassing van Obsidians Markdown-syntax (Callouts, Wikilinks etc.)
- **Uitgebreide metadata:** Integratie van tags en categorieën uit Obsidian-frontmatter.

## Workflow

> [!info] Mijn workflow
> Hier is mijn typische workflow:

1.  Ik maak en bewerk Markdown-bestanden met een teksteditor (optioneel Obsidian).
2.  Ik sla de Markdown-bestanden lokaal op.
3.  Ik upload mijn wijzigingen naar de Git-repository met Github Desktop.
4.  Ik laat de website automatisch genereren met MkDocs.
5.  Ik publiceer de website met Github Pages.

## Bestandsstructuur

> [!info] Directorystructuur
> Hier is de directorystructuur van mijn systeem:
>
> ```
>/docs/     (Hier staan mijn Markdown-bestanden)
>/site/     (Hier wordt de website gegenereerd)
>license    (Licentie-informatie)
>mkdocs.yml (Configuratiebestand voor MkDocs)
>readme.md  (Bestand ter beschrijving van de repository)
>```

## Alternatieven voor het creëren van inhoud

> [!info] Alternatieven voor het creëren van inhoud
> Ik ben me ervan bewust dat niet iedereen bekend is met Markdown en Git. Daarom bied ik de volgende alternatieven aan:

1.  **Wordpress:** Inhoud kan in Wordpress als een pagina worden aangemaakt.
2.  **Tekstbestand, Word-bestand:** Inhoud kan worden aangemaakt als tekstbestand, Word-bestand (of in andere typische formaten).

In deze gevallen kan ik de inhoud vervolgens in het systeem verwerken.
