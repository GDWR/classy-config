from classy_config.config import get_raw_config, register_config

register_config(filepath="config.toml")
register_config(filepath="conflict.toml")

print(get_raw_config())
