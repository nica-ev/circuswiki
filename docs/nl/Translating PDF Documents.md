---
lang: nl
translation_id: translating-pdf-documents
created: 2025-05-03 21:32:10
update: 2025-05-03 22:24:12
publish: true
tags:
  - tutorial
title: PDF-documenten vertalen met grote taalmodellen
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Translating PDF Documents.md
translation_source_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-14T19:33:32+00:00
translation_source_body_hash: 7bbc7641e762f3590c7d2e1804e38167ac9308ba9d7c1d8fc5254c7feff26d23
translation_source_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T19:33:32+00:00
translation_source_localized_metadata_hash: 6785222fbc9a9243423a809c8415e44aa15130e8a66ad15714af391851b8b82f
translation_source_structural_metadata_hash: 2b0fe62dfc02049e3f55e308c77f83a911789c48b0827769d60d3f00737d38b6
---
# Tutorial: PDF-documenten vertalen met grote taalmodellen

## Introductie

Deze tutorial beschrijft een proces voor het vertalen van de inhoud van PDF-documenten, met name die met niet-selecteerbare, op afbeeldingen gebaseerde tekst, met behulp van grote taalmodellen (LLM's). De workflow omvat het optimaliseren van de PDF, het extraheren van tekst via Optical Character Recognition (OCR), het vertalen van de tekst en ten slotte het opnieuw formatteren van de vertaling naar een PDF.

**Vereisten:**

*   Een Google-account (voor toegang tot Google AI Studio).
*   Optioneel: Software voor PDF-optimalisatie (bijv. pdf24 Creator).
*   Optioneel: Een teksteditor of tekstverwerker die Markdown kan verwerken en kan exporteren naar PDF (bijv. Obsidian, Microsoft Word).

## Stap 1: Het PDF-document voorbereiden

**Doel:** De bestandsgrootte van de PDF verkleinen om deze te optimaliseren voor verwerking door de LLM, terwijl de leesbaarheid van de tekst behouden blijft. LLM's hebben vaak limieten voor de invoergrootte en kleinere bestanden worden efficiënter verwerkt.

**Overwegingen:**

*   **Tekstgebaseerde PDF's:** Als de tekst in de PDF geselecteerd kan worden (wat betekent dat deze elektronisch is ingebed), is het verkleinen van de bestandsgrootte doorgaans eenvoudiger en kan dit zonder kwaliteitsverlies tot kleinere formaten leiden.
*   **Op afbeeldingen gebaseerde PDF's:** Als de PDF-pagina's afbeeldingen van tekst zijn (tekst kan niet individueel worden geselecteerd), omvat het verkleinen van de bestandsgrootte beeldcompressie. Er moet voor worden gezorgd dat de kwaliteit niet zozeer wordt verminderd dat de tekst onleesbaar wordt voor OCR.

**Procedure (Voorbeeld met pdf24):**

1.  Open uw PDF-document in een tool zoals pdf24 Creator ([https://www.pdf24.org/](https://www.pdf24.org/)).
2.  Gebruik de functies voor compressie of groottevermindering. Veelgebruikte effectieve instellingen zijn:
    *   Weboptimalisatie inschakelen.
    *   Kleuren omzetten naar grijstinten.
3.  Experimenteer met compressieniveaus, streef naar een bestandsgrootte onder de **5 MB**, terwijl u ervoor zorgt dat de tekst duidelijk en leesbaar blijft.
4.  Sla het geoptimaliseerde PDF-bestand op.

## Stap 2: Tekst extraheren met Google AI Studio (Transcriptie/OCR)

**Doel:** De multimodale mogelijkheden van een LLM gebruiken om OCR uit te voeren op de voorbereide PDF en de tekstinhoud in een gestructureerd formaat te extraheren.

**Procedure:**

1.  Ga naar **Google AI Studio** ([https://aistudio.google.com/](https://aistudio.google.com/)) en log in met uw Google-account. Opmerking: AI Studio is voornamelijk een tool voor het experimenteren met modellen en prompts.
2.  Start een nieuwe sessie of chat.
3.  Voeg het geoptimaliseerde PDF-bestand toe aan uw sessie (bijv. via de bijlageknop of door slepen en neerzetten).
4.  Voer de volgende prompt in het gebruikersberichtgebied in:
    ```
    Please transcribe the attached PDF. It contains images with text, requiring OCR. Output the transcription in proper Markdown format, utilizing headers and lists to create a structure that closely mimics the original document's layout.
    ```
5.  Configureer de modelinstellingen:
    *   Houd de standaardinstellingen aan, tenzij u specifieke vereisten heeft.
    *   Stel de **Temperatuur** in op **0.1**. Een lagere temperatuur bevordert meer deterministische en minder creatieve uitvoer, wat geschikt is voor nauwkeurige transcriptie.
6.  Dien de prompt in. Het transcriptieproces kan enkele minuten duren (mogelijk 4-6 minuten of langer, afhankelijk van de PDF-grootte en complexiteit).
7.  Nadat de generatie is voltooid, kopieert u de resulterende Markdown-tekst.
    *   *Methode 1:* Gebruik de kopieeroptie die vaak binnen de interface wordt aangeboden (bijv. via een menu dat aan het antwoord is gekoppeld).
    *   *Methode 2:* Selecteer handmatig alle gegenereerde tekst en kopieer deze (Ctrl+C of rechtermuisknop -> Kopiëren).
8.  Plak de gekopieerde Markdown-tekst in een platte teksteditor (zoals Kladblok, VS Code, Obsidian, etc.).
9.  Sla deze inhoud op als een plat tekstbestand. Het gebruik van `.txt` of `.md` (Markdown) extensies wordt aanbevolen. De Markdown-opmaak helpt de structuur van het document (koppen, lijsten) te behouden.

![Google AI Studio - Screenshot Transcription](../img/Screenshot-Google-AiStudio-Transcription.png){ width=600 }

## Stap 3: De geëxtraheerde tekst vertalen met Google AI Studio

**Doel:** De geëxtraheerde Markdown-tekst vertalen naar de gewenste doeltaal, waarbij de oorspronkelijke structuur en opmaak behouden blijven.

**Procedure:**

1.  Start in **Google AI Studio** een **nieuwe chat** om een frisse context voor de vertaaltaak te garanderen.
2.  Voeg het opgeslagen `.txt` of `.md` bestand toe met de geëxtraheerde Markdown-tekst.
3.  Voer een vertaalprompt in, waarbij de bron- en doeltalen worden gespecificeerd. Voorbeeld van Engels naar Italiaans:
    ```
    Please translate the attached Markdown file (English) into Italian. Maintain the original structure, formatting, tone, and style of speech precisely.
    ```
    *   **Pas de prompt aan** volgens uw specifieke bron- en doeltalen (bijv. "...translate the attached Markdown file (German) into Spanish..."). De vertaalkwaliteit kan variëren afhankelijk van het taalpaar.
4.  Configureer de modelinstellingen:
    *   Zorg ervoor dat de standaardinstellingen geschikt zijn.
    *   Stel de **Temperatuur** in op **0.1** om getrouwheid aan de brontekst en structuur tijdens de vertaling te bevorderen.
5.  Dien de prompt in. Vertaling kan ook enkele minuten duren, vergelijkbaar met de transcriptietijd.
6.  Zodra deze is gegenereerd, kopieert u de vertaalde Markdown-tekst met behulp van de methoden die in Stap 2 worden beschreven (kopieerknop in de interface of handmatige selectie).

![Google AI Studio - Screenshot Translation](../img/Screenshot-Google-AiStudio-Translation.png){ width=600 }

## Stap 4: De vertaalde tekst opnieuw formatteren naar een PDF-document

**Doel:** De vertaalde Markdown-tekst converteren naar een PDF-document voor delen of archivering.

**Procedure:**

1.  Plak de gekopieerde vertaalde Markdown-tekst in een geschikte toepassing.
2.  **Aanbevolen:** Gebruik een teksteditor of tekstverwerker die Markdown-opmaak begrijpt om de structuur (koppen, lijsten, etc.) te behouden.
    *   **Obsidian** ([https://obsidian.md/](https://obsidian.md/)) is een gratis tool die goed werkt met Markdown-bestanden en vaak PDF-exportmogelijkheden heeft (direct of via plug-ins).
    *   Moderne tekstverwerkers (zoals Microsoft Word) kunnen ook Markdown importeren of plakken en toestaan om als PDF op te slaan/exporteren, hoewel de getrouwheid van de opmaak kan variëren.
    *   Specifieke Markdown-naar-PDF-converters zijn ook online of als installeerbare software beschikbaar.
3.  Gebruik de functie "Exporteren naar PDF" of "Opslaan als PDF" van de toepassing.
4.  Controleer de resulterende PDF om er zeker van te zijn dat de opmaak en inhoud naar verwachting worden weergegeven.

## Conclusie

Deze tutorial demonstreerde een workflow voor het benutten van Google AI Studio om PDF-documenten te transcriberen en vertalen, inclusief die welke OCR vereisen. Door de PDF voor te bereiden, tekst te extraheren met een geconfigureerde LLM, het resultaat te vertalen en opnieuw te formatteren, kunnen gebruikers vertaalde versies van hun documenten verkrijgen. Hoewel deze methode een gratis of goedkope oplossing biedt, moeten gebruikers zich bewust zijn van mogelijke variaties in OCR-nauwkeurigheid en vertaalkwaliteit, met name voor complexe lay-outs of minder gangbare talen. Verwerkingstijden zijn sterk afhankelijk van de documentgrootte en de serverbelasting.
