# Copyright (c) 2018, 2019, 2021  Peter Pentchev <roam@ringlet.net>
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

"""Query a program for the list of features that it supports."""

from __future__ import annotations

import subprocess

from . import defs
from . import parser as fparser
from . import version as fver


class ObtainError(defs.FCError):
    """A base class for errors in obtaining the program's features."""


class ObtainExecError(ObtainError):
    """An error that occurred while executing the queried program."""

    def __init__(self, exc: Exception) -> None:
        """Initialize an error object."""
        super().__init__(1, str(exc))


class ObtainNoFeaturesError(ObtainError):
    """An error that occurred while looking for the features line."""

    def __init__(self, program: str, option: str, prefix: str) -> None:
        """Initialize an error object."""
        super().__init__(
            2,
            f"The '{program} {option}' output did not contain "
            f"a single '{prefix}' line",
        )


def obtain_features(
    program: str,
    option: str = defs.DEFAULT_OPTION,
    prefix: str = defs.DEFAULT_PREFIX,
) -> dict[str, fver.Version]:
    """Execute the specified program and get its list of features.

    The program is run with the specified query option (default:
    "--features") and its output is examined for a line starting with
    the specified prefix (default: "Features: ").  The rest of the line
    is parsed as a whitespace-separated list of either feature names or
    "name=version" pairs.  The function returns a dictionary of the features
    obtained with their versions (or "1.0" if only a feature name was found
    in the program's output).

        import feature_check

        data = feature_check.obtain_features("timelimit")
        print(data.get("subsecond", "not supported"))

    For programs that need a different command-line option to list features:

        import feature_check

        print("SSL" in feature_check.obtain_features("curl",
                                                     option="--version"))
    """
    try:
        res = subprocess.run(
            [program, option],
            capture_output=True,
            check=False,
            stdin=None,
        )
        if res.returncode != 0 or res.stderr.decode() != "":
            # It does not support '--features', does it?
            raise Exception(
                f"The {program} program does not seem to support "
                f"the {option} option for querying features"
            )

        lines = res.stdout.decode().split("\n")
    except Exception as exc:
        # Something went wrong in the --features processing
        raise ObtainExecError(exc) from exc

    matching = [line for line in lines if line.startswith(prefix)]
    if len(matching) != 1:
        raise ObtainNoFeaturesError(program, option, prefix)

    return fparser.parse_features_line(matching[0][len(prefix) :])
