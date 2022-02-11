from typing import Dict, List, Type, TypeVar, cast

from pydantic import BaseModel
from typing_inspect import get_origin

from .classy_config import ClassyConfig
from .exceptions import InstanceNotCreated

T = TypeVar("T")


class _ResolveFromConfig(type):
    def __call__(cls, variable_path: str, _type: Type[T], deliminator: str = ".") -> T:

        config = ClassyConfig.instance
        if config is None:
            raise InstanceNotCreated("Please create an instance of ClassyConfig before using ConfigParam")

        data = config.raw_config
        for step in variable_path.split(deliminator):
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


class ConfigParam(metaclass=_ResolveFromConfig):
    """Resolve to a value defined within the config."""
