Getting Started
===============

Installation
*************

ClassyConfig is available on `pipy <https://pypi.org/project/classy-config/>`_, this will allow you to use ``pip`` to install ClassyConfig.

.. code-block::

    pip install classy_config


Usage
******

.. code-block:: python

    from classy_config import BaseModel, ConfigValue, register_config

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
