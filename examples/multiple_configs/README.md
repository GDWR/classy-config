# Multiple Config Files

There maybe a time were having multiple config files would allow for cleaner deployment,
readability and maintainability.

To accommodate this, `ClassyConfig` allows you to prefix your config files to allow them to be
used alongside each other.

So for this example, we have the following two configuration files.

`config.toml` 
```toml
app_name="Example App"

[database]
port=2345
```

`database.toml`
```toml
host='127.0.0.1'
port=5432
```

This is how they would be loaded, to run alongside each other.

```python
from classy_config import register_config, ConfigValue

register_config(filepath="config.toml")  # This will allow gathering of all values, as usual
register_config(filepath="database.toml", prefix="database")  # This will allow gathering of all values, with the prefix 'database'

app_name = ConfigValue('app_name', str)
print(f"Starting application: {app_name}")

database_host = ConfigValue('database.host', str)
database_port = ConfigValue('database.port', int)
print(f"Connecting to database: {database_host}:{database_port}")
```