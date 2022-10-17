from collections import deque
from typing import List, TypeVar

T = TypeVar("T")


class CircularDependencyException(Exception):
    """Raised when a circular dependency is detected."""

    pass


class TopologicalSortMixin:
    """Mixin that provides methods required for topological sorting.
    Sorting is acheived using Khan's algorithm against an adjancey list.
    Constraints:
      - adjancey list represnts a directed acylic graph.
    """

    @staticmethod
    def in_degrees(graph: dict, size: int) -> dict:
        """produce a dict of in-degree counts for each vertex.

        Args:
            graph (dict): adjaceny list representing graph.
            size (int): size of the graph

        Returns:
            dict: key: vertex, value: indegree count
        """
        degrees = dict.fromkeys(graph.keys(), 0)
        for value in graph.values():
            for dependency in value:
                degrees[dependency] += 1
        return degrees

    @staticmethod
    def sort(graph: dict, size: int) -> List:
        """Return a list with containing the topological ordering of the graph.

        Args:
            graph (dict): adjaceny list representing graph.
            size (int): size of the graph.

        Returns:
            List: topological ordering.
        """
        queue = deque()
        degrees = TopologicalSortMixin.in_degrees(graph, size)
        topological = []

        # add verticies with in-degree of 0 to queue.
        for vertex in degrees:
            in_degree = degrees[vertex]
            if in_degree == 0:
                queue.append(vertex)

        while queue:
            # pop queue and add to stack
            vertex = queue.popleft()
            topological.append(vertex)

            # decrement degree of all affected verticies
            for neighbour in graph[vertex]:
                degrees[neighbour] -= 1
                # if degree of neighbour becomes 0 add to queue
                if degrees[neighbour] == 0:
                    queue.append(neighbour)

        if len(topological) != size:
            raise CircularDependencyException("Cycle detected")
        else:
            return topological
