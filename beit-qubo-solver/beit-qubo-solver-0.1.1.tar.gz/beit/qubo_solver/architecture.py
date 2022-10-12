import dwave_networkx as dnx


def make_chimera_architecture():
    architecture = dnx.chimera_graph(8, 16, 4)
    architecture.add_edges_from((v, v) for v in architecture.nodes)
    return architecture.to_directed() # Create edges both ways
