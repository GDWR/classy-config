Using Multiple Configs
======================

`View on GitHub <https://github.com/GDWR/classy-config/tree/main/examples/multiple_configs>`_

There are times when having multiple config files would allow for cleaner deployment,
readability, and maintainability of your code base.

To accommodate this, ``ClassyConfig`` allows you to load multiple config files
with designated prefixes, so you can use all the config values alongside each other.

For example, we have the following two separate configuration files:

``config.toml``

.. code-block:: toml

    app_name="Example App"


``database.toml``

.. code-block:: toml

    host="127.0.0.1"
    port=5432


First, load your two configuration files. We'll use the prefix of ``"db"`` for the second one:

.. code-block:: python

    from classy_config import register_config, ConfigValue

    register_config(filepath="config.toml")
    register_config(filepath="database.toml", prefix="db")  # Note the prefix


Now use your config values from both files with ease:

.. code-block:: python

    app_name = ConfigValue("app_name", str)
    print(f"Starting application: {app_name}")

    database_host = ConfigValue("db.host", str)
    database_port = ConfigValue("db.port", int)
    print(f"Connecting to database: {database_host}:{database_port}")


