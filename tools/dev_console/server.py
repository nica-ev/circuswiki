from __future__ import annotations

import argparse
import json
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[2]
STATIC = Path(__file__).resolve().parent / "static"
sys.path.insert(0, str(ROOT / "tools"))

from dev_console import routes_base_labels, routes_cleanup, routes_dynamic, routes_graph, routes_link_repair, routes_navigation, routes_obsidian, routes_translation  # noqa: E402


class DevConsoleHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC), **kwargs)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)

        if parsed.path in {"/", "/index.html"}:
            return self.send_index()

        for routes in (
            routes_translation,
            routes_navigation,
            routes_graph,
            routes_obsidian,
            routes_dynamic,
            routes_base_labels,
            routes_cleanup,
            routes_link_repair,
        ):
            if routes.handle_get(self, parsed.path, parsed.query):
                return

        return super().do_GET()

    def do_POST(self) -> None:
        parsed = urlparse(self.path)

        payload = self.read_json()
        if payload is None:
            return self.send_error_json(400, "Invalid JSON")

        for routes in (
            routes_translation,
            routes_navigation,
            routes_graph,
            routes_obsidian,
            routes_dynamic,
            routes_base_labels,
            routes_cleanup,
            routes_link_repair,
        ):
            if routes.handle_post(self, parsed.path, payload):
                return

        return self.send_error_json(404, "Unknown endpoint")

    def read_json(self) -> dict[str, object] | None:
        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length).decode("utf-8")
            return json.loads(raw)
        except Exception:
            return None

    def send_json(self, payload: object, status: int = 200) -> None:
        data = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def send_error_json(self, status: int, message: str) -> None:
        self.send_json({"error": message}, status=status)

    def send_index(self) -> None:
        path = STATIC / "index.html"
        text = path.read_text(encoding="utf-8")
        text = text.replace('href="styles.css"', f'href="styles.css?v={asset_version("styles.css")}"')
        text = text.replace('src="app.js"', f'src="app.js?v={asset_version("app.js")}"')
        data = text.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def asset_version(name: str) -> str:
    path = STATIC / name
    try:
        return str(int(path.stat().st_mtime))
    except OSError:
        return "0"


def main() -> None:
    parser = argparse.ArgumentParser(description="CircusWiki local dev console")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8787)
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), DevConsoleHandler)
    print(f"Dev console: http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
