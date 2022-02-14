import pytest

from classy_config._util import merge_dicts


def test_simple_merge_dicts():
    dict_one = {"1": 1, "2": 2}
    dict_two = {"3": 3, "4": 4}

    merged = merge_dicts(dict_one, dict_two)

    assert merged == {"1": 1, "2": 2, "3": 3, "4": 4}


def test_merge_nested_dicts():
    dict_one = {
        "1": 1,
        "2": {
            "3": 3,
            "4": 4
        }
    }

    dict_two = {
        "2": {
            "5": 5,
            "6": 6,
        },
        "7": 7
    }

    merged = merge_dicts(dict_one, dict_two)

    assert merged == {"1": 1, "2": {"3": 3, "4": 4, "5": 5, "6": 6}, "7": 7}


def test_merge_dicts_conflict():
    dict_one = {
        "1": 1,
        "2": 2
    }

    dict_two = {
        "2": 3
    }

    with pytest.raises(ValueError):
        merge_dicts(dict_one, dict_two)


def test_merge_dicts_nested_conflict():
    dict_one = {
        "1": 1,
        "2": {
            "3": 3,
            "4": 4
        }
    }

    dict_two = {
        "2": {
            "4": 5
        }
    }

    with pytest.raises(ValueError):
        merge_dicts(dict_one, dict_two)
