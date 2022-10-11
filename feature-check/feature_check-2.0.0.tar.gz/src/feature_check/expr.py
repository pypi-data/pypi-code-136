# Copyright (c) 2018, 2019, 2021, 2022  Peter Pentchev <roam@ringlet.net>
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

"""Expression evaluation for the feature-check Python library."""

from __future__ import annotations

import dataclasses

from typing import Callable, List

from . import defs
from . import version as fver


BoolOpFunction = Callable[[List[defs.Result]], bool]


@dataclasses.dataclass(frozen=True)
class ResultBool(defs.Result):
    """A boolean result of an expression; the "value" member is boolean."""

    value: bool

    def __str__(self) -> str:
        return f"ResultBool: {self.value}"


@dataclasses.dataclass(frozen=True)
class ResultVersion(defs.Result):
    """A version number as a result of an expression.

    The "value" member is the version number string.
    """

    value: fver.Version

    def __str__(self) -> str:
        return f"ResultVersion: {self.value.value}"


@dataclasses.dataclass(frozen=True)
class ExprFeature(defs.Expr):
    """An expression that returns a program feature name as a string."""

    name: str

    def evaluate(self, data: dict[str, fver.Version]) -> ResultVersion:
        """Look up the feature, return the result in a ResultVersion object."""
        return ResultVersion(value=data[self.name])


@dataclasses.dataclass(frozen=True)
class ExprVersion(defs.Expr):
    """An expression that returns a version number for a feature."""

    value: fver.Version

    def evaluate(self, _data: dict[str, fver.Version]) -> ResultVersion:
        """Return the version number as a ResultVersion object."""
        return ResultVersion(value=self.value)


@dataclasses.dataclass(frozen=True)
class BoolOp:
    """A two-argument boolean operation."""

    args: list[type[defs.Result]]
    action: BoolOpFunction


def _def_op_bool_ver(check: Callable[[int], bool]) -> BoolOpFunction:
    def _op_bool_ver(args: list[defs.Result]) -> bool:
        """Check whether the arguments are in the expected relation."""
        assert len(args) == 2
        assert isinstance(args[0], ResultVersion)
        assert isinstance(args[1], ResultVersion)
        return check(fver.version_compare(args[0].value, args[1].value))

    return _op_bool_ver


NAMED_OPS = {
    "lt": BoolOp(
        args=[ResultVersion, ResultVersion],
        action=_def_op_bool_ver(lambda res: res < 0),
    ),
    "le": BoolOp(
        args=[ResultVersion, ResultVersion],
        action=_def_op_bool_ver(lambda res: res <= 0),
    ),
    "eq": BoolOp(
        args=[ResultVersion, ResultVersion],
        action=_def_op_bool_ver(lambda res: res == 0),
    ),
    "ge": BoolOp(
        args=[ResultVersion, ResultVersion],
        action=_def_op_bool_ver(lambda res: res >= 0),
    ),
    "gt": BoolOp(
        args=[ResultVersion, ResultVersion],
        action=_def_op_bool_ver(lambda res: res > 0),
    ),
}

SYNONYMS = {"<": "lt", "<=": "le", "=": "eq", ">=": "ge", ">": "gt"}

OPS = dict(
    list(NAMED_OPS.items())
    + [(name, NAMED_OPS[value]) for name, value in SYNONYMS.items()],
)


@dataclasses.dataclass(frozen=True)
class ExprOp(defs.Expr):
    """A two-argument operation expression."""

    op: BoolOp  # pylint: disable=invalid-name
    args: list[defs.Expr]

    def __post_init__(self) -> None:
        """Validate the passed arguments."""
        # TODO(roam): handle all, any  # pylint: disable=fixme
        if len(self.args) != len(self.op.args):
            raise ValueError("args")

    def evaluate(self, data: dict[str, fver.Version]) -> ResultBool:
        """Evaluate the expression over the specified data."""
        args = [expr.evaluate(data) for expr in self.args]

        # TODO(roam): handle all, any  # pylint: disable=fixme
        for (idx, value) in enumerate(args):
            if not isinstance(value, self.op.args[idx]):
                raise ValueError(f"op argument {idx}")

        return ResultBool(value=self.op.action(args))
