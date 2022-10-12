import subprocess
from dataclasses import dataclass

from packaging import version


@dataclass
class Hugo:
    """Dataclass for Hugo"""
    path: str
    exists: bool
    version: version.Version


def hugo_version_cmd() -> bytes:
    """
    Returns Hugo version

    :return: Hugo version
    """

    return subprocess.check_output(["hugo", "version"]).strip()
