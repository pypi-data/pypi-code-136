import abc
import typing

from src.ok_zadanie_1.edge import Edge
from src.ok_zadanie_1.vertex import Vertex

from .graph import Graph

E = typing.TypeVar("E", bound=Edge)


class AbstractGraph(Graph[E], abc.ABC, typing.Generic[E]):

	def _add_vertices(self, new_vertices: set[Vertex]) -> None:
		for new_vertex in new_vertices:
			self._add_vertex(new_vertex)

	def _remove_vertices(self, rem_vertices: set[Vertex]) -> None:
		for rem_vertex in rem_vertices:
			self._remove_vertex(rem_vertex)

	def _remove_edges(self, rem_edges: set[E]) -> None:
		for rem_edge in rem_edges:
			self._remove_edge(rem_edge)

	def _add_edges(self, new_edges: set[E]) -> None:
		for new_edge in new_edges:
			self._add_edge(new_edge)

	def _add_vertices_and_edges(
		self,
		new_vertices: set[Vertex],
		new_edges: set[E],
	) -> None:
		self._add_vertices(new_vertices)
		self._add_edges(new_edges)

	def _remove_vertices_and_edges(
		self,
		rem_vertices: set[Vertex],
		rem_edges: set[E],
	) -> None:
		self._remove_edges(rem_edges)
		self._remove_vertices(rem_vertices)

	@abc.abstractmethod
	def _add_vertex(self, new_vertex: Vertex) -> None:
		pass

	@abc.abstractmethod
	def _add_edge(self, new_edge: E) -> None:
		pass

	@abc.abstractmethod
	def _remove_vertex(self, rem_vertex: Vertex) -> None:
		pass

	@abc.abstractmethod
	def _remove_edge(self, rem_edge: E) -> None:
		pass

	def _check_if_edge_has_vertices_in_graph(
		self,
		edge: E,
	) -> bool:
		return \
			edge.get_vertex_1() in self.get_vertices() \
			and edge.get_vertex_2() in self.get_vertices()

	def _assert_edge_with_correct_vertices_having_vertices(
		self,
		edge: E,
		vertices: set[Vertex],
	) -> None:
		self._assert_valid_existing_vertex_having_vertices(
			edge.get_vertex_1(),
			vertices,
		)
		self._assert_valid_existing_vertex_having_vertices(
			edge.get_vertex_2(),
			vertices,
		)

	def _assert_valid_new_edge_having_vertices(
		self,
		edge: E,
		vertices: set[Vertex],
	) -> None:
		self._assert_edge_with_correct_vertices_having_vertices(
			edge,
			vertices,
		)
		if self._check_if_edge_has_vertices_in_graph(edge):
			self._assert_valid_new_edge(edge)

	def _assert_valid_existing_edge_having_vertices(
		self,
		edge: E,
		vertices: set[Vertex],
	) -> None:
		self._assert_edge_with_correct_vertices_having_vertices(
			edge,
			vertices,
		)
		if self._check_if_edge_has_vertices_in_graph(edge):
			self._assert_valid_existing_edge(edge)

	# override
	def __init__(
		self,
	) -> None:
		self._matrix: dict[Vertex, dict[Vertex, set[E]]] = dict()

	# @classmethod
	# # override
	# def from_vertices(
	# 	cls,
	# 	new_vertices: set[Vertex],
	# ) -> Graph[E]:
	# 	graph = cls()
	# 	graph.add_vertices(new_vertices)
	# 	return graph

	# @classmethod
	# # override
	# def from_vertices_and_edges(
	# 	cls,
	# 	new_vertices: set[Vertex],
	# 	new_edges: set[E],
	# ) -> Graph[E]:
	# 	graph = cls()
	# 	graph.add_vertices_and_edges(new_vertices, new_edges)
	# 	return graph

	# override
	def get_vertices(self) -> set[Vertex]:
		return set(self._matrix.keys())

	# override
	def get_edges(self) -> set[E]:
		edges: set[E] = set()
		for vertex_1 in self._matrix.keys():
			for vertex_2 in self._matrix[vertex_1].keys():
				edges.update(self._matrix[vertex_1][vertex_2])
		return edges

	# override
	def get_edges_from_vertex(self, exi_vertex: Vertex) -> set[E]:
		self._assert_valid_existing_vertex(exi_vertex)
		edges: set[E] = set()
		for vertex_2 in self._matrix[exi_vertex].keys():
			edges.update(self._matrix[exi_vertex][vertex_2])
		return edges

	# override
	def get_edges_to_vertex(self, exi_vertex: Vertex) -> set[E]:
		self._assert_valid_existing_vertex(exi_vertex)
		edges: set[E] = set()
		for vertex_1 in self._matrix.keys():
			edges.update(self._matrix[vertex_1][exi_vertex])
		return edges

	# override
	def get_edges_from_vertex_to_vertex(
		self,
		exi_starting_vertex: Vertex,
		exi_ending_vertex: Vertex,
	) -> set[E]:
		self._assert_valid_existing_vertex(exi_starting_vertex)
		self._assert_valid_existing_vertex(exi_ending_vertex)
		edges: set[E] = set()
		edges.update(self._matrix[exi_starting_vertex][exi_ending_vertex])
		return edges

	# override
	def add_vertex(self, new_vertex: Vertex) -> None:
		self._assert_valid_new_vertex(new_vertex)
		self._add_vertex(new_vertex)

	# override
	def add_vertices(
		self,
		new_vertices: set[Vertex],
	) -> None:
		self._assert_valid_new_vertices(new_vertices)
		self._add_vertices(new_vertices)

	# override
	def add_edge(self, new_edge: E) -> None:
		self._assert_valid_new_edge(new_edge)
		self._add_edge(new_edge)

	# override
	def add_edges(self, new_edges: set[E]) -> None:
		self._assert_valid_new_edges(new_edges)
		self._add_edges(new_edges)

	# override
	def add_vertices_and_edges(
		self,
		new_vertices: set[Vertex],
		new_edges: set[E],
	) -> None:
		self._assert_valid_new_vertices_and_new_edges(new_vertices, new_edges)
		self._add_vertices_and_edges(new_vertices, new_edges)

	# override
	def remove_vertex(self, rem_vertex: Vertex) -> None:
		self._assert_valid_existing_vertex(rem_vertex)
		self._remove_vertex(rem_vertex)

	# override
	def remove_vertices(self, rem_vertices: set[Vertex]) -> None:
		self._assert_valid_existing_vertices(rem_vertices)
		self._remove_vertices(rem_vertices)

	# override
	def remove_edge(self, rem_edge: E) -> None:
		self._assert_valid_existing_edge(rem_edge)
		self._remove_edge(rem_edge)

	# override
	def remove_edges(self, rem_edges: set[E]) -> None:
		self._assert_valid_existing_edges(rem_edges)
		self._remove_edges(rem_edges)

	# override
	def remove_vertices_and_edges(
		self,
		rem_vertices: set[Vertex],
		rem_edges: set[E],
	) -> None:
		self._assert_valid_existing_vertices_and_existing_edges(
			rem_vertices,
			rem_edges,
		)
		self._remove_vertices_and_edges(rem_vertices, rem_edges)

	def _assert_valid_new_edges_having_vertices(
		self,
		edges: set[E],
		vertices: set[Vertex],
	) -> None:
		for edge in edges:
			self._assert_valid_new_edge_having_vertices(edge, vertices)

	def _assert_valid_existing_edges_having_vertices(
		self,
		edges: set[E],
		vertices: set[Vertex],
	) -> None:
		for edge in edges:
			self._assert_valid_existing_edge_having_vertices(edge, vertices)

	def _assert_valid_existing_vertex(self, exi_vertex: Vertex) -> None:
		self._assert_valid_existing_vertex_having_vertices(
			exi_vertex,
			self.get_vertices(),
		)

	def _assert_valid_existing_vertex_having_vertices(
		self,
		exi_vertex: Vertex,
		vertices: set[Vertex],
	) -> None:
		if exi_vertex not in vertices:
			raise ValueError(f"Vertex {exi_vertex} does not exist in graph")

	def _assert_valid_new_vertex(self, new_vertex: Vertex) -> None:
		self._assert_valid_new_vertex_having_vertices(
			new_vertex,
			self.get_vertices(),
		)

	def _assert_valid_new_vertex_having_vertices(
		self,
		new_vertex: Vertex,
		vertices: set[Vertex],
	) -> None:
		if new_vertex in vertices:
			raise ValueError(f"Vertex {new_vertex} already exists in graph")

	def _assert_valid_new_vertices(self, new_vertices: set[Vertex]) -> None:
		for new_vertex in new_vertices:
			self._assert_valid_new_vertex(new_vertex)

	@abc.abstractmethod
	def _assert_valid_new_edge(self, new_edge: E) -> None:
		pass

	def _assert_valid_new_edges(self, new_edges: set[E]) -> None:
		for new_edge in new_edges:
			self._assert_valid_new_edge(new_edge)

	def _assert_valid_new_vertices_and_new_edges(
		self,
		new_vertices: set[Vertex],
		new_edges: set[E],
	) -> None:
		self._assert_valid_new_vertices(new_vertices)
		self._assert_valid_new_edges_having_vertices(
			new_edges,
			self.get_vertices().union(new_vertices),
		)

	def _assert_valid_existing_vertices(self, exi_vertices: set[Vertex]) -> None:
		for exi_vertex in exi_vertices:
			self._assert_valid_existing_vertex(exi_vertex)

	def _assert_valid_existing_edge(self, exi_edge: E) -> None:
		self._assert_valid_existing_edge_having_vertices(
			exi_edge,
			self.get_vertices(),
		)

	def _assert_valid_existing_edges(self, exi_edges: set[E]) -> None:
		for exi_edge in exi_edges:
			self._assert_valid_existing_edge(exi_edge)

	def _assert_valid_existing_vertices_and_existing_edges(
		self,
		exi_vertices: set[Vertex],
		exi_edges: set[E],
	) -> None:
		self._assert_valid_existing_edges_having_vertices(
			exi_edges,
			self.get_vertices(),
		)
		self._assert_valid_existing_vertices(exi_vertices)
