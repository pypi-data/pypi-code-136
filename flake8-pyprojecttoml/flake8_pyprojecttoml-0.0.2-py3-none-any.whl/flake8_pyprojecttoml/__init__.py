"""Flake8 extension to add pyproject.toml support."""

from __future__ import annotations

import sys
from configparser import RawConfigParser
from pathlib import Path
from typing import TYPE_CHECKING

from flake8.options import config  # type: ignore

if sys.version_info < (3, 11):  # pragma: no cover
    import tomli as tomllib
else:  # pragma: no cover
    import tomllib

if TYPE_CHECKING:
    from typing import Any

    from flake8.options.manager import OptionManager  # type: ignore


class Dummy:  # pylint: disable=too-few-public-methods
    """Dummy class used as reporter entry point."""


_parse_config = config.parse_config


def parse_config(
    option_manager: OptionManager,
    cfg: RawConfigParser,
    cfg_dir: str,
) -> dict[str, Any]:
    """Parse and normalize the typed configuration options."""
    path = Path.cwd()

    def stat_key(path: Path) -> tuple[int, int]:
        stat = path.stat()
        return stat.st_ino, stat.st_dev

    prevkey = None
    pathkey = stat_key(path)
    while pathkey != prevkey:
        pyproject = path / 'pyproject.toml'
        if pyproject.exists():
            with pyproject.open('rb') as file:
                dct = tomllib.load(file).get('tool', {}).get('flake8')
                if dct:
                    cfg = RawConfigParser()
                    cfg.add_section('flake8')
                    for key, value in dct.items():
                        value = str(value) if isinstance(value, bool) else value
                        cfg.set('flake8', key, value)
                    return _parse_config(option_manager, cfg, str(path))  # type: ignore
        prevkey = pathkey
        path = path.parent

    return _parse_config(option_manager, cfg, cfg_dir)  # type: ignore


config.parse_config = parse_config
