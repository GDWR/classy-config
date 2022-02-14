from classy_config.config import ConfigValue, register_config

register_config(filepath="config.toml")  # This will allow gathering of all values, as usual
register_config(filepath="database.toml", prefix="database")  # This will allow gathering of all values, with the prefix 'database'

app_name = ConfigValue('app_name', str)
print(f"Starting application: {app_name}")

database_host = ConfigValue('database.host', str)
database_port = ConfigValue('database.port', int)
print(f"Connecting to database: {database_host}:{database_port}")
