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
"""Construction and manipulation of RQL syntax trees.

This module defines only first level nodes (i.e. statements). Child nodes are
defined in the nodes module
"""
from copy import deepcopy
from warnings import warn

from logilab.common.deprecation import callable_deprecated

from rql import BadRQLQuery, CoercionError, nodes
from rql.base import BaseNode, Node
from rql.utils import rqlvar_maker

from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Union as Union_,
    Any,
    Iterable,
    Optional,
    cast,
    Set as Set_,
    Tuple,
    Iterator,
    Sequence,
)

_MARKER: object = object()

__docformat__: str = "restructuredtext en"

if TYPE_CHECKING:
    import rql

Solution = Dict[str, str]
SolutionsList = List[Solution]


# this is a node of the syntax tree
# used, for now, for Select.vargraph
Graph = Dict[Union_[Tuple[str, str], str], List[str]]


def _check_references(
    defined: Dict[str, Union_["rql.nodes.Variable", "rql.nodes.ColumnAlias"]],
    varrefs: Iterable[Union_["rql.nodes.VariableRef", "rql.base.BaseNode"]],
) -> bool:
    refs = {}
    for var in defined.values():
        for vref in var.references():
            # be careful, Variable and VariableRef define __cmp__
            if not [v for v in varrefs if v is vref]:
                raise AssertionError("vref %r is not in the tree" % vref)
            refs[id(vref)] = 1
    for vref in varrefs:
        if id(vref) not in refs:
            raise AssertionError("vref %r is not referenced (%r)" % (vref, vref.stmt))
    return True


class undo_modification:
    def __init__(self, select):
        self.select = select

    def __enter__(self):
        self.select.save_state()

    def __exit__(self):
        self.select.recover()


class ScopeNode(BaseNode):
    def __init__(self):
        # dictionnary of defined variables in the original RQL syntax tree
        self.defined_vars: Dict[str, "rql.nodes.Variable"] = {}
        self.with_: List["rql.nodes.SubQuery"] = []
        # list of possibles solutions for used variables
        self.solutions: SolutionsList = []
        self._varmaker = None  # variable names generator, built when necessary
        self.where: Optional["rql.base.Node"] = None  # where clause node
        self.having: Iterable["rql.base.Node"] = ()  # XXX now a single node
        # "ScopeNode" has no attribute "schema"
        self.schema: Optional[Any] = None
        # "ScopeNode" has no attribute "aliases"
        self.aliases: Dict[str, "rql.nodes.ColumnAlias"] = {}

    # "ScopeNode" has no attribute "undo_manager"
    @property
    def undo_manager(self):
        try:
            return self._undo_manager
        except AttributeError:
            from rql.undo import SelectionManager

            self._undo_manager = SelectionManager(self)
            return self._undo_manager

    @property
    def should_register_op(self):
        return None

    def get_selected_variables(self):
        return self.selected_terms()

    def set_where(self, node: "rql.base.Node") -> None:
        self.where = node
        node.parent = self

    def set_having(self, terms: Iterable["rql.base.Node"]) -> None:
        if self.should_register_op:
            from rql.undo import SetHavingOperation

            # "ScopeNode" has no attribute "undo_manager"  [attr-defined]
            # either we ignore, either we redefine
            self.undo_manager.add_operation(SetHavingOperation(self, self.having))
        self.having = terms
        for node in terms:
            node.parent = self

    # Signature of "copy" incompatible with supertype "BaseNode"
    # either add a parameter that won't be used, either ignore
    def copy(
        self,
        stmt: Optional["Statement"] = None,
        copy_solutions: bool = True,
        solutions: SolutionsList = None,
    ) -> "rql.base.BaseNode":
        new = self.__class__()
        if self.schema is not None:
            new.schema = self.schema
        if solutions is not None:
            new.solutions = solutions
        elif copy_solutions and self.solutions:
            new.solutions = deepcopy(self.solutions)
        return new

    # construction helper methods #############################################
    def get_etype(self, name: str) -> "rql.nodes.Constant":
        """return the type object for the given entity's type name

        raise BadRQLQuery on unknown type
        """
        return nodes.Constant(name, "etype")

    def get_variable(
        self, name: str
    ) -> Union_["rql.nodes.Variable", "rql.nodes.ColumnAlias"]:
        """get a variable instance from its name

        the variable is created if it doesn't exist yet
        """
        try:
            return self.defined_vars[name]
        except Exception:
            self.defined_vars[name] = var = nodes.Variable(name)
            var.stmt = self
            return var

    def allocate_varname(self) -> str:
        """return an yet undefined variable name"""
        if self._varmaker is None:
            self._varmaker = rqlvar_maker(
                defined=self.defined_vars,
                # XXX only on Select node
                aliases=getattr(self, "aliases", None),
            )
        return next(self._varmaker)

    def make_variable(self) -> "rql.nodes.Variable":
        """create a new variable with an unique name for this tree"""
        var = self.get_variable(self.allocate_varname())
        if self.should_register_op:
            from rql.undo import MakeVarOperation

            self.undo_manager.add_operation(MakeVarOperation(var))
        return cast("rql.nodes.Variable", var)

    def set_possible_types(
        self,
        solutions: SolutionsList,
        kwargs: Optional[Union_[object, Dict[str, str]]] = _MARKER,
        key: str = "possibletypes",
    ) -> None:
        if key == "possibletypes":
            self.solutions = solutions
        defined = self.defined_vars
        for var in defined.values():
            var.stinfo[key] = set()
            for solution in solutions:
                var.stinfo[key].add(solution[var.name])
        # for debugging
        # for sol in solutions:
        #    for vname in sol:
        #        assert vname in self.defined_vars or vname in self.aliases

    def check_references(self) -> bool:
        """test function"""
        try:
            defined = cast(
                Dict[str, Union_["rql.nodes.ColumnAlias", "rql.nodes.Variable"]],
                self.aliases.copy(),
            )

        except AttributeError:
            defined = cast(
                Dict[str, Union_["rql.nodes.ColumnAlias", "rql.nodes.Variable"]],
                self.defined_vars.copy(),
            )
        else:
            defined.update(self.defined_vars)
            for subq in self.with_:
                subq.query.check_references()
        varrefs = [
            vref for vref in self.get_nodes(nodes.VariableRef) if vref.stmt is self
        ]
        try:
            _check_references(defined, varrefs)
        except Exception:
            print(repr(self))
            raise
        return True


class Statement:
    """base class for statement nodes"""

    # default values for optional instance attributes, set on the instance when
    # used
    schema: Optional["rql.interfaces.ISchema"] = None
    annotated: bool = False  # set by the annotator

    if TYPE_CHECKING:

        def get_variable(self, name, column=None):
            raise NotImplementedError()

    # navigation helper methods #############################################

    @property
    def root(self):
        """return the root node of the tree"""
        return self

    @property
    def stmt(self):
        return self

    @property
    def scope(self):
        return self

    def ored(
        self, traverse_scope: bool = False, _fromnode: Optional["rql.nodes.And"] = None
    ) -> Optional["rql.nodes.Or"]:
        return None

    def neged(
        self, traverse_scope: bool = False, _fromnode: Optional["rql.nodes.Or"] = None
    ) -> Optional["rql.nodes.Not"]:
        return None


class Union(Statement, Node):
    """the select node is the root of the syntax tree for selection statement
    using UNION
    """

    TYPE: str = "select"
    # default values for optional instance attributes, set on the instance when
    # used
    undoing: bool = False  # used to prevent from memorizing when undoing !
    memorizing: int = 0  # recoverable modification attributes

    def wrap_selects(self) -> None:
        """return a new rqlst root containing the given union as a subquery"""
        child = Union()
        for select in self.children[:]:
            child.append(select)
            self.remove_select(cast("Select", select))
        newselect: "Select" = Select()
        aliases: List["rql.nodes.VariableRef"] = []
        for i in range(len(cast("Select", select).selection)):
            aliases.append(nodes.VariableRef(newselect.make_variable()))
        newselect.add_subquery(nodes.SubQuery(aliases, child), check=False)
        for vref in aliases:
            newselect.append_selected(nodes.VariableRef(vref.variable))
        self.append_select(newselect)

    def _get_offset(self) -> int:
        warn("offset is now a Select node attribute", DeprecationWarning, stacklevel=2)
        last_children = cast("Select", self.children[-1])
        return last_children.offset

    def set_offset(self, offset: int) -> None:
        if len(self.children) == 1:
            last_children = cast("Select", self.children[-1])
            last_children.set_offset(offset)
        # we have to introduce a new root
        # XXX not undoable since a new root has to be introduced
        self.wrap_selects()
        first_child = cast("Select", self.children[0])
        first_child.set_offset(offset)

    offset = property(_get_offset, set_offset)

    def _get_limit(self):
        warn("limit is now a Select node attribute", DeprecationWarning, stacklevel=2)
        return self.children[-1].limit

    def set_limit(self, limit: int) -> None:
        if len(self.children) == 1:
            cast("Select", self.children[-1]).set_limit(limit)
            return None
        self.wrap_selects()
        cast("Select", self.children[0]).set_limit(limit)
        return None

    limit = property(_get_limit, set_limit)

    @property
    def root(self):
        """return the root node of the tree"""
        if self.parent is None:
            return self
        return self.parent.root

    def get_description(
        self,
        mainindex: Optional[int] = None,
        tr: Optional["rql.nodes.TranslationFunction"] = None,
    ) -> List[List[str]]:
        """
        `mainindex`:
          selection index to consider as main column, useful to get smarter
          results
        `tr`:
          optional translation function taking a string as argument and
          returning a string
        """
        if tr is None:

            def tr(msg, context=None):
                return msg

        return [
            c.get_description(mainindex, tr)
            for c in cast(Sequence["Select"], self.children)
        ]

    # repr / as_string / copy #################################################

    def __repr__(self) -> str:
        return "\nUNION\n".join(repr(select) for select in self.children)

    def as_string(self, kwargs: Optional[Dict] = None) -> str:
        """return the tree as an encoded rql string"""
        strings: List[str] = [
            select.as_string(kwargs=kwargs) for select in self.children
        ]
        if len(strings) == 1:
            return strings[0]
        return " UNION ".join("(%s)" % part for part in strings)

    def copy(
        self, stmt: Optional["Statement"] = None, copy_children: bool = True
    ) -> "Union":
        new: "Union" = Union()
        if self.schema is not None:
            new.schema = self.schema
        if copy_children:
            for child in self.children:
                new.append(child.copy())
                assert new.children[-1].parent is new
        return new

    # union specific methods ##################################################

    # XXX for bw compat, should now use get_variable_indices (cw > 3.8.4)
    def get_variable_variables(self) -> Set_[int]:
        change: Set_[int] = set()
        for idx in self.get_variable_indices():
            first_child = self.children[0]
            vrefs = (
                cast("Select", first_child).selection[idx].iget_nodes(nodes.VariableRef)
            )

            for vref in vrefs:
                change.add(vref.name)
        return change

    def get_variable_indices(self) -> Set_[int]:
        """return the set of selection indexes which take different types
        according to the solutions
        """
        change: Set_[int] = set()
        values: Dict[int, Set_] = {}
        for select in self.children:
            for descr in cast("Select", select).get_selection_solutions():
                for i, etype in enumerate(descr):
                    values.setdefault(i, set()).add(etype)
        for idx, etypes in values.items():
            if len(etypes) > 1:
                change.add(idx)
        return change

    def _locate_subquery(
        self, col: int, etype: str, kwargs: Optional[Dict[Any, Any]] = None
    ) -> Tuple:
        first_child = self.children[0]
        has_children = len(self.children) == 1
        first_child_subqueries = not cast("Select", first_child).with_
        if has_children and first_child_subqueries:
            return self.children[0], col
        for select in cast(Sequence["Select"], self.children):
            term = select.selection[col]
            try:
                if term.name in select.aliases:
                    alias = select.aliases[term.name]
                    return alias.query._locate_subquery(alias.colnum, etype, kwargs)
            except AttributeError:
                # term has no 'name' attribute
                pass
            for i, solution in enumerate(select.solutions):
                if term.get_type(solution, kwargs) == etype:
                    return select, col
        raise Exception(f"internal error, {etype} not found on col {col}")

    def locate_subquery(
        self, col: int, etype: str, kwargs: Optional[Dict] = None
    ) -> Any:
        """return a select node and associated selection index where root
        variable at column `col` is of type `etype`
        """
        try:
            # Cannot determine type of '_subq_cache'  [has-type]
            return self._subq_cache[(col, etype)]  # type: ignore[has-type]
        except AttributeError:
            self._subq_cache = {}
        except KeyError:
            pass
        self._subq_cache[(col, etype)] = self._locate_subquery(col, etype, kwargs)
        return self._subq_cache[(col, etype)]

    def subquery_selection_index(self, subselect: Any, col: int) -> int:
        """given a select sub-query and a column index in the root query, return
        the selection index for this column in the sub-query
        """
        selectpath: List = []
        while subselect.parent.parent is not None:
            subq = subselect.parent.parent
            subselect = subq.parent
            selectpath.insert(0, subselect)
        for select in selectpath:
            col = select.selection[col].variable.colnum
        return col

    # recoverable modification methods ########################################

    # don't use @cached: we want to be able to disable it while this must still
    # be cached
    @property
    def undo_manager(self) -> "rql.undo.SelectionManager":
        from rql.undo import SelectionManager

        undo_manager = getattr(self, "_undo_manager", None)
        if undo_manager:
            return undo_manager
        self._undo_manager = SelectionManager(self)
        return self._undo_manager

    @property
    def should_register_op(self):
        return self.memorizing and not self.undoing

    def undo_modification(self) -> "undo_modification":
        return undo_modification(self)

    def save_state(self) -> None:
        """save the current tree"""
        self.undo_manager.push_state()
        self.memorizing += 1

    def recover(self) -> None:
        """reverts the tree as it was when save_state() was last called"""
        self.memorizing -= 1
        assert self.memorizing >= 0
        self.undo_manager.recover()

    def check_references(self) -> bool:
        """test function"""
        for select in cast(Sequence["Select"], self.children):
            select.check_references()
        return True

    def append_select(self, select: "Select") -> None:
        if self.should_register_op:
            from rql.undo import AppendSelectOperation

            self.undo_manager.add_operation(AppendSelectOperation(self, select))
        self.children.append(select)

    def remove_select(self, select: "Select") -> None:
        idx: int = self.children.index(select)
        if self.should_register_op:
            from rql.undo import RemoveSelectOperation

            self.undo_manager.add_operation(RemoveSelectOperation(self, select, idx))
        self.children.pop(idx)


class Select(Statement, nodes.EditableMixIn, ScopeNode):
    """the select node is the base statement of the syntax tree for selection
    statement, always child of a UNION root.
    """

    vargraph: Graph = {}
    parent = None
    distinct: bool = False
    # limit / offset
    limit: Optional[int] = None
    offset: int = 0
    # already defined inside ScopeNode right?
    # But py3 fails when I change anything here
    # RecursionError: maximum recursion depth excedeed
    # set by the annotator
    has_aggregat: bool = False

    def __init__(self):
        Statement.__init__(self)
        ScopeNode.__init__(self)
        self.selection: List = []
        # subqueries alias
        self.aliases: Dict[str, "rql.nodes.ColumnAlias"] = {}
        # syntax tree meta-information
        self.stinfo: Dict[str, Dict] = {"rewritten": {}}

        # select clauses
        self.groupby: List[Any] = []
        self.orderby: List[Any] = []

    @property
    def root(self):
        """return the root node of the tree"""
        return self.parent

    def get_description(
        self,
        mainindex: Optional[int] = None,
        tr: Optional["rql.nodes.TranslationFunction"] = None,
    ) -> List[str]:
        """return the list of types or relations (if not found) associated to
        selected variables.
        mainindex is an optional selection index which should be considered has
        'pivot' entity.
        """
        descr: List[str] = []
        for term in self.selection:
            # don't translate Any
            try:
                descr.append(term.get_description(mainindex, tr) or "Any")
            except CoercionError:
                descr.append("Any")
        return descr

    @property
    def children(self):
        children = self.selection[:]
        if self.groupby:
            children += self.groupby
        if self.orderby:
            children += self.orderby
        if self.where:
            children.append(self.where)
        if self.having:
            children += self.having
        if self.with_:
            children += self.with_
        return children

    # repr / as_string / copy #################################################

    def __repr__(self) -> str:
        return self.as_string(userepr=True)

    def as_string(self, kwargs: Optional[Dict] = None, userepr: bool = False) -> str:
        """return the tree as an encoded rql string"""
        if userepr:
            as_string = repr
        else:

            def as_string(x):
                return x.as_string(kwargs=kwargs)

        s = [",".join(as_string(term) for term in self.selection)]
        if self.groupby:
            s.append("GROUPBY " + ",".join(as_string(term) for term in self.groupby))
        if self.orderby:
            s.append("ORDERBY " + ",".join(as_string(term) for term in self.orderby))
        if self.limit is not None:
            s.append("LIMIT %s" % self.limit)
        if self.offset:
            s.append("OFFSET %s" % self.offset)
        if self.where is not None:
            s.append("WHERE " + as_string(self.where))
        if self.having:
            s.append("HAVING " + ",".join(as_string(term) for term in self.having))
        if self.with_:
            s.append("WITH " + ",".join(as_string(term) for term in self.with_))
        if self.distinct:
            return "DISTINCT Any " + " ".join(s)
        return "Any " + " ".join(s)

    def copy(
        self,
        stmt: Optional["Statement"] = None,
        copy_solutions: bool = True,
        solutions: Optional[SolutionsList] = None,
    ) -> "Select":
        new = super().copy(self, copy_solutions, solutions)

        # "ScopeNode" has no attribute ....  [attr-defined]
        new = cast("Select", new)

        if self.with_:
            new.set_with([sq.copy(new) for sq in self.with_], check=False)
        for child in self.selection:
            new_var_ref = child.copy(new)
            new.append_selected(new_var_ref)
        if self.groupby:
            new.set_groupby([sq.copy(new) for sq in self.groupby])
        if self.orderby:
            new.set_orderby([sq.copy(new) for sq in self.orderby])
        # Argument 1 to "set_where" of "ScopeNode" has incompatible type "Node"
        # expected "Union[Or, Not, And, Relation]"  [arg-type]
        if self.where:
            new.set_where(self.where.copy(new))
        if self.having:
            new.set_having([sq.copy(new) for sq in self.having])
        new.distinct = self.distinct
        new.limit = self.limit
        new.offset = self.offset
        new.vargraph = self.vargraph
        return new

    # select specific methods #################################################

    def set_possible_types(
        self,
        solutions: SolutionsList,
        kwargs: Optional[Union_[object, Dict[str, str]]] = _MARKER,
        key: str = "possibletypes",
    ) -> None:
        super(Select, self).set_possible_types(solutions, kwargs, key)
        for ca in self.aliases.values():
            ca.stinfo[key] = capt = set()
            for solution in solutions:
                capt.add(solution[ca.name])
            if kwargs is _MARKER:
                continue
            # propagage to subqueries in case we're introducing additional
            # type constraints
            for stmt in ca.query.children[:]:
                # better type for term
                term: Any = stmt.selection[ca.colnum]
                sols: List = [
                    sol for sol in stmt.solutions if term.get_type(sol, kwargs) in capt
                ]
                if not sols:
                    ca.query.remove_select(stmt)
                else:
                    stmt.set_possible_types(sols)

    def set_statement_type(self, etype: str) -> None:
        """set the statement type for this selection
        this method must be called last (i.e. once selected variables has been
        added)
        """
        assert self.selection
        # Person P  ->  Any P where P is Person
        if etype != "Any":
            variables: List["rql.nodes.VariableRef"] = list(
                self.get_selected_variables()
            )
            if not variables:
                raise BadRQLQuery(
                    "Setting type in selection is only allowed "
                    "when some variable is selected"
                )
            for var in variables:
                self.add_type_restriction(var.variable, etype)

    def set_distinct(self, value: bool) -> None:
        """mark DISTINCT query"""
        if self.should_register_op and value != self.distinct:
            from rql.undo import SetDistinctOperation

            self.undo_manager.add_operation(SetDistinctOperation(self.distinct, self))
        self.distinct = value

    def set_limit(self, limit: int) -> None:
        if limit is not None and (not isinstance(limit, int) or limit <= 0):
            raise BadRQLQuery("bad limit %s" % limit)
        if self.should_register_op and limit != self.limit:
            from rql.undo import SetLimitOperation

            self.undo_manager.add_operation(SetLimitOperation(self.limit, self))
        self.limit = limit

    def set_offset(self, offset: int) -> None:
        if offset is not None and (not isinstance(offset, int) or offset < 0):
            raise BadRQLQuery("bad offset %s" % offset)
        if self.should_register_op and offset != self.offset:
            from rql.undo import SetOffsetOperation

            self.undo_manager.add_operation(SetOffsetOperation(self.offset, self))
        self.offset = offset

    def set_orderby(self, terms: List["rql.nodes.SortTerm"]) -> None:
        self.orderby = terms
        for node in terms:
            node.parent = self

    def set_groupby(
        self, terms: List[Union_["rql.nodes.Function", "rql.nodes.VariableRef"]]
    ) -> None:
        self.groupby = terms
        for node in terms:
            node.parent = self

    def set_with(self, terms: List["rql.nodes.SubQuery"], check: bool = True) -> None:
        self.with_ = []
        for node in terms:
            self.add_subquery(node, check)

    def add_subquery(self, node: "rql.nodes.SubQuery", check: bool = True) -> None:

        assert node.query
        node.parent = self
        self.with_.append(node)

        # "BaseNode" has no attribute "selection"
        if check and len(node.aliases) != len(
            cast("Select", node.query.children[0]).selection
        ):
            raise BadRQLQuery(
                "Should have the same number of aliases than "
                "selected terms in sub-query"
            )
        for i, alias in enumerate(node.aliases):
            if check and alias.name in self.aliases:
                raise BadRQLQuery("Duplicated alias %s" % alias)
            ca = self.get_variable(alias.name, i)
            # "Variable" has no attribute "query"
            # classes with query attribute: ColumnAlias, Exists, SubQuery
            ca = cast("rql.nodes.ColumnAlias", ca)
            ca.query = node.query

    def remove_subquery(self, node: "rql.nodes.SubQuery") -> None:
        self.with_.remove(node)
        node.parent = None
        for i, alias in enumerate(node.aliases):
            del self.aliases[alias.name]

    # Signature of "get_variable" incompatible with supertype "ScopeNode"  [override]
    def get_variable(
        self, name: str, colnum: Optional[int] = None
    ) -> Union_["rql.nodes.Variable", "rql.nodes.ColumnAlias"]:
        """get a variable instance from its name

        the variable is created if it doesn't exist yet
        """
        if name in self.aliases.keys():
            return self.aliases[name]
        if colnum is not None:  # take care, may be 0
            self.aliases[name] = calias = nodes.ColumnAlias(name, colnum)
            calias.stmt = self
            # alias may already have been used as a regular variable, replace it
            if name in self.defined_vars:
                var = self.defined_vars.pop(name)
                calias.stinfo["references"] = var.stinfo["references"]
                for vref in var.references():
                    vref.variable = calias
            return self.aliases[name]
        return super(Select, self).get_variable(name)

    def clean_solutions(self, solutions: Optional[SolutionsList] = None) -> None:
        """when a rqlst has been extracted from another, this method returns
        solutions which make sense for this sub syntax tree
        """
        if solutions is None:
            solutions = self.solutions
        # this may occurs with rql optimization, for instance on
        # 'Any X WHERE X eid 12' query
        if not (self.defined_vars or self.aliases):
            self.solutions = [{}]
        else:
            newsolutions: SolutionsList = []
            for origsol in solutions:
                asol: Solution = {}
                for var in self.defined_vars:
                    asol[var] = origsol[var]
                for var in self.aliases:
                    asol[var] = origsol[var]
                if asol not in newsolutions:
                    newsolutions.append(asol)
            self.solutions = newsolutions

    def get_selection_solutions(self) -> Set_[Tuple[str, ...]]:
        """return the set of variable names which take different type according
        to the solutions
        """
        descriptions: Set_ = set()
        for solution in self.solutions:
            descr: List = []
            for term in self.selection:
                try:
                    descr.append(term.get_type(solution=solution))
                except CoercionError:
                    pass
            descriptions.add(tuple(descr))
        return descriptions

    # quick accessors #########################################################

    def get_selected_variables(self) -> Iterator["rql.nodes.VariableRef"]:
        """returns all selected variables, including those used in aggregate
        functions
        """
        for term in self.selection:
            for node in term.iget_nodes(nodes.VariableRef):
                yield node

    # construction helper methods #############################################

    def save_state(self) -> None:
        """save the current tree"""
        assert self.parent is not None
        self.parent.save_state()

    def recover(self) -> None:
        """reverts the tree as it was when save_state() was last called"""
        assert self.parent is not None
        self.parent.recover()

    def append_selected_method_call(
        self, function_call: str, args: List[nodes.Constant] = []
    ) -> None:
        varname, function = function_call.split(".")
        term = nodes.VariableRefMethodCall(self.get_variable(varname), function, args)
        self.append_selected(term)

    def append_selected_attribute_access(
        self,
        get_attribute: str,
    ) -> None:
        varname, attribute = get_attribute.split(".")
        term = nodes.VariableRefAttributeAccess(self.get_variable(varname), attribute)
        self.append_selected(term)

    def append_selected(
        self,
        term: Union_[
            "rql.nodes.Function",
            "rql.nodes.MathExpression",
            "rql.nodes.VariableRef",
            "rql.nodes.Constant",
        ],
    ) -> None:
        if isinstance(term, nodes.Constant) and term.type == "etype":
            raise BadRQLQuery("Entity type are not allowed in selection")
        term.parent = self
        self.selection.append(term)

    # XXX proprify edition, we should specify if we want:
    # * undo support
    # * references handling
    # skipped here
    def replace(
        self, oldnode: "rql.base.BaseNode", newnode: "rql.base.BaseNode"
    ) -> Tuple["rql.base.BaseNode", "rql.base.BaseNode", Optional[int]]:
        if oldnode is self.where:
            self.where = cast("rql.base.Node", newnode)
        elif any(oldnode.is_equivalent(s) for s in self.selection):
            index = next(
                i for i, s in enumerate(self.selection) if oldnode.is_equivalent(s)
            )
            self.selection[index] = newnode
        elif any(oldnode.is_equivalent(o) for o in self.orderby):
            index = next(
                i for i, o in enumerate(self.orderby) if oldnode.is_equivalent(o)
            )
            self.orderby[index] = newnode
        elif any(oldnode.is_equivalent(g) for g in self.groupby):
            index = next(
                i for i, g in enumerate(self.groupby) if oldnode.is_equivalent(g)
            )
            self.groupby[index] = newnode
        elif any(oldnode.is_equivalent(h) for h in self.having):
            index = next(
                i for i, h in enumerate(self.having) if oldnode.is_equivalent(h)
            )
            # Unsupported target for indexed assignment ("Iterable[Node]")  [index]
            self.having = cast(List, self.having)
            self.having[index] = newnode
        else:
            raise Exception("duh XXX %s" % oldnode)
        # XXX no undo/reference support 'by design' (i.e. breaks things if you add
        # it...)
        oldnode.parent = None
        newnode.parent = self
        return oldnode, self, None

    def remove(
        self, node: "rql.nodes.SortTerm"
    ) -> Tuple["BaseNode", Optional["BaseNode"], Optional[int]]:
        if node is self.where:
            self.where = None
        elif any(node.is_equivalent(o) for o in self.orderby):
            self.remove_sort_term(node)
        elif any(node.is_equivalent(g) for g in self.groupby):
            self.remove_group_term(node)
        elif any(node.is_equivalent(h) for h in self.having):
            # "Iterable[Node]" has no attribute "remove"  [attr-defined]
            self.having = cast(List, self.having)
            self.having.remove(node)
        # XXX selection
        else:
            raise Exception("duh XXX")
        node.parent = None
        return node, self, None

    def undefine_variable(self, var: "rql.nodes.Variable") -> None:
        """undefine the given variable and remove all relations where it appears"""
        # remove relations where this variable is referenced
        for vref in var.references():
            rel = vref.relation()
            if rel is not None:
                self.remove_node(rel)
            # XXX may have other nodes between vref and the sort term
            elif isinstance(vref.parent, nodes.SortTerm):
                self.remove_sort_term(vref.parent)
            elif vref in self.groupby:
                self.remove_group_term(vref)
            else:  # selected variable
                self.remove_selected(vref)
        # effective undefine operation
        if self.should_register_op:
            from rql.undo import UndefineVarOperation

            solutions = [d.copy() for d in self.solutions]
            self.undo_manager.add_operation(UndefineVarOperation(var, self, solutions))
        for sol in self.solutions:
            sol.pop(var.name, None)
        del self.defined_vars[var.name]

    def _var_index(
        self, var: Union_["rql.nodes.Variable", "rql.nodes.VariableRef"]
    ) -> int:
        """get variable index in the list using identity (Variable and VariableRef
        define __cmp__
        """
        for i, term in enumerate(self.selection):
            if term is var:
                return i
        raise IndexError()

    def remove_selected(
        self, var: Union_["rql.nodes.Variable", "rql.nodes.VariableRef"]
    ) -> None:
        """deletes var from selection variable"""
        # assert isinstance(var, VariableRef)
        index = self._var_index(var)
        if self.should_register_op:
            from rql.undo import UnselectVarOperation

            self.undo_manager.add_operation(UnselectVarOperation(var, index))
        for vref in self.selection.pop(index).iget_nodes(nodes.VariableRef):
            vref.unregister_reference()

    def add_selected(
        self,
        term: Union_["rql.nodes.Variable", "rql.nodes.VariableRef"],
        index: Optional[int] = None,
    ) -> None:
        """override Select.add_selected to memoize modification when needed"""
        if isinstance(term, nodes.Variable):
            term = nodes.VariableRef(term, noautoref=1)
            term.register_reference()
        else:
            for var in term.iget_nodes(nodes.VariableRef):
                var = nodes.variable_ref(var)
                var.register_reference()
        if index is not None:
            self.selection.insert(index, term)
            term.parent = self
        else:
            self.append_selected(term)
        if self.should_register_op:
            from rql.undo import SelectVarOperation

            self.undo_manager.add_operation(SelectVarOperation(term))

    def add_group_var(
        self,
        var: Union_["rql.nodes.Variable", "rql.nodes.VariableRef"],
        index: Optional[int] = None,
    ):
        """add var in 'orderby' constraints
        asc is a boolean indicating the group order (ascendent or descendent)
        """
        vref = nodes.variable_ref(var)
        vref.register_reference()
        if index is None:
            self.groupby.append(vref)
        else:
            self.groupby.insert(index, vref)
        vref.parent = self
        if self.should_register_op:
            from rql.undo import AddGroupOperation

            self.undo_manager.add_operation(AddGroupOperation(vref))

    def remove_group_term(self, term: "rql.base.BaseNode") -> None:
        """remove the group variable and the group node if necessary"""
        if self.should_register_op:
            from rql.undo import RemoveGroupOperation

            self.undo_manager.add_operation(RemoveGroupOperation(term))
        for vref in term.iget_nodes(nodes.VariableRef):
            vref.unregister_reference()
        index = next(i for i, g in enumerate(self.groupby) if term.is_equivalent(g))
        del self.groupby[index]

    remove_group_var = callable_deprecated("[rql 0.29] use remove_group_term instead")(
        remove_group_term
    )

    def remove_groups(self) -> None:
        for vref in self.groupby[:]:
            self.remove_group_term(vref)

    def add_sort_var(
        self, var: "rql.nodes.Variable", asc: Optional[bool] = True
    ) -> None:
        """add var in 'orderby' constraints
        asc is a boolean indicating the sort order (ascendent or descendent)
        """
        vref = nodes.variable_ref(var)
        vref.register_reference()
        term = nodes.SortTerm(vref, cast(int, asc))  # cast bool to int ?
        self.add_sort_term(term)

    def add_sort_term(
        self, term: "rql.nodes.SortTerm", index: Optional[int] = None
    ) -> None:
        if index is None:
            self.orderby.append(term)
        else:
            self.orderby.insert(index, term)
        term.parent = self
        for vref in term.iget_nodes(nodes.VariableRef):
            try:
                vref.register_reference()
            except AssertionError:
                pass  # already referenced
        if self.should_register_op:
            from rql.undo import AddSortOperation

            self.undo_manager.add_operation(AddSortOperation(term))

    def remove_sort_terms(self) -> None:
        if self.orderby:
            for term in self.orderby[:]:
                self.remove_sort_term(term)

    def remove_sort_term(self, term: "rql.nodes.SortTerm") -> None:
        """remove a sort term and the sort node if necessary"""
        if self.should_register_op:
            from rql.undo import RemoveSortOperation

            self.undo_manager.add_operation(RemoveSortOperation(term))
        for vref in term.iget_nodes(nodes.VariableRef):
            vref.unregister_reference()
        self.orderby.remove(term)

    def select_only_variables(self) -> None:
        selection: List["rql.nodes.VariableRef"] = []
        for term in self.selection:
            for vref in term.iget_nodes(nodes.VariableRef):
                if not any(vref.is_equivalent(s) for s in selection):
                    vref.parent = self
                    selection.append(vref)
        self.selection = selection


class Delete(Statement, ScopeNode):
    """the Delete node is the root of the syntax tree for deletion statement"""

    TYPE = "delete"

    def __init__(self):
        Statement.__init__(self)
        ScopeNode.__init__(self)
        self.main_variables = []
        self.main_relations = []

    @property
    def children(self):
        children = self.selection[:]
        children += self.main_relations
        if self.where:
            children.append(self.where)
        if self.having:
            children += self.having
        return children

    @property
    def selection(self) -> List["rql.nodes.VariableRef"]:
        return [vref for et, vref in self.main_variables]

    def add_main_variable(self, etype: str, vref: "rql.nodes.VariableRef") -> None:
        """add a variable to the list of deleted variables"""
        # if etype == 'Any':
        #    raise BadRQLQuery('"Any" is not supported in DELETE statement')
        vref.parent = self
        self.main_variables.append((etype, vref))

    def add_main_relation(self, relation):
        """add a relation to the list of deleted relations"""
        assert isinstance(relation.children[0], nodes.VariableRef)
        assert isinstance(relation.children[1], nodes.Comparison)
        assert isinstance(relation.children[1].children[0], nodes.VariableRef)
        relation.parent = self
        self.main_relations.append(relation)

    # repr / as_string / copy #################################################

    def __repr__(self) -> str:
        result = ["DELETE"]
        if self.main_variables:
            result.append(
                ", ".join(
                    ["%r %r" % (etype, var) for etype, var in self.main_variables]
                )
            )
        if self.main_relations:
            if self.main_variables:
                result.append(",")
            result.append(", ".join([repr(rel) for rel in self.main_relations]))
        if self.where is not None:
            result.append(repr(self.where))
        if self.having:
            result.append("HAVING " + ",".join(repr(term) for term in self.having))
        return " ".join(result)

    def as_string(self, kwargs: Optional[Dict] = None) -> str:
        """return the tree as an encoded rql string"""
        result = ["DELETE"]
        if self.main_variables:
            result.append(
                ", ".join(
                    ["%s %s" % (etype, var) for etype, var in self.main_variables]
                )
            )
        if self.main_relations:
            if self.main_variables:
                result.append(",")
            result.append(
                ", ".join([rel.as_string(kwargs=kwargs) for rel in self.main_relations])
            )
        if self.where is not None:
            result.append("WHERE " + self.where.as_string(kwargs=kwargs))
        if self.having:
            result.append(
                "HAVING "
                + ",".join(term.as_string(kwargs=kwargs) for term in self.having)
            )
        return " ".join(result)

    # Signature of "copy" incompatible with supertype "ScopeNode"  [override]
    # Signature of "copy" incompatible with supertype "BaseNode"  [override]
    def copy(self) -> "Delete":  # type:ignore[override]
        new = Delete()
        for etype, var in self.main_variables:
            vref = nodes.VariableRef(new.get_variable(var.name))
            new.add_main_variable(etype, vref)
        for child in self.main_relations:
            new.add_main_relation(child.copy(new))
        if self.where:
            new.set_where(self.where.copy(new))
        if self.having:
            new.set_having([sq.copy(new) for sq in self.having])
        return new


class Insert(Statement, ScopeNode):
    """the Insert node is the root of the syntax tree for insertion statement"""

    TYPE = "insert"

    def __init__(self):
        Statement.__init__(self)
        ScopeNode.__init__(self)
        self.main_variables = []
        self.main_relations = []
        self.inserted_variables = {}

    @property
    def children(self):
        children = self.selection[:]
        children += self.main_relations
        if self.where:
            children.append(self.where)
        if self.having:
            children += self.having
        return children

    @property
    def selection(self):
        return [vref for et, vref in self.main_variables]

    def add_main_variable(self, etype: str, vref: "rql.nodes.VariableRef") -> None:
        """add a variable to the list of inserted variables"""
        if etype == "Any":
            raise BadRQLQuery('"Any" is not supported in INSERT statement')
        self.main_variables.append((etype, vref))
        vref.parent = self
        self.inserted_variables[vref.variable] = 1

    def add_main_relation(self, relation: "rql.nodes.Relation") -> None:
        """add a relation to the list of inserted relations"""
        var = cast("rql.nodes.VariableRef", relation.children[0]).variable
        rhs = relation.children[1]
        if var not in self.inserted_variables:
            if isinstance(rhs, nodes.Constant):
                msg = "Using variable %s in declaration but %s is not an \
insertion variable"
                raise BadRQLQuery(msg % (var, var))
        relation.parent = self
        self.main_relations.append(relation)

    # repr / as_string / copy #################################################

    def __repr__(self) -> str:
        result = ["INSERT"]
        result.append(
            ", ".join(["%r %r" % (etype, var) for etype, var in self.main_variables])
        )
        if self.main_relations:
            result.append(":")
            result.append(", ".join([repr(rel) for rel in self.main_relations]))
        if self.where is not None:
            result.append("WHERE " + repr(self.where))
        if self.having:
            result.append("HAVING " + ",".join(repr(term) for term in self.having))
        return " ".join(result)

    def as_string(self, kwargs: Optional[Any] = None) -> str:
        """return the tree as an encoded rql string"""
        result = ["INSERT"]
        result.append(
            ", ".join(["%s %s" % (etype, var) for etype, var in self.main_variables])
        )
        if self.main_relations:
            result.append(":")
            result.append(
                ", ".join([rel.as_string(kwargs=kwargs) for rel in self.main_relations])
            )
        if self.where is not None:
            result.append("WHERE " + self.where.as_string(kwargs=kwargs))
        if self.having:
            result.append(
                "HAVING "
                + ",".join(term.as_string(kwargs=kwargs) for term in self.having)
            )
        return " ".join(result)

    # Signature of "copy" incompatible with supertype "ScopeNode"  [override]
    # Signature of "copy" incompatible with supertype "BaseNode"  [override]
    def copy(self) -> "Insert":  # type:ignore[override]
        new = Insert()
        for etype, var in self.main_variables:
            vref = nodes.VariableRef(new.get_variable(var.name))
            new.add_main_variable(etype, vref)
        for child in self.main_relations:
            new.add_main_relation(child.copy(new))
        if self.where:
            new.set_where(self.where.copy(new))
        if self.having:
            new.set_having([sq.copy(new) for sq in self.having])
        return new


class Set(Statement, ScopeNode):
    """the Set node is the root of the syntax tree for update statement"""

    TYPE = "set"

    def __init__(self):
        Statement.__init__(self)
        ScopeNode.__init__(self)
        self.main_relations = []

    @property
    def children(self):
        children = self.main_relations[:]
        if self.where:
            children.append(self.where)
        if self.having:
            children += self.having
        return children

    @property
    def selection(self):
        return []

    def add_main_relation(self, relation: "rql.nodes.Relation") -> None:
        """add a relation to the list of modified relations"""
        relation.parent = self
        self.main_relations.append(relation)

    # repr / as_string / copy #################################################

    def __repr__(self) -> str:
        result = ["SET"]
        result.append(", ".join(repr(rel) for rel in self.main_relations))
        if self.where is not None:
            result.append("WHERE " + repr(self.where))
        if self.having:
            result.append("HAVING " + ",".join(repr(term) for term in self.having))
        return " ".join(result)

    def as_string(self, kwargs: Optional[Any] = None) -> str:
        """return the tree as an encoded rql string"""
        result = ["SET"]
        result.append(
            ", ".join(rel.as_string(kwargs=kwargs) for rel in self.main_relations)
        )
        if self.where is not None:
            result.append("WHERE " + self.where.as_string(kwargs=kwargs))
        if self.having:
            result.append(
                "HAVING "
                + ",".join(term.as_string(kwargs=kwargs) for term in self.having)
            )
        return " ".join(result)

    # Signature of "copy" incompatible with supertype "ScopeNode"  [override]
    # Signature of "copy" incompatible with supertype "BaseNode"  [override]
    def copy(self) -> "Set":  # type:ignore[override]
        new = Set()
        for child in self.main_relations:
            new.add_main_relation(child.copy(new))
        if self.where:
            new.set_where(self.where.copy(new))
        if self.having:
            new.set_having([sq.copy(new) for sq in self.having])
        return new


AnyStatement = Union_[
    Set,
    Delete,
    Union,
    Insert,
]


AnyScopeNode = Union_[
    Set,
    Delete,
    Insert,
    Select,
]
