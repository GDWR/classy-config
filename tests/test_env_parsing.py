from classy_config import ConfigValue
from classy_config.config import register_config

test_values = [
    "1",
    "2",
    "3",
    "4"
]

def test_env_config():
    register_config(filepath="tests/configs/test-config.env", prefix="env")

    for count, test_val in enumerate(test_values, start=1):
        assert ConfigValue(f"env.test_{count}", str) == test_val
