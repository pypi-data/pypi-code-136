"""
Use a part of your program remotely without making an api

When using the package you can just use the toplevel Server and Client classes,
no need to import the submodules unless you need to change how it works
"""

from . import models

from .client import Client
from .server import Server
