from os import environ

from classy_config import ConfigValue
from classy_config.config import register_config

test_values = [
    "1",
    "2",
    "3",
    "4"
]

def test_env_config():
    """
    Asserts that an integer can be set to the OS environment and can be properly loaded.
    Asserts that multiple string values can be loaded from a .env file.
    Does not check whether multipe configs are working together.
    Does not cover most typing on .env values.
    """
    register_config(filepath="tests/configs/test-config.env", prefix="env")

    environ["test_5"] = "5"

    assert ConfigValue("env.test_5", int) == 5

    for count, test_val in enumerate(test_values, start=1):
        assert ConfigValue(f"env.test_{count}", str) == test_val
