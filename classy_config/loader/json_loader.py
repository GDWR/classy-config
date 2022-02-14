import json
from pathlib import Path
from typing import Any, MutableMapping


def json_loader(filepath: Path) -> MutableMapping[str, Any]:
    """
    Open and load a config mapping from a JSON file.

    :param filepath: The path of the file to load from.
    :return: The mapping of keys to value loaded from the file.
    """
    with filepath.open("r") as f:
        return json.load(f)
