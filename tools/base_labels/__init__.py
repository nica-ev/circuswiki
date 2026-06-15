from __future__ import annotations

from . import config
from .cli import main
from .config import (
    BASES,
    CONFIG_PATH,
    DEFAULT_BASE_URL,
    DEFAULT_MODEL,
    ROOT,
    canonical_base_files,
    rel,
    resolve_base,
    source_hash,
)
from .materialize import localize_base_text, materialize_all_base_labels, materialize_base_labels
from .parser import (
    DISPLAY_NAME_RE,
    LANGUAGE_FILTER_RE,
    PROPERTY_KEY_RE,
    TOP_LEVEL_RE,
    apply_display_names,
    extract_display_names,
    properties_section_bounds,
    quote_yaml_scalar,
    unquote_yaml_scalar,
)
from .service import (
    labels_for_language,
    load_config,
    plan_base_label_translation,
    save_config,
    scan_base_labels,
    translate_base_labels,
    update_config_sources,
)
from .translation import (
    call_label_translation_model,
    chat_completions_url,
    default_model,
    label_prompt,
    load_local_env,
    strip_code_fences,
)

__all__ = [
    "apply_display_names",
    "BASES",
    "call_label_translation_model",
    "canonical_base_files",
    "chat_completions_url",
    "CONFIG_PATH",
    "config",
    "DEFAULT_BASE_URL",
    "DEFAULT_MODEL",
    "default_model",
    "DISPLAY_NAME_RE",
    "extract_display_names",
    "label_prompt",
    "LANGUAGE_FILTER_RE",
    "labels_for_language",
    "load_config",
    "load_local_env",
    "localize_base_text",
    "main",
    "materialize_all_base_labels",
    "materialize_base_labels",
    "plan_base_label_translation",
    "properties_section_bounds",
    "PROPERTY_KEY_RE",
    "quote_yaml_scalar",
    "rel",
    "resolve_base",
    "ROOT",
    "save_config",
    "scan_base_labels",
    "source_hash",
    "strip_code_fences",
    "TOP_LEVEL_RE",
    "translate_base_labels",
    "unquote_yaml_scalar",
    "update_config_sources",
]
