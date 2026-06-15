"""CircusWiki local tooling package.

Most tool commands are documented as ``python tools/name.py``. In that mode,
``tools/`` is on ``sys.path`` and sibling packages resolve as top-level imports
such as ``core`` and ``translation``. Add the same path for ``python -m tools.*``
so both invocation styles behave consistently.
"""

from __future__ import annotations

import sys
from pathlib import Path

_TOOLS_DIR = str(Path(__file__).resolve().parent)
if _TOOLS_DIR not in sys.path:
    sys.path.insert(0, _TOOLS_DIR)
