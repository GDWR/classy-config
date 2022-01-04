# ClassyConfig

Inject your config variables into methods, so they are as close to usage as possible.


```py

from classy_config import BaseModel, ClassyConfig, ConfigParam

# Create your global config manager (example config.json below)
config = ClassyConfig(config_file="config.json")

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
```
```json
{
  "version": "0.0.1",
  
  "author": {
    "username": "GDWR",
    "email": "gregory.dwr@gmail.com",
    "lucky_number": 17
  }
}
```