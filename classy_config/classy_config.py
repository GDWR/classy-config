import json
from os import PathLike
from typing import Union, Optional

from .exceptions import DoubleCreation


class ClassyConfig:
    instance: Optional["ClassyConfig"] = None
    _raw_config: Optional[dict] = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is not None:
            raise DoubleCreation("Can only create one ClassyConfig")

        cls.instance = super(ClassyConfig, cls).__new__(cls)
        return cls.instance

    def __init__(self, config_file: Union[str, PathLike]):
        self.config_file = config_file

    def _get_raw_config_file(self) -> dict:
        if self._raw_config is None:
            with open(self.config_file, "r") as f:
                self._raw_config = json.load(f)

        return self._raw_config

    @property
    def raw_config(self) -> dict:
        return self._get_raw_config_file()
