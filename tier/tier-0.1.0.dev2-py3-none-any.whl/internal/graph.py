# std
from __future__ import annotations
from collections import defaultdict
from typing import Generator, Generic, Iterable, Iterator, List, TypeVar, Union

# types
T = TypeVar('T')


class IdGenerator:

    def __init__(self):
        self._next_id: int = 0

    def __next__(self) -> int:
        next_id = self._next_id
        self._next_id += 1
        return next_id

    def next(self) -> int:
        return next(self)

    def reset(self):
        self._next_id = 0


class Vertex(Generic[T]):
    id_generator = IdGenerator()

    def __init__(self, data: T):
        self.data: T = data
        self.edges: List[DirectedEdge] = []
        self.id = self.id_generator.next()

    def __rshift__(self, other: Vertex):
        self.add_edge(other)

    def add_edge(self, destination: Vertex):
        edge = DirectedEdge(self, destination)
        if edge not in self.edges:
            self.edges.append(edge)

    def get_neighbors(self) -> List[Vertex]:
        return [e.destination for e in self.edges]


class DirectedEdge:

    def __init__(self, source: Vertex, destination: Vertex):
        self.source = source
        self.destination = destination
        self.ids = (source.id, destination.id)

    def __eq__(self, other: DirectedEdge) -> bool:
        return self.ids == other.ids


class Graph(Generic[T]):

    def __init__(self, *vertices: Vertex[T]):
        self.vertices: List[Vertex[T]] = list(vertices)

    def __add__(self, vertex_or_vertices: Union[Vertex[T], Iterable[Vertex[T]]]) -> Graph[T]:
        if isinstance(vertex_or_vertices, Vertex):
            self.add_vertex(vertex_or_vertices)
        else:
            self.add_vertices(*vertex_or_vertices)
        return self

    def add_vertex(self, vertex: Vertex[T]) -> Graph[T]:
        if vertex not in self.vertices:
            self.vertices.append(vertex)
        return self

    def add_vertices(self, *vertices: Vertex[T]) -> Graph[T]:
        for vertex in vertices:
            self.add_vertex(vertex)
        return self

    def add_edge(self, source: Vertex[T], destination: Vertex[T]) -> Graph[T]:
        self.add_vertices(source, destination)
        source.add_edge(destination)
        return self

    def depth_first_search(self) -> Iterable[Vertex[T]]:
        return DepthFirstSearch(self)


class DepthFirstSearch(Iterable[Vertex[T]]):

    def __init__(self, graph: Graph[T]):
        self.graph = graph
        self.visited = defaultdict(lambda: 0)

    def __iter__(self) -> Iterator[Vertex[T]]:
        return self.search(self.graph.vertices)

    def search(self, vertices: Iterable[Vertex[T]]) -> Generator[Vertex[T], None, None]:
        for vertex in vertices:
            for destination in self.search(vertex.get_neighbors()):
                yield destination
            if not self.visited[vertex.id]:
                yield vertex
                self.visited[vertex.id] += 1
