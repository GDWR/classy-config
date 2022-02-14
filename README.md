# ClassyConfig

`ClassyConfig` is a Python3 package aiming to remove the need for a `config.py` or `settings.py` file.

```py

from classy_config import ConfigValue, register_config
from pydantic import BaseModel

# Create your global config manager (example test-config.json below)
register_config(filepath="config.toml")


# Resolve default values based on your config
def print_current_version(version: str = ConfigValue("package", str)) -> None:
    print(version)


# Use Pydantic Models for your config
class Author(BaseModel):
    username: str
    email: str
    lucky_number: int


# Resolve default values based on your config
def print_author(author: Author = ConfigValue("author", Author)) -> None:
    print(author)


# Allows for nested values
def print_value(value: int = ConfigValue("nested.value", int)) -> None:
    print(value)
```

```toml
package="ClassyConfig"

[author]
username="GDWR"
email="gregory.dwr@gmail.com"
lucky_number=17

[nested]
value=10
```
