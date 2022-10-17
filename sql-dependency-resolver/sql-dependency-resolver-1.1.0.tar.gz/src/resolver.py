from os import listdir
from os.path import isfile, join, split
from pathlib import Path
from typing import List

from src.graph import Graph
from src.sql_node import ViewNode
from src.topological_sort import TopologicalSortMixin


class DependencyResolver(TopologicalSortMixin):
    """Resolver class implements a create and drop method providing the conflict-free ordering for creation and destruction of SQL objects.

    Args:
        TopologicalSortMixin (class): sort mixin for topological sorting.
    """
    type_class = None

    def __init__(self, objects_path: str) -> None:
        self.graph = Graph()
        self.files = [
            join(objects_path, f)
            for f in listdir(objects_path)
            if isfile(join(objects_path, f))
        ]
        self.create_nodes()
        self.order = self.sort(graph=self.graph.graph, size=self.graph.size)

    def create_nodes(self) -> None:
        """Create SQL nodes and append to dependency graph."""
        for file in self.files:
            node = self.type_class(file)
            name = Path(file).stem
            for dependency in node.dependencies:
                self.graph.add_edge(dependency, name)

    def create_order(self) -> List:
        """The order to create SQL objects.

        Returns:
            List: creation order.
        """
        return self.order

    def drop_order(self) -> List:
        """The order to destroy the SQL objects.

        Returns:
            List: destruction order.
        """
        return list(reversed(self.order))

class ViewDependencyResolver(DependencyResolver):
    type_class = ViewNode