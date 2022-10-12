import os
import subprocess

import psutil
from packaging import version

from . import Hugo, hugo_version_cmd

__all__ = ["check_hugo"]


def _check_hugo_cmd_term() -> Hugo:
    """
    Checks for Hugo instillation using cmd

    :return Hugo: A dataclass object with ``path``, ``exists`` and ``version``
    """

    try:
        _path = subprocess.check_output(["where.exe", "hugo"]).strip()
    except Exception:
        return Hugo("", False, version.Version("0"))

    _hugo_version_str = hugo_version_cmd()

    try:
        _hugo_version = _hugo_version_str.decode('utf-8').split(" ")[4].split("/")[0]
        ver = version.Version(_hugo_version)
    except version.InvalidVersion:
        _hugo_version = _hugo_version_str.decode('utf-8').split(" ")[1].split("-")[0]
        ver = version.Version(_hugo_version)

    return Hugo(_path.decode('utf-8'), True, ver)


def _check_hugo_pwsh_term() -> Hugo:
    """
    Checks for Hugo instillation using pwsh

    :return Hugo: A dataclass object with ``path``, ``exists`` and ``version``
    """

    try:
        _path = subprocess.check_output(["gcm", "hugo"]).strip()
    except Exception:
        return Hugo("", False, version.Version("0"))

    _hugo_version_str = hugo_version_cmd()

    try:
        _hugo_version = _hugo_version_str.decode('utf-8').split(" ")[4].split("/")[0]
        ver = version.Version(_hugo_version)
    except version.InvalidVersion:
        _hugo_version = _hugo_version_str.decode('utf-8').split(" ")[1].split("-")[0]
        ver = version.Version(_hugo_version)

    return Hugo(_path.decode('utf-8'), True, ver)


def check_hugo() -> Hugo:
    """
    Checks for Hugo instillation

    :return Hugo: A dataclass object with ``path``, ``exists`` and ``version``
    """

    parent_pid = os.getppid()
    term = psutil.Process(parent_pid).name()

    if term == "pwsh":
        return _check_hugo_pwsh_term()
    else:
        return _check_hugo_cmd_term()
