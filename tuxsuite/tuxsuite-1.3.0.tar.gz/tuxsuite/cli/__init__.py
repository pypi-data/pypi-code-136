# -*- coding: utf-8 -*-

"""
This is the tuxsuite command.
"""


import argparse
import contextlib
import sys

from tuxsuite import __version__
from tuxsuite.cli.config import load_config
from tuxsuite.cli.utils import error
from tuxsuite.cli.bake import (
    handlers as bake_handlers,
    setup_parser as bake_parser,
)
from tuxsuite.cli.build import (
    handlers as build_handlers,
    setup_parser as build_parser,
)
from tuxsuite.cli.plan import (
    handlers as plan_handlers,
    setup_parser as plan_parser,
)
from tuxsuite.cli.test import (
    handlers as test_handlers,
    setup_parser as test_parser,
)
from tuxsuite.cli.results import (
    handlers as results_handlers,
    setup_parser as results_parser,
)


def setup_parser():
    parser = argparse.ArgumentParser(
        prog="tuxsuite",
        description="The TuxSuite CLI is the supported interface to TuxBuild and TuxTest.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s, {__version__}"
    )

    sub_parser = parser.add_subparsers(dest="command", help="Command")
    sub_parser.required = True

    bake = sub_parser.add_parser(
        "bake",
        help="Do an OE/Yocto build with bitbake like 'tuxsuite bake submit <build-definition.json>'",
    ).add_subparsers(dest="sub_command", help="Commands")
    bake.required = True
    bake_cmds = bake_parser(bake)

    build = sub_parser.add_parser("build", help="Run a single build.").add_subparsers(
        dest="sub_command", help="Commands"
    )
    build.required = True
    build_cmds = build_parser(build)

    plan = sub_parser.add_parser("plan", help="Run a plan file.").add_subparsers(
        dest="sub_command", help="Commands"
    )
    plan.required = True
    plan_cmds = plan_parser(plan)

    test = sub_parser.add_parser("test", help="Test a kernel.").add_subparsers(
        dest="sub_command", help="Commands"
    )
    test.required = True
    test_cmds = test_parser(test)

    results = sub_parser.add_parser("results", help="Fetch results.").add_subparsers(
        dest="sub_command", help="Commands"
    )
    results.required = True
    results_cmds = results_parser(results)

    return (
        parser,
        {
            "bake": bake_cmds,
            "build": build_cmds,
            "plan": plan_cmds,
            "test": test_cmds,
            "results": results_cmds,
        },
    )


def main():
    (parser, cmds) = setup_parser()

    if "--help" not in sys.argv and "-h" not in sys.argv:
        with contextlib.suppress(IndexError):
            if sys.argv[1] == "results" and sys.argv[2] not in cmds["results"]:
                sys.argv.insert(2, "fetch")
            elif sys.argv[1] == "build" and sys.argv[2] not in cmds["build"]:
                sys.argv.insert(2, "submit")
            elif sys.argv[1] == "plan" and sys.argv[2] not in cmds["plan"]:
                sys.argv.insert(2, "submit")
            elif sys.argv[1] == "test" and sys.argv[2] not in cmds["test"]:
                sys.argv.insert(2, "submit")

    (options, extra_arguments) = parser.parse_known_args()

    cfg = load_config()
    # Handle command
    if options.command == "results":
        results_handlers[options.sub_command](options, extra_arguments, cfg)
        return
    elif options.command == "bake":
        bake_handlers[options.sub_command](options, extra_arguments, cfg)
        return
    elif options.command == "build":
        build_handlers[options.sub_command](options, extra_arguments, cfg)
        return
    elif options.command == "test":
        test_handlers[options.sub_command](options, extra_arguments, cfg)
        return
    elif options.command == "plan":
        plan_handlers[options.sub_command](options, extra_arguments, cfg)
        return
    else:
        error("Unknown sub command")
        sys.exit(2)


if __name__ == "__main__":
    sys.exit(main())
