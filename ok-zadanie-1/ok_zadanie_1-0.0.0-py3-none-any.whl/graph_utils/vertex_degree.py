from src.ok_zadanie_1.graph import DirectedGraph, UndirectedGraph
from src.ok_zadanie_1.vertex import Vertex


def calculate_vertex_degree(
	graph: UndirectedGraph,
	vertex: Vertex,
) -> int:
	return len(graph.get_edges_on_vertex(vertex))


def calculate_all_vertices_degrees(
	graph: UndirectedGraph,
) -> dict[Vertex, int]:
	return {
		vertex: calculate_vertex_degree(graph, vertex)
		for vertex in graph.get_vertices()
	}


def calculate_max_degree(
	graph: UndirectedGraph,
) -> int:
	return max(calculate_all_vertices_degrees(graph).values())


def calculate_min_degree(
	graph: UndirectedGraph,
) -> int:
	return min(calculate_all_vertices_degrees(graph).values())


def calculate_all_vertices_indegrees(
	graph: DirectedGraph,
) -> dict[Vertex, int]:
	return {
		vertex: calculate_vertex_indegree(graph, vertex)
		for vertex in graph.get_vertices()
	}


def calculate_all_vertices_outdegrees(
	graph: DirectedGraph,
) -> dict[Vertex, int]:
	return {
		vertex: calculate_vertex_outdegree(graph, vertex)
		for vertex in graph.get_vertices()
	}


def calculate_vertex_indegree(
	graph: DirectedGraph,
	vertex: Vertex,
) -> int:
	return len(graph.get_edges_to_vertex(vertex))


def calculate_max_indegree(
	graph: DirectedGraph,
) -> int:
	return max(calculate_all_vertices_indegrees(graph).values())


def calculate_max_outdegree(
	graph: DirectedGraph,
) -> int:
	return max(calculate_all_vertices_outdegrees(graph).values())


def calculate_vertex_outdegree(
	graph: DirectedGraph,
	vertex: Vertex,
) -> int:
	return len(graph.get_edges_from_vertex(vertex))


def calculate_min_indegree(
	graph: DirectedGraph,
) -> int:
	return min(calculate_all_vertices_indegrees(graph).values())


def calculate_min_outdegree(
	graph: DirectedGraph,
) -> int:
	return min(calculate_all_vertices_outdegrees(graph).values())


def calculate_modulo_stats_from_degrees(
	graph: UndirectedGraph,
	modulo: int,
) -> dict[int, int]:
	all_vertices_degrees = calculate_all_vertices_degrees(graph)
	modulo_stats: dict[int, int] = {i: 0 for i in range(modulo)}
	for vertex_degree in all_vertices_degrees.values():
		modulo_stats[vertex_degree % modulo] += 1
	return modulo_stats


def calculate_modulo_stats_from_indegrees(
	graph: DirectedGraph,
	modulo: int,
) -> dict[int, int]:
	all_vertices_indegrees = calculate_all_vertices_indegrees(graph)
	modulo_stats: dict[int, int] = {i: 0 for i in range(modulo)}
	for vertex_indegree in all_vertices_indegrees.values():
		modulo_stats[vertex_indegree % modulo] += 1
	return modulo_stats


def calculate_modulo_stats_from_outdegrees(
	graph: DirectedGraph,
	modulo: int,
) -> dict[int, int]:
	all_vertices_outdegrees = calculate_all_vertices_outdegrees(graph)
	print(all_vertices_outdegrees)
	modulo_stats: dict[int, int] = {i: 0 for i in range(modulo)}
	for vertex_outdegree in all_vertices_outdegrees.values():
		modulo_stats[vertex_outdegree % modulo] += 1
	return modulo_stats

def get_degrees_sorted(
	graph: UndirectedGraph,
) -> list[int]:
	return sorted(calculate_all_vertices_degrees(graph).values())

def get_indegrees_sorted(
	graph: DirectedGraph,
) -> list[int]:
	return sorted(calculate_all_vertices_indegrees(graph).values())

def get_outdegrees_sorted(
	graph: DirectedGraph,
) -> list[int]:
	return sorted(calculate_all_vertices_outdegrees(graph).values())
