from __future__ import annotations

import argparse
import os
import posixpath
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

from core.languages import normalize_base_path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
URL_PREFIX = normalize_base_path(os.getenv("CIRCUSWIKI_SITE_BASE_PATH"))


class PrefixedSiteHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(SITE), **kwargs)

    def do_GET(self) -> None:
        if urlparse(self.path).path == URL_PREFIX.rstrip("/"):
            self.send_response(301)
            self.send_header("Location", URL_PREFIX)
            self.end_headers()
            return
        super().do_GET()

    def do_HEAD(self) -> None:
        if urlparse(self.path).path == URL_PREFIX.rstrip("/"):
            self.send_response(301)
            self.send_header("Location", URL_PREFIX)
            self.end_headers()
            return
        super().do_HEAD()

    def translate_path(self, path: str) -> str:
        url_path = urlparse(path).path
        if url_path.startswith(URL_PREFIX):
            url_path = "/" + url_path[len(URL_PREFIX) :]

        url_path = posixpath.normpath(unquote(url_path))
        parts = [
            part
            for part in url_path.split("/")
            if part and part not in (".", "..")
        ]
        return str(SITE.joinpath(*parts))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Serve the compiled multilingual site locally under the configured base path."
    )
    parser.add_argument("--host", default="127.0.0.1", help="Address to bind to.")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind to.")
    parser.add_argument("--base-path", default=os.getenv("CIRCUSWIKI_SITE_BASE_PATH"), help="URL prefix to map to site/.")
    args = parser.parse_args()

    if not SITE.exists():
        raise SystemExit("Missing site directory. Run tools/build_multilang.ps1 first.")

    global URL_PREFIX
    URL_PREFIX = normalize_base_path(args.base_path)

    server = ThreadingHTTPServer((args.host, args.port), PrefixedSiteHandler)
    print(f"Multilingual site preview: http://{args.host}:{args.port}{URL_PREFIX}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
