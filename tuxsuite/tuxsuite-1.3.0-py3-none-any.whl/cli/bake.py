# -*- coding: utf-8 -*-

import os
import sys
import json
import argparse
import tuxsuite

from tuxsuite.cli.utils import (
    error,
    file_or_url,
    format_result,
    wait_for_object,
)


def handle_submit(cmdargs, _, config):
    build_definition = cmdargs.build_definition[0]
    try:
        with open(os.path.abspath(build_definition)) as reader:
            data = json.load(reader)
    except Exception:
        sys.stderr.write(
            f"Problem parsing {build_definition}, Is it a valid json file ?\n"
        )
        sys.exit(1)
    if cmdargs.local_manifest:
        data["manifest"] = cmdargs.local_manifest

    data["no_cache"] = cmdargs.no_cache

    try:
        build = tuxsuite.Bitbake(data=data)
    except (AssertionError, tuxsuite.exceptions.TuxSuiteError) as e:
        error(e)
    print(
        "*** WARNING: BITBAKE SUPPORT IS EXPERIMENTAL ***\n"
        "Building targets: {} with bitbake from {} source with distro: {} machine: {} arguments".format(
            build.build_definition.targets,
            build.build_definition.sources,
            build.build_definition.distro,
            build.build_definition.machine,
        )
    )
    try:
        build.build()
        print("uid: {}".format(build.uid))
    except tuxsuite.exceptions.BadRequest as e:
        error(str(e))

    build_result = True

    if cmdargs.no_wait:
        format_result(build.status, tuxapi_url=build.build_data)
    else:
        build_result = wait_for_object(build)

    if cmdargs.download:
        tuxsuite.download.download(build, cmdargs.output_dir)

    if cmdargs.json_out:
        cmdargs.json_out.write(json.dumps(build.status, sort_keys=True, indent=4))
    if not build_result:
        sys.exit(1)


handlers = {
    "submit": handle_submit,
}


def bake_cmd_options(sp):
    sp.add_argument(
        "--json-out",
        help="Write json build status out to a named file path",
        type=argparse.FileType("w", encoding="utf-8"),
    )
    sp.add_argument(
        "-l",
        "--local-manifest",
        type=file_or_url,
        default=None,
        help=(
            "Path to a local manifest file which will be used during repo sync."
            "This input is ignored if sources used is git_trees in the build"
            " definition. Should be a valid XML"
        ),
    )
    sp.add_argument(
        "-n",
        "--no-wait",
        default=False,
        action="store_true",
        help="Don't wait for the builds to finish",
    )
    sp.add_argument(
        "-d",
        "--download",
        default=False,
        action="store_true",
        help="Download artifacts after builds finish. Can't be used with no-wait",
    )
    sp.add_argument(
        "-o",
        "--output-dir",
        default=".",
        help="Directory where to download artifacts",
    )
    sp.add_argument(
        "-C",
        "--no-cache",
        default=False,
        action="store_true",
        help="Build without using any compilation cache",
    )


def setup_parser(parser):
    # "bake submit"
    t = parser.add_parser("submit")
    t.add_argument(
        "build_definition",
        metavar="build_definition",
        help="Path to build_definition.json'",
        nargs=1,
    )
    bake_cmd_options(t)

    return sorted(parser._name_parser_map.keys())
