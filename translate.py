import os
import shutil
import argparse
import logging
import re
from dotenv import load_dotenv
from markdown_it import MarkdownIt

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class MarkdownTranslator:
    def __init__(self, input_dir, output_dir, target_lang, api_key):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.target_lang = target_lang.upper()
        self.api_key = api_key
        self.translated_files = 0
        self.skipped_files = 0
        self.testing_mode = not api_key
        self.text_log = open("translation_log.txt", "w", encoding="utf-8") if self.testing_mode else None
        self.wikilink_pattern = re.compile(r'\[\[(.*?)\]\]')

    def extract_translatable_text(self, markdown_text):
        md = MarkdownIt()
        tokens = md.parse(markdown_text)
        translatable = []
        in_code = False

        for token in tokens:
            if token.type in ["code_block", "fence"]:
                in_code = not in_code
                continue
            if in_code:
                continue

            # Process inline tokens and their children
            if token.type == "inline" and token.children:
                for child in token.children:
                    if child.type == "text":
                        # Extract wikilinks from text content
                        wikilinks = self.wikilink_pattern.findall(child.content)
                        for link in wikilinks:
                            title = link.split("|")[0] if "|" in link else link
                            translatable.append(('link_title', title.strip()))
                        
                        # Handle remaining text after removing wikilinks
                        remaining_text = self.wikilink_pattern.sub('', child.content).strip()
                        if remaining_text:
                            translatable.append(('text', remaining_text))

            # Handle standard markdown links
            elif token.type == "link_open" and "title" in token.attrs:
                translatable.append(('link_title', token.attrs["title"]))

            # Handle standalone text tokens
            elif token.type == "text" and token.content.strip():
                translatable.append(('text', token.content.strip()))

        logging.debug(f"Found {len(translatable)} translatable segments")
        return translatable

    def translate_text(self, text_blocks):
        if self.testing_mode:
            for ttype, text in text_blocks:
                self.text_log.write(f"{ttype.upper()}: {text}\n")
            return [(ttype, text) for ttype, text in text_blocks]
        return text_blocks

    def replace_translated_text(self, original, translations):
        translated = original
        translation_iter = iter(translations)
        
        def replace_wikilink(match):
            try:
                original_content = match.group(1)
                if "|" in original_content:
                    title_part, rest = original_content.split("|", 1)
                    translated_title = next(t for t in translation_iter if t[0] == 'link_title')[1]
                    return f"[[{translated_title}|{rest}]]"
                else:
                    translated_title = next(t for t in translation_iter if t[0] == 'link_title')[1]
                    return f"[[{translated_title}]]"
            except (StopIteration, IndexError):
                return match.group(0)

        # Replace wikilinks first
        translated = self.wikilink_pattern.sub(replace_wikilink, translated)
        
        # Replace remaining text content
        for (ttype, orig), (_, new) in zip(self.extract_translatable_text(original), translations):
            if ttype == 'text':
                translated = translated.replace(orig, new, 1)
        
        return translated

    def process_markdown_file(self, input_path, output_path):
        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

            yaml_front = re.match(r'^---\n.*?\n---\n', content, re.DOTALL)
            body = content[len(yaml_front.group(0)):] if yaml_front else content

            translatable = self.extract_translatable_text(body)
            if not translatable:
                shutil.copyfile(input_path, output_path)
                self.skipped_files += 1
                logging.debug(f"Skipped {input_path} - no translatable content")
                return

            translated = self.translate_text(translatable)
            new_body = self.replace_translated_text(body, translated)

            with open(output_path, 'w', encoding='utf-8') as f:
                if yaml_front:
                    f.write(yaml_front.group(0))
                f.write(new_body)

            self.translated_files += 1

        except Exception as e:
            logging.error(f"Error processing {input_path}: {str(e)}")
            self.skipped_files += 1

    def run(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        for root, _, files in os.walk(self.input_dir):
            for file in files:
                if file.lower().endswith(('.md', '.markdown')):
                    input_path = os.path.join(root, file)
                    rel_path = os.path.relpath(input_path, self.input_dir)
                    output_path = os.path.join(self.output_dir, rel_path)
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    self.process_markdown_file(input_path, output_path)

        if self.text_log:
            self.text_log.close()

        logging.info(f"Processed {self.translated_files} files, skipped {self.skipped_files}")

def main():
    parser = argparse.ArgumentParser(description="Markdown translation tool")
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--target-lang", required=True)
    parser.add_argument("--deepl-api-key", default=os.getenv("DEEPL_API_KEY"))
    
    args = parser.parse_args()
    
    translator = MarkdownTranslator(
        args.input_dir,
        args.output_dir,
        args.target_lang,
        args.deepl_api_key
    )
    translator.run()

if __name__ == "__main__":
    main()