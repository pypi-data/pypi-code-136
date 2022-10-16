import typing

from src.ok_zadanie_1.vertex import Vertex

from .edge import Edge


class DirectedEdge(Edge):

	def __init__(self, starting_vertex: Vertex, ending_vertex: Vertex) -> None:
		self._starting_vertex: typing.Final[Vertex] = starting_vertex
		self._ending_vertex: typing.Final[Vertex] = ending_vertex

	def get_starting_vertex(self) -> Vertex:
		return self._starting_vertex

	def get_ending_vertex(self) -> Vertex:
		return self._ending_vertex

	# override
	def get_vertex_1(self) -> Vertex:
		return self.get_starting_vertex()

	# override
	def get_vertex_2(self) -> Vertex:
		return self.get_ending_vertex()
