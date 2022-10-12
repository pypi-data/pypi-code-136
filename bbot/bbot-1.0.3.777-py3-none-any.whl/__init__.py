# version placeholder (replaced by poetry-dynamic-versioning)
__version__ = "v1.0.3.777"

# global app config
from .core import configurator

config = configurator.config

# helpers
from .core import helpers
