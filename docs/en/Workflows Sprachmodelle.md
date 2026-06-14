---
lang: en
translation_id: workflows-sprachmodelle
created: 2025-01-21 18:09:55
update: 2025-03-10 23:07:38
publish: true
tags: 
title: Language Model Workflows
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Workflows Sprachmodelle.md
translation_source_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-06T19:30:13+00:00
translation_source_body_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_source_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:28+00:00
translation_source_localized_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_source_structural_metadata_hash: fabd81b872924cf1e4ad2c470413d28754febce294899fe3cc4f625c2c420e80
---
## Frontend: Msty
I use the [Msty](https://msty.app) app as my frontend.

It's fundamentally free to use. There are a few features behind a paywall, but these are more convenience features, not essential functions.

Msty allows me to integrate various commercial APIs from different providers (OpenAI, Gemini, Claude, etc.) and also use local models.
The app handles all the installation aspects. You just need to choose a model from a huge database (Ollama and Huggingface), click "Install" – that's it. For commercial APIs, you just need to enter your API key.

All chats are saved locally and can be easily exported as JSON or Markdown.
Msty supports branched chats (e.g., if I regenerate an answer with changed parameters or a different model, I effectively have multiple conversation threads I can continue) and synchronized chats (automatically sending the same prompt to multiple models).

It also makes RAG incredibly easy. RAG simply means I can use various sources (like different documents, websites, YouTube links), and then relevant context from these sources is automatically added to my prompt. This is particularly useful when working with smaller, local models that don't know certain topics and tend to hallucinate amusingly. If you use RAG in such cases, the small model can suddenly provide relevant and factually correct answers on those topics. (It's not a silver bullet, though – I've always had better results with large, commercial models that have such a large context window that I can just send all the documents along).

In general, Msty also offers a simple way to manage prompts. This significantly simplifies working with more complex prompts, such as system prompts that are always included, regardless of your current prompt.

## Workflows

For the actual work, I've developed various workflows, from super simple to relatively complex. In principle, however, it's more about experimenting a lot; there's no "one-size-fits-all" solution.

Here are a few examples of workflows I use:

### General Prompt Creation

For most non-trivial tasks, a good system prompt can turn a "so-so" result into a "good to very good" one.

My current system prompt for creating new prompts is:
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

It's best to use this with a large model (see [[Seedbox/Workflows Sprachmodelle#Modelle|Models]]).
Generally, the output quality is slightly better when everything is done in English. However, most large models are quite good with German now. It also doesn't hurt if you mix languages, as long as it remains clearly understandable. So, I can do everything in English first and then simply ask for a German output at the end. But that's more like fine-tuning...

In principle, it then works like a normal chatbot, so you can definitely "talk normally."

""
```
I think I need a prompt like this, I want a chatbot that helps me with my homework.
```

Often, this also leads to "follow-up questions," meaning the model will ask for additional information, depending on how precisely you described it beforehand. I just want to say: If you use large models like those from OpenAI, Google, etc., any beginner can use them; no special format or syntax is required.

Generally, I do this when I'm working on something repeatedly, meaning I have similar or the same tasks over and over again. Then I build a system prompt (or a user prompt) – it's more like a template that I can then simply insert.

### Evaluate / Improve Application

1. Relevant documents (i.e., funding conditions, formats, etc... usually about 3-4 PDFs, depending on the funding) and the finished application text.
2. For this, I currently use ```gemini-2.0.-flash-exp``` because it allows for 1 million tokens of context – more than enough to attach 100 pages of PDFs.
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

4. Then simply attach the PDFs to the chat; that's usually enough.
5. This is incredibly helpful for critically evaluating your own applications and seeing where and how you can improve them.

### Other Workflows

I have many other workflows, from creating applications to writing progress reports, etc.
The basic principle is always the same: create a good system prompt (ideally with the help of the "Prompt Designer" system prompt) and then chat normally as you would with a person. The better you can express and describe yourself, and the clearer and more structured your questions/prompts are, the better the result will be... it's a matter of practice and experience.

## Models / API

I now only use one API: https://openrouter.ai/
It's basically like Netflix for language models.

This means I can use all other providers through this API without having to get an API from each one individually (and usually having to deposit at least 5-10 Euros). This way, I have access to all of them, and billing is handled through a single provider that I pay.
Many models on OpenRouter are also free, meaning you can fundamentally use the service for free.

Then there are constantly changing "free" models because they are new, etc. (the payment is then your data, as with all commercial models).
I'm currently using the following a lot:

| Provider | Model Name                     |
| -------- | ------------------------------ |
| Deepseek | Deepseek R1 (free)             |
| Gemini   | gemini-2.0.-flash-exp          |
| Gemini   | gemini-2.0.-flash-thinking-exp |
|          |                                |

However, this changes from time to time.

## Local Models

With Msty as the frontend, experimenting with local models is super easy. I currently have a 4-year-old gaming laptop, so it's not exactly high-end.
I have an ```NVidia Geforce GTX 1050 Ti``` – which isn't really great by today's standards.
Small models (1B - 2B) run super fast, and I can still use them up to 4B. But it's more than enough for experimenting, and some small models are surprisingly good now, much better than GPT3 or 3.5 were at the beginning.

For example:
```
qwen2.5:7b  ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b  (1.12 GB)
```

are already quite good, considering how little hardware you need to run them locally.

Models like
```
Tiny Llama ( 600 mb )
```
are incredibly fast and probably run on a toaster, but their quality is light-years away from larger models.

They are great for testing, though, as the models initially spit out more garbage than anything else (but super fast), and you can clearly see the influence of good system prompts, model parameter settings, etc.

## Model Parameters

Really important are:
- Context Size (how much output can be generated at maximum before the model simply stops)
- Temperature (simply put: low for facts, medium to high for more "creativity")
