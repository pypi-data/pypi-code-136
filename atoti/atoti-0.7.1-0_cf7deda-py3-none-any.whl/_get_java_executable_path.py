import os
from pathlib import Path
from typing import Optional

_ATOTI_JAVA_HOME_ENV_VAR = "ATOTI_JAVA_HOME"
_JAVA_HOME_ENV_VAR = "JAVA_HOME"


def _get_java_home() -> Optional[Path]:
    if _ATOTI_JAVA_HOME_ENV_VAR in os.environ:
        return Path(os.environ[_ATOTI_JAVA_HOME_ENV_VAR])
    try:
        from jdk4py import JAVA_HOME  # pylint:disable=nested-import

        return JAVA_HOME
    except ImportError:
        if _JAVA_HOME_ENV_VAR in os.environ:
            return Path(os.environ[_JAVA_HOME_ENV_VAR])

        return None


def get_java_executable_path(*, executable_name: str = "java") -> Path:
    java_home = _get_java_home()

    return java_home / "bin" / executable_name if java_home else Path(executable_name)
