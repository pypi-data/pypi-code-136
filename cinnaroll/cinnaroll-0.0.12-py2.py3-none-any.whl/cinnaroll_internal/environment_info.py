import sys
from typing import Union, Tuple, List

from cinnaroll_internal import constants


class UnknownFrameworkError(Exception):
    ...


class FrameworkPackageNotFoundError(Exception):
    ...


class EnvironmentInfo:
    def __init__(self, framework: str):
        self.python_version = _get_python_version()
        self.requirements = _get_requirements()
        self.framework_version = _get_framework_version(framework, self.requirements)


def _get_python_version() -> Tuple[int, int, int, str, int]:
    return sys.version_info


def _get_requirements() -> List[str]:
    try:
        from pip._internal.operations import freeze
    except ImportError:
        raise ImportError("Import error occurred while importing pip. Upgrade pip!")
    return list(freeze.freeze())


def _infer_possible_package_names(framework: str) -> Union[str, Tuple[str, ...]]:
    if framework == constants.PYTORCH:
        return constants.PYTORCH_PACKAGE_NAME
    elif framework in (constants.KERAS, constants.TENSORFLOW):
        return constants.TENSORFLOW_PACKAGE_NAME, f"{constants.TENSORFLOW_PACKAGE_NAME}-macos"
    raise UnknownFrameworkError


def _get_framework_version(framework: str, requirements: List[str]) -> str:
    possible_package_names = _infer_possible_package_names(framework)
    possible_framework_version_prefix: Union[str, Tuple[str, ...]]
    if type(possible_package_names) is tuple:
        possible_framework_version_prefix = tuple(map(lambda x: f"{x}==", possible_package_names))
    else:
        possible_framework_version_prefix = f"{possible_package_names}=="
    for req in requirements:
        if req.startswith(possible_framework_version_prefix):
            return req.split("==")[1]
    raise FrameworkPackageNotFoundError(f"Couldn't find one of {possible_package_names} "
                                        f"in packages installed in currently used environment. "
                                        f"Run pip freeze in your terminal to inspect installed packages.")
