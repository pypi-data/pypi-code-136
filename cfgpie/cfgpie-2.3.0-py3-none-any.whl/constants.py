# -*- coding: UTF-8 -*-

from os.path import dirname, realpath, join
from sys import modules
from types import ModuleType
from typing import TypeVar
from weakref import WeakValueDictionary

# types:
Key = TypeVar("Key")
Value = TypeVar("Value")

# container for all instances:
INSTANCES = WeakValueDictionary()

# main python module:
MODULE: ModuleType = modules.get("__main__")

# root directory:
ROOT: str = dirname(realpath(MODULE.__file__))

# config default file path:
CONFIG: str = join(ROOT, "config", "config.ini")
