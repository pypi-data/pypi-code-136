from __future__ import annotations
import sys
from pathlib import Path

_venv: Path|None = None
_venv_lookedup = False

def get_venv() -> Path|None:
    """ Returns venv Path if any, else None """
    global _venv, _venv_lookedup

    if not _venv_lookedup:
        _venv = None
        _venv_lookedup = True
        cwd = Path.cwd()
        potential_venv = Path(sys.executable).parent.parent
        if cwd in potential_venv.parents:
            _venv = potential_venv

    return _venv
