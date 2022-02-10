class ClassyConfigException(BaseException):
    """
    All ClassyConfig exceptions inherit from this exception.

    This is to allow a generic exception handler for
    any exception that could be raised from this module.
    """


class DoubleCreation(ClassyConfigException):
    """Raised when attempting to create the global context for the second time."""


class InstanceNotCreated(ClassyConfigException):
    """Raised when attempting to get a ConfigParam before creating the global context."""
