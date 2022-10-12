import subprocess

from packaging import version

from . import Hugo, hugo_version_cmd

__all__ = ["check_hugo"]


def check_hugo() -> Hugo:
    """
    Checks for Hugo instillation

    :return Hugo: A dataclass object with ``path``, ``exists`` and ``version``
    """

    try:
        _path = subprocess.check_output(["command", "-v", "hugo"]).strip()
    except Exception:
        return Hugo("", False, version.Version("0"))

    _hugo_version_str = hugo_version_cmd()

    try:
        _hugo_version = _hugo_version_str.decode('utf-8').split(" ")[4].split("/")[0].split("-")[0]
        ver = version.Version(_hugo_version)
    except version.InvalidVersion:
        _hugo_version = _hugo_version_str.decode('utf-8').split(" ")[1].split("-")[0]
        ver = version.Version(_hugo_version)

    return Hugo(_path.decode('utf-8'), True, ver)
