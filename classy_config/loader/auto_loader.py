from pathlib import Path
from typing import Any, Dict, MutableMapping

from .env_loader import env_loader
from .json_loader import json_loader
from .loader import Loader
from .toml_loader import toml_loader

__parser_mapping: Dict[str, Loader] = {
    ".json": json_loader,
    ".toml": toml_loader,
    ".env": env_loader,
}


def auto_loader(filepath: Path) -> MutableMapping[str, Any]:
    """
    Resolve a loader based on the file's extension, then use loader to construct a dict.

    :param filepath:
    :return:
    """
    resolved_parser = __parser_mapping[filepath.suffix]
    return resolved_parser(filepath)


def register_loader(extension: str, loader: Loader) -> None:
    """
    Register a loader for the auto_loader to use. This will resolve a loader from the provided extension.

    :param extension: The file extension this loader will be assigned to.
    :param loader: The loader function.
    :return:
    """
    __parser_mapping[extension] = loader
