"""
llvm_snapshot_builder.cmd provides functions for the command line interface.
"""

import sys

from .util import get_action, build_main_parser

if __name__ == "__main__":
    sys.exit(0 if get_action(build_main_parser()).run() else 1)
