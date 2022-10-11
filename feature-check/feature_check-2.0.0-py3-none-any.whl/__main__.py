# Copyright (c) 2018, 2019, 2021, 2022  Peter Pentchev
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

"""Query a program's list of features."""

from __future__ import annotations

import argparse
import dataclasses
import functools
import sys

try:
    import simplejson as js
except ImportError:
    import json as js  # type: ignore

from . import defs
from . import expr as fexpr
from . import obtain
from . import parser as fparser
from . import version as fver

# functools.singledispatch() will try to parse the type annotation
if sys.version_info < (3, 9):
    from typing import Dict
else:
    Dict = dict


@dataclasses.dataclass(frozen=True)
class Config:
    # pylint: disable=too-many-instance-attributes
    """Runtime configuration for this program."""

    args: list[str]
    display_version: bool
    features_prefix: str
    option_name: str
    output_format: str

    program: str = "(unknown)"


def version() -> None:
    """Display program version information."""
    print(f"feature-check {defs.VERSION_STRING}")


def features() -> None:
    """Display program features information."""
    print(
        f"{defs.DEFAULT_PREFIX}feature-check={defs.VERSION_STRING} "
        f"single=1.0 list=1.0 simple=1.0"
    )


def output_tsv(data: dict[str, fver.Version]) -> None:
    """List the obtained features as tab-separated name/value pairs."""
    for feature in sorted(data.keys()):
        print(f"{feature}\t{data[feature].value}")


def output_json(data: dict[str, fver.Version]) -> None:
    """List the obtained features as a JSON object."""
    print(
        js.dumps(
            {name: value.value for name, value in data.items()},
            sort_keys=True,
            indent=2,
        )
    )


OUTPUT = {"tsv": output_tsv, "json": output_json}


@functools.singledispatch
def process(mode: defs.Mode, cfg: Config, data: dict[str, fver.Version]) -> None:
    """Base function for performing the requested feature-check operation."""
    sys.exit(f"Internal error: process(mode={mode!r}, cfg={cfg!r}, data={data!r}")


@process.register
def process_list(
    _mode: defs.ModeList, cfg: Config, data: Dict[str, fver.Version]
) -> None:
    """List the obtained features using the specified method."""
    OUTPUT[cfg.output_format](data)


@process.register
def process_single(
    mode: defs.ModeSingle, cfg: Config, data: Dict[str, fver.Version]
) -> None:
    """Check whether a single feature is present."""
    if mode.feature in data:
        if cfg.display_version:
            print(data[mode.feature].value)
        sys.exit(0)
    else:
        sys.exit(1)


@process.register
def process_simple(
    mode: defs.ModeSimple, _cfg: Config, data: Dict[str, fver.Version]
) -> None:
    """Evaluate an expression against the obtained features list."""
    res = mode.ast.evaluate(data)
    assert isinstance(
        res, fexpr.ResultBool
    ), f"how to handle a {type(res).__name__} object?"
    sys.exit(0 if res.value else 1)


def main() -> None:
    """The main routine: parse command-line arguments, do things."""
    parser = argparse.ArgumentParser(
        prog="feature-check",
        usage="""
    feature-check [-v] [-O optname] [-P prefix] program feature
    feature-check [-O optname] [-P prefix] program feature op version
    feature-check [-O optname] [-o json|tsv] [-P prefix] -l program
    feature-check -V | -h""",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="store_true",
        help="display program version information and exit",
    )
    parser.add_argument(
        "--features",
        action="store_true",
        help="display supported features and exit",
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="list the features supported by a program",
    )
    parser.add_argument(
        "-O",
        "--option-name",
        type=str,
        default=defs.DEFAULT_OPTION,
        help="the query-features option to pass",
    )
    parser.add_argument(
        "-o",
        "--output-format",
        default=defs.DEFAULT_OUTPUT_FMT,
        choices=sorted(OUTPUT.keys()),
        help="specify the output format for the list",
    )
    parser.add_argument(
        "-P",
        "--features-prefix",
        type=str,
        default=defs.DEFAULT_PREFIX,
        help="the features prefix in the program output",
    )
    parser.add_argument(
        "-v",
        "--display-version",
        action="store_true",
        help="display the feature version",
    )
    parser.add_argument("args", nargs="*", help="the program and features to test")

    args = parser.parse_args()
    if args.version:
        version()
        sys.exit(0)
    if args.features:
        features()
        sys.exit(0)

    program: str | None = args.args.pop(0) if args.args else None
    cfg = Config(
        args=args.args,
        display_version=args.display_version,
        features_prefix=args.features_prefix,
        option_name=args.option_name,
        output_format=args.output_format,
    )

    if args.list:
        if program is None:
            parser.error("No program specified")
        cfg = dataclasses.replace(cfg, program=program)
        mode: defs.Mode = defs.ModeList()
    else:
        if len(cfg.args) < 1:
            parser.error("No program or feature specified")
        cfg = dataclasses.replace(cfg, program=program)
        expr = " ".join(cfg.args)
        try:
            mode = fparser.parse_expr(expr)
        except fparser.ParseError:
            parser.error("Only querying a single feature supported so far")

    try:
        data = obtain.obtain_features(cfg.program, cfg.option_name, cfg.features_prefix)
    except obtain.ObtainError as exc:
        sys.exit(exc.code)

    process(mode, cfg, data)


if __name__ == "__main__":
    main()
