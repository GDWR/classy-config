from classy_config import ConfigValue
from classy_config.config import get_raw_config, register_config


def test_toml_config():
    register_config(filepath="configs/test-config.toml", prefix="toml")

    raw_config = get_raw_config()
    raw_value = raw_config["toml"]["nested"]["config"]["value"]

    def assert_value(value: str = ConfigValue("nested.config.value", str)) -> None:
        assert raw_value == value

    assert_value()
