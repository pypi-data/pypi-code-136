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
"""RQL library (implementation independant)."""

from math import log

import sys
import threading

import pkg_resources
from io import StringIO

from rql._exceptions import (  # noqa
    UsesReservedWord,
    RQLSyntaxError,
    RQLException,
    MissingType,
    UsesReservedWord,
    RQLSyntaxError,
    TypeResolverException,
    BadRQLQuery,
    CoercionError,
)
from rql.analyze import ETypeResolver
from typing import TYPE_CHECKING, Optional, Dict, List, Any, Set, cast

__docformat__: str = "restructuredtext en"
__version__: str = pkg_resources.get_distribution("rql").version

if TYPE_CHECKING:
    import rql

# REQUIRED_TYPES = ['String', 'Float', 'Int', 'Boolean', 'Date']


class RQLHelper:
    """Helper class for RQL handling

    give access to methods for :
      - parsing RQL strings
      - variables type resolving
      - comparison of two queries
    """

    def __init__(
        self,
        schema: "rql.interfaces.ISchema",
        uid_func_mapping: "rql.analyze.UIDFuncMapping" = None,
        special_relations: Dict[str, str] = {},
        backend: Optional[Any] = None,
    ) -> None:
        # chech schema
        # for e_type in REQUIRED_TYPES:
        #    if not schema.has_entity(e_type):
        #        raise MissingType(e_type)
        # create helpers
        from rql.stcheck import RQLSTChecker, RQLSTAnnotator

        if uid_func_mapping:
            for key in uid_func_mapping:
                special_relations[key] = "uid"
        self._checker = RQLSTChecker(schema, special_relations, backend)
        self._annotator = RQLSTAnnotator(schema, special_relations)
        self._analyser_lock = threading.Lock()
        self._analyser = ETypeResolver(schema, uid_func_mapping)
        # IgnoreTypeRestriction analyser
        from rql.analyze import ETypeResolverIgnoreTypeRestriction

        self._itr_analyser_lock = threading.Lock()
        self._itr_analyser = ETypeResolverIgnoreTypeRestriction(
            schema, uid_func_mapping
        )
        self.set_schema(schema)

    def set_schema(self, schema: "rql.interfaces.ISchema") -> None:
        from rql.utils import is_keyword

        for etype in schema.entities():
            etype = str(etype)
            if is_keyword(etype) or etype.capitalize() == "Any":
                raise UsesReservedWord(etype)
        for rtype in schema.relations():
            rtype = str(rtype)
            if is_keyword(rtype):
                raise UsesReservedWord(rtype)
        self._checker.schema = schema
        self._annotator.schema = schema
        self._analyser.set_schema(schema)

    def get_backend(self) -> Any:
        return self._checker.backend

    def set_backend(self, backend: Any) -> None:
        self._checker.backend = backend

    backend = property(get_backend, set_backend)

    def parse(self, rqlstring: str, annotate: bool = True) -> "rql.stmts.AnyStatement":
        """Return a syntax tree created from a RQL string."""
        rqlst = parse(rqlstring, False)
        self._checker.check(rqlst)
        if annotate:
            self.annotate(rqlst)
        rqlst.schema = self._annotator.schema
        return rqlst

    def annotate(self, rqlst: "rql.stmts.Statement") -> None:
        self._annotator.annotate(rqlst)

    def compute_solutions(
        self,
        rqlst: "rql.stmts.AnyStatement",
        uid_func_mapping: "rql.analyze.UIDFuncMapping" = None,
        kwargs: Optional[Dict] = None,
        debug: bool = False,
    ) -> Set:
        """Set solutions for variables of the syntax tree.

        Each solution is a dictionary with variable's name as key and
        variable's type as value.
        """
        with self._analyser_lock:
            return self._analyser.visit(rqlst, uid_func_mapping, kwargs, debug)

    def compute_all_solutions(
        self, rqlst, uid_func_mapping=None, kwargs=None, debug=False
    ):
        """compute syntax tree solutions with all types restriction (eg
        is/instance_of relations) ignored
        """
        with self._itr_analyser_lock:
            self._itr_analyser.visit(rqlst, uid_func_mapping, kwargs, debug)

    def simplify(self, rqlst: "rql.stmts.Union") -> None:
        """Simplify `rqlst` by rewriting non-final variables associated to a const
        node (if annotator say we can...)

        The tree is modified in-place.
        """
        # print('simplify', rqlst.as_string())
        # seems like only Union as TYPE attribute, I should double check
        if rqlst.TYPE == "select":
            for select in rqlst.children:
                self._simplify(cast("rql.stmts.Select", select))

    def _simplify(self, select: "rql.stmts.Select") -> None:
        # recurse on subqueries first
        for subquery in select.with_:
            for subselect in subquery.query.children:
                self._simplify(cast("rql.stmts.Select", subselect))
        rewritten = False
        for var in list(select.defined_vars.values()):
            stinfo = var.stinfo
            if (
                stinfo["constnode"]
                and not stinfo.get("blocsimplification")
                and not var.has_attribute_or_function_var_references()
            ):
                uidrel = stinfo["uidrel"]
                var = uidrel.children[0].variable
                vconsts: List["rql.nodes.Constant"] = []
                rhs = uidrel.children[1].children[0]
                for vref in var.references():
                    rel = vref.relation()
                    if rel is None:
                        term = vref
                        while term.parent is not select:
                            term = term.parent
                        if any(term.is_equivalent(t) for t in select.selection):
                            rhs = copy_uid_node(select, rhs, vconsts)
                            if vref is term:
                                index = next(
                                    i
                                    for i, var in enumerate(select.selection)
                                    if vref.is_equivalent(var)
                                )
                                select.selection[index] = rhs
                                rhs.parent = select
                            else:
                                vref.parent.replace(vref, rhs)
                        elif any(term.is_equivalent(o) for o in select.orderby):
                            # remove from orderby
                            select.remove(term)
                        elif not select.having:
                            # remove from groupby if no HAVING clause
                            select.remove(term)
                        else:
                            rhs = copy_uid_node(select, rhs, vconsts)
                            # "Iterable[Any]" has no attribute "index"  [attr-defined]
                            select.groupby = cast(List, select.groupby)
                            select.groupby[select.groupby.index(vref)] = rhs
                            rhs.parent = select
                    elif rel is uidrel:
                        uidrel.parent.remove(uidrel)
                    elif rel.is_types_restriction():
                        stinfo["typerel"] = None
                        rel.parent.remove(rel)
                    else:
                        rhs = copy_uid_node(select, rhs, vconsts)
                        vref.parent.replace(vref, rhs)
                del select.defined_vars[var.name]
                stinfo["uidrel"] = None
                rewritten = True
                if vconsts:
                    select.stinfo["rewritten"][var.name] = vconsts
        if rewritten and select.solutions:
            select.clean_solutions()


def copy_uid_node(
    select: "rql.stmts.Select",
    node: "rql.nodes.Constant",
    vconsts: List["rql.nodes.Constant"],
) -> "rql.nodes.Constant":
    # Incompatible types in assignment
    #  (expression has type "BaseNode", variable has type "Constant")
    node = node.copy(select)  # type:ignore[assignment]
    node.uid = True
    vconsts.append(node)
    return node


def parse(rqlstring: str, print_errors: bool = True) -> "rql.stmts.AnyStatement":
    """Return a syntax tree created from a RQL string."""
    from yapps.runtime import print_error, SyntaxError, NoMoreTokens
    from rql.parser import Hercule, HerculeScanner

    # make sure rql string ends with a semi-colon
    rqlstring = rqlstring.strip()
    if rqlstring and not rqlstring.endswith(";"):
        rqlstring += ";"
    # parse the RQL string
    parser = Hercule(HerculeScanner(rqlstring))
    try:
        return parser.goal()
    except SyntaxError as ex:
        if not print_errors:
            if ex.pos is not None:
                multi_lines_rql = rqlstring.splitlines()
                nb_lines = len(multi_lines_rql)
                if nb_lines > 5:
                    width = log(nb_lines, 10) + 1
                    template = " %%%ii: %%s" % width
                    rqlstring = "\n".join(
                        template % (idx + 1, line)
                        for idx, line in enumerate(multi_lines_rql)
                    )

                padding = 30
                _, line, column = ex.pos

                rql_line = multi_lines_rql[line - 1]

                if len(rql_line) <= (padding * 2):
                    around = rql_line
                    here_left_padding = len("around: ") + column
                elif column < padding:
                    around = rql_line[: padding * 2] + "..."
                    here_left_padding = len("around: ") + column
                elif (len(rql_line) - padding) < column:
                    around = "..." + rql_line[-(padding * 2) :]
                    here_left_padding = len("around: ...") + (
                        column - (len(rql_line) - (padding * 2))
                    )
                else:
                    around = (
                        "..." + rql_line[column - padding : column + padding] + "..."
                    )
                    here_left_padding = len("around: ...") + padding

                here = " " * (here_left_padding - 1) + "^ here"
                msg = "%s in:\n%s\n\nat line %s and column %s\naround: %s\n%s" % (
                    ex.msg,
                    rqlstring,
                    line,
                    column,
                    around,
                    here,
                )
            else:
                msg = "%s\n%s" % (rqlstring, ex.msg)
            exc = RQLSyntaxError(msg)
            exc.__traceback__ = sys.exc_info()[-1]
            raise exc
        # try to get error message from yapps
        try:
            out = sys.stderr
            sys.stderr = stream = StringIO()
            try:
                print_error(ex, parser._scanner)
            finally:
                sys.stderr = out
            exc = RQLSyntaxError(stream.getvalue())
            exc.__traceback__ = sys.exc_info()[-1]
            raise exc
        except ImportError:  # duh?
            sys.stderr = out
            exc = RQLSyntaxError(
                "Syntax Error",
                ex.msg,
                "on line",
                1 + out.count("\n", 0, ex.pos),  # type:ignore
            )
            exc.__traceback__ = sys.exc_info()[-1]
            raise exc
    except NoMoreTokens:
        msg = "Could not complete parsing; stopped around here: \n%s"
        exc = RQLSyntaxError(msg % parser._scanner)
        exc.__traceback__ = sys.exc_info()[-1]
        raise exc
