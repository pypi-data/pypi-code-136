import re
from src.ok_zadanie_1.edge import (
	DirectedEdge,
	UndirectedEdge,
)
from src.ok_zadanie_1.edge import Edge
from src.ok_zadanie_1.graph import (
	DirectedGraph,
	UndirectedGraph,
)
from src.ok_zadanie_1.vertex import Vertex

# format is
# 1 -> 2
# 2 -> 3
# 3 -> 4
# 4 -> 5
directed_regex = re.compile(r"\s*(?P<starting_vertex>\d+)\s*->\s*(?P<ending_vertex>\d+)\s*")

def create_directed_graph_from_string(string: str) -> tuple[DirectedGraph, dict[Vertex, str]]:

	lines: list[str] = string.split("\n")
	edges_data: list[tuple[str, str]] = []
	for line in lines:
		match = directed_regex.match(line)
		if match:
			edges_data.append((match.group("starting_vertex"), match.group("ending_vertex")))
		else:
			raise ValueError(f"Invalid line: {line}")
	mapping_str_v: dict[str, Vertex] = dict()
	for edge in edges_data:
		for vertex_str in edge:
			if vertex_str not in mapping_str_v:
				mapping_str_v[vertex_str] = Vertex()
	mapping_v_str: dict[Vertex, str] = {v: k for k, v in mapping_str_v.items()}
	edges: set[DirectedEdge] = set()
	for edge in edges_data:
		edges.add(DirectedEdge(mapping_str_v[edge[0]], mapping_str_v[edge[1]]))
	vertices: set[Vertex] = set(mapping_str_v.values())
	return (DirectedGraph.from_vertices_and_edges(vertices, edges), mapping_v_str)

undirected_regex = re.compile(r"\s*(?P<vertex_1>\d+)\s*-\s*(?P<vertex_2>\d+)\s*")

def create_undirected_graph_from_string(string: str) -> tuple[UndirectedGraph, dict[Vertex, str]]:

	lines: list[str] = string.split("\n")
	edges_data: list[tuple[str, str]] = []
	for line in lines:
		match = undirected_regex.match(line)
		if match:
			edges_data.append((match.group("vertex_1"), match.group("vertex_2")))
		else:
			raise ValueError(f"Invalid line: {line}")
	mapping_str_v: dict[str, Vertex] = dict()
	for edge in edges_data:
		for vertex_str in edge:
			if vertex_str not in mapping_str_v:
				mapping_str_v[vertex_str] = Vertex()
	mapping_v_str: dict[Vertex, str] = {v: k for k, v in mapping_str_v.items()}
	edges: set[UndirectedEdge] = set()
	for edge in edges_data:
		edges.add(UndirectedEdge(mapping_str_v[edge[0]], mapping_str_v[edge[1]]))
	vertices: set[Vertex] = set(mapping_str_v.values())
	return (UndirectedGraph.from_vertices_and_edges(vertices, edges), mapping_v_str)
