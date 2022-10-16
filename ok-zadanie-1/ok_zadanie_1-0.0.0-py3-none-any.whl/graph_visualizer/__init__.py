import matplotlib.pyplot as plt # type: ignore
import networkx as nx  # type: ignore
from src.ok_zadanie_1.graph import DirectedGraph
from src.ok_zadanie_1.edge import DirectedEdge
from src.ok_zadanie_1.vertex import Vertex

def visualize_directed_graph(
	graph: DirectedGraph,
) -> None:
	nx_graph = nx.Graph()
	name_by_vertex: dict[Vertex, str] = {
		vertex: str(vertex) for vertex in graph.get_vertices()
	}
	for edge in graph.get_edges():
		nx_graph.add_edge(
			name_by_vertex[edge.get_starting_vertex()],
			name_by_vertex[edge.get_ending_vertex()],
		)
	nx.draw(nx_graph, with_labels=True)
	plt.show()