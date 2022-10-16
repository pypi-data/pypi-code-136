from __future__ import annotations
from src.ok_zadanie_1.edge import UndirectedEdge
from src.ok_zadanie_1.vertex import Vertex

from .abstract_graph import AbstractGraph


class UndirectedGraph(AbstractGraph[UndirectedEdge]):

	@classmethod
	def from_vertices(
		cls,
		new_vertices: set[Vertex],
	) -> UndirectedGraph:
		graph = cls()
		graph.add_vertices(new_vertices)
		return graph

	@classmethod
	def from_vertices_and_edges(
		cls,
		new_vertices: set[Vertex],
		new_edges: set[UndirectedEdge],
	) -> UndirectedGraph:
		graph = cls()
		graph.add_vertices_and_edges(new_vertices, new_edges)
		return graph

	# override
	def _add_vertex(self, new_vertex: Vertex) -> None:
		for vertex in self._matrix:
			self._matrix[vertex][new_vertex] = set()
		self._matrix[new_vertex] = dict()
		self._matrix[new_vertex][new_vertex] = set()
		for vertex in self._matrix:
			self._matrix[new_vertex][vertex] = self._matrix[vertex][new_vertex]

	# override
	def _remove_vertex(self, rem_vertex: Vertex) -> None:
		del self._matrix[rem_vertex]
		for vertex in self._matrix:
			del self._matrix[vertex][rem_vertex]

	# override
	def _add_edge(self, new_edge: UndirectedEdge) -> None:
		self._matrix[
			new_edge.get_vertex_1()
		][
			new_edge.get_vertex_2()
		].add(new_edge)

	# override
	def _remove_edge(self, rem_edge: UndirectedEdge) -> None:
		self._matrix[
			rem_edge.get_vertex_1()
		][
			rem_edge.get_vertex_2()
		].remove(rem_edge)

	# override
	def _assert_valid_new_edge(
		self,
		new_edge: UndirectedEdge,
	) -> None:
		if \
			new_edge in self._matrix[
				new_edge.get_vertex_1()
			][
				new_edge.get_vertex_2()
			]:
			raise ValueError("Edge already exists in graph")

	# override
	def _assert_valid_existing_edge(
		self,
		exi_edge: UndirectedEdge,
	) -> None:
		if \
			exi_edge not in self._matrix[
				exi_edge.get_vertex_1()
			][
				exi_edge.get_vertex_2()
			]:
			raise ValueError("Edge does not exist in graph")

	def get_edges_on_vertex(self, vertex: Vertex) -> set[UndirectedEdge]:
		return self.get_edges_from_vertex(vertex)
