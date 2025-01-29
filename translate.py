import os
import shutil
import argparse
import logging
import time
import re
from dotenv import load_dotenv

from markdown_it import MarkdownIt
from markdown_it.rules_inline import StateInline
from markdown_it.rules_block import StateBlock
from deepl import Translator

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_translatable_text(markdown_text):
    """
    Extracts translatable text from markdown, preserving structure.

    Returns:
        A tuple: (list of text chunks, list of markdown tokens, list of text types, list of original text)
    """
    md = MarkdownIt()
    tokens = md.parse(markdown_text)
    translatable_texts = []
    translatable_tokens = []
    translatable_types = []
    original_texts = []

    for token in tokens:
        if token.type == 'text' and token.content.strip():
            # Check if the text is inside a code block
            if any(t.type == 'code_block' for t in tokens if t.level < token.level):
                continue

            # Check if the text is inside an inline code block
            if any(t.type == 'code_inline' for t in tokens if t.level < token.level):
                continue
            
             # Check if the text is within an HTML tag.
            if any(t.type == 'html_block' or t.type == 'html_inline' for t in tokens if t.level < token.level):
                continue
            
            # Check if the text is within a blockquote
            if any(t.type == 'blockquote_open' for t in tokens if t.level < token.level):
                translatable_texts.append(token.content)
                translatable_tokens.append(token)
                translatable_types.append('blockquote')
                original_texts.append(token.content)
                continue
            
            # Check if the text is within an image alt text
            if token.type == 'text' and any(t.type == 'image' for t in tokens if t.level < token.level):
                translatable_texts.append(token.content)
                translatable_tokens.append(token)
                translatable_types.append('image_alt')
                original_texts.append(token.content)
                continue

            # Check if the text is within a link text
            if any(t.type == 'link_open' for t in tokens if t.level < token.level):
                 translatable_texts.append(token.content)
                 translatable_tokens.append(token)
                 translatable_types.append('link_text')
                 original_texts.append(token.content)
                 continue
            
            #Check if text is within a button
            if any(t.type == 'text' and t.content.endswith('{.md-button}') for t in tokens if t.level < token.level):
                 translatable_texts.append(token.content.replace('{.md-button}', ''))
                 translatable_tokens.append(token)
                 translatable_types.append('button_text')
                 original_texts.append(token.content)
                 continue
            
            #Check if text is within a table cell
            if any(t.type == 'td_open' for t in tokens if t.level < token.level):
                 translatable_texts.append(token.content)
                 translatable_tokens.append(token)
                 translatable_types.append('table_cell')
                 original_texts.append(token.content)
                 continue

            #Check if text is within a table header cell
            if any(t.type == 'th_open' for t in tokens if t.level < token.level):
                 translatable_texts.append(token.content)
                 translatable_tokens.append(token)
                 translatable_types.append('table_header_cell')
                 original_texts.append(token.content)
                 continue

            #Otherwise it is a paragraph or heading
            translatable_texts.append(token.content)
            translatable_tokens.append(token)
            translatable_types.append('paragraph_heading')
            original_texts.append(token.content)

        #Handle button syntax
        if token.type == 'text' and token.content.endswith('{.md-button}'):
            translatable_texts.append(token.content.replace('{.md-button}', ''))
            translatable_tokens.append(token)
            translatable_types.append('button_text')
            original_texts.append(token.content)
        
        #Handle link titles (wikilinks, and normal links)
        if token.type == 'link_open' and token.content:
             # Handle link titles in the format [[link|title]]
            match = re.match(r'\[\[[^|]+\|([^\]]+)\]\]', token.content)
            if match:
                translatable_texts.append(match.group(1))
                translatable_tokens.append(token)
                translatable_types.append('link_title')
                original_texts.append(match.group(1))
                continue

            # Handle link titles in the format [text](url "title")
            match = re.search(r'"([^"]+)"\)$', token.content)
            if match:
                translatable_texts.append(match.group(1))
                translatable_tokens.append(token)
                translatable_types.append('link_title')
                original_texts.append(match.group(1))
                continue
    return translatable_texts, translatable_tokens, translatable_types, original_texts

def replace_translated_text(markdown_text, translated_texts, translatable_tokens, translatable_types, original_texts):
    """Replaces original text with translated text, preserving markdown structure."""
    md = MarkdownIt()
    tokens = md.parse(markdown_text)
    translated_markdown = ""
    original_text_index = 0 # Track the index of the original text being translated

    for token in tokens:
        if token.type == 'text' and token.content.strip():
            #Check if the text is inside a code block
            if any(t.type == 'code_block' for t in tokens if t.level < token.level):
                translated_markdown += token.content
                continue
            # Check if the text is inside an inline code block
            if any(t.type == 'code_inline' for t in tokens if t.level < token.level):
                translated_markdown += token.content
                continue
            
            # Check if the text is within an HTML tag.
            if any(t.type == 'html_block' or t.type == 'html_inline' for t in tokens if t.level < token.level):
                translated_markdown += token.content
                continue

            # Check if the text is within a blockquote
            if any(t.type == 'blockquote_open' for t in tokens if t.level < token.level):
                if translatable_types[original_text_index] == 'blockquote':
                    translated_markdown += translated_texts[original_text_index]
                    original_text_index += 1
                    continue
                else:
                   translated_markdown += token.content
                   continue
            
            # Check if the text is within an image alt text
            if token.type == 'text' and any(t.type == 'image' for t in tokens if t.level < token.level):
                if translatable_types[original_text_index] == 'image_alt':
                    translated_markdown += translated_texts[original_text_index]
                    original_text_index += 1
                    continue
                else:
                    translated_markdown += token.content
                    continue

            # Check if the text is within a link text
            if any(t.type == 'link_open' for t in tokens if t.level < token.level):
                if translatable_types[original_text_index] == 'link_text':
                    translated_markdown += translated_texts[original_text_index]
                    original_text_index += 1
                    continue
                else:
                   translated_markdown += token.content
                   continue

            #Check if text is within a button
            if any(t.type == 'text' and t.content.endswith('{.md-button}') for t in tokens if t.level < token.level):
                if translatable_types[original_text_index] == 'button_text':
                    translated_markdown += translated_texts[original_text_index]
                    original_text_index += 1
                    continue
                else:
                    translated_markdown += token.content
                    continue

            #Check if text is within a table cell
            if any(t.type == 'td_open' for t in tokens if t.level < token.level):
                if translatable_types[original_text_index] == 'table_cell':
                    translated_markdown += translated_texts[original_text_index]
                    original_text_index += 1
                    continue
                else:
                    translated_markdown += token.content
                    continue
            
            #Check if text is within a table header cell
            if any(t.type == 'th_open' for t in tokens if t.level < token.level):
                if translatable_types[original_text_index] == 'table_header_cell':
                    translated_markdown += translated_texts[original_text_index]
                    original_text_index += 1
                    continue
                else:
                    translated_markdown += token.content
                    continue
            
            #Otherwise it is a paragraph or heading
            if translatable_types[original_text_index] == 'paragraph_heading':
                translated_markdown += translated_texts[original_text_index]
                original_text_index += 1
                continue
            else:
                 translated_markdown += token.content
                 continue

        #Handle button syntax
        if token.type == 'text' and token.content.endswith('{.md-button}'):
             if translatable_types[original_text_index] == 'button_text':
                translated_markdown += translated_texts[original_text_index] + '{.md-button}'
                original_text_index += 1
                continue
             else:
                 translated_markdown += token.content
                 continue
        
        #Handle link titles
        if token.type == 'link_open' and token.content:
             # Handle link titles in the format [[link|title]]
            match = re.match(r'\[\[[^|]+\|([^\]]+)\]\]', token.content)
            if match:
                if translatable_types[original_text_index] == 'link_title':
                    translated_markdown += f'[[{token.content.split("|")[0].replace("[[","")}'+f'|{translated_texts[original_text_index]}]]'
                    original_text_index += 1
                    continue
                else:
                    translated_markdown += token.content
                    continue

            # Handle link titles in the format [text](url "title")
            match = re.search(r'"([^"]+)"\)$', token.content)
            if match:
                 if translatable_types[original_text_index] == 'link_title':
                     translated_markdown += token.content.replace(f'"{original_texts[original_text_index]}"', f'"{translated_texts[original_text_index]}"')
                     original_text_index += 1
                     continue
                 else:
                     translated_markdown += token.content
                     continue
        
        translated_markdown += token.content
    return translated_markdown

def translate_text(text_chunks, target_lang, api_key):
    """Translates text chunks using the Deepl API.
       If no API key is provided, it returns the original text."""
    if not api_key:
        logging.warning("No Deepl API key provided. Returning original text for testing.")
        return text_chunks  # Return original text if no API key
    
    translator = Translator(api_key)
    try:
        result = translator.translate_text(text_chunks, target_lang=target_lang)
        translated_texts = [r.text for r in result]
        return translated_texts
    except Exception as e:
        logging.error(f"Deepl API error: {e}")
        return None

def process_markdown_file(input_file, output_file, target_lang, api_key):
    """Processes a single markdown file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
    except Exception as e:
        logging.error(f"Error reading file {input_file}: {e}")
        return

    #Check if the file has YAML frontmatter
    yaml_match = re.match(r'^---\n(.*?)\n---', markdown_text, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(0)
        markdown_text = markdown_text[len(yaml_content):] #remove the YAML frontmatter for processing
    else:
        yaml_content = ""

    translatable_texts, translatable_tokens, translatable_types, original_texts = extract_translatable_text(markdown_text)

    if not translatable_texts:
        logging.info(f"No translatable text found in {input_file}")
        # Copy file if no text to translate
        if yaml_content:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(yaml_content + markdown_text)
        else:
            shutil.copy2(input_file, output_file)
        return

    translated_texts = translate_text(translatable_texts, target_lang, api_key)

    if translated_texts:
        translated_markdown = replace_translated_text(markdown_text, translated_texts, translatable_tokens, translatable_types, original_texts)

        # Add YAML frontmatter back if present
        if yaml_content:
            translated_markdown = yaml_content + translated_markdown

        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(translated_markdown)
            logging.info(f"Translated: {input_file} -> {output_file}")
        except Exception as e:
            logging.error(f"Error writing to file {output_file}: {e}")
    else:
        logging.error(f"Translation failed for {input_file}")


def main():
    parser = argparse.ArgumentParser(description="Translate markdown files using the Deepl API.")
    parser.add_argument("--input-dir", required=True, help="Path to the input directory containing markdown files.")
    parser.add_argument("--output-dir", required=True, help="Path to the output directory for translated files.")
    parser.add_argument("--target-lang", required=True, help="Target language code (e.g., en, fr, es).")
    parser.add_argument("--deepl-api-key", default=os.getenv('DEEPL_API_KEY'), help="Your Deepl API key.")

    args = parser.parse_args()

    if not args.deepl_api_key:
        logging.error("Deepl API key is missing. Please provide it as an argument or set the DEEPL_API_KEY environment variable.")
        return

    for root, _, files in os.walk(args.input_dir):
        for file in files:
            if file.lower().endswith(('.md', '.markdown')):
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(input_file, args.input_dir)
                output_file = os.path.join(args.output_dir, relative_path)

                # Create output directory if it doesn't exist
                os.makedirs(os.path.dirname(output_file), exist_ok=True)

                process_markdown_file(input_file, output_file, args.