---
created: 2025-01-21 18:09:55
update: 2025-03-10 23:07:38
publish: true
tags: 
title: Workflows Sprachmodelle
description: 
authors:
  - Marc Bielert
---

## Frontend: Msty
Als Frontend nutze ich die App [Msty](https://msty.app).

Die ist grundsätzlich komplett kostenlos nutzbar. Es gibt ein paar wenige Features, die hinter einer Paywall liegen, aber das sind eher so Komfort-Sachen, keine grundlegenden Funktionen.

Msty erlaubt es mir, verschiedenste kommerzielle APIs von unterschiedlichen Anbietern (OpenAI, Gemini, Claude, usw.) einzubinden und auch lokale Modelle zu nutzen.
Dabei übernimmt die App eigentlich alles zum Thema Installation. Es ist wirklich nur ein Modell aus einer riesigen Datenbank (Ollama und Huggingface) aussuchen, auf "Installieren" klicken – das war's. Bei den kommerziellen APIs muss man halt nur den API-Key eintragen.

Alle Chats werden lokal gespeichert und können problemlos als JSON oder Markdown exportiert werden.
Msty unterstützt verzweigte Chats (also z.B. wenn ich eine Antwort mit geänderten Parametern oder einem anderen Modell neu generiere, dann habe ich praktisch mehrere Gesprächsstränge, die ich weiterführen kann) und synchronisierte Chats (automatisches Senden des gleichen Prompts an mehrere Modelle).

Außerdem macht es RAG super einfach. RAG bedeutet einfach, dass ich verschiedene Quellen nutzen kann (wie verschiedene Dokumente, Webseiten, YouTube-Links), und dann wird automatisch relevanter Kontext aus diesen Quellen zu meinem Prompt hinzugefügt. Das ist besonders nützlich, wenn man mit kleineren, lokalen Modellen arbeitet, die bestimmte Themen einfach nicht kennen und dann lustig vor sich hin halluzinieren. Nutzt man in solchen Fällen RAG, kann das kleine Modell plötzlich doch relevante und faktisch korrekte Antworten zu diesen Themen liefern. (Ist aber kein Allheilmittel – ich hatte bisher immer bessere Ergebnisse mit großen, kommerziellen Modellen, die so ein großes Kontextfenster haben, dass ich die ganzen Dokumente einfach mitschicken kann).

Generell bietet Msty auch eine einfache Möglichkeit, Prompts zu verwalten. Das vereinfacht die Arbeit mit komplexeren Prompts deutlich, wie z.B. Systemprompts, die immer mitgeschickt werden, egal was dein aktueller Prompt ist.

## Workflows

Für die eigentliche Arbeit habe ich mittlerweile verschiedene Workflows entwickelt, von super simpel bis relativ komplex. Prinzipiell ist es aber eher so: viel experimentieren, und es gibt keine "One-fits-all"-Lösung.

Hier sind ein paar Beispiele für Workflows, die ich nutze:

### Allgemein Prompt-Erstellung

Bei den meisten nicht trivialen Aufgaben macht ein guter Systemprompt aus einem "geht so" Ergebnis ein "gut bis sehr gut".

Mein aktueller Systemprompt für das Erstellen von neuen Prompts ist:
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

Am besten nutzt man den natürlich mit einem großen Modell (siehe [[Seedbox/Workflows Sprachmodelle#Modelle|Modelle]]).
Grundsätzlich ist die Qualität des Outputs immer ein kleines bisschen besser, wenn man alles auf Englisch macht. Die meisten großen Modelle sind aber mittlerweile auch recht gut mit Deutsch. Es macht auch nichts, wenn man Sprachen mischt, solange es klar verständlich bleibt. Ich kann also erstmal alles auf Englisch machen und dann am Ende einfach um eine Ausgabe auf Deutsch bitten. Aber das ist eher schon so Feintuning…

Im Prinzip funktioniert das dann wie ein normaler Chatbot, man kann also durchaus "normal" reden.

""
```
Ich brauche so einen Prompt glaub ich, also ich will halt nen Chatbot der mit mir meine Hausaufgaben macht und mir da so hilft.
```

Oft führt das bei solchen Antworten auch zu "Nachfragen", also das Modell fragt dann durchaus noch nach zusätzlichen Infos, je nachdem, wie genau man das vorher beschrieben hat.  Ich will damit nur sagen: Wenn man große Modelle wie von OpenAI, Google usw. nimmt, dann kann das jeder Anfänger nutzen, da braucht es keine besondere Form oder Syntax.

Generell mache ich das, wenn ich öfter an etwas arbeite, also immer wieder ähnliche oder gleiche Aufgaben habe. Dann baue ich mir so einen Systemprompt (oder auch Userprompt) – das ist halt eher wie eine Vorlage, die ich dann einfach einfügen kann.

### Antrag bewerten / verbessern

1. Relevante Dokumente (also Förderbedingungen, Formate etc... meist so 3-4 PDFs, je nach Förderung) sowie der fertige Antragstext.
2. Hierfür nutze ich zur Zeit ```gemini-2.0.-flash-exp```, da es 1 Million Token Kontext erlaubt – mehr als genug, um 100 Seiten PDFs mit dranzuhängen.
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

4. Dann einfach die PDFs an den Chat anhängen, das reicht meistens schon.
5. Das hilft unglaublich, um die eigenen Anträge kritisch zu bewerten und zu sehen, wo und wie man sie noch verbessern kann.

### Sonstige Workflows

Ich habe dann noch zig andere Workflows, vom Erstellen der Anträge bis zum Schreiben der Sachberichte usw.
Das Grundprinzip ist aber immer das gleiche: einen guten Systemprompt erstellen (am besten mithilfe des "Promptdesigner"-Systemprompts) und dann normal wie mit einem Menschen reden. Je besser man sich ausdrücken und beschreiben kann, und je klarer und strukturierter die eigenen Fragen/Prompts sind, desto besser ist halt auch das Ergebnis… ist halt ein bisschen Übungs- und Erfahrungssache.

## Modelle / API

Ich nutze mittlerweile nur noch eine API: https://openrouter.ai/
Das ist im Prinzip wie Netflix für Sprachmodelle.

Das heißt, ich kann alle anderen Anbieter über diese API nutzen, ohne mir bei jedem einzelnen eine API holen zu müssen (und meistens mindestens 5-10 Euro hinterlegen zu müssen). So habe ich Zugang zu allen und die Abrechnung läuft über einen einzigen Anbieter, bei dem ich bezahle.
Viele Modelle bei OpenRouter sind auch kostenlos, d.h. man kann den Service grundsätzlich auch kostenlos nutzen.

Dann gibt es immer wieder wechselnde "kostenlose" Modelle, weil sie gerade neu sind usw. (die Bezahlung sind dann halt deine Daten, wie bei allen kommerziellen Modellen).
Folgende nutze ich gerade viel:

| Anbieter | Modell Name                     |
| -------- | ------------------------------ |
| Deepseek | Deepseek R1 (free)             |
| Gemini   | gemini-2.0.-flash-exp          |
| Gemini   | gemini-2.0.-flash-thinking-exp |
|          |                                |

Das ändert sich aber auch immer mal wieder.

## Lokale Modelle

Mit Msty als Frontend ist das Rumprobieren mit lokalen Modellen super einfach. Ich selbst habe zur Zeit einen 4 Jahre alten Gaming Laptop, also nicht gerade High-End.
Ich habe eine ```NVidia Geforce GTX 1050 Ti``` – das ist jetzt nichts wirklich Tolles nach heutigen Maßstäben.
Kleine Modelle (1B - 2B) laufen superschnell, und bis zu 4B kann ich die noch benutzen. Zum Experimentieren reicht das aber schon allemal, und manche kleinen Modelle sind mittlerweile erstaunlich gut, deutlich besser als GPT3 oder 3.5 am Anfang waren.

z.B.
```
qwen2.5:7b  ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b  (1.12 GB)
```

sind wirklich schon recht gut, wenn man bedenkt, mit wie wenig Hardware man das lokal ausführen kann.

Modelle wie
```
Tiny Llama ( 600 mb )
```
sind halt krass schnell und laufen wahrscheinlich auch noch auf einem Toaster, aber die Qualität ist Lichtjahre von größeren Modellen entfernt.

Zum Testen aber super, da die Modelle erstmal mehr Schrott als alles andere ausspucken (aber super schnell), und man sehr deutlich sieht, welchen Einfluss gute Systemprompts, Einstellungen der Modellparameter usw. haben.

## Modellparameter

Wirklich wichtig sind:
- Context Size (wieviel Output maximal erzeugt werden kann, bevor das Modell einfach stoppt)
- Temperatur (simpel gesagt: für Fakten eher niedrig, für mehr "Kreativität" eher mittel bis hoch)