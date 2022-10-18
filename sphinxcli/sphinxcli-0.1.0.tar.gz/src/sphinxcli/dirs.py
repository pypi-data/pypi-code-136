from pathlib import Path

from sphinxcli.tool_config import ToolConfig


def project_dirs(
    tool_config: ToolConfig,
    srcdir: Path,
    confdir: Path,
    outdir: Path,
    doctreedir: Path,
    builder: str,
) -> dict[str, Path]:
    pyproject = tool_config.pyproject
    if pyproject is not None:
        root_path = pyproject.parent
    else:
        root_path = Path.cwd()

    if not srcdir.is_absolute():
        srcdir = root_path / srcdir

    if not outdir.is_absolute():
        outdir = root_path / outdir

    if not doctreedir.is_absolute():
        doctreedir = root_path / doctreedir

    if not confdir.is_absolute():
        confdir = root_path / confdir

    return {
        "source": srcdir,
        "build": outdir,
        "doctree": doctreedir,
        "config": confdir,
    }
