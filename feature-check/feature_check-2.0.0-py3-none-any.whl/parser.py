# Copyright (c) 2022  Peter Pentchev <roam@ringlet.net>
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

"""Parse feature names, versions, and simple expressions."""

from __future__ import annotations

import pyparsing as pyp

from . import defs
from . import expr as fexpr
from . import version as fver


_p_comp_num = pyp.Word(pyp.srange("[0-9]"))

_p_comp_rest = pyp.Word(pyp.srange("[A-Za-z~-]"), pyp.srange("[0-9A-Za-z~-]"))

_p_version_comp = (
    _p_comp_num.set_results_name("num")
    + pyp.Opt(_p_comp_rest.set_results_name("rest_first"))
) | _p_comp_rest.set_results_name("rest_only")

_p_version = _p_version_comp + pyp.ZeroOrMore(
    pyp.Char(".").suppress() + _p_version_comp
)

_p_feature = pyp.Word(pyp.srange("[A-Za-z0-9_-]"))

_p_op_sign = pyp.one_of(["<=", "<", "=", ">=", ">"])

_p_op_word = pyp.one_of(["le", "lt", "eq", "ge", "gt"])

_p_op_sign_and_value = (
    pyp.Opt(pyp.White()).suppress()
    + _p_op_sign
    + pyp.Opt(pyp.White()).suppress()
    + _p_version
)

_p_op_word_and_value = (
    pyp.White().suppress() + _p_op_word + pyp.White().suppress() + _p_version
)

_p_expr = _p_feature + pyp.Opt(_p_op_sign_and_value | _p_op_word_and_value)

_p_feature_version = _p_feature + pyp.Opt(pyp.Literal("=").suppress() + _p_version)

_p_features_line = _p_feature_version + pyp.ZeroOrMore(
    pyp.White().suppress() + _p_feature_version
)


@_p_version_comp.set_parse_action
def _process_version_comp(tokens: pyp.ParseResults) -> fver.VersionComponent:
    """Build a `VersionComponent` object out of the numeric and string parts."""
    tok_dict: dict[str, str] = tokens.as_dict()
    num_str = tok_dict.get("num")
    rest = tok_dict.get("rest_first", tok_dict.get("rest_only", ""))
    return fver.VersionComponent(
        num=int(num_str) if num_str is not None else None, rest=rest
    )


@_p_version.set_parse_action
def _process_version(tokens: pyp.ParseResults) -> fver.Version:
    """Build a `Version` object out of the version components."""
    res = tokens.as_list()
    assert all(isinstance(comp, fver.VersionComponent) for comp in res), repr(res)
    return fver.Version(value=".".join(str(comp) for comp in res), components=res)


@_p_op_sign.set_parse_action
def _parse_op_sign(tokens: pyp.ParseResults) -> fexpr.BoolOp:
    """Parse a boolean operation written as a sign ("<", ">=", etc)."""
    return fexpr.OPS[tokens[0]]


@_p_op_word.set_parse_action
def _parse_op_word(tokens: pyp.ParseResults) -> fexpr.BoolOp:
    """Parse a boolean operation written as a sign ("lt", "ge", etc)."""
    return fexpr.OPS[tokens[0]]


@_p_expr.set_parse_action
def _parse_expr(tokens: pyp.ParseResults) -> defs.Mode:
    """Build a `Mode` out of a single feature name or a simple expression."""
    res = tokens.as_list()
    if len(res) < 1 or not isinstance(res[0], str):
        raise ParseError(2, f"Weird expr parse results: {res!r}")
    feature_name = res[0]
    feature = fexpr.ExprFeature(feature_name)
    if len(res) == 1:
        return defs.ModeSingle(feature=feature_name, ast=feature)

    if (
        len(res) != 3
        or not isinstance(res[1], fexpr.BoolOp)
        or not isinstance(res[2], fver.Version)
    ):
        raise ParseError(2, f"Weird expr parse results: {res!r}")
    return defs.ModeSimple(
        ast=fexpr.ExprOp(op=res[1], args=[feature, fexpr.ExprVersion(res[2])])
    )


@_p_feature_version.set_parse_action
def _parse_feature_version(tokens: pyp.ParseResults) -> tuple[str, fver.Version]:
    """Parse a feature name and a version, defaulting to "1.0"."""
    res = tokens.as_list()
    if len(res) < 1 or not isinstance(res[0], str):
        raise ParseError(2, f"Weird feature/version parse results: {res!r}")
    feature = res[0]
    if len(res) == 1:
        return (feature, parse_version("1.0"))

    if len(res) != 2 or not isinstance(res[1], fver.Version):
        raise ParseError(2, f"Weird feature/version parse results: {res!r}")
    return (feature, res[1])


@_p_features_line.set_parse_action
def _parse_features_line(tokens: pyp.ParseResults) -> dict[str, fver.Version]:
    """Build a features dictionary out of the parsed name/version tuples."""
    res = tokens.as_list()
    if len(res) < 1 or not all(
        isinstance(pair, tuple)
        and len(pair) == 2
        and isinstance(pair[0], str)
        and isinstance(pair[1], fver.Version)
        for pair in res
    ):
        raise ParseError(2, f"Weird features line parse results: {res!r}")
    return dict(res)


_p_version_complete = _p_version.leave_whitespace()

_p_expr_complete = _p_expr.leave_whitespace()

_p_features_line_complete = _p_features_line.leave_whitespace()


class ParseError(defs.FCError):
    """An error that occurred while parsing the expression."""


def parse_version(value: str) -> fver.Version:
    """Parse a version string into a `Version` object."""
    res = _p_version_complete.parse_string(value).as_list()
    if len(res) != 1:
        raise ParseError(
            2, f"Could not parse {value!r} as a version string (result: {res!r})"
        )
    ver = res[0]
    if not isinstance(ver, fver.Version) or ver.value != value:
        raise ParseError(
            2,
            f"Could not parse the whole of {value!r} as a version string "
            f"(parsed {ver!r} from {res!r})",
        )
    return ver


def parse_expr(expr: str) -> defs.Mode:
    """Parse a simple "feature-name op version" expression.

    If the expression is valid, return an `Expr` object corresponding
    to the specified check.  Use this object's `evaluate()` method and
    pass a features dictionary as returned by the `obtain_features()`
    function to get a `Result` object; for simple expressions it will be
    a `ResultBool` object with a boolean `value` member.

        from feature_check import expr as fexpr
        from feature_check import obtain as fobtain

        data = fobtain.obtain_features("timelimit");
        expr = fexpr.parse_simple("subsecond > 0")
        print(expr.evaluate(data).value)
    """
    res = _p_expr_complete.parse_string(expr).as_list()
    if len(res) != 1 or not isinstance(res[0], defs.Mode):
        raise ParseError(
            2, f"Could not parse {expr!r} as an expression (results: {res!r})"
        )
    return res[0]


def parse_features_line(features_line: str) -> dict[str, fver.Version]:
    """Parse the features list, default to version "1.0"."""
    res = _p_features_line_complete.parse_string(features_line).as_list()
    if len(res) != 1 or not isinstance(res[0], dict):
        raise ParseError(
            2,
            f"Could not parse {features_line!r} as a features line (results: {res!r})",
        )
    return res[0]
