---
lang: pt
translation_id: workflows-sprachmodelle
created: 2025-01-21 18:09:55
update: 2025-03-10 23:07:38
publish: true
tags: 
title: Fluxos de Trabalho de Modelos de Linguagem
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Workflows Sprachmodelle.md
translation_source_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T19:15:36+00:00
translation_source_body_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_source_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:33+00:00
translation_source_localized_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_source_structural_metadata_hash: fabd81b872924cf1e4ad2c470413d28754febce294899fe3cc4f625c2c420e80
---
## Frontend: Msty
Como frontend, utilizo a aplicação [Msty](https://msty.app).

Esta aplicação é, fundamentalmente, de uso totalmente gratuito. Existem algumas poucas funcionalidades que estão atrás de um paywall, mas são mais questões de conveniência, não funções básicas.

O Msty permite-me integrar diversas APIs comerciais de diferentes fornecedores (OpenAI, Gemini, Claude, etc.) e também utilizar modelos locais.
A aplicação trata de toda a instalação. É realmente só escolher um modelo de uma base de dados enorme (Ollama e Huggingface), clicar em "Instalar" – e pronto. Para as APIs comerciais, basta inserir a chave de API.

Todos os chats são guardados localmente e podem ser exportados sem problemas como JSON ou Markdown.
O Msty suporta chats ramificados (ou seja, por exemplo, se eu regenerar uma resposta com parâmetros alterados ou um modelo diferente, tenho praticamente vários fluxos de conversa que posso continuar) e chats sincronizados (envio automático do mesmo prompt para vários modelos).

Além disso, torna o RAG super fácil. RAG significa simplesmente que posso usar várias fontes (como diferentes documentos, páginas web, links do YouTube) e, em seguida, o contexto relevante dessas fontes é adicionado automaticamente ao meu prompt. Isto é particularmente útil quando se trabalha com modelos menores e locais que simplesmente não conhecem certos tópicos e, em seguida, começam a "alucinar" de forma divertida. Se usar RAG nesses casos, o modelo pequeno pode de repente fornecer respostas relevantes e factualmente corretas sobre esses tópicos. (Mas não é uma panaceia – até agora, tive sempre melhores resultados com modelos comerciais grandes, que têm uma janela de contexto tão grande que posso simplesmente enviar todos os documentos).

Em geral, o Msty também oferece uma forma simples de gerir prompts. Isto simplifica significativamente o trabalho com prompts mais complexos, como prompts de sistema, que são sempre enviados, independentemente do seu prompt atual.

## Fluxos de Trabalho

Para o trabalho em si, desenvolvi entretanto vários fluxos de trabalho, desde super simples a relativamente complexos. Em princípio, é mais assim: muita experimentação, e não existe uma solução "tamanho único".

Aqui estão alguns exemplos de fluxos de trabalho que utilizo:

### Criação Geral de Prompts

Para a maioria das tarefas não triviais, um bom prompt de sistema transforma um resultado "mediano" num resultado "bom a muito bom".

O meu prompt de sistema atual para a criação de novos prompts é:
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

O ideal é usá-lo com um modelo grande (ver [[Seedbox/Workflows Sprachmodelle#Modelle|Modelos]]).
Em princípio, a qualidade do output é sempre um pouco melhor se tudo for feito em inglês. No entanto, a maioria dos modelos grandes é atualmente bastante boa com o alemão. Também não há problema em misturar idiomas, desde que permaneça claramente compreensível. Posso, portanto, fazer tudo em inglês primeiro e depois, no final, pedir simplesmente uma saída em alemão. Mas isso já é mais um ajuste fino...

Em princípio, funciona como um chatbot normal, pelo que se pode falar "normalmente".

""
```
Acho que preciso de um prompt assim, quero um chatbot que me ajude com os meus trabalhos de casa.
```

Muitas vezes, isto leva a "perguntas de seguimento" nas respostas, ou seja, o modelo pergunta por informações adicionais, dependendo da precisão com que descreveu as coisas anteriormente. Só quero dizer com isto: se usar modelos grandes como os da OpenAI, Google, etc., qualquer iniciante pode utilizá-los, não é necessária nenhuma forma ou sintaxe especial.

Em geral, faço isto quando trabalho frequentemente em algo, ou seja, quando tenho tarefas semelhantes ou idênticas repetidamente. Então, crio um prompt de sistema (ou também um prompt de utilizador) – é mais como um modelo que posso simplesmente inserir.

### Avaliar / Melhorar Candidatura

1. Documentos relevantes (ou seja, condições de financiamento, formatos, etc... geralmente cerca de 3-4 PDFs, dependendo do financiamento) e o texto final da candidatura.
2. Para isto, utilizo atualmente o ```gemini-2.0.-flash-exp```, pois permite 1 milhão de tokens de contexto – mais do que suficiente para anexar 100 páginas de PDFs.
3. Prompt de sistema:
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

4. Em seguida, basta anexar os PDFs ao chat, isso geralmente é suficiente.
5. Isto ajuda imensamente a avaliar criticamente as próprias candidaturas e a ver onde e como podem ser melhoradas.

### Outros Fluxos de Trabalho

Tenho então inúmeros outros fluxos de trabalho, desde a criação de candidaturas à redação de relatórios de progresso, etc.
O princípio básico é sempre o mesmo: criar um bom prompt de sistema (idealmente com a ajuda do prompt de sistema "Designer de Prompts") e depois conversar normalmente como com uma pessoa. Quanto melhor se conseguir expressar e descrever, e quanto mais claras e estruturadas forem as próprias perguntas/prompts, melhor será o resultado... é uma questão de prática e experiência.

## Modelos / API

Atualmente, utilizo apenas uma API: https://openrouter.ai/
É, em princípio, como a Netflix para modelos de linguagem.

Isto significa que posso usar todos os outros fornecedores através desta API, sem ter de obter uma API de cada um deles (e geralmente depositar pelo menos 5-10 euros). Desta forma, tenho acesso a todos e a faturação é feita através de um único fornecedor, a quem pago.
Muitos modelos no OpenRouter são também gratuitos, o que significa que o serviço pode, em princípio, ser utilizado gratuitamente.

Depois, existem modelos "gratuitos" que mudam constantemente, porque são novos, etc. (o pagamento são os seus dados, como em todos os modelos comerciais).
Atualmente utilizo muito os seguintes:

| Fornecedor | Nome do Modelo                  |
| ---------- | ------------------------------- |
| Deepseek   | Deepseek R1 (gratuito)          |
| Gemini     | gemini-2.0.-flash-exp           |
| Gemini     | gemini-2.0.-flash-thinking-exp  |
|            |                                 |

No entanto, isto também muda de vez em quando.

## Modelos Locais

Com o Msty como frontend, experimentar com modelos locais é super fácil. Eu próprio tenho atualmente um portátil de gaming de 4 anos, portanto, não é exatamente de ponta.
Tenho uma ```NVidia Geforce GTX 1050 Ti``` – que não é nada de especial pelos padrões atuais.
Modelos pequenos (1B - 2B) correm super rápido, e até 4B consigo utilizá-los. Para experimentação, já é suficiente, e alguns modelos pequenos são surpreendentemente bons atualmente, muito melhores do que o GPT3 ou 3.5 eram no início.

Por exemplo:
```
qwen2.5:7b  ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b  (1.12 GB)
```

são realmente muito bons, considerando a pouca quantidade de hardware com que se pode executar localmente.

Modelos como
```
Tiny Llama ( 600 mb )
```
são incrivelmente rápidos e provavelmente ainda funcionam num torradeira, mas a qualidade está a anos-luz de modelos maiores.

São ótimos para testar, pois os modelos inicialmente produzem mais lixo do que qualquer outra coisa (mas super rápido), e vê-se claramente a influência de bons prompts de sistema, configurações de parâmetros do modelo, etc.

## Parâmetros do Modelo

Realmente importantes são:
- Tamanho do Contexto (quanto output máximo pode ser gerado antes que o modelo pare simplesmente)
- Temperatura (dito de forma simples: para factos, mais baixo; para mais "criatividade", mais médio a alto)
