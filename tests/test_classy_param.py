from typing import Tuple, Type, TypeVar

import pytest
from pydantic import BaseModel

from classy_config import ConfigValue
from classy_config.config import get_raw_config

T = TypeVar("T")


@pytest.mark.parametrize(
    "test_value", [
        ("value0", int),
        ("value1", bool),
        ("value2", str),
        ("value3", list),
        ("value4", dict)
    ]
)
def test_config_param(test_value: Tuple[str, Type[T]]):
    config_path, config_type = test_value

    raw_config = get_raw_config()
    raw_value = raw_config[config_path]

    typed_value = config_type(raw_value)

    def asset_value(value: Type[T] = ConfigValue(config_path, config_type)) -> None:
        assert typed_value == value

    asset_value()


def test_config_model():

    raw_config = get_raw_config()
    raw_value = raw_config["GDWR"]

    typed_value = User(**raw_value)

    def assert_value(value: User = ConfigValue("GDWR", User)) -> None:
        assert typed_value == value

    assert_value()


class User(BaseModel):
    name: str
    alive: bool
    age: int
    email: str


def test_nested_config():
    raw_config = get_raw_config()
    raw_value = raw_config["nested"]["config"]["value"]

    def assert_value(value: str = ConfigValue("nested.config.value", str)) -> None:
        assert raw_value == value

    assert_value()


def test_nested_config_model():
    raw_config = get_raw_config()
    raw_value = raw_config["nested"]["config"]["GDWR"]

    typed_value = User(**raw_value)

    def assert_value(value: User = ConfigValue("nested.config.GDWR", User)) -> None:
        assert typed_value == value

    assert_value()


def test_custom_deliminator():
    raw_config = get_raw_config()
    raw_value = raw_config["nested"]["config"]["GDWR"]

    typed_value = User(**raw_value)

    def assert_value(value: User = ConfigValue("nested->config->GDWR", User, deliminator="->")) -> None:
        assert typed_value == value

    assert_value()


def test_gather_param_inline():
    raw_config = get_raw_config()
    raw_value = raw_config["nested"]["config"]["GDWR"]

    typed_value = User(**raw_value)

    value = ConfigValue("nested->config->GDWR", User, deliminator="->")

    assert typed_value == value
