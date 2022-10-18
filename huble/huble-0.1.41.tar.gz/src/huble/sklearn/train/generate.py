from jinja2 import Environment, FileSystemLoader
from .templates import return_function 
import os



def convert_graph(graph):
    """
    Convert graph to adjacency matrix.
    """
    nodes = graph["nodes"]
    edges = graph["edges"]
    edge_map = {}
    node_map = {}
    for node in nodes:
        node_map[node["id"]] = node
    for edge in edges:
        edge_map[edge["source"]] = edge["target"]
    return node_map, edge_map


def generate_steps(nodes, edges):
    """
    Generate steps for processing data.
    """
    steps_list = []
    current_node = edges["999"]
    traversing = True
    node_steps = []
    while traversing:
        if current_node in nodes:
            node_steps.append(nodes[current_node]['data']['name'])
            steps_list.append(return_function(nodes[current_node]))
            current_node = edges[current_node]
        else:
            raise Exception("Invalid node")
        if edges[current_node] == "998":
            steps_list.append(return_function(nodes[current_node]))
            traversing = False
    print(node_steps)
    return steps_list


def generate_script(graph):
    """
    Generate script for training data.
    """
    print(os.getcwd())
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'template')
    file_loader = FileSystemLoader(filename)
    env = Environment(loader=file_loader)
    template = env.get_template("train.j2")
    node_map,edge_map = convert_graph(graph)
    steps_list = generate_steps(node_map, edge_map)
    parameters = {
        "steps_list": steps_list
    }
    output = template.render(parameters)
    return output
