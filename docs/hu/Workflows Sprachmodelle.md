---
lang: hu
translation_id: workflows-sprachmodelle
created: 2025-01-21 18:09:55
update: 2025-03-10 23:07:38
publish: true
tags: 
title: Munkafolyamatok nyelvi modellekkel
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Workflows Sprachmodelle.md
translation_source_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T22:55:27+00:00
translation_source_body_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_source_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:29+00:00
translation_source_localized_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_source_structural_metadata_hash: fabd81b872924cf1e4ad2c470413d28754febce294899fe3cc4f625c2c420e80
---
## Frontend: Msty
Frontendként a [Msty](https://msty.app) alkalmazást használom.

Ez alapvetően teljesen ingyenesen használható. Van néhány funkció, ami mögött fizetős fal van, de ezek inkább kényelmi extrák, nem alapvető funkciók.

A Msty lehetővé teszi különféle kereskedelmi API-k (OpenAI, Gemini, Claude stb.) integrálását, valamint helyi modellek használatát is.
Az alkalmazás gyakorlatilag mindent elvégez a telepítéssel kapcsolatban. Csak ki kell választani egy modellt egy hatalmas adatbázisból (Ollama és Huggingface), rákattintani a "Telepítés" gombra – ennyi. A kereskedelmi API-k esetében csak az API-kulcsot kell megadni.

Minden csevegés helyben tárolódik, és problémamentesen exportálható JSON vagy Markdown formátumban.
A Msty támogatja az elágazó csevegéseket (tehát például, ha egy választ módosított paraméterekkel vagy egy másik modellel generálok újra, akkor gyakorlatilag több beszélgetési szálam lesz, amelyeket folytathatok), valamint a szinkronizált csevegéseket (ugyanazon prompt automatikus küldése több modellnek).

Emellett a RAG (Retrieval-Augmented Generation) használatát is rendkívül egyszerűvé teszi. A RAG lényegében azt jelenti, hogy különféle forrásokat (például dokumentumokat, weboldalakat, YouTube-linkeket) használhatok fel, és ezekből a forrásokból automatikusan releváns kontextus kerül hozzáadásra a promptomhoz. Ez különösen hasznos, ha kisebb, helyi modellekkel dolgozom, amelyek nem ismernek bizonyos témákat, és ezért viccesen kezdenek el "hallucinálni". Ha ilyen esetekben RAG-ot használunk, a kis modell hirtelen releváns és tényekben helytálló válaszokat tud adni ezekről a témákról. (Ez azonban nem csodaszer – eddig mindig jobb eredményeket értem el nagy, kereskedelmi modellekkel, amelyeknek olyan nagy a kontextusablaka, hogy az egész dokumentumot el tudom küldeni nekik.)

Általánosságban a Msty egyszerű módot kínál a promptok kezelésére is. Ez jelentősen megkönnyíti a komplexebb promptokkal való munkát, mint például a rendszer-promptok, amelyeket mindig elküldenek, függetlenül attól, hogy mi az aktuális prompt.

## Munkafolyamatok
A tényleges munkához mára különféle munkafolyamatokat fejlesztettem ki, az egészen egyszerűtől a viszonylag komplexig. Alapvetően azonban inkább arról van szó: sok kísérletezés, és nincs "mindenre jó" megoldás.

Íme néhány példa a használt munkafolyamataimra:

### Általános prompt-készítés

A legtöbb nem triviális feladatnál egy jó rendszer-prompt egy "elmegy" eredményt "jó vagy nagyon jó" eredménnyé tesz.

Jelenlegi rendszer-promptom új promptok készítéséhez a következő:
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

Ezt természetesen a legjobb egy nagy modellel használni (lásd [[Seedbox/Workflows Sprachmodelle#Modelle|Modelle]]).
Alapvetően az eredmény minősége mindig egy kicsit jobb, ha mindent angolul csinálunk. A legtöbb nagy modell azonban manapság már németül is elég jól boldogul. Az sem baj, ha keverjük a nyelveket, amíg világosan érthető marad. Tehát először mindent megcsinálhatok angolul, és a végén egyszerűen kérek egy német nyelvű kimenetet. De ez már inkább finomhangolás…

Alapvetően ez úgy működik, mint egy normál chatbot, tehát lehet "normálisan" is beszélgetni.

""
```
Szerintem szükségem van egy ilyen promptra, mert szeretnék egy chatbotot, aki velem csinálja a házi feladatot és segít benne.
```

Gyakran ez ilyen válaszoknál "visszakérdezéshez" vezet, tehát a modell további információkat kér, attól függően, hogy mennyire pontosan írtad le előtte. Csak azt akarom mondani: Ha nagy modelleket használsz, mint az OpenAI, Google stb., akkor bárki, aki kezdő, használhatja, nincs szükség különleges formára vagy szintaxisra.

Általában ezt akkor csinálom, ha valamivel gyakran foglalkozom, tehát mindig hasonló vagy azonos feladataim vannak. Akkor építek egy ilyen rendszer-promptot (vagy akár felhasználói promptot) – ez inkább egy sablon, amit aztán egyszerűen beilleszthetek.

### Kérelem értékelése / javítása

1. Releváns dokumentumok (tehát a támogatási feltételek, formátumok stb. ... általában 3-4 PDF, a támogatástól függően), valamint a kész kérelmi szöveg.
2. Ehhez jelenleg a ```gemini-2.0.-flash-exp```-et használom, mivel 1 millió token kontextust engedélyez – több mint elég ahhoz, hogy 100 oldalas PDF-eket csatoljak.
3. Rendszer-prompt:
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

4. Aztán egyszerűen csatolni kell a PDF-eket a csevegéshez, ez általában elegendő.
5. Ez hihetetlenül segít a saját kérelmek kritikus értékelésében, és abban, hogy lássam, hol és hogyan tudom őket még javítani.

### Egyéb munkafolyamatok

Rengeteg más munkafolyamatom is van, a kérelmek elkészítésétől a jelentések megírásáig stb.
Az alapelv azonban mindig ugyanaz: egy jó rendszer-promptot készíteni (a legjobb a "Promptdesigner" rendszer-prompt segítségével), és aztán normálisan beszélni, mintha emberrel tennéd. Minél jobban tudod kifejezni és leírni magad, és minél tisztábbak és strukturáltabbak a saját kérdéseid/promptjaid, annál jobb az eredmény... ez egy kis gyakorlás és tapasztalat kérdése.

## Modellek / API
Már csak egy API-t használok: https://openrouter.ai/
Ez alapvetően olyan, mint a Netflix a nyelvi modellek számára.

Ez azt jelenti, hogy az összes többi szolgáltatót ezen az API-n keresztül tudom használni, anélkül, hogy mindegyiknél külön API-t kellene szereznem (és általában legalább 5-10 eurót letétbe helyeznem). Így hozzáférésem van mindhez, és a számlázás egyetlen szolgáltatón keresztül történik, akinek fizetek.
Az OpenRouteron sok modell ingyenes, tehát az alapvető szolgáltatást ingyen is lehet használni.

Aztán vannak mindig változó "ingyenes" modellek, mert éppen újak stb. (a fizetség ilyenkor az adataid, mint minden kereskedelmi modellnél).
A következőket használom mostanában sokat:

| Szolgáltató | Modell neve                     |
| -------- | ------------------------------ |
| Deepseek | Deepseek R1 (ingyenes)             |
| Gemini   | gemini-2.0.-flash-exp          |
| Gemini   | gemini-2.0.-flash-thinking-exp |
|          |                                |

Ez azonban mindig változik.

## Helyi modellek
A Msty mint frontend segítségével a helyi modellekkel való kísérletezés rendkívül egyszerű. Jelenleg egy 4 éves gamer laptopom van, tehát nem éppen csúcskategória.
Van egy ```NVidia Geforce GTX 1050 Ti```-em – ez ma már nem számít valami nagy számnak.
A kis modellek (1B - 2B) szupergyorsan futnak, és egészen 4B-ig tudom őket használni. Kísérletezéshez ez már bőven elég, és néhány kis modell ma már meglepően jó, sokkal jobb, mint amilyen a GPT3 vagy a 3.5 volt az elején.

Például:
```
qwen2.5:7b  ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b  (1.12 GB)
```

már tényleg egészen jók, ha belegondolunk, hogy milyen kevés hardverrel lehet őket helyben futtatni.

Olyan modellek, mint
```
Tiny Llama ( 600 mb )
```
nagyon gyorsak, és valószínűleg még egy kenyérpirítón is elfutnak, de a minőségük fényévekkel marad el a nagyobb modellekétől.

Tesztelésre viszont szuper, mivel a modellek eleinte inkább csak szemetet adnak ki (de szupergyorsan), és nagyon jól látszik, milyen hatása van a jó rendszer-promptoknak, a modellparaméterek beállításainak stb.

## Modellparaméterek
Igazán fontosak:
- Kontextus mérete (mennyi kimenet hozható létre maximálisan, mielőtt a modell egyszerűen megáll)
- Hőmérséklet (egyszerűen fogalmazva: tényekhez inkább alacsony, több "kreativitáshoz" inkább közepes vagy magas)
