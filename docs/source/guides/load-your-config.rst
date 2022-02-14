Load your config
================

ClassyConfig makes loading you config simple.

.. code-block:: python

    from classy_config import register_config

    register_config(filepath="config.toml")

Now you have registered your config, any usage of ``ConfigValue`` will be resolved from the config.

.. code-block:: python

    from classy_config import ConfigValue

    app_name = ConfigValue("app.name", str)
