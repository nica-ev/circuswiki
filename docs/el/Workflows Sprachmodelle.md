---
lang: el
translation_id: workflows-sprachmodelle
created: 2025-01-21 18:09:55
update: 2025-03-10 23:07:38
publish: true
tags: 
title: Ροές εργασίας γλωσσικών μοντέλων
description: 
authors:
  - Marc Bielert
translation_status: machine-translated
translation_source_lang: de
translation_source: docs/de/Workflows Sprachmodelle.md
translation_source_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_model: google/gemini-2.5-flash-lite
translation_updated: 2026-06-07T13:56:32+00:00
translation_source_body_hash: f29637995eb7abf2230ea93ecf6f6b5bcb9e58876dd94b41aff9b588fc9d9d6a
translation_source_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_metadata_model: google/gemini-2.5-flash-lite
translation_metadata_status: machine-translated
translation_metadata_updated: 2026-06-14T16:27:31+00:00
translation_source_localized_metadata_hash: e40faf3144a04df85cb6b4d640d09cd517d51971ce4b223b43e7fac8cf0e8385
translation_source_structural_metadata_hash: fabd81b872924cf1e4ad2c470413d28754febce294899fe3cc4f625c2c420e80
---
## Frontend: Msty
Ως frontend χρησιμοποιώ την εφαρμογή [Msty](https://msty.app).

Είναι κατά βάση πλήρως δωρεάν στη χρήση. Υπάρχουν μερικά ελάχιστα χαρακτηριστικά που βρίσκονται πίσω από paywall, αλλά αυτά είναι περισσότερο θέματα ευκολίας, όχι βασικές λειτουργίες.

Το Msty μου επιτρέπει να ενσωματώνω διάφορα εμπορικά APIs από διαφορετικούς παρόχους (OpenAI, Gemini, Claude, κ.λπ.) και επίσης να χρησιμοποιώ τοπικά μοντέλα.
Η εφαρμογή αναλαμβάνει ουσιαστικά τα πάντα σχετικά με την εγκατάσταση. Είναι πραγματικά απλό: επιλέγεις ένα μοντέλο από μια τεράστια βάση δεδομένων (Ollama και Huggingface), κάνεις κλικ στο "Εγκατάσταση" – αυτό ήταν. Για τα εμπορικά APIs, απλώς πρέπει να εισαγάγεις το API key.

Όλες οι συνομιλίες αποθηκεύονται τοπικά και μπορούν εύκολα να εξαχθούν ως JSON ή Markdown.
Το Msty υποστηρίζει διακλαδούμενες συνομιλίες (δηλαδή, αν για παράδειγμα ξαναδημιουργήσω μια απάντηση με τροποποιημένες παραμέτρους ή με διαφορετικό μοντέλο, έχω ουσιαστικά πολλαπλές ροές συνομιλίας που μπορώ να συνεχίσω) και συγχρονισμένες συνομιλίες (αυτόματη αποστολή του ίδιου prompt σε πολλαπλά μοντέλα).

Επιπλέον, κάνει το RAG (Retrieval-Augmented Generation) εξαιρετικά εύκολο. RAG σημαίνει απλώς ότι μπορώ να χρησιμοποιήσω διάφορες πηγές (όπως διαφορετικά έγγραφα, ιστοσελίδες, συνδέσμους YouTube) και στη συνέχεια προστίθεται αυτόματα σχετικό περιεχόμενο από αυτές τις πηγές στο prompt μου. Αυτό είναι ιδιαίτερα χρήσιμο όταν εργάζομαι με μικρότερα, τοπικά μοντέλα που απλώς δεν γνωρίζουν συγκεκριμένα θέματα και στη συνέχεια "παραισθάνονται" αστεία. Χρησιμοποιώντας RAG σε τέτοιες περιπτώσεις, το μικρό μοντέλο μπορεί ξαφνικά να παρέχει σχετικές και πραγματικά ακριβείς απαντήσεις σε αυτά τα θέματα. (Ωστόσο, δεν είναι πανάκεια – μέχρι στιγμής είχα πάντα καλύτερα αποτελέσματα με μεγάλα, εμπορικά μοντέλα που έχουν τόσο μεγάλο παράθυρο περιεχομένου που μπορώ απλώς να στείλω όλα τα έγγραφα μαζί τους).

Γενικά, το Msty προσφέρει επίσης έναν απλό τρόπο διαχείρισης των prompts. Αυτό απλοποιεί σημαντικά την εργασία με πιο σύνθετα prompts, όπως τα system prompts, τα οποία αποστέλλονται πάντα, ανεξάρτητα από το τρέχον prompt σας.

## Ροές Εργασίας (Workflows)

Για την πραγματική εργασία, έχω πλέον αναπτύξει διάφορες ροές εργασίας, από πολύ απλές έως σχετικά σύνθετες. Κατ' αρχήν, όμως, είναι περισσότερο έτσι: πολύ πειραματισμός, και δεν υπάρχει λύση "μία για όλα".

Εδώ είναι μερικά παραδείγματα ροών εργασίας που χρησιμοποιώ:

### Γενική Δημιουργία Prompt

Για τις περισσότερες μη τετριμμένες εργασίες, ένα καλό system prompt μετατρέπει ένα αποτέλεσμα "έτσι κι έτσι" σε "καλό έως πολύ καλό".

Το τρέχον system prompt μου για τη δημιουργία νέων prompts είναι:
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

Καλύτερα να το χρησιμοποιείς με ένα μεγάλο μοντέλο (βλ. [[Seedbox/Workflows Sprachmodelle#Modelle|Μοντέλα]]).
Κατ' αρχήν, η ποιότητα του αποτελέσματος είναι πάντα λίγο καλύτερη αν τα κάνεις όλα στα Αγγλικά. Τα περισσότερα μεγάλα μοντέλα, όμως, είναι πλέον αρκετά καλά και με τα Γερμανικά. Δεν πειράζει ούτε αν ανακατεύεις γλώσσες, αρκεί να παραμένει σαφώς κατανοητό. Μπορώ λοιπόν αρχικά να τα κάνω όλα στα Αγγλικά και μετά στο τέλος απλώς να ζητήσω μια έξοδο στα Γερμανικά. Αλλά αυτό είναι ήδη περισσότερο λεπτομερής ρύθμιση…

Στην ουσία, λειτουργεί σαν ένα κανονικό chatbot, οπότε μπορείς να μιλάς "κανονικά".

""
```
Νομίζω ότι χρειάζομαι ένα τέτοιο prompt, δηλαδή θέλω ένα chatbot που να κάνει μαζί μου τις εργασίες μου και να με βοηθάει εκεί.
```

Συχνά, τέτοιες απαντήσεις οδηγούν και σε "διευκρινίσεις", δηλαδή το μοντέλο ρωτάει για επιπλέον πληροφορίες, ανάλογα με το πόσο ακριβώς το έχεις περιγράψει προηγουμένως. Θέλω απλώς να πω: Αν χρησιμοποιείς μεγάλα μοντέλα όπως αυτά της OpenAI, Google κ.λπ., τότε μπορεί να τα χρησιμοποιήσει οποιοσδήποτε αρχάριος, δεν χρειάζεται ιδιαίτερη μορφή ή σύνταξη.

Γενικά, το κάνω αυτό όταν δουλεύω συχνά σε κάτι, δηλαδή όταν έχω συνεχώς παρόμοιες ή ίδιες εργασίες. Τότε φτιάχνω ένα τέτοιο system prompt (ή και user prompt) – αυτό είναι περισσότερο σαν ένα πρότυπο που μπορώ απλώς να εισάγω.

### Αξιολόγηση / Βελτίωση Αίτησης

1. Σχετικά έγγραφα (δηλαδή όροι επιχορήγησης, μορφές κ.λπ. ... συνήθως 3-4 PDF, ανάλογα με την επιχορήγηση) καθώς και το κείμενο της ολοκληρωμένης αίτησης.
2. Για αυτό, χρησιμοποιώ αυτήν τη στιγμή το ```gemini-2.0.-flash-exp```, καθώς επιτρέπει 1 εκατομμύριο tokens περιεχομένου – υπεραρκετό για να επισυνάψεις 100 σελίδες PDF.
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

4. Στη συνέχεια, απλώς επισυνάπτετε τα PDF στη συνομιλία, αυτό συνήθως αρκεί.
5. Αυτό βοηθάει απίστευτα στην κριτική αξιολόγηση των δικών σας αιτήσεων και στο να δείτε πού και πώς μπορείτε να τις βελτιώσετε περαιτέρω.

### Άλλες Ροές Εργασίας

Έχω μετά άπειρες άλλες ροές εργασίας, από τη δημιουργία αιτήσεων μέχρι τη συγγραφή εκθέσεων προόδου κ.λπ.
Η βασική αρχή, όμως, είναι πάντα η ίδια: δημιουργία ενός καλού system prompt (ιδανικά με τη βοήθεια του system prompt "Promptdesigner") και στη συνέχεια συνομιλία κανονικά, σαν να μιλάς με άνθρωπο. Όσο καλύτερα μπορείς να εκφραστείς και να περιγράψεις, και όσο πιο σαφείς και δομημένες είναι οι δικές σου ερωτήσεις/prompts, τόσο καλύτερο είναι και το αποτέλεσμα… είναι λίγο θέμα εξάσκησης και εμπειρίας.

## Μοντέλα / API

Χρησιμοποιώ πλέον μόνο ένα API: https://openrouter.ai/
Είναι ουσιαστικά σαν το Netflix για τα γλωσσικά μοντέλα.

Αυτό σημαίνει ότι μπορώ να χρησιμοποιήσω όλους τους άλλους παρόχους μέσω αυτού του API, χωρίς να χρειάζεται να αποκτήσω API από τον καθένα ξεχωριστά (και συνήθως να καταθέσω τουλάχιστον 5-10 ευρώ). Έτσι, έχω πρόσβαση σε όλα και η χρέωση γίνεται μέσω ενός μόνο παρόχου, στον οποίο πληρώνω.
Πολλά μοντέλα στο OpenRouter είναι επίσης δωρεάν, δηλαδή μπορείτε ουσιαστικά να χρησιμοποιήσετε την υπηρεσία δωρεάν.

Στη συνέχεια, υπάρχουν συνεχώς εναλλασσόμενα "δωρεάν" μοντέλα, επειδή είναι νέα κ.λπ. (η πληρωμή είναι τότε τα δεδομένα σας, όπως σε όλα τα εμπορικά μοντέλα).
Τα παρακάτω χρησιμοποιώ αυτήν τη στιγμή πολύ:

| Πάροχος | Όνομα Μοντέλου                 |
| -------- | ------------------------------ |
| Deepseek | Deepseek R1 (free)             |
| Gemini   | gemini-2.0.-flash-exp          |
| Gemini   | gemini-2.0.-flash-thinking-exp |
|          |                                |

Αυτό, όμως, αλλάζει και κατά καιρούς.

## Τοπικά Μοντέλα

Με το Msty ως frontend, το πειραματισμός με τοπικά μοντέλα είναι εξαιρετικά εύκολος. Εγώ ο ίδιος έχω αυτήν τη στιγμή ένα gaming laptop 4 ετών, δηλαδή όχι ακριβώς high-end.
Έχω μια ```NVidia Geforce GTX 1050 Ti``` – αυτό δεν είναι τίποτα σπουδαίο με τα σημερινά δεδομένα.
Μικρά μοντέλα (1B - 2B) τρέχουν σούπερ γρήγορα, και μέχρι 4B μπορώ ακόμα να τα χρησιμοποιήσω. Για πειραματισμό, όμως, αρκεί απόλυτα, και μερικά μικρά μοντέλα είναι πλέον εκπληκτικά καλά, πολύ καλύτερα από ό,τι ήταν αρχικά το GPT3 ή το 3.5.

π.χ.
```
qwen2.5:7b  ( 4.5 GB )
llama 3.2 (2 GB)
deepseek-r1:1.5b  (1.12 GB)
```

είναι πραγματικά ήδη αρκετά καλά, αν σκεφτείς πόσο λίγο υλικό χρειάζεται για να τα εκτελέσεις τοπικά.

Μοντέλα όπως
```
Tiny Llama ( 600 mb )
```
είναι απίστευτα γρήγορα και πιθανότατα τρέχουν ακόμα και σε μια τοστιέρα, αλλά η ποιότητα είναι έτη φωτός μακριά από μεγαλύτερα μοντέλα.

Για δοκιμές, όμως, είναι υπέροχα, καθώς τα μοντέλα αρχικά βγάζουν περισσότερα σκουπίδια παρά οτιδήποτε άλλο (αλλά σούπερ γρήγορα), και βλέπεις πολύ καθαρά την επίδραση των καλών system prompts, των ρυθμίσεων παραμέτρων του μοντέλου κ.λπ.

## Παράμετροι Μοντέλου

Πραγματικά σημαντικές είναι:
- Μέγεθος Περιεχομένου (πόσο μέγιστο output μπορεί να παραχθεί πριν το μοντέλο απλώς σταματήσει)
- Θερμοκρασία (απλά το πούμε: για γεγονότα μάλλον χαμηλά, για περισσότερη "δημιουργικότητα" μάλλον μέτρια έως υψηλά)
