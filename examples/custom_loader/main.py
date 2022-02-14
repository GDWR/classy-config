from pathlib import Path

from classy_config import ConfigValue, register_config, register_loader


def txt_loader(filepath: Path) -> dict:
    out = {}

    with filepath.open() as f:
        for line in f.readlines():
            key, value = line.split(">")
            out[key] = value

    return out


register_loader(".txt", txt_loader)
register_config("config.txt")

print(f"data: {ConfigValue('data', int)}")
print(f"name: {ConfigValue('name', str)}")
