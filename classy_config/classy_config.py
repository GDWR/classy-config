from __future__ import annotations

import json
from os import PathLike
from typing import Optional, Union

from .exceptions import DoubleCreation


class ClassyConfig:
    """Define your config filepath."""

    instance: Optional["ClassyConfig"] = None
    _raw_config: Optional[dict] = None

    def __new__(cls, *args, **kwargs) -> ClassyConfig:
        """
        Singleton implementation.

        if the object has already been created a DoubleCreation error is raised.
        """
        if cls.instance is not None:
            raise DoubleCreation("Can only create one ClassyConfig")

        cls.instance = super(ClassyConfig, cls).__new__(cls)
        return cls.instance

    def __init__(self, config_file: Union[str, PathLike]) -> None:
        self.config_file = config_file

    @property
    def raw_config(self) -> dict:
        """
        Gathers the raw config from the file.

        This config file is read once & saved to an instance attribute,
            so future access will not require another file read.
        """
        if self._raw_config is None:
            with open(self.config_file, "r") as f:
                self._raw_config = json.load(f)

        return self._raw_config
