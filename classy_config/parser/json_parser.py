import json
from pathlib import Path


def json_parser(filepath: Path) -> dict:
    """Open, read and construct dict from JSON file."""
    with filepath.open("r") as f:
        return json.load(f)
