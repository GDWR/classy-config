from pathlib import Path
from typing import Any, MutableMapping

import toml


def toml_loader(filepath: Path) -> MutableMapping[str, Any]:
    """Open and load a dict from a TOML file."""
    with filepath.open("r") as f:
        return toml.load(f)
