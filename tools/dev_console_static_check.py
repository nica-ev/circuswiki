from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "tools" / "dev_console" / "static"
IMPORT_RE = re.compile(r"""import\s+(?:[^'"]+\s+from\s+)?["']([^"']+)["']""")
CSS_IMPORT_RE = re.compile(r"""@import\s+url\(["']?([^"')]+)["']?\)""")
FEATURE_ID_RE = re.compile(r"""\{\s*id:\s*["']([^"']+)["']""")
PANEL_ID_RE = re.compile(r"""id=["']tab-([^"']+)["']""")


def fail(message: str) -> int:
    print(f"FAIL {message}", file=sys.stderr)
    return 1


def check_css_imports() -> list[str]:
    errors: list[str] = []
    for css_path in STATIC.rglob("*.css"):
        content = css_path.read_text(encoding="utf-8")
        for specifier in CSS_IMPORT_RE.findall(content):
            if specifier.startswith(("http://", "https://")):
                continue
            target = (css_path.parent / specifier).resolve()
            if not target.exists():
                errors.append(f"{css_path.relative_to(ROOT)} imports missing {specifier}")
    return errors


def check_js_imports() -> list[str]:
    errors: list[str] = []
    for js_path in STATIC.rglob("*.js"):
        content = js_path.read_text(encoding="utf-8")
        for specifier in IMPORT_RE.findall(content):
            if not specifier.startswith("."):
                continue
            target = (js_path.parent / specifier).resolve()
            candidates = [target, target.with_suffix(".js")]
            if not any(candidate.exists() for candidate in candidates):
                errors.append(f"{js_path.relative_to(ROOT)} imports missing {specifier}")
    return errors


def run_node_check() -> list[str]:
    node = shutil.which("node")
    if not node:
        return ["node executable not found; skipped JavaScript syntax check"]
    errors: list[str] = []
    for js_path in STATIC.rglob("*.js"):
        result = subprocess.run(
            [node, "--check", str(js_path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            errors.append(f"{js_path.relative_to(ROOT)} failed node --check\n{result.stderr or result.stdout}")
    return errors


def check_feature_shell_contract() -> list[str]:
    errors: list[str] = []
    registry = (STATIC / "features" / "registry.js").read_text(encoding="utf-8")
    lifecycle = (STATIC / "features" / "lifecycle.js").read_text(encoding="utf-8")
    app = (STATIC / "app.js").read_text(encoding="utf-8")
    html = (STATIC / "index.html").read_text(encoding="utf-8")

    features_source = registry.split("export const FEATURES =", 1)[1]
    feature_ids = set(FEATURE_ID_RE.findall(features_source))
    panel_ids = set(PANEL_ID_RE.findall(html))
    if feature_ids != panel_ids:
        errors.append(
            "feature registry and tab panels differ: "
            f"missing panels={sorted(feature_ids - panel_ids)}, extra panels={sorted(panel_ids - feature_ids)}"
        )

    for feature_id in sorted(feature_ids):
        quoted = f'"{feature_id}"' if "-" in feature_id else f"{feature_id}:"
        if quoted not in lifecycle:
            errors.append(f"lifecycle does not reference feature {feature_id}")

    if "createPanelStore" not in app:
        errors.append("app.js does not use createPanelStore")
    if "mountFeature(state.activeTab" not in app:
        errors.append("app.js does not mount the active feature explicitly")
    if "unmountFeature(state.activeTab" not in app:
        errors.append("app.js does not unmount the active feature before switching")
    return errors


def main() -> int:
    errors = check_css_imports()
    errors.extend(check_js_imports())
    errors.extend(check_feature_shell_contract())
    node_messages = run_node_check()
    node_errors = [message for message in node_messages if "failed node --check" in message]
    node_skips = [message for message in node_messages if "skipped" in message]
    errors.extend(node_errors)

    for message in node_skips:
        print(message)
    if errors:
        for error in errors:
            fail(error)
        return 1
    print("Frontend static check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
