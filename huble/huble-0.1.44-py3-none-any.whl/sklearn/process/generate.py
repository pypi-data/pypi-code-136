from jinja2 import Environment, FileSystemLoader
# import templating
from .templating import return_function
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
    Generate script for processing data.
    """
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'template')
    file_loader = FileSystemLoader(filename)
    env = Environment(loader=file_loader)
    template = env.get_template("preprocess.j2")
    node_map,edge_map = convert_graph(graph)
    steps_list = generate_steps(node_map, edge_map)
    parameters = {
        "steps_list": steps_list
    }
    output = template.render(parameters)
    
    return output


# test = """{"nodes":[{"id":"999","type":"custom","position":{"x":633.4002817498528,"y":186.5000289469027},"data":{"name":"Raw Data","value":"Raw Data","color":"green.400","isInput":true,"parameters":{"Dataset":"Test"},"node_type":"preprocess"},"width":400,"height":76,"selected":false,"positionAbsolute":{"x":633.4002817498528,"y":186.5000289469027},"dragging":false},{"id":"998","type":"custom","position":{"x":634.8003512224192,"y":719.1997645651916},"data":{"name":"Clean Data","value":"Clean Data","color":"pink.400","isOutput":true,"parameters":{"Dataset":"Test"},"node_type":"preprocess"},"width":400,"height":76,"selected":false,"positionAbsolute":{"x":634.8003512224192,"y":719.1997645651916},"dragging":false},{"id":"1","type":"custom","position":{"x":546,"y":341},"data":{"name":"Remove NAN values","value":"Remove NAN values","parameters":{"axis":0,"how":"all","subset":[],"inplace":false},"node_type":"preprocess","color":"yellow.400"},"width":400,"height":76,"selected":false,"positionAbsolute":{"x":546,"y":341},"dragging":false},{"id":"3","type":"custom","position":{"x":554,"y":535},"data":{"name":"Dropping rows or columns","value":"Dropping rows or columns","parameters":{"labels":[{"value":"Sex","label":"Sex"},{"value":"Pclass","label":"Pclass"},{"value":"Parch","label":"Parch"}],"axis":0,"index":[],"columns":[],"inplace":false,"errors":"raise"},"node_type":"preprocess","columnList":{"labels":[[{"value":"Survived","label":"Survived"},{"value":"Sex","label":"Sex"}]],"axis":0,"index":[],"columns":[],"inplace":false,"errors":"raise"},"color":"teal.400"},"width":400,"height":76,"selected":true,"positionAbsolute":{"x":554,"y":535},"dragging":false}],"edges":[{"source":"999","sourceHandle":null,"target":"1","targetHandle":null,"type":"custom","data":{"sourceColor":"green.400","targetColor":"yellow.400"},"id":"reactflow__edge-999-1"},{"source":"1","sourceHandle":null,"target":"2","targetHandle":null,"type":"custom","data":{"sourceColor":"yellow.400","targetColor":"#805AD5"},"id":"reactflow__edge-1-2"},{"source":"2","sourceHandle":null,"target":"998","targetHandle":null,"type":"custom","data":{"sourceColor":"#805AD5","targetColor":"pink.400"},"id":"reactflow__edge-2-998"},{"source":"3","sourceHandle":null,"target":"998","targetHandle":null,"type":"custom","data":{"sourceColor":"teal.400","targetColor":"pink.400"},"id":"reactflow__edge-3-998"},{"source":"1","sourceHandle":null,"target":"3","targetHandle":null,"type":"custom","data":{"sourceColor":"yellow.400","targetColor":"teal.400"},"id":"reactflow__edge-1-3"}]}"""
# import json
# graph = json.loads(test)

# res=generate_script(graph)
# print(res)

