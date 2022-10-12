"""Command line for bfet"""
import argparse
from typing import Dict, Union


def analyse_args(args: Dict[str, Union[str, bool]]):
    modules = args.get("modules")
    testing_library = args.get("testing-library")
    coverage = args.get("coverage")
    if modules:
        pass
    if testing_library:
        pass
    if coverage:
        pass


def cli():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-m",
        "--modules",
        nargs="?",
        help=(
            "A list of modules to create tests from. If no module is provided, a test"
            " is created for everything."
        ),
    )

    parser.add_argument(
        "-tl",
        "--testing-library",
        nargs="?",
        default="pytest",
        choices=["pytest", "unittest", "nose"],
        help="The library used to run the tests. The default is set to pytest",
    )

    parser.add_argument(
        "-c",
        "--coverage",
        action="store_true",
        help="Create coverage for the tests ran.",
    )

    parser.add_argument(
        "-cs",
        "--create-settings",
        action="store_true",
        help="Create the defaults settings if there.",
    )

    analyse_args(vars(parser.parse_args()))
