"""Configuration"""
# Configuration vairables and defaults
# pylint: disable=subprocess-run-check
import argparse
import configparser
import logging
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from typing import Callable, ClassVar

from glob_linters import linters

# Default config file
DEFAULT_CONFIG_FILE_PATH: str = ".github/glob-linters.ini"
MYPY_PACKAGE_REQUIREMENTS_FILE_PATH: str = os.path.abspath(
    ".github/mypy_requirements.txt"
)

# User-defined linter config directory for GitHub action
USER_DEFIEND_LINTER_CONFIG_ROOT: str = os.path.abspath(".github/linter-configs")

# Supported file extension/suffix
SUPPORTED_FILE_SUFFIX: list[str] = [".cpp", ".py"]

logger = logging.getLogger(__name__)


@dataclass
class Configs:
    """Class to store configs/settings"""

    # Exit code record
    return_code: ClassVar[int] = 0

    # Indicator of reading file
    has_read_config_file: ClassVar[bool] = False

    # Lint targets settings
    target_dir: ClassVar[str] = "."
    target_suffix: ClassVar[list[str]] = SUPPORTED_FILE_SUFFIX

    # Running mode
    debug: ClassVar[bool] = False

    # Linter dict for running
    # Clang Linters
    cpplint: ClassVar[linters.Cpplint] = linters.Cpplint("cpplint")
    clang_format: ClassVar[linters.ClangFormat] = linters.ClangFormat("clang-format")
    # Python
    pylint: ClassVar[linters.Pylint] = linters.Pylint("pylint")
    flake8: ClassVar[linters.Flake8] = linters.Flake8("flake8")
    black: ClassVar[linters.Black] = linters.Black("black")
    isort: ClassVar[linters.Isort] = linters.Isort("isort")
    mypy: ClassVar[linters.Mypy] = linters.Mypy("mypy")

    # Linters needed for each file extension
    linters_enabled: ClassVar[dict[str, list[str]]] = {
        ".cpp": ["cpplint", "clang_format"],
        ".py": ["pylint", "flake8", "black", "isort", "mypy"],
    }

    # Available configs
    set_configs: ClassVar[dict[str, dict[str, Callable]]] = {
        "target": {
            "target_dir": lambda x: setattr(Configs, "target_dir", x),
            "target_suffix": lambda x: setattr(
                Configs, "target_suffix", re.split(r"[,\s]", x)
            ),
        },
        "executable": {
            # Clang
            "cpplint": lambda x: setattr(Configs.cpplint, "executable", x),
            "cpplint.options": lambda x: setattr(
                Configs.cpplint,
                "options",
                Configs.cpplint.options + re.split(r"[,\s]", x),
            ),
            "clang_format": lambda x: setattr(Configs.clang_format, "executable", x),
            "clang_format.options": lambda x: setattr(
                Configs.clang_format,
                "options",
                Configs.clang_format.options + re.split(r"[,\s]", x),
            ),
            # Python
            "pylint": lambda x: setattr(Configs.pylint, "executable", x),
            "pylint.options": lambda x: setattr(
                Configs.pylint,
                "options",
                Configs.pylint.options + re.split(r"[,\s]", x),
            ),
            "flake8": lambda x: setattr(Configs.flake8, "executable", x),
            "flake8.options": lambda x: setattr(
                Configs.flake8,
                "options",
                Configs.flake8.options + re.split(r"[,\s]", x),
            ),
            "black": lambda x: setattr(Configs.black, "executable", x),
            "black.options": lambda x: setattr(
                Configs.black, "options", Configs.black.options + re.split(r"[,\s]", x)
            ),
            "isort": lambda x: setattr(Configs.isort, "executable", x),
            "isort.options": lambda x: setattr(
                Configs.isort, "options", Configs.isort.options + re.split(r"[,\s]", x)
            ),
            "mypy": lambda x: setattr(Configs.mypy, "executable", x),
            "mypy.options": lambda x: setattr(
                Configs.mypy, "options", Configs.mypy.options + re.split(r"[,\s]", x)
            ),
        },
        "env": {
            "debug": lambda x: setattr(Configs, "debug", x),
            ".cpp.linters": lambda x: getattr(Configs, "linters_enabled").update(
                {".cpp": re.split(r",\s", x)}
            ),
            ".cpp.disable_linters": lambda x: getattr(
                Configs, "linters_enabled"
            ).update(
                {
                    ".cpp": [
                        value
                        for value in Configs.linters_enabled[".cpp"]
                        if value not in re.split(r"[,\s]", x)
                    ]
                }
            ),
            ".py.linters": lambda x: getattr(Configs, "linters_enabled").update(
                {".py": re.split(r"[,\s]", x)}
            ),
            ".py.disable_linters": lambda x: getattr(Configs, "linters_enabled").update(
                {
                    ".py": [
                        value
                        for value in Configs.linters_enabled[".py"]
                        if value not in re.split(r"[,\s]", x)
                    ]
                }
            ),
        },
        "_set-config-file": {
            "cpplint": lambda: os.symlink(
                os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, "CPPLINT.cfg"),
                "CPPLINT.cfg",
            )
            if os.path.exists(
                os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, "CPPLINT.cfg")
            )
            else -1,
            "clang_format": lambda: os.symlink(
                os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, ".clang-format"),
                ".clang-format",
            )
            if os.path.exists(
                os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, ".clang-format")
            )
            else -1,
            "pylint": lambda: Configs.pylint.options.extend(
                ["--rcfile", os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, ".pylintrc")]
            )
            if os.path.exists(
                os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, ".pylintrc")
            )
            else -1,
            "flake8": lambda: Configs.flake8.options.extend(
                ["--config", os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, ".flake8")]
            )
            if os.path.exists(os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, ".flake8"))
            else -1,
            "black": lambda: Configs.black.options.extend(
                ["--config", os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, ".black")]
            )
            if os.path.exists(os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, ".black"))
            else -1,
            "isort": lambda: Configs.isort.options.extend(
                [
                    "--settings-file",
                    os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, ".isort.cfg"),
                ]
            )
            if os.path.exists(
                os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, ".isort.cfg")
            )
            else -1,
            "mypy": lambda: Configs.mypy.options.extend(
                [
                    "--config-file",
                    os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, ".mypy.ini"),
                ]
            )
            if os.path.exists(
                os.path.join(USER_DEFIEND_LINTER_CONFIG_ROOT, ".mypy.ini")
            )
            else -1,
        },
    }


def parse_config_file(config_file: str) -> None:
    """Parse configuration from configparser-like file

    Parameters
    ----------
    config_file : str
        Configuration file path

    Raises
    ------
    ValueError
        Invalid section/option found in config file
    """
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    for section in config_parser:
        if section == "DEFAULT":
            continue
        if section not in Configs.set_configs:
            raise ValueError(f"No such section supported: {section}")
        for option in config_parser[section]:
            if option not in config_parser[section]:
                raise ValueError(f"No such option supported: {option}")
            if option == "target_suffix":
                diff = set(re.split(r"[,\s]", config_parser[section][option])) - set(
                    SUPPORTED_FILE_SUFFIX
                )
                if len(diff) > 0:
                    raise ValueError(f"No supported file suffix: {diff}")
            Configs.set_configs[section][option](config_parser[section][option])


def parse_args(args: argparse.Namespace) -> None:
    """Parse command line arguments

    Parameters
    ----------
    args : argparse.Namespace
        Arguments returned by `argparse.parse_args`

    Raises
    ------
    ValueError
        Invalid linter name found
    """
    if os.path.exists(args.config_file):
        parse_config_file(args.config_file)
    else:
        Configs.debug = args.debug
        Configs.target_dir = args.target_dir
        Configs.target_suffix = re.split(r"\s", args.target_suffix)
        if args.configs is not None:
            for key, value in map(lambda x: re.split("=", x), args.configs):
                if key in Configs.set_configs["executable"]:
                    if "options" in key:
                        Configs.set_configs["executable"][key](value)
                    else:
                        Configs.set_configs["executable"][key](value)
                elif key in Configs.set_configs["env"]:
                    Configs.set_configs["env"][key](value)
                else:
                    raise ValueError(f"No such linter supported: {key}")


def install_mypy_package_requirements() -> None:
    """Install additional packages for mypy linting"""
    if not os.path.exists(MYPY_PACKAGE_REQUIREMENTS_FILE_PATH):
        logger.info("Not found mypy_requirements.txt, skip package installation")
        return
    logger.info("Install packages for mypy checking...")
    cmd = ["pip", "install", "-r", MYPY_PACKAGE_REQUIREMENTS_FILE_PATH]
    logger.debug("Install command: %s", " ".join(cmd))
    cmd_result = subprocess.run(cmd, capture_output=True)

    logger.debug("Installation output:")
    for line in cmd_result.stdout.decode().strip().split("\n"):
        logger.debug("\t%s", line)

    if cmd_result.returncode != 0:
        logger.error("Package installaltion failed:")
        for line in cmd_result.stderr.decode().strip().split("\n"):
            logger.error("\t%s", line)
        sys.exit(1)


def load_linter_configs() -> None:
    """Load config file for each enabled linter"""
    for ext in Configs.target_suffix:
        for linter_name in Configs.linters_enabled[ext]:
            logger.debug("Setting linter config for [%s]", linter_name)
            # Check whether set config file
            # If set, return None, -1 otherwise
            return_value = Configs.set_configs["_set-config-file"][linter_name]()
            if return_value is None:
                getattr(Configs, linter_name).use_config_file = True
