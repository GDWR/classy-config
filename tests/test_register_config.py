from pathlib import Path

from classy_config import ConfigValue, register_loader
from classy_config.config import register_config


def _stub_loader(filepath: Path) -> dict:
    output = {}

    with filepath.open() as f:
        for line in f.readlines():
            key, value = line.split(">")
            output[key] = value.strip()

    return output


class TestRegisterAndUseLoader:

    def test_register_loader(self):
        register_loader(".test", _stub_loader)

    def test_use_loader(self):
        register_config("configs/test-config.test", prefix="test-loader")

    def test_loaded_values(self):
        assert ConfigValue("test-loader.value0", int) == 0
        assert ConfigValue("test-loader.value1", int) == 1
        assert ConfigValue("test-loader.value2", int) == 2
        assert ConfigValue("test-loader.value3", int) == 3
