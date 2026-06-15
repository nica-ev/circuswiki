from __future__ import annotations

import argparse
import json

from .materialize import materialize_all_base_labels
from .service import plan_base_label_translation, scan_base_labels, translate_base_labels


def main() -> None:
    parser = argparse.ArgumentParser(description="Translate Obsidian Base displayName labels")
    subcommands = parser.add_subparsers(dest="command", required=True)
    subcommands.add_parser("scan", help="Scan base displayName labels")
    plan_parser = subcommands.add_parser("plan", help="Plan missing/stale label translations")
    plan_parser.add_argument("--base", default="")
    plan_parser.add_argument("--target-lang", default="all")
    translate_parser = subcommands.add_parser("translate", help="Translate missing/stale labels")
    translate_parser.add_argument("--base", default="")
    translate_parser.add_argument("--target-lang", default="all")
    translate_parser.add_argument("--model")
    translate_parser.add_argument("--dry-run", action="store_true")
    materialize_parser = subcommands.add_parser("materialize", help="Regenerate localized generated base files")
    materialize_parser.add_argument("--base", default="")
    materialize_parser.add_argument("--target-lang", default="all")
    args = parser.parse_args()

    if args.command == "scan":
        print(json.dumps(scan_base_labels(), ensure_ascii=False, indent=2))
    elif args.command == "plan":
        print(json.dumps(plan_base_label_translation(args.base, args.target_lang), ensure_ascii=False, indent=2))
    elif args.command == "translate":
        print(json.dumps(translate_base_labels(args.base, args.target_lang, args.model, args.dry_run), ensure_ascii=False, indent=2))
    elif args.command == "materialize":
        print(json.dumps(materialize_all_base_labels(args.base, args.target_lang), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
