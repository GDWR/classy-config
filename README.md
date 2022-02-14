<div align="center">
    <img align="center" src="https://raw.githubusercontent.com/GDWR/classy-config/main/docs/favicon.ico" alt="ClassyConfig Logo">
</div>


<h2 align="center">ClassyConfig</h2>

<div align="center">
    <strong>ClassyConfig</strong> is a Python3 package aiming to remove the need for a <strong>config.py</strong> or <strong>settings.py</strong> file.
</div>

<br>

<div align="center">
    <a href="https://github.com/GDWR/classy-config/actions"><img alt="Checks Pipeline Badge" src="https://github.com/GDWR/classy-config/actions/workflows/checks.yml/badge.svg?branch=main"></a>
    <a href="https://github.com/GDWR/classy-config/actions"><img alt="Create Documentation Badge" src="https://github.com/GDWR/classy-config/actions/workflows/create-documentation.yml/badge.svg?branch=main"></a>
    <a href="https://github.com/GDWR/classy-config/actions"><img alt="Build and Publish Badge" src="https://github.com/GDWR/classy-config/actions/workflows/build-and-publish.yml/badge.svg?branch=main"></a>
</div>
<div align="center">
    <a href="https://pypi.org/project/classy-config/"><img alt="PyPI" src="https://img.shields.io/pypi/v/classy-config"></a>
    <a href="https://github.com/GDWR/classy-config/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
    <a href="https://pepy.tech/project/black"><img alt="Downloads" src="https://pepy.tech/badge/classy-config"></a>
</div> 

---

## [Documentation](https://gdwr.github.io/classy-config/)

## Installation

**ClassyConfig** is avliable via Pypi, so it can be installed using **pip**

```shell
$ pip install classy_config
```

## Usage

[View on the docs](https://gdwr.github.io/classy-config/source/getting-started/index.html)

```python
from classy_config import ConfigValue, register_config
from pydantic import BaseModel

# Register your config file to be used
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