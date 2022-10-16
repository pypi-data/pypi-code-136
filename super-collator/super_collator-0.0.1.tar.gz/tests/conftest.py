import argparse
import sys

import pytest

class DebugAction(argparse.Action):
    """Turn on debug mode for coverage tests."""
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        """This is called if the --debug-mode option is passed to pytest."""
        if option_string in self.option_strings:
            # do something to turn on debug mode
            pass



def pytest_addoption(parser):
    parser.addoption(
        "--performance", action="store_true", help="run performance tests"
    )
    parser.addoption(
        "--debug-mode", action=DebugAction, help="turn on DEBUG mode while testing"
    )
