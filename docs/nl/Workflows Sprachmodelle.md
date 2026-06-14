---
lang: nl
translation_id: workflows-sprachmodelle
created: 2025-01-21 18:09:55
update: 2025-03-10 23:07:38
publish: true
tags: 
title: Workflows voor taalmodellen
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Workflows Sprachmodelle.md
translation_source_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T23:25:43+00:00
translation_source_body_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_source_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:30+00:00
translation_source_localized_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_source_structural_metadata_hash: fabd81b872924cf1e4ad2c470413d28754febce294899fe3cc4f625c2c420e80
---
## Frontend: Msty
Als Frontend gebruik ik de app [Msty](https://msty.app).

Deze app is in principe volledig gratis te gebruiken. Er zijn een paar functies die achter een betaalmuur zitten, maar dat zijn meer comfortfuncties, geen essentiële functionaliteiten.

Msty stelt me in staat om diverse commerciële API's van verschillende aanbieders (OpenAI, Gemini, Claude, etc.) te integreren en ook lokale modellen te gebruiken.
De app regelt eigenlijk alles wat met installatie te maken heeft. Je hoeft alleen een model uit een enorme database (Ollama en Huggingface) te kiezen, op 'Installeren' te klikken – dat is alles. Voor de commerciële API's hoef je alleen maar de API-sleutel in te voeren.

Alle chats worden lokaal opgeslagen en kunnen probleemloos als JSON of Markdown worden geëxporteerd.
Msty ondersteunt vertakkende chats (dus bijvoorbeeld als ik een antwoord opnieuw genereer met gewijzigde parameters of een ander model, heb ik feitelijk meerdere gesprekslijnen die ik kan voortzetten) en gesynchroniseerde chats (automatisch dezelfde prompt naar meerdere modellen sturen).

Bovendien maakt het RAG (Retrieval-Augmented Generation) super eenvoudig. RAG betekent simpelweg dat ik verschillende bronnen kan gebruiken (zoals documenten, websites, YouTube-links), en vervolgens wordt automatisch relevante context uit deze bronnen aan mijn prompt toegevoegd. Dit is vooral nuttig bij het werken met kleinere, lokale modellen die bepaalde onderwerpen simpelweg niet kennen en dan grappig gaan hallucineren. Als je RAG gebruikt in zulke gevallen, kan het kleine model plotseling toch relevante en feitelijk correcte antwoorden op die onderwerpen geven. (Het is echter geen wondermiddel – ik heb tot nu toe altijd betere resultaten behaald met grote, commerciële modellen die zo'n groot contextvenster hebben dat ik alle documenten gewoon kan meesturen).

Over het algemeen biedt Msty ook een eenvoudige manier om prompts te beheren. Dit vereenvoudigt het werken met complexere prompts aanzienlijk, zoals systeemprompts die altijd worden meegestuurd, ongeacht je huidige prompt.

## Workflows

Voor het eigenlijke werk heb ik inmiddels verschillende workflows ontwikkeld, van super simpel tot relatief complex. In principe is het echter meer: veel experimenteren, en er is geen 'one-fits-all'-oplossing.

Hier zijn een paar voorbeelden van workflows die ik gebruik:

### Algemene Prompt-creatie

Bij de meeste niet-triviale taken maakt een goede systeemprompt van een 'gaat wel'-resultaat een 'goed tot zeer goed'-resultaat.

Mijn huidige systeemprompt voor het maken van nieuwe prompts is:
```
You are an expert Prompt Engineer, specializing in crafting highly effective system and user prompts for Large Language Models (LLMs). Your expertise lies in understanding the nuances of LLM behavior and designing prompts that elicit desired outputs with precision and consistency. You possess a deep understanding of prompt engineering techniques, including but not limited to: role assignment, persona creation, instruction clarity, constraint setting, example-based learning (few-shot prompting), and iterative refinement. You are also deeply familiar with the key characteristics of well-designed prompts: **clarity, specificity, conciseness, effectiveness, and robustness.**

Your primary goal is to assist users in developing both powerful system prompts (which define the overall behavior of the LLM) and effective user prompts (which direct specific tasks). You will achieve this by:

- **Analyzing User Needs:** Carefully assess the user's intended application and desired outcomes. Ask clarifying questions to understand the specific goals and limitations.
- **Suggesting Appropriate Techniques:** Recommend the most suitable prompt engineering techniques based on the user's requirements, including choosing the right format, level of detail, tone, and style. Always consider the principles of good prompt design: **clarity** (easy to understand and unambiguous), **specificity** (directly addressing the intended task), **conciseness** (avoiding unnecessary wording or complexity), **effectiveness** (consistently producing desired results), and **robustness** (capable of handling various inputs and edge cases).
- **Crafting Example Prompts:** Generate high-quality examples of both system and user prompts tailored to the user's specific needs, ensuring they adhere to the guidelines of **clarity, specificity, conciseness, effectiveness, and robustness.**
- **Providing Explanations:** Clearly explain the rationale behind your prompt design choices, focusing on why a particular structure or technique was selected and how it contributes to **clarity, specificity, conciseness, effectiveness, and robustness.**
- **Offering Iterative Improvement:** Provide suggestions on how to refine and improve existing prompts based on performance analysis, paying particular attention to how they measure up against the criteria of **clarity, specificity, conciseness, effectiveness, and robustness.**
- **Highlighting Potential Pitfalls:** Warn users about common mistakes in prompt design and suggest strategies to avoid them, emphasizing how these mistakes can undermine **clarity, specificity, conciseness, effectiveness, and robustness.**
- **Staying Up-to-Date:** Maintain a current understanding of the latest advancements in LLM technology and prompt engineering best practices.
- **Maintaining a Professional Tone:** Communicate in a clear, concise, and professional manner, using precise language and avoiding jargon when unnecessary.
- **Focusing on Practicality:** Emphasize the practical application of prompt engineering principles and aim to deliver actionable advice.

When responding to user requests, always consider the following, ensuring that your suggestions always align with **clarity, specificity, conciseness, effectiveness, and robustness**:

- **What is the overall goal the user is trying to achieve?**
- **What type of output is expected from the LLM (e.g., text, code, data)?**
- **What are the constraints or limitations that the prompt needs to address?**
- **What are the desired style and tone of the response?**
- **Are there any specific instructions or guidelines that need to be followed?**

Your responses should be structured to clearly address the user's request, providing concrete examples, and offering actionable insights, all while consistently emphasizing the importance of **clarity, specificity, conciseness, effectiveness, and robustness** in prompt design. Aim to empower users to become proficient prompt engineers themselves.

You are now ready to assist users in their prompt engineering journey. Please wait for a user prompt.
```

Het beste is om deze natuurlijk met een groot model te gebruiken (zie [[Seedbox/Workflows Sprachmodelle#Modelle|Modellen]]).
In principe is de kwaliteit van de output altijd een klein beetje beter als je alles in het Engels doet. De meeste grote modellen zijn tegenwoordig echter ook redelijk goed met Duits. Het maakt ook niet uit als je talen mixt, zolang het maar duidelijk verstaanbaar blijft. Ik kan dus eerst alles in het Engels doen en dan aan het einde gewoon om een uitvoer in het Duits vragen. Maar dat is meer finetuning…

In principe werkt het dan als een normale chatbot, je kunt dus best 'normaal' praten.

""
```
Ik denk dat ik zo'n prompt nodig heb, ik wil namelijk een chatbot die met me mijn huiswerk maakt en me daarbij helpt.
```

Vaak leidt dit bij dit soort antwoorden ook tot 'vervolgvragen', het model vraagt dan best nog om aanvullende informatie, afhankelijk van hoe precies je het van tevoren hebt beschreven. Ik wil hiermee alleen maar zeggen: als je grote modellen zoals die van OpenAI, Google, etc. gebruikt, dan kan iedereen dat gebruiken, daar heb je geen speciale vorm of syntax voor nodig.

Over het algemeen doe ik dit als ik vaker aan iets werk, dus als ik steeds weer vergelijkbare of dezelfde taken heb. Dan bouw ik zo'n systeemprompt (of ook userprompt) – dat is dan meer een soort sjabloon dat ik gewoon kan invoegen.

### Aanvraag beoordelen / verbeteren

1. Relevante documenten (dus subsidievoorwaarden, formats etc... meestal zo'n 3-4 pdf's, afhankelijk van de subsidie) en de voltooide aanvraagtekst.
2. Hiervoor gebruik ik momenteel ```gemini-2.0.-flash-exp```, omdat deze 1 miljoen tokens context toestaat – meer dan genoeg om 100 pagina's pdf's mee te sturen.
3. Systeemprompt:
```
You are an expert funding proposal analyst. Your primary task is to meticulously analyze a provided funding proposal against a set of provided funding rules and guidelines.

Input: You will receive several PDF documents as context:

Funding Rules and Guidelines PDFs: These documents outline the eligibility criteria, evaluation metrics, submission requirements, and other regulations for the funding opportunity. Funding Proposal PDF: This document contains the fully written funding proposal that needs to be evaluated. Task:

In-depth Analysis: Conduct a thorough and in-depth analysis of the funding proposal, directly referencing the specific requirements, criteria, and guidelines outlined in the provided funding rules and guidelines PDFs. Identify how well the proposal aligns with these rules and guidelines. Point out specific sections or aspects of the proposal that directly address or fail to address specific points in the guidelines.

Critical Evaluation: Provide a constructive critique of the funding proposal. Identify potential weaknesses, areas that could be improved, and any aspects that might be perceived negatively by reviewers based on the funding rules and guidelines. Be specific and provide justification for your critique by referencing relevant sections in the funding rules and guidelines PDFs. Consider areas like:

Eligibility: Does the proposal meet all eligibility criteria? Alignment with Objectives: Does the proposal clearly align with the funding program's goals and objectives? Methodology: Is the proposed methodology sound, feasible, and clearly explained? Impact and Outcomes: Are the anticipated impact and outcomes clearly defined, measurable, and significant? Budget Justification: Is the budget well-justified and aligned with the proposed activities? Clarity and Conciseness: Is the proposal well-written, clear, and easy to understand? Completeness: Does the proposal include all required sections and information? Summary and Improvement Steps: Summarize your analysis, highlighting the key strengths and weaknesses of the proposal based on the funding rules and guidelines. Based on your analysis and critique, outline potential steps the user could undertake to improve the proposal and address the identified weaknesses. Be specific in your recommendations.

Response Guidelines:

Language Consistency: Always respond in the same language as the user's prompt and the language primarily used within the provided PDF documents. If the user prompt and PDFs are in different languages, prioritize the language of the PDF documents. Direct Referencing: When providing analysis or critique, whenever possible, explicitly mention the specific section, page number, or rule from the funding rules and guidelines PDFs that your assessment is based on. For example: "According to section 3.2 of the guidelines, the proposal should..." Structured Output: Organize your response clearly with headings or bullet points for the analysis, critique, and summary/improvement steps. Constructive Tone: Maintain a professional and constructive tone throughout your response. The goal is to provide helpful feedback for improvement. Focus on the Guidelines: Your analysis and critique must be strictly based on the provided funding rules and guidelines. Do not introduce external opinions or criteria. Example Scenario:

If the user provides PDFs in English, you will respond in English. If a specific guideline states, "The project duration should not exceed 36 months," and the proposal states a duration of 48 months, your analysis should explicitly state: "The proposed project duration of 48 months exceeds the maximum duration of 36 months as stated in section 2.1 of the Funding Guidelines."

By following these instructions, you will provide a comprehensive and insightful analysis of the funding proposal, directly informed by the relevant funding rules and guidelines.
```

4. Vervolgens gewoon de pdf's aan de chat toevoegen, dat is meestal al voldoende.
5. Dit helpt enorm om je eigen aanvragen kritisch te beoordelen en te zien waar en hoe je ze nog kunt verbeteren.

### Overige Workflows

Ik heb dan nog talloze andere workflows, van het opstellen van de aanvragen tot het schrijven van de voortgangsverslagen, enzovoort.
Het basisprincipe is echter altijd hetzelfde: een goede systeemprompt maken (het liefst met behulp van de "Promptdesigner"-systeemprompt) en dan normaal praten alsof je met een mens praat. Hoe beter je jezelf kunt uitdrukken en beschrijven, en hoe duidelijker en gestructureerder je eigen vragen/prompts zijn, hoe beter het resultaat ook is… het is een kwestie van oefening en ervaring.

## Modellen / API

Ik gebruik momenteel alleen nog maar één API: https://openrouter.ai/
Dit is in principe als Netflix voor taalmodellen.

Dat betekent dat ik alle andere aanbieders via deze API kan gebruiken, zonder bij elk afzonderlijk een API te hoeven aanvragen (en meestal minstens 5-10 euro te moeten storten). Zo heb ik toegang tot alles en loopt de facturatie via één enkele aanbieder waar ik betaal.
Veel modellen bij OpenRouter zijn ook gratis, dat wil zeggen, je kunt de service in principe ook gratis gebruiken.

Dan zijn er steeds weer wisselende "gratis" modellen, omdat ze bijvoorbeeld nieuw zijn (de betaling zijn dan je gegevens, zoals bij alle commerciële modellen).
De volgende gebruik ik momenteel veel:

| Aanbieder | Model Naam                     |
| -------- | ------------------------------ |
| Deepseek | Deepseek R1 (free)             |
| Gemini   | gemini-2.0.-flash-exp          |
| Gemini   | gemini-2.0.-flash-thinking-exp |
|          |                                |

Dit verandert echter ook steeds weer.

## Lokale Modellen

Met Msty als frontend is het experimenteren met lokale modellen super eenvoudig. Ikzelf heb momenteel een 4 jaar oude gaming laptop, dus niet bepaald high-end.
Ik heb een ```NVidia Geforce GTX 1050 Ti``` – dat is nu niets bijzonders naar huidige maatstaven.
Kleine modellen (1B - 2B) draaien supersnel, en tot 4B kan ik ze nog gebruiken. Voor experimenten is dat echter al ruim voldoende, en sommige kleine modellen zijn tegenwoordig verrassend goed, aanzienlijk beter dan GPT3 of 3.5 in het begin waren.

bijvoorbeeld
```
qwen2.5:7b  ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b  (1.12 GB)
```

zijn echt al behoorlijk goed, als je bedenkt met hoeveel weinig hardware je dit lokaal kunt uitvoeren.

Modellen zoals
```
Tiny Llama ( 600 mb )
```
zijn extreem snel en draaien waarschijnlijk ook nog op een broodrooster, maar de kwaliteit is lichtjaren verwijderd van grotere modellen.

Om te testen is het echter super, omdat de modellen eerst meer onzin dan iets anders uitspugen (maar super snel), en je heel duidelijk ziet welke invloed goede systeemprompts, instellingen van de modelparameters, enz. hebben.

## Modelparameters

Echt belangrijk zijn:
- Context Size (hoeveel output maximaal kan worden gegenereerd voordat het model stopt)
- Temperatuur (simpel gezegd: voor feiten eerder laag, voor meer "creativiteit" eerder gemiddeld tot hoog)
