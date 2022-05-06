Getting Started
===============

Installation
*************

ClassyConfig is available on `pypi <https://pypi.org/project/classy-config/>`_,
making it easy to install via ``pip``:

.. code-block::

    pip install classy_config


Usage
******

.. code-block:: python

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
