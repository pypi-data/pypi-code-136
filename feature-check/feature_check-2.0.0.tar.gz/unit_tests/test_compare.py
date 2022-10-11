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

""" Test the version comparison functions. """

from __future__ import annotations

import pytest

from feature_check import defs
from feature_check import expr as fexpr
from feature_check import parser as fparser
from feature_check import version as fver

from . import data


def parsed_features() -> dict[str, fver.Version]:
    """Parse the versions of the features used in the test."""
    return {name: fparser.parse_version(value) for name, value in data.FEATURES.items()}


def do_test_compare(var: str, op_name: str, right: str, expected: bool) -> None:
    """Test the comparison functions."""
    feature = " ".join([var, op_name, right])
    mode = fparser.parse_expr(feature)
    assert isinstance(mode, defs.ModeSimple)
    expr = mode.ast
    assert isinstance(expr, fexpr.ExprOp)
    # https://github.com/PyCQA/pylint/issues/7325
    # pylint: disable-next=no-member
    assert len(expr.args) == 2
    # pylint: disable-next=no-member
    assert isinstance(expr.args[0], fexpr.ExprFeature)
    # pylint: disable-next=no-member
    assert isinstance(expr.args[1], fexpr.ExprVersion)

    res = expr.evaluate(parsed_features())
    assert isinstance(res, fexpr.ResultBool)
    assert res.value == expected


@pytest.mark.parametrize("var,op_name,right,expected", data.COMPARE)
def test_compare(var: str, op_name: str, right: str, expected: bool) -> None:
    """Test the comparison functions with word operands."""
    return do_test_compare(var, op_name, right, expected)


@pytest.mark.parametrize("var,op_name,right,expected", data.COMPARE)
def test_synonyms(var: str, op_name: str, right: str, expected: bool) -> None:
    """Test the comparison functions with word operands."""
    return do_test_compare(var, data.SYNONYMS[op_name], right, expected)


@pytest.mark.parametrize("var", (item[0] for item in data.COMPARE))
def test_single(var: str) -> None:
    """Test obtaining the version of a single feature."""
    # pylint: disable=no-member
    mode = fparser.parse_expr(var)
    assert isinstance(mode, defs.ModeSingle)
    assert mode.feature == var
    expr = mode.ast
    assert isinstance(expr, fexpr.ExprFeature)
    assert expr.name == var

    res = expr.evaluate(parsed_features())
    assert isinstance(res, fexpr.ResultVersion)
    ver = res.value
    assert ver.value
    assert ver.components
