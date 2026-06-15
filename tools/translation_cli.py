from __future__ import annotations

import argparse
import json

from translation.workflow import (
    health_summary,
    inspect_page,
    metadata_batch_plan,
    translate_metadata_page,
    translate_page,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="CircusWiki translation workflow")
    subcommands = parser.add_subparsers(dest="command", required=True)

    health_parser = subcommands.add_parser("health", help="Inspect all source pages")
    health_parser.add_argument("--source-lang", required=True)
    health_parser.add_argument("--target-lang", required=True)

    inspect_parser = subcommands.add_parser("inspect", help="Inspect one source page")
    inspect_parser.add_argument("path")
    inspect_parser.add_argument("--source-lang", required=True)
    inspect_parser.add_argument("--target-lang", required=True)

    translate_parser = subcommands.add_parser("translate", help="Translate one source page")
    translate_parser.add_argument("path")
    translate_parser.add_argument("--source-lang", required=True)
    translate_parser.add_argument("--target-lang", required=True)
    translate_parser.add_argument("--model")
    translate_parser.add_argument("--prompt")
    translate_parser.add_argument("--dry-run", action="store_true", help="Call the translation API and show the result metadata without writing the target file.")

    metadata_parser = subcommands.add_parser("translate-metadata", help="Translate target frontmatter title/description only")
    metadata_parser.add_argument("path")
    metadata_parser.add_argument("--source-lang", required=True)
    metadata_parser.add_argument("--target-lang", required=True)
    metadata_parser.add_argument("--model")
    metadata_parser.add_argument("--dry-run", action="store_true", help="Call the metadata translation API and show the result metadata without writing the target file.")

    metadata_plan_parser = subcommands.add_parser("metadata-plan", help="Plan batch metadata translation")
    metadata_plan_parser.add_argument("--target-lang", required=True)
    metadata_plan_parser.add_argument("--source-lang", default="all")
    metadata_plan_parser.add_argument("--reason", default="all")
    metadata_plan_parser.add_argument("--path-filter", default="")
    metadata_plan_parser.add_argument("--max-files", type=int, required=True)

    args = parser.parse_args()

    if args.command == "health":
        print(json.dumps(health_summary(args.source_lang, args.target_lang), ensure_ascii=False, indent=2))
        return

    if args.command == "inspect":
        print(
            json.dumps(
                inspect_page(args.path, args.source_lang, args.target_lang).__dict__,
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "translate":
        print(
            json.dumps(
                translate_page(
                    source_path=args.path,
                    source_lang=args.source_lang,
                    target_lang=args.target_lang,
                    model=args.model,
                    prompt=args.prompt,
                    dry_run=args.dry_run,
                ),
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "translate-metadata":
        print(
            json.dumps(
                translate_metadata_page(
                    source_path=args.path,
                    source_lang=args.source_lang,
                    target_lang=args.target_lang,
                    model=args.model,
                    dry_run=args.dry_run,
                ),
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "metadata-plan":
        print(
            json.dumps(
                metadata_batch_plan(
                    target_lang=args.target_lang,
                    max_files=args.max_files,
                    source_lang=args.source_lang,
                    reason=args.reason,
                    path_filter=args.path_filter,
                ),
                ensure_ascii=False,
                indent=2,
            )
        )


if __name__ == "__main__":
    main()
