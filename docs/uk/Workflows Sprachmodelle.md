---
lang: uk
translation_id: workflows-sprachmodelle
created: 2025-01-21 18:09:55
update: 2025-03-10 23:07:38
publish: true
tags: 
title: Робочі процеси мовних моделей
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Workflows Sprachmodelle.md
translation_source_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T14:33:36+00:00
translation_source_body_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_source_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:32+00:00
translation_source_localized_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_source_structural_metadata_hash: fabd81b872924cf1e4ad2c470413d28754febce294899fe3cc4f625c2c420e80
---
## Frontend: Msty
Як фронтенд я використовую додаток [Msty](https://msty.app).

Він, загалом, повністю безкоштовний. Є кілька функцій, які знаходяться за платною стіною, але це радше зручності, а не базові функції.

Msty дозволяє мені підключати різноманітні комерційні API від різних постачальників (OpenAI, Gemini, Claude тощо), а також використовувати локальні моделі.
Додаток фактично бере на себе все, що стосується встановлення. Вам потрібно лише вибрати модель з величезної бази даних (Ollama та Huggingface), натиснути "Встановити" – і все. Для комерційних API потрібно лише ввести API-ключ.

Усі чати зберігаються локально та можуть бути легко експортовані як JSON або Markdown.
Msty підтримує розгалужені чати (тобто, наприклад, якщо я перегенерую відповідь зі зміненими параметрами або іншою моделлю, я отримую кілька гілок розмови, які можу продовжувати) та синхронізовані чати (автоматичне надсилання одного й того ж запиту до кількох моделей).

Крім того, він робить RAG надзвичайно простим. RAG означає, що я можу використовувати різні джерела (як-от різні документи, вебсайти, посилання на YouTube), а потім релевантний контекст з цих джерел автоматично додається до мого запиту. Це особливо корисно при роботі з меншими локальними моделями, які не знають певних тем і тому схильні до "галюцинацій". Якщо в таких випадках використовувати RAG, невелика модель раптом зможе надавати релевантні та фактично правильні відповіді на ці теми. (Хоча це не панацея – я досі мав кращі результати з великими комерційними моделями, які мають настільки велике контекстне вікно, що я можу просто надсилати їм усі документи).

Загалом, Msty також пропонує простий спосіб керування запитами. Це значно спрощує роботу зі складнішими запитами, такими як системні запити, які завжди надсилаються, незалежно від вашого поточного запиту.

## Робочі процеси

Для фактичної роботи я розробив різні робочі процеси, від дуже простих до відносно складних. В принципі, це радше так: багато експериментів, і немає універсального рішення.

Ось кілька прикладів робочих процесів, які я використовую:

### Загальне створення запитів

Для більшості нетривіальних завдань хороший системний запит перетворює результат "так собі" на "добрий або дуже добрий".

Мій поточний системний запит для створення нових запитів:
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

Найкраще використовувати його з великою моделлю (див. [[Seedbox/Workflows Sprachmodelle#Modelle|Моделі]]).
Загалом, якість виведення завжди трохи краща, якщо все робити англійською. Однак більшість великих моделей зараз досить добре розуміють німецьку. Також не проблема змішувати мови, якщо це залишається зрозумілим. Отже, я можу спочатку зробити все англійською, а потім в кінці просто попросити вивести німецькою. Але це вже більше схоже на тонке налаштування…

В принципі, це працює як звичайний чат-бот, тому ви можете спілкуватися "нормально".

""
```
Мені потрібен такий запит, я хочу чат-бота, який допомагатиме мені з домашніми завданнями.
```

Часто це призводить до "уточнень" у відповідях, тобто модель може поставити додаткові запитання, залежно від того, наскільки точно ви описали завдання. Я хочу сказати цим: якщо ви використовуєте великі моделі, як від OpenAI, Google тощо, то з цим впорається будь-який новачок, не потрібна особлива форма чи синтаксис.

Загалом, я роблю це, коли часто працюю над чимось, тобто коли маю схожі або однакові завдання. Тоді я створюю такий системний запит (або користувацький запит) – це радше як шаблон, який я потім можу просто вставити.

### Оцінка / покращення заявки

1. Відповідні документи (тобто умови фінансування, формати тощо... зазвичай 3-4 PDF, залежно від фінансування) та готовий текст заявки.
2. Для цього я зараз використовую ```gemini-2.0.-flash-exp```, оскільки він дозволяє контекст до 1 мільйона токенів – цього більш ніж достатньо, щоб додати 100 сторінок PDF.
3. Системний запит:
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

4. Потім просто додайте PDF до чату, цього зазвичай достатньо.
5. Це неймовірно допомагає критично оцінити власні заявки та побачити, де і як їх можна покращити.

### Інші робочі процеси

У мене є ще безліч інших робочих процесів, від створення заявок до написання звітів тощо.
Але основний принцип завжди той самий: створити хороший системний запит (найкраще за допомогою системного запиту "Promptdesigner") і потім спілкуватися нормально, як з людиною. Чим краще ви можете висловлюватися та описувати, і чим чіткішими та структурованішими є ваші запитання/запити, тим кращим буде результат… це вимагає певної практики та досвіду.

## Моделі / API

Наразі я використовую лише одну API: https://openrouter.ai/
Це, по суті, як Netflix для мовних моделей.

Це означає, що я можу використовувати всіх інших постачальників через цю API, не отримуючи API від кожного окремо (і зазвичай не вносячи щонайменше 5-10 євро депозиту). Таким чином, я маю доступ до всіх, а розрахунки відбуваються через одного постачальника, якому я плачу.
Багато моделей на OpenRouter також безкоштовні, тобто ви можете користуватися сервісом взагалі безкоштовно.

Потім є постійно змінні "безкоштовні" моделі, тому що вони нові тощо (оплата – це ваші дані, як і у всіх комерційних моделей).
Зараз я багато використовую наступні:

| Постачальник | Назва моделі                |
| ------------- | --------------------------- |
| Deepseek      | Deepseek R1 (free)          |
| Gemini        | gemini-2.0.-flash-exp       |
| Gemini        | gemini-2.0.-flash-thinking-exp |
|               |                             |

Але це теж постійно змінюється.

## Локальні моделі

З Msty як фронтендом експериментувати з локальними моделями надзвичайно просто. Наразі я маю ігровий ноутбук чотирирічної давності, тобто не зовсім хай-енд.
У мене є ```NVidia Geforce GTX 1050 Ti``` – це не дуже вражає за сучасними мірками.
Невеликі моделі (1B - 2B) працюють надзвичайно швидко, і до 4B я можу їх використовувати. Але для експериментів цього цілком достатньо, і деякі маленькі моделі зараз дивовижно хороші, значно кращі, ніж GPT3 або 3.5 були на початку.

Наприклад:
```
qwen2.5:7b  ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b  (1.12 GB)
```

вже досить хороші, якщо врахувати, з якою малою кількістю обладнання їх можна запускати локально.

Моделі на кшталт
```
Tiny Llama ( 600 mb )
```
працюють надзвичайно швидко і, ймовірно, запустяться навіть на тостері, але якість знаходиться на світлові роки від більших моделей.

Але для тестування вони чудові, оскільки моделі спочатку видають більше сміття, ніж будь-чого іншого (але дуже швидко), і ви дуже чітко бачите, який вплив мають хороші системні запити, налаштування параметрів моделі тощо.

## Параметри моделі

Справді важливі:
- Розмір контексту (скільки максимум виведення може бути згенеровано, перш ніж модель просто зупиниться)
- Температура (простими словами: для фактів краще низька, для більшої "креативності" – середній або високий рівень)
