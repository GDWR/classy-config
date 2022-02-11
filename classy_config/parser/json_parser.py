import json
from pathlib import Path
from typing import Any, MutableMapping


def json_parser(filepath: Path) -> MutableMapping[str, Any]:
    """Open, read and construct dict from JSON file."""
    with filepath.open("r") as f:
        return json.load(f)
