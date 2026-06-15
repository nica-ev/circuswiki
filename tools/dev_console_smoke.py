from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / "tools" / "dev_console" / "server.py"

DEFAULT_PATHS = [
    "/",
    "/styles.css",
    "/styles/tokens.css",
    "/styles/shell.css",
    "/styles/controls.css",
    "/styles/panes.css",
    "/styles/tables.css",
    "/styles/features.css",
    "/app.js",
    "/api/config",
    "/api/vault-health",
]


def request_status(url: str, timeout: float) -> int:
    with urlopen(url, timeout=timeout) as response:
        return response.status


def wait_until_ready(base_url: str, timeout_seconds: float) -> bool:
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        try:
            if request_status(f"{base_url}/api/config", timeout=1.0) == 200:
                return True
        except (OSError, TimeoutError, URLError):
            time.sleep(0.25)
    return False


def run_smoke(host: str, port: int, paths: list[str], startup_timeout: float) -> int:
    base_url = f"http://{host}:{port}"
    process = subprocess.Popen(
        [sys.executable, str(SERVER), "--host", host, "--port", str(port)],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    try:
        if not wait_until_ready(base_url, startup_timeout):
            process.terminate()
            output = process.communicate(timeout=5)[0]
            print(f"Dev console did not become ready at {base_url}.", file=sys.stderr)
            if output:
                print(output, file=sys.stderr)
            return 1

        failed = False
        for path in paths:
            url = f"{base_url}{path}"
            try:
                status = request_status(url, timeout=10.0)
            except (OSError, TimeoutError, URLError) as error:
                print(f"FAIL {path}: {error}", file=sys.stderr)
                failed = True
                continue
            print(f"{status} {path}")
            if status != 200:
                failed = True
        return 1 if failed else 0
    finally:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke test the local dev console server.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8791)
    parser.add_argument("--startup-timeout", type=float, default=10.0)
    parser.add_argument("--path", action="append", dest="paths", help="Path to check. Can be provided more than once.")
    args = parser.parse_args()
    return run_smoke(args.host, args.port, args.paths or DEFAULT_PATHS, args.startup_timeout)


if __name__ == "__main__":
    raise SystemExit(main())
