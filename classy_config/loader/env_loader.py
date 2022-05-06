from os import environ
from pathlib import Path
from typing import Any, MutableMapping

from dotenv import load_dotenv


def env_loader(filepath: Path) -> MutableMapping[str, str]:
    """
    Load the given *.env file and the user's environment variables.

    Prioritizes system/user environment variables. Will not override any existing environment variables from the
    system.

    :param filepath: The path of the file to load from.
    :return: The mapping of keys to value loaded from the env file and user's environment.
    """
    if filepath:
        load_dotenv(filepath)

    return environ
