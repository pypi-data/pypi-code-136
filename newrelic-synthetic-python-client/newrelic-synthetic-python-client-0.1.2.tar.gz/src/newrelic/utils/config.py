from typing import List
import os
import pathlib

from newrelic.utils.log import log


def get_json_file() -> pathlib.Path:
    """Search the NR configuration JSON file in some places.

    Search order
    1. $HOME/.newrelic-python-client.json
    2. $HOME/.config/newrelic-python-client.json
    3. $CWD/newrelic-python-client.json
    4. Specified by environment $NEWRELIC_PYTHON_CLIENT_JSON

    The higher number will take precedence. If both #1 and #2 exist, #2 will
    take effect. If all #1, #2, #3, #4 exist, #4 will take effect.

    :return: the configuration JSON file path
    :rtype: pathlib.Path
    """
    p = None
    fname = "newrelic-python-client.json"
    home_dir = pathlib.Path().home()
    env_path = os.getenv(
        "NEWRELIC_PYTHON_CLIENT_JSON",
        "NEWRELIC_PYTHON_CLIENT_JSON"  # make sure the value is not exist file
        )
    path_to_test: List[pathlib.Path] = [
        home_dir / f'.{fname}',
        home_dir / ".config" / fname,
        pathlib.Path().cwd() / fname,
        pathlib.Path(env_path),
    ]
    for _p in path_to_test:
        log.debug(f"Check if file exists: {_p}")
        if _p.exists():
            log.debug(f"File {_p} exist, overwrite the previous value {p}")
            p = _p
    assert p is not None, "Unable to find any configuration file"
    log.info(f"Using file {p} as configuration")
    return p
