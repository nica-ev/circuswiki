from __future__ import annotations

from pathlib import Path

from core.llm import chat_completion, chat_message_content, strip_code_fences
from dynamic.blocks import parse_dynamic_blocks
from dynamic.workflow import render_block

from . import link_repair
from .config import DEFAULT_CONTEXT_DESCRIPTION, language_name


def translate_markdown_segment(
    segment: str,
    source_lang: str,
    target_lang: str,
    model: str,
    prompt: str | None,
) -> tuple[str, link_repair.LinkRepairResult]:
    if not segment.strip():
        return segment, link_repair.LinkRepairResult(body=segment, changed=False, repair_count=0, diagnostics=[])

    translated = call_translation_model(
        body=segment,
        source_lang=source_lang,
        target_lang=target_lang,
        model=model,
        prompt=prompt,
    )
    repair_result = link_repair.repair_link_targets(segment, translated)
    return repair_result.body, repair_result


def translate_body(
    source_body: str,
    target_path: Path,
    source_lang: str,
    target_lang: str,
    model: str,
    prompt: str | None,
) -> tuple[str, link_repair.LinkRepairResult, list[dict[str, object]]]:
    blocks = parse_dynamic_blocks(source_body)
    if not blocks:
        translated_body, link_result = translate_markdown_segment(
            source_body,
            source_lang=source_lang,
            target_lang=target_lang,
            model=model,
            prompt=prompt,
        )
        return translated_body, link_result, []

    pieces: list[str] = []
    cursor = 0
    repair_count = 0
    diagnostics: list[link_repair.LinkRepairDiagnostic] = []
    dynamic_results: list[dict[str, object]] = []

    for block in blocks:
        translated_segment, segment_result = translate_markdown_segment(
            source_body[cursor:block.start],
            source_lang=source_lang,
            target_lang=target_lang,
            model=model,
            prompt=prompt,
        )
        pieces.append(translated_segment)
        repair_count += segment_result.repair_count
        diagnostics.extend(segment_result.diagnostics)

        pieces.append(source_body[block.start:block.content_start])
        block_result = render_block(target_path, block)
        dynamic_results.append(block_result)
        if not block_result.get("ok"):
            errors = ", ".join(str(error) for error in block_result.get("errors", []))
            raise RuntimeError(f"Dynamic block {block.index} render failed for {target_path}: {errors}")
        pieces.append(str(block_result["markdown"]).strip("\n"))
        pieces.append("\n\n")
        pieces.append(source_body[block.content_end:block.end])
        cursor = block.end

    translated_tail, tail_result = translate_markdown_segment(
        source_body[cursor:],
        source_lang=source_lang,
        target_lang=target_lang,
        model=model,
        prompt=prompt,
    )
    pieces.append(translated_tail)
    repair_count += tail_result.repair_count
    diagnostics.extend(tail_result.diagnostics)

    translated_body = "".join(pieces)
    return (
        translated_body,
        link_repair.LinkRepairResult(
            body=translated_body,
            changed=repair_count > 0,
            repair_count=repair_count,
            diagnostics=diagnostics,
        ),
        dynamic_results,
    )


def restore_internal_link_targets(source_body: str, translated_body: str) -> str:
    return link_repair.restore_internal_link_targets(source_body, translated_body)


def restore_markdown_link_targets(source_body: str, translated_body: str) -> str:
    return link_repair.restore_markdown_link_targets(source_body, translated_body)


def restore_wikilink_targets(source_body: str, translated_body: str) -> str:
    return link_repair.restore_wikilink_targets(source_body, translated_body)


def is_local_markdown_target(target: str) -> bool:
    return link_repair.is_local_markdown_target(target)


def wikilink_target(body: str) -> str:
    return link_repair.wikilink_target(body)


def wikilink_alias(body: str) -> str:
    return link_repair.wikilink_alias(body)


def call_translation_model(body: str, source_lang: str, target_lang: str, model: str, prompt: str | None = None) -> str:
    system_prompt = render_prompt(prompt, source_lang, target_lang)
    data = chat_completion(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": body},
        ],
        title="CircusWiki Translation Console",
    )
    content = chat_message_content(data, "translation")
    return strip_code_fences(content).strip() + "\n"


def default_prompt(source_lang: str, target_lang: str) -> str:
    return render_prompt(None, source_lang, target_lang)


def default_prompt_template() -> str:
    return """You are an expert {source_language}-to-{target_language} translator and localization specialist. Your mission is to translate {source_language} text into {target_language} that is not just grammatically correct, but also completely natural, idiomatic, and clear, as if it were originally written by a native {target_language} speaker for a {target_language} audience.

Guiding Principles:
1. **Clarity is paramount.** The reader must understand the text's meaning and intent without any confusion.
2. **Natural flow over literal accuracy.** You must restructure sentences and choose different words to make the text sound natural in {target_language}.
3. **Context is key.** You must understand the purpose of the text (e.g., game rules, marketing copy, technical description) and adapt your translation accordingly. The context for this text is: {context_description}

Strict Translation Rules:
1. **AVOID "SOURCE-ISMS":** You must actively identify and eliminate calques (word-for-word translations of {source_language} structures). Do not mirror {source_language} sentence structure, word order, or unique grammatical features. Rephrase the entire idea using natural {target_language} syntax.
2. **LOGICAL INFERENCE FOR INSTRUCTIONS:** When translating instructions, rules, or procedures, you must validate their logic. If a literal translation results in a nonsensical or illogical instruction in {target_language}, you are required to infer the true, logical intent and translate that intent instead.
3. **USE ACTIVE & IDIOMATIC VERBS:** Prefer natural {target_language} verbal constructions over awkward noun phrases common in literal translations. For example, a direct translation might produce a clunky noun phrase, but the goal is to find the fluid, verb-centric equivalent in {target_language}.
4. **ADAPT IDIOMS:** Never translate {source_language} idioms or colloquialisms literally. Find the closest functional equivalent in {target_language} or rephrase the meaning plainly if no direct equivalent exists.

Markdown and Structure Rules:
1. Return only translated Markdown body content.
2. Preserve Markdown structure, headings, tables, admonitions, comments, code blocks, links, image links, and Obsidian wikilinks.
3. Translate natural language text only.
4. Do not translate file names, URLs, anchors, image paths, YAML, HTML attributes, IDs, placeholders, or code.
5. Keep formatting intact.

Output Format Constraint:
Your response MUST contain ONLY the final, translated {target_language} text. Do not include any titles, headers, notes, explanations, or any other text before or after the translation. Your entire output is the translation itself."""


def render_prompt(prompt: str | None, source_lang: str, target_lang: str) -> str:
    template = prompt or default_prompt_template()
    source_language = language_name(source_lang)
    target_language = language_name(target_lang)
    replacements = {
        "{source_lang}": source_lang,
        "{target_lang}": target_lang,
        "{source_language}": source_language,
        "{target_language}": target_language,
        "{SOURCE_LANGUAGE}": source_language,
        "{TARGET_LANGUAGE}": target_language,
        "{{SOURCE_LANGUAGE}}": source_language,
        "{{TARGET_LANGUAGE}}": target_language,
        "{context_description}": DEFAULT_CONTEXT_DESCRIPTION,
        "{CONTEXT_DESCRIPTION}": DEFAULT_CONTEXT_DESCRIPTION,
        "{{CONTEXT_DESCRIPTION}}": DEFAULT_CONTEXT_DESCRIPTION,
    }
    rendered = template
    for placeholder, value in replacements.items():
        rendered = rendered.replace(placeholder, value)
    return rendered
