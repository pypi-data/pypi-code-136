"""
Module _Cli
"""

import argparse
import signal
import sys

import requests
from pkg_resources import get_distribution
from pystub._cli_core import CliCore
from pystub._common_utils import exit_with_code
from pystub._logger import init_pystub_cli_logger

from . import _cli_modules

LOG = init_pystub_cli_logger(loglevel="ERROR")
BANNER = " pystub "


class SetVerbosity(argparse.Action):
    """
    Class: SetVerbosity
    """

    def __call__(self, parser, namespace, values, option_string=None):
        LOG.setLevel(_get_log_level([option_string]))


NAME = "pystub"
DESCRIPTION = "pystub"
GLOBAL_ARGS = [
    [
        ["-q", "--quiet"],
        {
            "action": SetVerbosity,
            "nargs": 0,
            "help": "reduce output to the minimum",
            "dest": "_quiet",
        },
    ],
    [
        ["-d", "--debug"],
        {
            "action": SetVerbosity,
            "nargs": 0,
            "help": "adds debug output and tracebacks",
            "dest": "_debug",
        },
    ],
]


def _welcome():
    LOG.info("{}\n".format(BANNER))
    try:
        # check_for_update()  #Not implemented yet
        pass
    except Exception:  # pylint: disable=broad-except
        LOG.debug("Unexpected error", exc_info=True)


def _setup_logging(args, exit_func=exit_with_code):
    log_level = _get_log_level(args, exit_func=exit_func)
    LOG.setLevel(log_level)
    return log_level


def _print_tracebacks(log_level):
    return log_level == "DEBUG"


def _get_log_level(args, exit_func=exit_with_code):
    log_level = "INFO"
    if ("-d" in args or "--debug" in args) and ("-q" in args or "--quiet" in args):
        exit_func(1, "--debug and --quiet cannot be specified simultaneously")
    if "-d" in args or "--debug" in args:
        log_level = "DEBUG"
    if "-q" in args or "--quiet" in args:
        log_level = "ERROR"
    return log_level


def _sigint_handler(signum, frame):
    LOG.debug("SIGNAL {} caught at {}".format(signum, frame))
    exit_with_code(1)


def get_pip_version(url):
    """
    Given the url to PypI package info url returns the current live version
    """
    return requests.get(url, timeout=5.0).json()["info"]["version"]


def get_installed_version():
    """
    Given the url to PypI package info url returns the installed version
    """
    try:
        return get_distribution(NAME).version
    except Exception:  # pylint: disable=broad-except
        return "[local source] no pip module installed"


def main(cli_core_class=CliCore, exit_func=exit_with_code):
    """
    Init: ENV
    """
    signal.signal(signal.SIGINT, _sigint_handler)
    log_level = _setup_logging(sys.argv)
    args = sys.argv[1:]
    if not args:
        args.append("-h")
    try:
        _welcome()
        version = get_installed_version()
        cli = cli_core_class(NAME, _cli_modules, DESCRIPTION, version, GLOBAL_ARGS)
        cli.parse(args)
        cli.run()

    except Exception as err:  # pylint: disable=broad-except
        LOG.error(str(err), exc_info=_print_tracebacks(log_level))
        exit_func(1)
