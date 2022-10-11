# copyright 2004-2021 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of rql.
#
# rql is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# rql is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with rql. If not, see <http://www.gnu.org/licenses/>.
"""Miscellaneous utilities for RQL."""

import string

from logilab.database import SQL_FUNCTIONS_REGISTRY, FunctionDescr, CAST
from logilab.common.decorators import monkeypatch

from rql._exceptions import BadRQLQuery
from typing import (
    TYPE_CHECKING,
    Set,
    Optional,
    Mapping,
    Any,
    Callable,
    Generator,
    List,
    Union as Union_,
)

if TYPE_CHECKING:
    import rql
    import logilab

    from rql.base import BaseNode

__docformat__: str = "restructuredtext en"


def decompose_b26(index: int, table: str = string.ascii_uppercase) -> str:
    """Return a letter (base-26) decomposition of index."""
    div, mod = divmod(index, 26)

    if div == 0:
        return table[mod]

    return decompose_b26(div - 1) + table[mod]


class rqlvar_maker:
    """Yields consistent RQL variable names.

    :param stop: optional argument to stop iteration after the Nth variable
                 default is None which means 'never stop'
    :param defined: optional dict of already defined vars
    """

    # NOTE: written a an iterator class instead of a simple generator to be
    #       picklable

    def __init__(
        self,
        stop: Optional[int] = None,
        index: int = 0,
        defined: Optional[Mapping[str, Any]] = None,
        aliases: Optional[Mapping[str, Any]] = None,
    ) -> None:
        self.index = index
        self.stop = stop
        self.defined = defined
        self.aliases = aliases

    def __iter__(self):
        return self

    def __next__(self) -> str:
        while self.stop is None or self.index < self.stop:
            var = decompose_b26(self.index)
            self.index += 1
            if self.defined is not None and var in self.defined:
                continue
            if self.aliases is not None and var in self.aliases:
                continue
            return var
        raise StopIteration()

    next = __next__


KEYWORDS: Set[str] = set(
    (
        "INSERT",
        "SET",
        "DELETE",
        "UNION",
        "WITH",
        "BEING",
        "WHERE",
        "AND",
        "OR",
        "NOT",
        "IN",
        "LIKE",
        "ILIKE",
        "EXISTS",
        "DISTINCT",
        "TRUE",
        "FALSE",
        "NULL",
        "TODAY",
        "GROUPBY",
        "HAVING",
        "ORDERBY",
        "ASC",
        "DESC",
        "LIMIT",
        "OFFSET",
    )
)

RQL_FUNCTIONS_REGISTRY: "logilab.database._FunctionRegistry" = (
    SQL_FUNCTIONS_REGISTRY.copy()
)


@monkeypatch(FunctionDescr)
def st_description(  # noqa
    self,
    funcnode: "rql.nodes.Function",
    mainindex: Optional[int],
    tr: Callable[[str], str],
) -> str:
    return "%s(%s)" % (
        tr(self.name),
        ", ".join(
            sorted(
                child.get_description(mainindex, tr)
                for child in iter_funcnode_variables(funcnode)
            )
        ),
    )


@monkeypatch(FunctionDescr)
def st_check_backend(self, backend: Any, funcnode: "rql.nodes.Function") -> None:
    # XXX backend seems to always be None
    if not self.supports(backend):
        raise BadRQLQuery(
            "backend %s doesn't support function %s" % (backend, self.name)
        )


@monkeypatch(FunctionDescr)
def rql_return_type(self, funcnode: "rql.nodes.Function") -> Optional[str]:
    return self.rtype


@monkeypatch(CAST)  # type: ignore[no-redef] # noqa: F811
def st_description(  # noqa: F811
    self,
    funcnode: "rql.nodes.Function",
    mainindex: Optional[int],
    tr: Callable[[str], str],
) -> str:
    return self.rql_return_type(funcnode)


@monkeypatch(CAST)  # type: ignore[no-redef] # noqa: F811
def rql_return_type(self, funcnode: "rql.nodes.Function") -> str:  # noqa: F811
    # mypy: "BaseNode" has no attribute "value"  [attr-defined]
    # this is black magic to set rql_return_type to logilab.database classes
    # this code assume that CAST only works with nodes that has a value
    # attribute like Constant
    return funcnode.children[0].value  # type: ignore[attr-defined]


def iter_funcnode_variables(funcnode: "rql.nodes.Function") -> Generator:
    # funcnode: rql.nodes.Function
    # term: rql.nodes.VariableRef
    for term in funcnode.children:
        try:
            # term.variable.stinfo: dict
            # mypy: "BaseNode" has no attribute "variable"  [attr-defined]
            # same black magic than in rql_return_type above

            # error: Item "None" of "Optional[Variable]" has no attribute "stinfo"  [union-attr]
            assert getattr(term, "variable") is not None

            yield term.variable.stinfo["attrvar"] or term  # type: ignore[attr-defined]
        except AttributeError:
            yield term


def is_keyword(word: str) -> bool:
    """Return true if the given word is a RQL keyword."""
    return word.upper() in KEYWORDS


def common_parent(
    node1: Optional["BaseNode"], node2: Optional["BaseNode"]
) -> "BaseNode":
    """return the first common parent between node1 and node2

    algorithm :
     1) index node1's parents
     2) climb among node2's parents until we find a common parent
    """
    # index node1's parents
    node1_parents: Set["BaseNode"] = set()
    while node1:
        node1_parents.add(node1)
        node1 = node1.parent
    # climb among node2's parents until we find a common parent
    while node2:
        if node2 in node1_parents:
            return node2
        node2 = node2.parent
    raise Exception(f"Failed to get a common parent between '{node1}' and '{node2}'")


def register_function(funcdef: "logilab.database.FunctionDescr") -> None:
    RQL_FUNCTIONS_REGISTRY.register_function(funcdef)
    SQL_FUNCTIONS_REGISTRY.register_function(funcdef)


def function_description(funcname: str) -> "logilab.database.FunctionDescr":
    # return type is 'logilab.database.' + funcname
    """Return the description (:class:`FunctionDescr`) for a RQL function."""
    return RQL_FUNCTIONS_REGISTRY.get_function(funcname)


def quote(value: str) -> str:
    """Quote a string value."""
    res = ['"']
    for char in value:
        if char == '"':
            res.append("\\")
        res.append(char)
    res.append('"')
    return "".join(res)


def uquote(value: str) -> str:
    # XXX is this still useful?
    """Quote a unicode string value."""
    res: List[str] = ['"']
    for char in value:
        if char == '"':
            res.append("\\")
        res.append(char)
    res.append('"')
    return "".join(res)


class VisitableMixIn:
    def accept(
        self,
        visitor: Union_["rql.stcheck.RQLSTChecker", "rql.stcheck.RQLSTAnnotator"],
        *args: Optional["rql.stcheck.STCheckState"],
        **kwargs: Optional[Any],
    ) -> None:
        visit_id: str = self.__class__.__name__.lower()
        visit_method: Callable = getattr(visitor, "visit_%s" % visit_id)
        return visit_method(self, *args, **kwargs)

    def leave(
        self,
        visitor: Union_["rql.stcheck.RQLSTChecker", "rql.stcheck.RQLSTAnnotator"],
        *args: Optional["rql.stcheck.STCheckState"],
        **kwargs: Optional[Any],
    ) -> None:
        visit_id: str = self.__class__.__name__.lower()
        visit_method: Callable = getattr(visitor, "leave_%s" % visit_id)
        return visit_method(self, *args, **kwargs)


# should we redefine this as a Protocol?
class RQLVisitorHandler:
    """Handler providing a dummy implementation of all callbacks necessary
    to visit a RQL syntax tree.
    """

    def visit_union(self, union):
        pass

    def visit_insert(self, insert):
        pass

    def visit_delete(self, delete):
        pass

    def visit_set(self, update):
        pass

    def visit_select(self, selection):
        pass

    def visit_sortterm(self, sortterm):
        pass

    def visit_and(self, et):
        pass

    def visit_or(self, ou):
        pass

    def visit_not(self, not_):
        pass

    def visit_relation(self, relation):
        pass

    def visit_comparison(self, comparison):
        pass

    def visit_mathexpression(self, mathexpression):
        pass

    def visit_function(self, function):
        pass

    def visit_variableref(self, variable):
        pass

    def visit_variablerefattributeaccess(self, variable, attribute):
        pass

    def visit_variablerefmethodcall(self, variable, function, args):
        pass

    def visit_constant(self, constant):
        pass
