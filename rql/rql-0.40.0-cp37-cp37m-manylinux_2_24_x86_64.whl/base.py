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
"""Base classes for RQL syntax tree nodes.

Note: this module uses __slots__ to limit memory usage.
"""


from rql.utils import VisitableMixIn
from typing import (
    Tuple,
    List,
    Any,
    Optional,
    TYPE_CHECKING,
    Iterator,
    Union as Union_,
    Dict,
    Type,
    TypeVar,
    Iterable,
    Sequence,
)

__docformat__: str = "restructuredtext en"


if TYPE_CHECKING:
    import rql


_Y = TypeVar("_Y", bound="BaseNode")


class BaseNode(VisitableMixIn):
    __slots__: Iterable[str] = ("parent",)

    if TYPE_CHECKING:
        parent: Optional["BaseNode"]

        # the only class that doesn't have children is ScopeNode but it
        # doesn't seems to be used explicitely anywhere and ALL its children
        # have a "children" attribute, so we take the decision to make
        # everything simplier and, for typing, pretend that ALL nodes have
        # children
        # also ScopeNode really seems to be an abstract base class
        # note: ALL subclass of BaseNode (except ScopeNode) also have children
        children: Sequence["BaseNode"]

        # another option would be to define a new type like this:
        # NodeWithChildren = Union_[Node, LeafNode, SubQuery, Set, Insert, Delete,
        #                           Exists]
        # or create a protocol in the same fashion

    def __str__(self) -> str:
        s: str = self.as_string()
        return s

    def as_string(self, kwargs: Dict = None) -> str:
        """Return the tree as an encoded rql string."""
        raise NotImplementedError()

    def initargs(self, stmt: Optional["rql.stmts.Statement"]) -> Tuple[Any, ...]:
        """Return list of arguments to give to __init__ to clone this node.

        I don't use __getinitargs__ because I'm not sure it should interfer with
        copy/pickle
        """
        return ()

    # pyannotate suggested rql.stmts.Union as returned type, samples=2
    # but it sound like we should return a Node here
    @property
    def root(self) -> Optional["BaseNode"]:
        """Return the root node of the tree"""
        if self.parent is not None:
            return self.parent.root
        return None  # should we return None or something else?

    @property
    def stmt(self) -> Optional["rql.stmts.Statement"]:
        """Return the Select node to which this node belong"""
        if self.parent is not None:
            return self.parent.stmt
        return None  # should we return None or something else?

    @property
    def scope(self) -> Optional[Union_["rql.stmts.Statement", "BaseNode"]]:
        """Return the scope node to which this node belong (eg Select or Exists
        node)
        """
        if self.parent is not None:
            return self.parent.scope
        return None  # should we return None or something else?

    def get_nodes(self, klass: Type[_Y]) -> List[_Y]:
        """Return the list of nodes of a given class in the subtree.

        :type klass: a node class (Relation, Constant, etc.)
        :param klass: the class of nodes to return

        :rtype: list
        """
        stack: List[Any] = [self]
        result = []
        while stack:
            node = stack.pop()
            if isinstance(node, klass):
                result.append(node)
            else:
                stack += node.children
        return result

    def iget_nodes(self, klass: Type[_Y]) -> Iterator[_Y]:
        """Return an iterator over nodes of a given class in the subtree.

        :type klass: a node class (Relation, Constant, etc.)
        :param klass: the class of nodes to return

        :rtype: iterator
        """
        stack: List[Any] = [self]
        while stack:
            node = stack.pop()
            if isinstance(node, klass):
                yield node
            else:
                stack += node.children

    # Argument 1 to "is_equivalent" of "BaseNode" has incompatible type "IsOperator";
    # expected "BaseNode"  [arg-type]
    # Argument 2 to "is_equivalent" of "BaseNode" has incompatible type "IsOperator";
    # expected "BaseNode"  [arg-type]
    # def is_equivalent(self, other: "BaseNode") -> bool:
    # Any here really means: any children of BaseNode
    def is_equivalent(self: Any, other: Any) -> bool:
        if other.__class__ is not self.__class__:
            return False
        for i, child in enumerate(self.children):
            try:
                if not child.is_equivalent(other.children[i]):
                    return False
            except IndexError:
                return False
        return True

    def copy(self, stmt: Optional["rql.stmts.Statement"] = None) -> "BaseNode":
        raise NotImplementedError()

    def replace(
        self, old_child: "BaseNode", new_child: "BaseNode"
    ) -> Tuple["BaseNode", "BaseNode", Optional[int]]:
        raise NotImplementedError()


class Node(BaseNode):
    """Class for nodes of the tree which may have children (almost all...)"""

    __slots__: Iterable[str] = ("children",)

    def __init__(self):
        self.parent: Optional[BaseNode] = None
        self.children: List[BaseNode] = []

    def append(self, child: BaseNode):
        """add a node to children"""
        self.children.append(child)
        child.parent = self

    def remove(
        self, child: BaseNode
    ) -> Tuple[BaseNode, Optional[BaseNode], Optional[int]]:
        """Remove a child node. Return the removed node, its old parent and
        index in the children list.
        """
        index: int = self.children.index(child)
        del self.children[index]
        parent = child.parent
        child.parent = None
        return child, parent, index

    def insert(self, index: int, child: BaseNode):
        """insert a child node"""
        self.children.insert(index, child)
        child.parent = self

    def replace(
        self, old_child: BaseNode, new_child: BaseNode
    ) -> Tuple[BaseNode, BaseNode, Optional[int]]:
        """replace a child node with another"""
        i = self.children.index(old_child)
        self.children.pop(i)
        self.children.insert(i, new_child)
        new_child.parent = self
        return old_child, self, i

    def copy(self, stmt: Optional["rql.stmts.Statement"] = None) -> "Node":
        """Create and return a copy of this node and its descendant.

        stmt is the root node, which should be use to get new variables
        """
        new: Node = self.__class__(*self.initargs(stmt))
        for child in self.children:
            new.append(child.copy(stmt))
        return new


class BinaryNode(Node):
    __slots__: Iterable[str] = ()

    def __init__(
        self,
        lhs: Optional["BaseNode"] = None,
        rhs: Optional["BaseNode"] = None,
    ):

        Node.__init__(self)
        if lhs is not None:
            self.append(lhs)
        if rhs is not None:
            self.append(rhs)

    def remove(
        self, child: "BaseNode"
    ) -> Tuple["BaseNode", Optional["BaseNode"], Optional[int]]:
        """Remove the child and replace this node with the other child."""
        index: int = self.children.index(child)
        if self.parent is not None:
            return self.parent.replace(self, self.children[not index])
        return child, None, index

    def get_parts(self) -> Tuple["BaseNode", "BaseNode"]:
        """Return the left hand side and the right hand side of this node."""
        return self.children[0], self.children[1]


class LeafNode(BaseNode):
    """Class optimized for leaf nodes."""

    __slots__: Iterable[str] = ()

    # We can't do that because of a bug in mypy see
    # https://github.com/python/mypy/issues/4125#issuecomment-337187251
    # @property
    # def children(self) -> Sequence["BaseNode"]:
    @property
    def children(self):
        return ()

    def copy(
        self: "BaseNode", stmt: Optional["rql.stmts.Statement"] = None
    ) -> "BaseNode":
        """Create and return a copy of this node and its descendant.

        stmt is the root node, which should be use to get new variables.
        """
        return self.__class__(*self.initargs(stmt))
