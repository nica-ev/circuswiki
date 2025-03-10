import os
import re
import logging
import argparse
from datetime import datetime
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def setup_argparse():
    parser = argparse.ArgumentParser(description='Process markdown files for translation.')
    parser.add_argument('--input-dir', default='translation_test', help='Directory containing markdown files')
    parser.add_argument('--output-dir', default='output', help='Directory to save processed files')
    parser.add_argument('--target-lang', default='EN', help='Target language for translation')
    parser.add_argument('--exclude-dirs', nargs='+', default=[], help='Directories to exclude from processing')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    return parser.parse_args()

def extract_frontmatter(content):
    """Extract frontmatter from markdown content."""
    frontmatter_match = re.match(r'^---\s+(.*?)\s+---\s*', content, re.DOTALL)
    
    if frontmatter_match:
        frontmatter_text = frontmatter_match.group(1)
        try:
            # Use PyYAML to parse the frontmatter properly
            frontmatter = yaml.safe_load(frontmatter_text)
            if frontmatter is None:
                frontmatter = {}
        except Exception as e:
            logger.warning(f"Error parsing frontmatter: {str(e)}")
            frontmatter = {}
        
        # Remove frontmatter from content
        content = content[frontmatter_match.end():]
    else:
        frontmatter = {}
    
    return frontmatter, content

def extract_wikilink_titles(line):
    """Extract only the display titles from wikilinks in a line."""
    titles = []
    
    # First, remove all attributes to simplify parsing
    clean_line = re.sub(r'{\s*\..*?\s*}', '', line)
    
    # Find all wikilinks with titles: [[link|title]]
    for match in re.finditer(r'$$\[(.*?)\|(.*?)$$\]', clean_line):
        titles.append(match.group(2).strip())
    
    # Find all regular wikilinks: [[link]]
    for match in re.finditer(r'$$\[(.*?)$$\]', clean_line):
        # Make sure this isn't part of a wikilink with title
        full_match = match.group(0)
        if '|' not in full_match:
            titles.append(match.group(1).strip())
    
    return titles

def process_line_for_translation(line):
    """Process a line to extract translatable content."""
    # Check if line is a heading
    heading_match = re.match(r'^(#{1,6})\s+(.*)$', line)
    if heading_match:
        # For headings, extract the text part and process it
        heading_text = heading_match.group(2)
        # Extract wikilink titles from the heading text
        wikilink_titles = extract_wikilink_titles(heading_text)
        if wikilink_titles:
            return wikilink_titles
        else:
            # If no wikilinks, return the heading text
            return [heading_text.strip()]
    
    # Remove attributes first to simplify parsing
    clean_line = re.sub(r'{\s*\..*?\s*}', '', line)
    
    # Extract wikilink titles from the line
    wikilink_titles = extract_wikilink_titles(clean_line)
    if wikilink_titles:
        return wikilink_titles
    
    # If no wikilinks, return the line text (excluding non-translatable elements)
    # Remove wikilinks, embeds, attributes, and HTML tags
    clean_text = re.sub(r'$$\[.*?$$\]', '', clean_line)
    clean_text = re.sub(r'!$$\[.*?$$\]', '', clean_text)
    clean_text = re.sub(r'<.*?>', '', clean_text)
    
    # Clean up whitespace
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    if clean_text:
        return [clean_text]
    else:
        return []

def extract_translatable_text(content):
    """Extract translatable text from markdown content."""
    translatable_parts = []
    
    # Split content into lines
    lines = content.split('\n')
    in_code_block = False
    
    for line in lines:
        # Check for code block markers
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        
        # Skip code blocks and empty lines
        if in_code_block or not line.strip():
            continue
        
        # Process the line to extract translatable parts
        parts = process_line_for_translation(line)
        translatable_parts.extend(parts)
    
    return translatable_parts

def process_markdown(content, file_path, target_lang):
    """Process markdown content."""
    try:
        # Extract frontmatter
        frontmatter, content_without_frontmatter = extract_frontmatter(content)
        
        # Extract translatable content
        translatable_parts = extract_translatable_text(content_without_frontmatter)
        
        # Add processed frontmatter
        processed_frontmatter = frontmatter.copy() if frontmatter else {}  # Create a copy to preserve structure
        processed_frontmatter['lang'] = target_lang
        processed_frontmatter['processed_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Handle empty values in frontmatter
        for key, value in processed_frontmatter.items():
            if value is None:
                processed_frontmatter[key] = ''
        
        # Format frontmatter for output
        frontmatter_str = '---\n'
        frontmatter_yaml = yaml.dump(processed_frontmatter, default_flow_style=False, sort_keys=False)
        # Remove quotes around the date
        frontmatter_yaml = re.sub(r"'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'", r'\1', frontmatter_yaml)
        frontmatter_str += frontmatter_yaml
        frontmatter_str += '---\n\n'
        
        # Return processed content and translatable parts
        return frontmatter_str + content_without_frontmatter, translatable_parts
        
    except Exception as e:
        logger.error(f"Error processing markdown in {file_path}: {str(e)}")
        raise

def process_file(file_path, output_dir, target_lang, translation_log_file):
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        processed_content, translatable_parts = process_markdown(content, file_path, target_lang)
        
        # Create output file path
        rel_path = os.path.relpath(file_path, args.input_dir)
        output_path = os.path.join(output_dir, rel_path)
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write processed content to output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(processed_content)
        
        # Write translatable content to translation log
        if translatable_parts and translation_log_file:
            with open(translation_log_file, 'a', encoding='utf-8') as log:
                log.write(f"\n\n--- File: {rel_path} ---\n\n")
                for part in translatable_parts:
                    log.write(f"{part}\n\n")
        
        return True
    except Exception as e:
        logger.error(f"General error processing {file_path}: {str(e)}")
        return False

def process_directory(input_dir, output_dir, target_lang, exclude_dirs):
    """Process all markdown files in a directory."""
    processed_count = 0
    skipped_count = 0
    
    # Create translation log file
    translation_log_file = os.path.join(output_dir, 'translation_log.txt')
    
    # Initialize translation log
    with open(translation_log_file, 'w', encoding='utf-8') as log:
        log.write(f"Translation Log - Target Language: {target_lang}\n")
        log.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        log.write("="*50 + "\n\n")
    
    for root, dirs, files in os.walk(input_dir):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                if args.verbose:
                    logger.info(f"Processing {file_path}")
                
                success = process_file(file_path, output_dir, target_lang, translation_log_file)
                
                if success:
                    processed_count += 1
                else:
                    skipped_count += 1
    
    logger.info(f"Processed {processed_count} files, skipped {skipped_count}")
    logger.info(f"Translation log saved to {translation_log_file}")

if __name__ == "__main__":
    args = setup_argparse()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    process_directory(args.input_dir, args.output_dir, args.target_lang, args.exclude_dirs)