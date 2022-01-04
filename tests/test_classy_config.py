import json
from typing import Tuple, Type, List, get_origin, Dict

import pytest

from classy_config import ClassyConfig, ConfigParam, BaseModel
from classy_config.exceptions import DoubleCreation


@pytest.fixture(scope="session")
def classy_config() -> ClassyConfig:
    return ClassyConfig(
        config_file="config.json"
    )


def test_raw_config(classy_config: ClassyConfig):
    with open("config.json", "r") as f:
        data = json.load(f)

    assert classy_config.raw_config == data, "Data isn't the same"


def test_double_creation():
    with pytest.raises(DoubleCreation):
        config = ClassyConfig(
            config_file="config.json"
        )


@pytest.mark.parametrize(
    "test_value",
    [
        ("value0", int),
        ("value1", bool),
        ("value2", str),
        ("value3", List),
        ("value3", list),
        ("value4", Dict),
        ("value4", dict)
    ]
)
def test_config_param(test_value: Tuple[str, Type], classy_config: ClassyConfig):
    config_path, config_type = test_value

    raw_value = classy_config.raw_config[config_path]
    typed_value = raw_value

    if get_origin(config_type) not in (list, dict):
        typed_value = config_type(raw_value)

    def asset_value(value: Type = ConfigParam(config_path, config_type)) -> None:
        assert typed_value == value

    asset_value()


class User(BaseModel):
    name: str
    alive: bool
    age: int
    email: str


def test_config_model(classy_config: ClassyConfig):
    raw_value = classy_config.raw_config["GDWR"]
    typed_value = User(**raw_value)

    def assert_value(value: User = ConfigParam("GDWR", User)) -> None:
        assert typed_value == value

    assert_value()


def test_nested_config(classy_config: ClassyConfig):
    raw_value = classy_config.raw_config["nested"]["config"]["value"]

    def assert_value(value: str = ConfigParam("nested.config.value", str)) -> None:
        assert raw_value == value

    assert_value()


def test_nested_config_model(classy_config: ClassyConfig):
    raw_value = classy_config.raw_config["nested"]["config"]["GDWR"]
    typed_value = User(**raw_value)

    def assert_value(value: User = ConfigParam("nested.config.GDWR", User)) -> None:
        assert typed_value == value

    assert_value()


def test_custom_deliminator(classy_config: ClassyConfig):
    raw_value = classy_config.raw_config["nested"]["config"]["GDWR"]
    typed_value = User(**raw_value)

    def assert_value(value: User = ConfigParam("nested->config->GDWR", User, deliminator="->")) -> None:
        assert typed_value == value

    assert_value()
