from typing import List, Dict, Any, Union, Callable, Optional, Tuple
from pathlib import Path

from .io import prompt_yes_no
from .proc import which, call


def system_has_python3():
    return which("python3")


def get_python_version(python):
    return call([python, "--version"])[0].split()[-1]


def dir_is_venv(dir: Path):
    python = dir.joinpath("bin", "python")
    return python.exists() and python


def venv_has_pip(dir: Path):
    return venv_has_module(dir, "pip")


def venv_has_module(dir: Path, mod: str):
    python = dir_is_venv(dir)
    if python is not None:
        cmd = [python, "-c", f"import {mod}"]
        out, err = call(cmd)
    return not err


def create_venv_in_dir(dir: Path):
    import venv
    create = True
    if dir.exists():
        create = prompt_yes_no(f"Directory {dir} already exists. Overwrite? ")
    if create:
        venv.create(dir, system_site_packages=False, clear=True,
                    symlinks=False, upgrade=False, with_pip=True)


def install_requirements_in_venv(dir: Path, requirements_file: Path):
    python = dir_is_venv(dir)
    if python is not None and venv_has_pip(dir):
        out, err = call(f"{python} -m pip install -r {requirements_file}")
    if err:
        raise ValueError(err)


def get_venv_python_version(dir: Path):
    python = dir.joinpath("bin", "python")
    if python.exists():
        return get_python_version(python)
    else:
        raise FileNotFoundError(f"{python} not found")
