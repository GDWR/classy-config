from pathlib import Path
from typing import Any, MutableMapping

import tomli


def toml_loader(filepath: Path) -> MutableMapping[str, Any]:
    """Open and load a dict from a TOML file."""
    with filepath.open("rb") as f:
        return tomli.load(f)
