---
lang: it
translation_id: workflows-sprachmodelle
created: 2025-01-21 18:09:55
update: 2025-03-10 23:07:38
publish: true
tags: 
title: Flussi di lavoro per modelli linguistici
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Workflows Sprachmodelle.md
translation_source_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T23:10:06+00:00
translation_source_body_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_source_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:29+00:00
translation_source_localized_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_source_structural_metadata_hash: fabd81b872924cf1e4ad2c470413d28754febce294899fe3cc4f625c2c420e80
---
## Frontend: Msty
Come frontend utilizzo l'app [Msty](https://msty.app).

È fondamentalmente utilizzabile gratuitamente. Ci sono pochissime funzionalità a pagamento, ma si tratta più che altro di comodità, non di funzioni essenziali.

Msty mi permette di integrare diverse API commerciali di vari fornitori (OpenAI, Gemini, Claude, ecc.) e anche di utilizzare modelli locali.
L'app si occupa di tutto ciò che riguarda l'installazione. Devi solo scegliere un modello da un vasto database (Ollama e Huggingface), cliccare su "Installa" – e questo è tutto. Per le API commerciali, devi solo inserire la chiave API.

Tutte le chat vengono salvate localmente e possono essere esportate senza problemi come JSON o Markdown.
Msty supporta chat ramificate (ad esempio, se rigenero una risposta con parametri modificati o un modello diverso, ho praticamente più filoni di conversazione che posso continuare) e chat sincronizzate (invio automatico dello stesso prompt a più modelli).

Inoltre, rende il RAG (Retrieval-Augmented Generation) semplicissimo. RAG significa semplicemente che posso utilizzare diverse fonti (come documenti, siti web, link di YouTube) e poi il contesto pertinente da queste fonti viene automaticamente aggiunto al mio prompt. Questo è particolarmente utile quando si lavora con modelli più piccoli e locali che non conoscono determinati argomenti e quindi iniziano a "allucinare" in modo divertente. Utilizzando il RAG in questi casi, il modello piccolo può improvvisamente fornire risposte pertinenti e fattualmente corrette su questi argomenti. (Non è una panacea, tuttavia: finora ho sempre ottenuto risultati migliori con modelli commerciali di grandi dimensioni, che hanno una finestra di contesto così ampia da permettermi di inviare tutti i documenti semplicemente insieme al prompt).

In generale, Msty offre anche un modo semplice per gestire i prompt. Questo semplifica notevolmente il lavoro con prompt più complessi, come i system prompt, che vengono sempre inviati indipendentemente dal prompt corrente.

## Flussi di lavoro

Per il lavoro vero e proprio, ho sviluppato diversi flussi di lavoro, da super semplici a relativamente complessi. In linea di principio, però, è più una questione di sperimentare molto, e non esiste una soluzione "taglia unica".

Ecco alcuni esempi di flussi di lavoro che utilizzo:

### Creazione generale di prompt

Per la maggior parte dei compiti non banali, un buon system prompt trasforma un risultato "così così" in un risultato "buono o molto buono".

Il mio attuale system prompt per la creazione di nuovi prompt è:
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

È meglio usarlo con un modello di grandi dimensioni (vedi [[Seedbox/Workflows Sprachmodelle#Modelle|Modelli]]).
In linea di principio, la qualità dell'output è sempre leggermente migliore se si fa tutto in inglese. Tuttavia, la maggior parte dei modelli di grandi dimensioni è ormai abbastanza brava anche con il tedesco. Non c'è problema nemmeno a mescolare le lingue, purché rimanga chiaramente comprensibile. Posso quindi fare tutto in inglese all'inizio e poi chiedere semplicemente un output in tedesco alla fine. Ma questo è più un affinamento...

In linea di principio, funziona come un normale chatbot, quindi si può parlare "normalmente".

""
```
Credo di aver bisogno di un prompt del genere, cioè vorrei un chatbot che mi aiuti con i compiti e mi dia una mano.
```

Spesso, con risposte di questo tipo, si ottengono anche delle "richieste di chiarimento", ovvero il modello chiede ulteriori informazioni, a seconda di quanto precisamente è stato descritto in precedenza. Voglio dire solo questo: se si utilizzano modelli di grandi dimensioni come quelli di OpenAI, Google, ecc., chiunque può usarli, non è necessaria una forma o una sintassi particolare.

In generale, lo faccio quando lavoro spesso su qualcosa, cioè quando ho compiti simili o uguali da svolgere ripetutamente. Allora creo un system prompt (o anche un user prompt) – che è più una sorta di modello che posso semplicemente inserire.

### Valutare / migliorare una proposta

1. Documenti pertinenti (condizioni di finanziamento, formati, ecc... di solito 3-4 PDF, a seconda del finanziamento) e il testo della proposta completata.
2. Per questo, attualmente utilizzo ```gemini-2.0.-flash-exp```, poiché consente 1 milione di token di contesto – più che sufficiente per allegare 100 pagine di PDF.
3. System prompt:
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

4. Poi basta allegare i PDF alla chat, di solito è sufficiente.
5. Questo aiuta incredibilmente a valutare criticamente le proprie proposte e a vedere dove e come migliorarle ulteriormente.

### Altri flussi di lavoro

Ho poi innumerevoli altri flussi di lavoro, dalla creazione delle proposte alla stesura dei rapporti di avanzamento, ecc.
Il principio di base è sempre lo stesso: creare un buon system prompt (meglio se con l'aiuto del system prompt "Prompt designer") e poi parlare normalmente come con una persona. Più si è in grado di esprimersi e descrivere, e più chiari e strutturati sono i propri quesiti/prompt, migliore sarà il risultato... è una questione di pratica ed esperienza.

## Modelli / API

Ormai utilizzo solo un'API: https://openrouter.ai/
È fondamentalmente come Netflix per i modelli linguistici.

Ciò significa che posso utilizzare tutti gli altri fornitori tramite questa API, senza doverne ottenere una da ciascuno (e di solito dover depositare almeno 5-10 euro). In questo modo ho accesso a tutti e la fatturazione avviene tramite un unico fornitore, a cui pago.
Molti modelli su OpenRouter sono anche gratuiti, il che significa che il servizio può essere utilizzato fondamentalmente anche gratuitamente.

Poi ci sono modelli "gratuiti" che cambiano continuamente, perché sono nuovi, ecc. (il pagamento sono i tuoi dati, come per tutti i modelli commerciali).
Attualmente utilizzo molto i seguenti:

| Fornitore | Nome del Modello              |
| -------- | ------------------------------ |
| Deepseek | Deepseek R1 (free)             |
| Gemini   | gemini-2.0.-flash-exp          |
| Gemini   | gemini-2.0.-flash-thinking-exp |
|          |                                |

Ma anche questo cambia di tanto in tanto.

## Modelli Locali

Con Msty come frontend, sperimentare con modelli locali è semplicissimo. Io stesso ho attualmente un laptop da gaming di 4 anni, quindi non proprio di fascia alta.
Ho una ```NVidia Geforce GTX 1050 Ti``` – che non è niente di eccezionale secondo gli standard attuali.
Modelli piccoli (1B - 2B) funzionano super veloci, e fino a 4B posso ancora usarli. Per sperimentare, però, è più che sufficiente, e alcuni modelli piccoli sono ormai sorprendentemente buoni, molto meglio di quanto lo fossero GPT3 o 3.5 all'inizio.

Ad esempio:
```
qwen2.5:7b  ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b  (1.12 GB)
```

sono davvero già abbastanza buoni, considerando quanta poca hardware si può usare per eseguirli localmente.

Modelli come
```
Tiny Llama ( 600 mb )
```
sono incredibilmente veloci e probabilmente funzionano anche su un tostapane, ma la qualità è a anni luce di distanza dai modelli più grandi.

Sono comunque ottimi per i test, dato che i modelli inizialmente sputano più spazzatura che altro (ma super velocemente), e si vede molto chiaramente l'influenza di buoni system prompt, impostazioni dei parametri del modello, ecc.

## Parametri del Modello

Davvero importanti sono:
- Dimensione del contesto (quanto output massimo può essere generato prima che il modello si fermi semplicemente)
- Temperatura (semplicemente detto: per i fatti, meglio bassa; per più "creatività", meglio medio-alta)
