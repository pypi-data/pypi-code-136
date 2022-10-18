from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from typing import Tuple

INDENT_BLOCK = "  "

global_id = 0
global_map = {}


def get_new_id():
    global global_id
    global_id += 1
    return global_id


def reset_ids():
    """Resets the global id to 0, so that ids will start from 1.

    This should only be used for tests.
    """
    global global_id
    global_id = 0


def create_header(query_node: "QueryNode") -> str:
    """Assigns a unique id to the given QueryNode, adds it to a global map, and creates a header."""
    new_id = get_new_id()
    global_map[new_id] = query_node
    return f"<{new_id}>"


@dataclass
class NodeRef:
    """
    Used so we can more easily modify the QueryTree by inserting and removing nodes, e.g.
    def subtree_rewrite(subtree_node_ref):
        subtree_node_ref.node = NewNode(subtree_node_ref.node)
    """

    node: "QueryNode"

    @property
    def inputs(self):
        return self.node.inputs

    def as_str(self, verbose: bool = False) -> str:
        return self.node.as_str(verbose)

    def pretty_print(
        self,
        verbose: bool = False,
        indents: int = 0,
        indent_block: str = INDENT_BLOCK,
        show_ids: bool = True,
        names_only: bool = False,
    ):
        return self.node.pretty_print(verbose, indents, indent_block, show_ids, names_only)


class QueryNode(ABC):
    def as_ref(self) -> NodeRef:
        return NodeRef(self)

    # used for recursing through the tree for tree rewrites
    @property
    @abstractmethod
    def inputs(self) -> Tuple[NodeRef]:
        pass

    @abstractmethod
    def as_str(self, verbose: bool) -> str:
        """
        Prints contents of this node and calls recursively on its inputs.
        Used by tecton.TectonDataFrame.explain
        """
        pass

    def pretty_print_self(
        self,
        verbose: bool = False,
        indents: int = 0,
        indent_block: str = INDENT_BLOCK,
        show_ids: bool = True,
        names_only: bool = False,
    ):
        """
        Returns a formatted string representation of the contents of this node.
        Handles indentation, and optionally generates and displays an id.
        If `names_only` is True, only the class name of the node will be used.
        """
        header = create_header(self) if show_ids else ""
        header_length = len(header)

        s = ""

        if names_only:
            s += header
            s += INDENT_BLOCK * indents
            s += self.__class__.__name__
            s += "\n"
            return s

        lines = self.as_str(verbose=verbose).rstrip()
        for i, line in enumerate(lines.split("\n")):
            # We use the header for the first line; for all subsequent lines, we use
            # whitespace of an equal length.
            s += header if i == 0 else " " * header_length
            s += INDENT_BLOCK * indents + line + "\n"
        return s

    def pretty_print(
        self,
        verbose: bool = False,
        indents: int = 0,
        indent_block: str = INDENT_BLOCK,
        show_ids: bool = True,
        names_only: bool = False,
    ) -> str:
        """
        Returns a string representation of the contents of this node and all its ancestors.
        Handles indentation, and optionally generates ids for the node and its ancestors.
        If `names_only` is True, only the class names of the nodes will be used.
        """
        # Build string representation of this node.
        s = self.pretty_print_self(verbose, indents, indent_block, show_ids, names_only)

        # Recursively add ancestors.
        for i in self.inputs:
            s += i.pretty_print(verbose, indents + 1, indent_block, show_ids, names_only)

        return s
