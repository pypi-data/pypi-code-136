import json
from urllib.request import urlopen
import networkx as nx


def get_hpo_graph_in_networkx(hpo_url):
    """Obtain the HPO graph in networkx format
    :param hpo_url: URL to the HPO JSON file
    """
    with urlopen(hpo_url, timeout=30) as uh:
        data = uh.read()
        hpo_json = json.loads(data.decode("utf-8"))

    edge_list_in_json = hpo_json['graphs'][0]['edges']

    edge_list = []
    for edge in edge_list_in_json:
        # fix formatting to correspond to our wanted format
        # this does include obsolete terms, but does not add synonyms
        node_1 = edge['obj'].replace('http://purl.obolibrary.org/obo/', '').replace('_', ':')
        node_2 = edge['sub'].replace('http://purl.obolibrary.org/obo/', '').replace('_', ':')
        edge_list.append((node_1, node_2))

    obsolete_terms = [] #use a list to delete them all at once later and not call graph.remove_node each time
    for node in hpo_json['graphs'][0]['nodes']:
        if 'meta' in node:
            if 'deprecated' in node['meta']:
                if node['meta']['deprecated']:
                    obsolete_terms.append(node['id'].replace('http://purl.obolibrary.org/obo/', '').replace('_', ':'))

    G = nx.from_edgelist(edge_list, create_using=nx.DiGraph)
    G.remove_nodes_from(obsolete_terms)
    return G
