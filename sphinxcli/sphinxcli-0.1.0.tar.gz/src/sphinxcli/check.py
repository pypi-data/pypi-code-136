from os.path import commonpath

from sphinxcli.build import BuildParameters
from sphinxcli.config import get_sphinx_config


def check_build_parameters(params: BuildParameters) -> list[str]:
    errors: list[str] = []
    source = params["source"]
    target = params["target"]
    if not source.exists():
        errors.append(f"Source {source} does not exist.")
    elif not source.is_dir():
        errors.append(f"Source {source} is not a directory.")

    if not target.exists():
        errors.append(f"Target {target} does not exist.")
    elif not target.is_dir():
        errors.append(f"Target {target} is not a directory.")

    if source == target:
        errors.append("Source and target directory are the same.")

    if commonpath([source, target]) == target:
        errors.append(f"Target directory {target} contains source directory.")

    try:
        get_sphinx_config(params["config"])
    except ValueError as exc:
        errors.append(exc.args[0])

    return errors
