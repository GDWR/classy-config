from logging import getLogger
from pathlib import Path
from typing import Any, Dict, List, MutableMapping, Optional, Type, TypeVar, Union

from pydantic import BaseModel
from typing_inspect import get_origin

from ._util import merge_dicts
from .loader import Loader, auto_loader

logger = getLogger(__name__)

_config: MutableMapping[str, Any] = {}


def register_config(
    filepath: Union[str, Path],
    prefix: Optional[str] = None,
    loader: Loader = auto_loader,
    strict: bool = False
) -> None:
    """
    Register a config file to load from.

    :param filepath: Path to the config to load.
    :param prefix: Prefix all config values loaded.
    :param loader: Loader to user for gathering values from config file.
        The default `auto_loader` will resolve a loader from the config file's extension.
    :param strict: If strict, any duplicate keys will raise a ValueError.
        If not strict, duplicate keys will attempt to be merged if both values are dicts.
    :return:
    """
    if isinstance(filepath, str):
        filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(filepath)

    raw_config = loader(filepath)

    if prefix:
        raw_config = {prefix: raw_config}

    for key, val in raw_config.items():
        current_value = _config.get(key)

        if current_value is None:
            _config[key] = val
            continue

        if strict:
            raise ValueError("Conflicting config")

        logger.warning("Conflicting config value, merging")

        if not isinstance(current_value, dict):
            logger.warning("Dropping conflicting config value. [%s:%s]", key, val)
            continue

        _config[key] = merge_dicts(current_value, val)


def get_raw_config() -> MutableMapping[str, Any]:
    """:return: The current loaded config."""
    return _config.copy()


T = TypeVar("T")


class _ResolveFromConfig(type):
    def __call__(cls, variable_path: str, _type: Type[T], deliminator: str = ".") -> T:

        config_value_path = variable_path.split(deliminator)

        data = _config

        for step in config_value_path:
            try:
                data = data[step]
            except KeyError:
                raise KeyError(f"Config: {variable_path} does not exist")

        if get_origin(_type) in (List, Dict):
            return _type(data)
        if issubclass(_type, BaseModel):
            return _type(**data)
        else:
            return _type(data)


class ConfigValue(metaclass=_ResolveFromConfig):
    """Resolve to a value defined within the config."""
