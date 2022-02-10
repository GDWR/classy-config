import json

import pytest

from classy_config import ClassyConfig
from classy_config.exceptions import DoubleCreation


def test_raw_config(classy_config: ClassyConfig):
    with open("configs/test-config.json", "r") as f:
        data = json.load(f)

    assert classy_config.raw_config == data, "Data isn't the same"


def test_double_creation():
    with pytest.raises(DoubleCreation):
        ClassyConfig(
            filepath="configs/test-config.json"
        )
