from collections import defaultdict
from typing import TypeVar


T = TypeVar("T")


class Graph:
    """This class describes a directed graph, the graph is represented using an adjacency list."""

    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.size = 0

    def __repr__(self) -> str:
        """returns the representation of the graph in a pretty print format.

        Returns:
            str: adjancey list representation.
        """
        str_builder = [f"{u} => {v}\n" for u, v in self.graph.items()]
        return "".join(str_builder)

    def add_edge(self, u: T, v: T) -> None:
        """add an edge from u to v and store this in the adjancey list.
            Update the size of graph on every insert.

        Args:
            u (T): vertex from.
            v (T): vertex to.
        """
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []

        self.size = len(self.graph)
