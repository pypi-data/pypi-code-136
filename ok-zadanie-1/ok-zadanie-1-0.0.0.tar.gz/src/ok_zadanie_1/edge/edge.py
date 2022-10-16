from abc import ABC, abstractmethod

from src.ok_zadanie_1.vertex import Vertex


class Edge(ABC):

	@abstractmethod
	def __init__(self, vertex_1: Vertex, vertex_2: Vertex) -> None:
		pass

	@abstractmethod
	def get_vertex_1(self) -> Vertex:
		pass

	@abstractmethod
	def get_vertex_2(self) -> Vertex:
		pass
