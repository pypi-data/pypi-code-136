import typing

from src.ok_zadanie_1.vertex import Vertex

from .edge import Edge


class UndirectedEdge(Edge):

	def __init__(self, vertex_1: Vertex, vertex_2: Vertex) -> None:
		self._vertex_1: typing.Final[Vertex] = vertex_1
		self._vertex_2: typing.Final[Vertex] = vertex_2

	# override
	def get_vertex_1(self) -> Vertex:
		return self._vertex_1

	# override
	def get_vertex_2(self) -> Vertex:
		return self._vertex_2
