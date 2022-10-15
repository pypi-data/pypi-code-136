"""
This module is part of the 'web-compressor' package,
which is released under GPL-3.0-only license.
"""

from .handler import Handler
from .hasher import Hasher
from .minifier import Minifier
from .optimizer import Optimizer

__all__ = [
    # Base class
    "Handler",
    # Main classes
    "Hasher",
    "Minifier",
    "Optimizer",
]
