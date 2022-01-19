from pytest import fixture

from classy_config import ClassyConfig


@fixture(scope="session")
def classy_config() -> ClassyConfig:
    return ClassyConfig(
        config_file="test-config.json"
    )
