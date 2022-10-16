from __future__ import annotations

import abc
import typing

from src.ok_zadanie_1.edge import Edge
from src.ok_zadanie_1.vertex import Vertex

E = typing.TypeVar("E", bound=Edge)


class Graph(abc.ABC, typing.Generic[E]):
	@abc.abstractmethod
	def __init__(
		self,
	) -> None:
		pass

	@classmethod
	@abc.abstractmethod
	def from_vertices(
		cls,
		new_vertices: set[Vertex],
	) -> Graph[E]:
		pass

	@classmethod
	@abc.abstractmethod
	def from_vertices_and_edges(
		cls,
		new_vertices: set[Vertex],
		new_edges: set[E],
	) -> Graph[E]:
		pass

	@abc.abstractmethod
	def get_vertices(self) -> set[Vertex]:
		pass

	@abc.abstractmethod
	def get_edges(self) -> set[E]:
		pass

	@abc.abstractmethod
	def get_edges_from_vertex(self, exi_vertex: Vertex) -> set[E]:
		pass

	@abc.abstractmethod
	def get_edges_to_vertex(self, exi_vertex: Vertex) -> set[E]:
		pass

	@abc.abstractmethod
	def get_edges_from_vertex_to_vertex(
		self,
		exi_starting_vertex: Vertex,
		exi_ending_vertex: Vertex,
	) -> set[E]:
		pass

	@abc.abstractmethod
	def add_vertex(self, new_vertex: Vertex) -> None:
		pass

	@abc.abstractmethod
	def add_vertices(
		self,
		new_vertices: set[Vertex],
	) -> None:
		pass

	@abc.abstractmethod
	def add_edge(self, new_edge: E) -> None:
		pass

	@abc.abstractmethod
	def add_edges(self, new_edges: set[E]) -> None:
		pass

	@abc.abstractmethod
	def add_vertices_and_edges(
		self,
		new_vertices: set[Vertex],
		new_edges: set[E],
	) -> None:
		pass

	@abc.abstractmethod
	def remove_vertex(self, rem_vertex: Vertex) -> None:
		pass

	@abc.abstractmethod
	def remove_vertices(self, rem_vertices: set[Vertex]) -> None:
		pass

	@abc.abstractmethod
	def remove_edge(self, rem_edge: E) -> None:
		pass

	@abc.abstractmethod
	def remove_edges(self, rem_edges: set[E]) -> None:
		pass

	@abc.abstractmethod
	def remove_vertices_and_edges(
		self,
		rem_vertices: set[Vertex],
		rem_edges: set[E],
	) -> None:
		pass
