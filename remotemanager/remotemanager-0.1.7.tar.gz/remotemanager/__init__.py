from .dataset.dataset import *  # noqa: F403
from .connection.url import *  # noqa: F403
from .logging.log import *  # noqa: F403

__all__ = ['Dataset', 'URL']   # noqa: F405
__version__ = '0.1.7'

# attach a global Logger to the manager
Logger = Handler()    # noqa: F405
