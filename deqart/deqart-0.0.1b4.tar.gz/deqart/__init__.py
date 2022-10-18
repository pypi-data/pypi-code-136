import logging
from pathlib import Path

import packaging.version
import requests

from .api import API as _API
from .db.jobs import estimate_job_runtime, search_jobs, submit_job, wait_for_job
from .version import __version__

formatter = logging.Formatter(fmt="DEQART-PYTHON-SDK - %(levelname)s - %(message)s")
# formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger("deqart-python-sdk")
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def _check_version():
    local_version = packaging.version.parse(__version__)
    if local_version.is_prerelease:
        logger.warning(
            "Development version %s of Deqart Python SDK is being used", __version__
        )
    req = requests.get("https://pypi.python.org/pypi/deqart/json", timeout=5.0)
    if not req.ok:
        return

    # find max version on PyPI
    releases = req.json().get("releases", [])
    pip_version = packaging.version.parse("0")
    for release in releases:
        ver = packaging.version.parse(release)
        if not ver.is_prerelease or local_version.is_prerelease:
            pip_version = max(pip_version, ver)

    if pip_version.major > local_version.major:
        logger.warning(
            "There is a major upgrade of Deqart Python SDK available on PyPI. We recommend upgrading. Run 'pip install --upgrade deqart' to upgrade from your version %s to %s.",
            local_version,
            pip_version,
        )
    elif pip_version > local_version:
        logger.info(
            "There is a newer version of Deqart Python SDK available on PyPI. Run 'pip install --upgrade deqart' to upgrade from your version %s to %s.",
            local_version,
            pip_version,
        )


def init(
    api_token: str | None = None, path_to_config_json: str | Path | None = None
) -> _API:
    """Initializes and authenticates to Deqart platform using the config file.
    If not initialized then $HOME/.config/deqart/config.json
    will be used.

    :param api_token: The API token
    :type api_token: str | None

    :param path_to_config_json: Location to config JSON file
    :type path_to_config_json: str | Path | None
    """
    _api = _API.get_instance()
    _api.init(api_token, config_location=path_to_config_json)
    return _api


_check_version()
