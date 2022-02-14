from typing import Any, MutableMapping, Optional


def merge_dicts(a: MutableMapping[str, Any], b: MutableMapping[str, Any], path: Optional[list] = None) -> MutableMapping[str, Any]:
    """
    Merge the keys and values of the two dicts.

    :param a:
    :param b:
    :param path:
    :return:
    :raises ValueError: When both dicts assign the same key, with different values.
    """
    if path is None:
        path = []

    for key in b:

        if key not in a:
            a[key] = b[key]
            continue

        if isinstance(a[key], dict) and isinstance(b[key], dict):
            merge_dicts(a[key], b[key], path + [str(key)])
        elif a[key] == b[key]:
            pass  # same leaf value
        else:
            raise ValueError(f"Conflict at {'.'.join(path + [str(key)])}")

    return a
