"""cornflakes (Top-level package).
__________________________________

.. currentmodule:: cornflakes

.. autosummary::
   :toctree: _generate

    ini_load
    eval_type
    eval_datetime
    eval_csv
    extract_between
    apply_match
    ini_config
    generate_config_group
"""  # noqa: RST303 D205
from _cornflakes import apply_match, eval_csv, eval_datetime, eval_type, extract_between, ini_load
from cornflakes.decorator import ini_config, ini_group
from cornflakes.config import generate_config_group
from cornflakes.click import make_cli

__author__ = "Semjon Geist"
__email__ = "semjon.geist@ionos.com"
__version__ = "2.4.6"

__all__ = [
    "ini_load",
    "eval_type",
    "eval_datetime",
    "eval_csv",
    "extract_between",
    "apply_match",
    "ini_config",
    "ini_group",
    "generate_config_group",
    "make_cli",
]
