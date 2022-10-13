import importlib.util
import sys
from types import ModuleType
from pathlib import Path
from typing import Final


def require(path: str, name: str = "random_name"):
    """
    my_var = require("../path/from/variables.py")

    print(my_var.x) #=> 983

    print(my_var.y) #=> 32,66

    ########################With Sambura###################################

    with Sambura(require("../path/from/variables.py")): import x as var_1, y as var_2

    print(var_1) #=> 983

    print(var_2) #=> 32,66

    """
    DIR: Final[Path] = Path(path).resolve()
    spec_loc = importlib.util.spec_from_file_location(name, DIR)
    module = importlib.util.module_from_spec(spec_loc)
    sys.modules[name] = module
    spec_loc.loader.exec_module(module)
    success: ModuleType = __import__(name, globals(), locals(), ["*"], 0)
    del sys.modules[name]
    return success