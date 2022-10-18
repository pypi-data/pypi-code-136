import wefaas

# define the version before the other imports since these need it
__version__ = wefaas.__version__

from .core import Wefaas
