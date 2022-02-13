# ClassyConfig

`ClassyConfig` is a Python3 package aiming to remove the need for a `config.py` or `settings.py` file.

```py

from classy_config import BaseModel, ClassyConfig, ConfigParam

# Create your global config manager (example test-config.json below)
config = ClassyConfig(filepath="test-config.json")

# Resolve default values based on your config
def print_current_version(version: str = ConfigParam("version", str)) -> None:
    print(version)

# Use Pydantic Models for your config
class Author(BaseModel):
    username: str
    email: str
    lucky_number: int

# Resolve default values based on your config
def print_author(author: Author = ConfigParam("author", Author)) -> None:
    print(author)
    
# Allows for nested values
def print_value(value: int = ConfigParam("nested.value", int)) -> None:
    print(value)
```
```json
{
  "version": "0.0.1",
  
  "author": {
    "username": "GDWR",
    "email": "gregory.dwr@gmail.com",
    "lucky_number": 17
  },

  "nested": {
    "value": 10
  }
}
```
