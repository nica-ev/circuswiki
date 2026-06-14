---
lang: pl
translation_id: workflows-sprachmodelle
created: 2025-01-21 18:09:55
update: 2025-03-10 23:07:38
publish: true
tags: 
title: Przepływy pracy modeli językowych
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Workflows Sprachmodelle.md
translation_source_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T20:25:18+00:00
translation_source_body_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_source_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:28+00:00
translation_source_localized_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_source_structural_metadata_hash: fabd81b872924cf1e4ad2c470413d28754febce294899fe3cc4f625c2c420e80
---
## Frontend: Msty
Jako frontend wykorzystuję aplikację [Msty](https://msty.app).

Jest ona zasadniczo całkowicie darmowa. Istnieje kilka funkcji, które są płatne, ale są to raczej kwestie wygody, a nie podstawowe funkcje.

Msty pozwala mi na integrację z różnorodnymi komercyjnymi API od różnych dostawców (OpenAI, Gemini, Claude itp.), a także na korzystanie z modeli lokalnych.
Aplikacja zajmuje się praktycznie wszystkim związanym z instalacją. Wystarczy wybrać model z ogromnej bazy danych (Ollama i Huggingface), kliknąć „Zainstaluj” – i to wszystko. W przypadku komercyjnych API wystarczy wprowadzić klucz API.

Wszystkie czaty są zapisywane lokalnie i można je bez problemu eksportować jako JSON lub Markdown.
Msty obsługuje czaty rozgałęzione (czyli np. gdy generuję odpowiedź ponownie z zmienionymi parametrami lub innym modelem, mam praktycznie kilka wątków rozmowy, które mogę kontynuować) oraz czaty zsynchronizowane (automatyczne wysyłanie tego samego promptu do wielu modeli).

Ponadto, znacznie ułatwia RAG. RAG oznacza po prostu, że mogę korzystać z różnych źródeł (takich jak różne dokumenty, strony internetowe, linki do YouTube), a następnie odpowiedni kontekst z tych źródeł jest automatycznie dodawany do mojego promptu. Jest to szczególnie przydatne podczas pracy z mniejszymi, lokalnymi modelami, które po prostu nie znają pewnych tematów i zaczynają „halucynować”. W takich przypadkach, używając RAG, mały model może nagle dostarczyć trafnych i faktograficznie poprawnych odpowiedzi na te tematy. (Nie jest to jednak panaceum – osobiście zawsze uzyskiwałem lepsze wyniki z dużymi, komercyjnymi modelami, które mają tak duże okno kontekstowe, że mogę po prostu wysłać im wszystkie dokumenty).

Ogólnie rzecz biorąc, Msty oferuje również prosty sposób zarządzania promptami. Znacznie ułatwia to pracę ze złożonymi promptami, takimi jak prompty systemowe, które są zawsze wysyłane, niezależnie od bieżącego promptu.

## Przepływy pracy (Workflows)

Do właściwej pracy opracowałem już różne przepływy pracy, od bardzo prostych po stosunkowo złożone. Zasadniczo jednak jest to raczej kwestia: dużo eksperymentowania, i nie ma jednego „uniwersalnego” rozwiązania.

Oto kilka przykładów przepływów pracy, z których korzystam:

### Ogólne tworzenie promptów

W przypadku większości nietrywialnych zadań, dobry prompt systemowy zamienia wynik „tak sobie” na „dobry do bardzo dobrego”.

Mój obecny prompt systemowy do tworzenia nowych promptów brzmi:
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

Najlepiej korzystać z niego z dużym modelem (patrz [[Seedbox/Workflows Sprachmodelle#Modelle|Modele]]).
Zasadniczo jakość wyniku jest zawsze odrobinę lepsza, gdy wszystko robi się po angielsku. Większość dużych modeli jest jednak obecnie całkiem dobra w obsłudze języka niemieckiego. Nie ma też problemu z mieszaniem języków, o ile jest to jasno zrozumiałe. Mogę więc najpierw zrobić wszystko po angielsku, a na końcu poprosić o wynik po niemiecku. Ale to już bardziej kwestia dopracowania…

W zasadzie działa to jak zwykły chatbot, można więc rozmawiać „normalnie”.

""
```
Chyba potrzebuję takiego promptu, bo chcę mieć chatbota, który będzie mi pomagał w odrabianiu zadań domowych.
```

Często prowadzi to do „dodatkowych pytań” ze strony modelu, który dopytuje o dodatkowe informacje, w zależności od tego, jak dokładnie zostało to wcześniej opisane. Chcę przez to powiedzieć: jeśli korzysta się z dużych modeli, takich jak OpenAI, Google itp., to każdy początkujący może z nich korzystać, nie potrzeba do tego żadnej specjalnej formy ani składni.

Ogólnie robię tak, gdy pracuję nad czymś wielokrotnie, czyli gdy mam do czynienia z podobnymi lub identycznymi zadaniami. Wtedy tworzę taki prompt systemowy (lub prompt użytkownika) – to jest bardziej jak szablon, który mogę po prostu wstawić.

### Ocena / poprawa wniosku

1. Odpowiednie dokumenty (czyli warunki dofinansowania, formaty itp… zazwyczaj 3-4 pliki PDF, w zależności od dofinansowania) oraz gotowy tekst wniosku.
2. Do tego celu używam obecnie ```gemini-2.0.-flash-exp```, ponieważ pozwala na 1 milion tokenów kontekstu – więcej niż wystarczająco, aby dołączyć 100 stron PDF.
3. Prompt systemowy:
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

4. Następnie wystarczy dołączyć pliki PDF do czatu, to zazwyczaj wystarcza.
5. To niesamowicie pomaga w krytycznej ocenie własnych wniosków i zobaczeniu, gdzie i jak można je jeszcze poprawić.

### Inne przepływy pracy

Mam jeszcze mnóstwo innych przepływów pracy, od tworzenia wniosków po pisanie raportów rzeczowych itp.
Podstawowa zasada jest jednak zawsze ta sama: stworzyć dobry prompt systemowy (najlepiej za pomocą promptu systemowego „projektanta promptów”), a następnie rozmawiać normalnie, jak z człowiekiem. Im lepiej potrafisz się wyrazić i opisać, im jaśniejsze i bardziej ustrukturyzowane są Twoje pytania/prompty, tym lepszy jest wynik… to w zasadzie kwestia praktyki i doświadczenia.

## Modele / API

Obecnie korzystam tylko z jednego API: https://openrouter.ai/
To w zasadzie jak Netflix dla modeli językowych.

Oznacza to, że mogę korzystać z usług wszystkich innych dostawców za pośrednictwem tego jednego API, bez konieczności uzyskiwania dostępu do każdego z nich osobno (i zazwyczaj wpłacania co najmniej 5-10 euro). W ten sposób mam dostęp do wszystkich, a rozliczenie odbywa się przez jednego dostawcę, któremu płacę.
Wiele modeli w OpenRouter jest również darmowych, co oznacza, że z usługi można zasadniczo korzystać bezpłatnie.

Są też stale zmieniające się „darmowe” modele, ponieważ są nowe itp. (zapłatą są wtedy Twoje dane, jak we wszystkich komercyjnych modelach).
Obecnie dużo korzystam z następujących:

| Dostawca | Nazwa modelu                  |
| -------- | ----------------------------- |
| Deepseek | Deepseek R1 (free)            |
| Gemini   | gemini-2.0.-flash-exp         |
| Gemini   | gemini-2.0.-flash-thinking-exp |
|          |                               |

Ale to też się czasem zmienia.

## Modele lokalne

Z Msty jako frontendem, eksperymentowanie z modelami lokalnymi jest bardzo proste. Sam mam obecnie 4-letniego laptopa gamingowego, więc nie jest to sprzęt z najwyższej półki.
Mam ```NVidia Geforce GTX 1050 Ti``` – to nie jest nic rewelacyjnego według dzisiejszych standardów.
Małe modele (1B - 2B) działają super szybko, a do 4B mogę ich jeszcze używać. Do eksperymentowania to jednak w zupełności wystarcza, a niektóre małe modele są już zaskakująco dobre, znacznie lepsze niż GPT3 czy 3.5 na początku.

Na przykład:
```
qwen2.5:7b ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b (1.12 GB)
```

są już naprawdę całkiem dobre, biorąc pod uwagę, jak niewielkim sprzętem można je uruchomić lokalnie.

Modele takie jak
```
Tiny Llama ( 600 mb )
```
są po prostu niesamowicie szybkie i prawdopodobnie zadziałają nawet na tosterze, ale jakość jest lata świetlne od większych modeli.

Są jednak świetne do testowania, ponieważ modele na początku generują więcej „śmieci” niż czegokolwiek innego (ale super szybko), a można bardzo wyraźnie zobaczyć, jaki wpływ mają dobre prompty systemowe, ustawienia parametrów modelu itp.

## Parametry modelu

Naprawdę ważne są:
- Rozmiar kontekstu (ile maksymalnie można wygenerować wyniku, zanim model po prostu się zatrzyma)
- Temperatura (mówiąc prosto: dla faktów raczej nisko, dla większej „kreatywności” raczej średnio do wysoko)
