from os import PathLike
from pathlib import Path
from typing import Optional, Union

from .exceptions import DoubleCreation
from .parser import Parser, auto_parser


class ClassyConfig:
    """Define your config filepath."""

    instance: Optional["ClassyConfig"] = None
    _raw_config: Optional[dict] = None

    def __new__(cls, *args, **kwargs) -> "ClassyConfig":
        """
        Singleton implementation.

        if the object has already been created a DoubleCreation error is raised.
        """
        if cls.instance is not None:
            raise DoubleCreation("Can only create one ClassyConfig")

        cls.instance = super(ClassyConfig, cls).__new__(cls)
        return cls.instance

    def __init__(self, filepath: Union[str, PathLike], parser: Parser = auto_parser) -> None:
        self.config_file = Path(filepath)
        self.parser = parser

        if not self.config_file.exists():
            raise FileNotFoundError()

    @property
    def raw_config(self) -> dict:
        """
        Gathers the raw config from the file.

        This config file is read once & saved to an instance attribute,
            so future access will not require another file read.
        """
        if self._raw_config is None:
            self._raw_config = self.parser(self.config_file)

        return self._raw_config
