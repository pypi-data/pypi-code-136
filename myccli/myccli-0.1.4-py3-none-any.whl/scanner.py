import importlib
import os
import sys
from typing import Optional

from myc.build import is_building


class Scanner:
    """
    Runs a Mycelium project and gathers information on the way it's structured.
    """
    def __init__(self, project_path: str, app_path: str):
        self._project_path = project_path
        self._app_path = app_path
        self._app = None

    @property
    def app(self):
        return self._app

    def _scan_in_chdir(self):
        module_name, app_name = self._app_path.split(':')
        module = importlib.import_module(module_name)
        self._app = getattr(module, app_name)

    def scan(self):
        # change current directory to project path and update sys.path accordingly.
        last_dir = os.getcwd()
        os.chdir(self._project_path)
        sys.path.insert(0, '')

        try:
            is_building[0] = True
            self._scan_in_chdir()
        finally:
            is_building[0] = False

            # restore path settings
            sys.path.pop(0)
            os.chdir(last_dir)

        return self._app
