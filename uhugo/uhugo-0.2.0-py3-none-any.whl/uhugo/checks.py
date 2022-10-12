import json
import logging
import platform
from pathlib import Path

import requests
from rich import print

log = logging.getLogger(__name__)

if platform.system() == 'Windows':
    from .terminal_commands.windows import *
elif platform.system() == 'Linux' or platform.system() == 'Darwin':
    from .terminal_commands.posix import *
else:
    raise OSError("Unknown OS")


def bin_folder() -> str:
    """
    Gives the path of the user bin folder if exists else a bin folder is created in the
    ``<user home>/bin``

    :return: ``bin`` location
    """

    bin_path = Path(Path.home(), "bin")

    if not bin_path.is_dir():
        log.debug(f"bin directory does not exists. Creating one now. New path: {bin_path!r}")
        bin_path.mkdir()

    return str(bin_path)


def get_latest_version_api(override_version: str = None) -> str:
    """
    Get the latest Hugo version

    :param override_version: An override version of Hugo
    :return: version number
    """

    if override_version is not None:
        hugo_response = requests.get(f"https://api.github.com/repos/gohugoio/hugo/releases/tags/v{override_version}")
        if hugo_response.ok:
            return override_version
        else:
            log.debug("Override version request error occurred", hugo_response.content)
            print(f"\n[red bold]Hugo v{override_version} does not exists. See https://github.com/gohugoio/hugo/releases for more information.")
            exit(1)

    hugo_response = requests.get("https://api.github.com/repos/gohugoio/hugo/releases/latest")
    hugo_response = json.loads(hugo_response.content.decode('utf-8'))['tag_name'][1:]

    return hugo_response
