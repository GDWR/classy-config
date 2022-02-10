from pathlib import Path
from typing import Dict

from .json_parser import json_parser
from .parser import Parser
from .toml_parser import toml_parser

parser_mapping: Dict[str, Parser] = {
    ".json": json_parser,
    ".toml": toml_parser,
}


def auto_parser(filepath: Path) -> dict:
    """Resolve a parse using the file's extension & use it to construct a dict."""
    resolved_parser = parser_mapping[filepath.suffix]
    return resolved_parser(filepath)
