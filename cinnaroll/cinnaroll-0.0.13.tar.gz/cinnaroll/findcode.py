import inspect
import importlib
from modulefinder import ModuleFinder
from types import ModuleType
from typing import Dict


def modules(this_script: str) -> Dict[str, str]:
    extracted_modules = {}
    finder = ModuleFinder()
    finder.run_script(this_script)
    found_modules = finder.modules.items()

    for name, module in found_modules:
        # filtering out dunder functions
        if not name.startswith('__'):
            try:
                imported_module: ModuleType = importlib.import_module(name)
                source_code = inspect.getsource(imported_module)
                extracted_modules[name] = source_code
            except Exception:
                pass

    return extracted_modules
