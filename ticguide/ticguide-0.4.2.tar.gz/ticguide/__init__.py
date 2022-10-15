import os
from .version import __version__

__all__ = ['cli', 'pipeline']
__author__ = 'Ashley <ashleychontos@astro.princeton.edu>'

_ROOT = os.path.abspath(os.getcwd())
PATH = os.path.join(_ROOT,'')