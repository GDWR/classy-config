from classy_config import ClassyConfig, ConfigParam


def test_nested_config(classy_config: ClassyConfig):
    raw_value = classy_config.raw_config["nested"]["config"]["value"]

    def assert_value(value: str = ConfigParam("nested.config.value", str)) -> None:
        assert raw_value == value

    assert_value()
