from __future__ import annotations

import argparse
import json
from pathlib import Path

from circusfinder import export_datasets, load_entries


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate and export the CircusFinder directory")
    subcommands = parser.add_subparsers(dest="command", required=True)
    subcommands.add_parser("validate", help="Validate published CircusFinder Markdown entries")
    export_parser = subcommands.add_parser("export", help="Validate and write language datasets")
    export_parser.add_argument("--output", type=Path, default=ROOT / ".build")
    args = parser.parse_args()

    if args.command == "validate":
        entries = load_entries(ROOT / "docs")
        result = {"ok": True, "entry_files": len(entries)}
    else:
        counts = export_datasets(ROOT / "docs", args.output)
        result = {"ok": True, "output": str(args.output), "records_by_language": counts}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
