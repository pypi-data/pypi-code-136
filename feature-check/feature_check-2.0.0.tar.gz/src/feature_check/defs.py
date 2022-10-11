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

"""Constant definitions for the feature-check Python library."""

from __future__ import annotations

import abc
import dataclasses

from . import version as fver


DEFAULT_OPTION = "--features"
DEFAULT_PREFIX = "Features: "
DEFAULT_OUTPUT_FMT = "tsv"

VERSION_STRING = "2.0.0"


class FCError(Exception):
    """A base class for errors in handling a feature-check request."""

    def __init__(self, code: int, msg: str) -> None:
        """Initialize an error object."""
        super().__init__(msg)
        self._code = code
        self._msg = msg

    @property
    def code(self) -> int:
        """Return the numeric error code."""
        return self._code

    @property
    def message(self) -> str:
        """Return a human-readable error message."""
        return self._msg


@dataclasses.dataclass(frozen=True)
class Result:
    """The base class for an expression result."""


@dataclasses.dataclass(frozen=True)
class Expr(metaclass=abc.ABCMeta):
    """The (pretty much abstract) base class for an expression."""

    @abc.abstractmethod
    def evaluate(self, data: dict[str, fver.Version]) -> Result:
        """Evaluate the expression and return a Result object.

        Overridden in actual expression classes.
        """
        raise NotImplementedError(
            f"{type(self).__name__}.evaluate() must be overridden"
        )


@dataclasses.dataclass(frozen=True)
class Mode:
    """Base class for the feature-check operating modes."""


@dataclasses.dataclass(frozen=True)
class ModeList(Mode):
    """List the features supported by the program."""


@dataclasses.dataclass(frozen=True)
class ModeSingle(Mode):
    """Query for the presence or the version of a single feature."""

    feature: str
    ast: Expr


@dataclasses.dataclass(frozen=True)
class ModeSimple(Mode):
    """Verify whether a simple 'feature op version' expression holds true."""

    ast: Expr
