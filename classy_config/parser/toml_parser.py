from pathlib import Path

import toml


def toml_parser(filepath: Path) -> dict:
    """Open, read and construct dict from JSON file."""
    with filepath.open("r") as f:
        return toml.load(f)
