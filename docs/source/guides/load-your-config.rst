Load Your Config
================

ClassyConfig makes loading your config simple:

.. code-block:: python

    from classy_config import register_config

    register_config(filepath="config.toml")

Now that you have registered your config, any usage of ``ConfigValue``
will be resolved from the registered config file:

.. code-block:: python

    from classy_config import ConfigValue

    app_name = ConfigValue("app.name", str)
