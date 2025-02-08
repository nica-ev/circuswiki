---
created: 2025-01-21 18:09:55
update: 2025-02-08 20:55:06
publish: true
tags: 
title: Workflows Sprachmodelle
description: 
authors:
  - Marc Bielert
---

## Frontend Msty
Ich nutze als Frontend meistens die App [Msty](https://msty.app)
Kann man grundsätzlich komplett kostenfrei nutzen. Es gibt minimal Features die hinter einer Paywall sind. Das sind aber eher Quality of life sachen, keine grundlegenden Features.

Das erlaubt mir verschiedenste kommerzielle APIs von irgendwelchen Anbietern (OpenAI, Gemini, Claude, etc...) einzubinden, und ebenfalls lokale Modelle zu nutzen.  
Dabei übernimmt die App eigentlich alles zum Thema Installation, es ist wirklich nur Modell raussuchen aus einer riesigen Datenbank (Ollama und Huggingface), ein Klick auf installieren - das wars. Bei den kommerziellen APIs ist es halt nur den API key eintragen...  
  
Die Chats sind alle lokal gespeichert und können problemlos als JSON oder Markdown exportiert werden.  
Es erlaubt verzweigte Chats (also z.b. ich generiere eine Antwort neu mit geänderten Parametern, oder einem anderen Modell und habe dann praktisch mehrere Verläufe die ich fortführen kann) und synchronisierte Chats (automatisch den gleichen Prompt an mehrere Modelle versenden).  
  
Dann ist es sehr einfach RAG - was einfach heisst ich habe verschiedene Quellen z.b. verschiedene Dokumente, Webseiten, Youtube Links) und dann wird meinem Prompt automatisch relevanter Context aus diesen Quellen hinzugefügt. Ist z.b. cool wenn man mit kleinen, lokalen Modellen arbeitet - die bestimmte Themen einfach nicht kennen und dann lustig vor sich hin halluzinieren. Nutzt man RAG in diesem Fall, kann das kleine Modell auf einmal doch relevante und faktisch korrekte Antworten zu diesen Themen liefern. (Ist aber kein Allheilsmittel - bisher hatte ich immer bessere Ergebnisse mit großen, kommerziellen Modellen die ein so großen Context Fenster haben das ich die Dokumente einfach komplett mitsenden kann).  
  
Generell auch einfache Möglichkeit Prompts zu verwalten - was das arbeiten mit komplexeren Prompts (Systemprompts die z.b. immer mitgeschickt werden, unabhängig von deinem aktuellen Prompt) deutlich einfacher macht.  
  
## Workflows
  
Zum arbeiten selber: ich habe mittlerweile verschiedenste Workflows, von super simpel bis zu relativ komplex. Prinzipiell ist das eher so - viel experimentieren und es gibt keine "one fits all" Lösung.  
  
Als Beispiel mal ein paar Workflows die ich habe:

### Allgemein Prompt-erstellung

Bei den meisten nicht trivialen Aufgaben macht ein guter System Prompt aus einem "geht so" Ergebniss ein "das ist gut bis sehr gut".

Mein aktueller Systemprompt für das erstellen von neuen Prompts:
```
You are an expert Prompt Engineer, specializing in crafting highly effective system and user prompts for Large Language Models (LLMs). Your expertise lies in understanding the nuances of LLM behavior and designing prompts that elicit desired outputs with precision and consistency. You possess a deep understanding of prompt engineering techniques, including but not limited to: role assignment, persona creation, instruction clarity, constraint setting, example-based learning (few-shot prompting), and iterative refinement. You are also deeply familiar with the key characteristics of well-designed prompts: **clarity, specificity, conciseness, effectiveness, and robustness.**

Your primary goal is to assist users in developing both powerful system prompts (which define the overall behavior of the LLM) and effective user prompts (which direct specific tasks). You will achieve this by:

- **Analyzing User Needs:** Carefully assess the user's intended application and desired outcomes. Ask clarifying questions to understand the specific goals and limitations.
- **Suggesting Appropriate Techniques:** Recommend the most suitable prompt engineering techniques based on the user's requirements, including choosing the right format, level of detail, tone, and style. Always consider the principles of good prompt design: **clarity** (easy to understand and unambiguous), **specificity** (directly addressing the intended task), **conciseness** (avoiding unnecessary wording or complexity), **effectiveness** (consistently producing desired results), and **robustness** (capable of handling various inputs and edge cases).
- **Crafting Example Prompts:** Generate high-quality examples of both system and user prompts tailored to the user's specific needs, ensuring they adhere to the guidelines of **clarity, specificity, conciseness, effectiveness, and robustness.**
- **Providing Explanations:** Clearly explain the rationale behind your prompt design choices, focusing on why a particular structure or technique was selected and how it contributes to **clarity, specificity, conciseness, effectiveness, and robustness.**
- **Offering Iterative Improvement:** Provide suggestions on how to refine and improve existing prompts based on performance analysis, paying particular attention to how they measure up against the criteria of **clarity, specificity, conciseness, effectiveness, and robustness.**
- **Highlighting Potential Pitfalls:** Warn users about common mistakes in prompt design and suggest strategies to avoid them, emphasizing how these mistakes can undermine **clarity, specificity, conciseness, effectiveness, and robustness.**
- **Staying Up-to-Date:** Maintain a current understanding of the latest advancements in LLM technology and prompt engineering best practices.
- **Maintaining a Professional Tone:** Communicate in a clear, concise, and professional manner, using precise language and avoiding jargon when unnecessary.
- **Focusing on Practicality:** Emphasize the practical application of prompt engineering principles and aim to deliver actionable advice.

When responding to user requests, always consider the following, ensuring that your suggestions always align with **clarity, specificity, conciseness, effectiveness, and robustness**:

- **What is the overall goal the user is trying to achieve?**
- **What type of output is expected from the LLM (e.g., text, code, data)?**
- **What are the constraints or limitations that the prompt needs to address?**
- **What are the desired style and tone of the response?**
- **Are there any specific instructions or guidelines that need to be followed?**

Your responses should be structured to clearly address the user's request, providing concrete examples, and offering actionable insights, all while consistently emphasizing the importance of **clarity, specificity, conciseness, effectiveness, and robustness** in prompt design. Aim to empower users to become proficient prompt engineers themselves.

You are now ready to assist users in their prompt engineering journey. Please wait for a user prompt.
```

Am besten natürlich mit einem großen Modell nutzen (siehe [[Seedbox/Workflows Sprachmodelle#Modelle|Modelle]])
Grundsätzlich ist die Qualität des Outputs immer ein kleines bißchen besser wenn man alles in Englisch macht, die meisten großen Modelle sind aber auch mittlerweile recht gut mit Deutsch. Es ist egal wenn man Sprachen mixt solange es klar verständlich bleibt - ich kann also erstmal alles in Englisch machen und dann am Ende einfach um einen Output in Deutsch bitten. Ist aber eher schon so min-maxing...

Grundsätzlich funktioniert das dann wie als normaler chatbot, man kann also durchaus "normal" reden.

""
```
Ich brauche so einen Prompt glaub ich, also ich will halt nen Chatbot der mit mir meine Hausaufgaben macht und mir da so hilft.
```

Oft wird das bei solchen Antworten auch zu "Nachfragen" führen, also das Modell fragt dann durchaus noch nach zusätzlichen Infos. Je nachdem wie genau man das vorher so beschrieben hat. Will damit nur sagen - wenn man große Modelle wie von OpenAI, Google etc. nimmt - dann kann das jeder Anfänger nutzen, es braucht keine besondere Form oder Syntax.

Grundsätzlich mach ich das wenn ich öfter an etwas arbeite, also immer wieder ähnliche oder gleiche Aufgaben hab - dann baue ich mir so einen Systemprompt (oder auch Userprompt) - ist halt eher wie ein Template was ich dann einfach einfügen kann.

### Antrag bewerten / verbessern

1. relevante Dokumente  (also Förderbedingungen, Formate etc... meist so 3-4 Pdfs, je nach Förderung) sowie der fertige Antragstext.
2. hierfür nutze ich zur Zeit ```gemini-2.0.-flash-exp``` da es 1 million token context erlaubt - mehr als genug um 100 Seiten pdfs mit ranzuhängen
3. Systemprompt:
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

4. dann einfach die Pdfs an den Chat anhängen, reicht meist schon. 
5. Das hilft unglaublich um die eigenen Anträge kritisch zu bewerten und zu sehen wo und wie man noch verbessern kann.

### Sonstiges

Ich hab dann zig Workflows, vom erstellen der Anträge, schreiben der Sachberichte etc.
Das Grundprinzip ist aber immer das gleiche: einen guten Systemprompt erstellen (am besten mithilfe des "Promptdesigner" Systemprompts) und dann normal wie mit nem Menschen reden - je besser man beschreiben und sich ausdrücken kann, je klarer und strukturierter die eigenen Fragen/Prompts sind - desto besser ist halt auch das Ergebniss... ist halt ein bissel Übungs/Erfahrungssache.

## Modelle / API

Ich nutze mittlerweile nur noch eine API - https://openrouter.ai/
Ist prinzipiell wie Netflix für Sprachmodelle.

Meint, ich kann alle anderen Anbieter über diese API nutzen ohne mir bei jedem einzelnen ne API zu holen (und meist mindestens 5-10 Euro zu hinterlegen) - so habe ich Zugang zu allen und es läuft über genau einen Anbieter bei dem ich bezahle.
Viele Modelle bei OpenRouter sind auch kostenfrei - d.h. ich kann den Service grundsätzlich auch kostenlos nutzen. 

Dann gibt es immer wieder wechselnde "kostenlose" Modelle weil sie gerade neu sind etc. (die Bezahlung sind dann halt deine Daten, wie bei allen kommerziellen Modellen).
Folgende nutze ich gerade viel:

| Anbieter | Modell Name                    |
| -------- | ------------------------------ |
| Deepseek | Deepseek R1 (free)             |
| Gemini   | gemini-2.0.-flash-exp          |
| Gemini   | gemini-2.0.-flash-thinking-exp |
|          |                                |
Das ändert sich aber auch immer wieder mal.

## Lokale Modelle

Mit Msty als Frontend ist das rumprobieren mit lokalen Modellen super einfach. Ich habe selber zur Zeit einen 4 Jahre alten Gaming Laptop - also nicht gerade High-end.
Ich habe eine ```NVidia Geforce GTX 1050 Ti``` - das ist nix wirklich tolles für heutige Maßstäbe.
Kleine Modelle (1B - 2B) laufen superschnell, 
bis zu 4B kann ich die noch benutzen. Zum experimentieren reicht das aber schon allemal, und manche kleinen Modelle sind mittlerweile erstaunlich gut, deutlich besser als GPT3 oder 3.5 am Anfang war.

z.b.
```
qwen2.5:7b  ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b  (1.12 GB)
```

sind wirklich schon recht gut, wenn man bedenkt mit wenig Hardware man das lokal ausführen kann.

Modelle wie 
```
Tiny Llama ( 600 mb )
```
sind halt krass schnell und laufen wahrscheinlich auch noch auf nem Toaster - aber sind halt auch Lichtjahre von der Qualität größerer Modelle entfernt.

Zum testen aber super, da die Modelle erstmal mehr Schrott als alles andere ausspucken (aber super schnell) - und man sehr deutlich sieht welchen Einfluss gute system prompts, einstellungen der Modell Parameter etc. haben.

## Modell Parameter

Wirklich wichtig sind
- Context Size (wieviel Output maximal erzeugt werden kann bevor das Modell einfach stoppt)
- Temperatur ( simpel gesagt: für Fakten eher niedrig, für mehr "Kreativität" eher mittel bis hoch )