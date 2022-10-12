#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT

""" Contains Readwrite Class, to export a cg graph to other
formats like nx."""

# general imports
from typing import Tuple
from logging import Logger
import numpy as np
import networkx as nx
# causalgraph and owlready imports
import owlready2
from causalgraph.utils.logging_utils import init_logger
from causalgraph.utils.mapping import all_individuals_to_dict


class ReadWrite():
    """ Contains all methods to convert cg graphs to NetworkX graphs and vice versa.
    Furthermore, this Class contains methods to translate tigramite matrices to cg graphs.
    """
    def __init__(self, store: owlready2.Ontology, logger: Logger = None) -> None:
        self.store = store
        if logger is not None:
            self.logger = logger
        else:
            self.logger = init_logger("ReadWrite")
        self.nx = NetworkX_ReadWrite(self.store)
        self.tigra = Tigramite_ReadWrite(self.store, self.logger)


class NetworkX_ReadWrite():
    """This Class handles all methods with reference to NetworkX.
    """
    def __init__(self, store: owlready2.World) -> None:
        self.store = store


    def write(self) -> nx.MultiDiGraph:
        """Converts a cg Graph into a NetworkX MultiDiGraph and returns it.
        This method adds the cg properties to the NetworkX individuals as NetworkX attributes.
        CAUTION: Will not add Creators because NetworkX cannot handle them. But Creators will
        still be a part of properties of Nodes and Edges. Lonely Creators will be lost, because
        there are no records of them within the properties of any CausalEdge or CausalNode.

        :return: The converted NetworkX MultiDiGraph.
        :rtype: nx.MultiDiGraph
        """
        g_nx = nx.MultiDiGraph()
        graph_dict = all_individuals_to_dict(self.store)

        for individual in graph_dict:
            individual_type = graph_dict[individual]["type"]
            individual_name = individual
            properties_dict = graph_dict[individual]
            if individual_type == "CausalNode":
                # Delete unwanted properties
                properties_dict.pop("type", None)
                # Add nx node
                g_nx.add_node(individual_name, **properties_dict)
            if individual_type == "CausalEdge":
                cause = graph_dict[individual]["cause"][0]
                effect = graph_dict[individual]["effect"][0]
                # Delete unwanted properties
                properties_dict.pop("type", None)
                properties_dict.pop("cause", None)
                properties_dict.pop("effect", None)
                # Add nx edge
                g_nx.add_edge(cause, effect, edge_name=individual_name, **properties_dict)
            if individual_type == "Creator":
                # NetworkX cannot handle Creators, thats why this will be skipped
                pass
        # return the g_nx Graph
        return g_nx


    def read(self, nx_graph: nx.MultiDiGraph) -> dict:
        """Creates a property dictionary from a parsed NetworkX MultiDiGraph that comes in
        the same form as one that was created via mapping.propertiesOfAllIndividualToDict().

        :param nx_graph: The NetworkX MultiDiGraph that will be used to create a properties dict.
        :type nx_graph: nx.MultiDiGraph
        :return: A properties dict that contains all individuals and their properties.
        :rtype: dict
        """
        graph_dict = {}
        creators = {}
        nx_nodes = list(nx_graph.nodes(data=True))
        nx_edges = list(nx_graph.edges(data=True))
        # Write all nx nodes into properties graph_dict
        for node in nx_nodes:
            graph_dict[node[0]] = {}
            graph_dict[node[0]]["type"] = "CausalNode"
            for prop in node[1]:
                graph_dict[node[0]][prop] = node[1][prop]
                if prop == "creator":
                    # Try to append the current node if "created" property already
                    # exists within the creators dict. Will fail if not.
                    try:
                        creators[node[1][prop][0]]["created"].append(node[0])
                    # Create first "created" property with this node. After that further
                    # nodes can be appended within the try statement.
                    except KeyError:
                        creators[node[1][prop][0]] = {"created": [node[0]]}
        # Write all nx edges into the properties graph_dict
        for edge in nx_edges:
            graph_dict[edge[2]["edge_name"]] = {}
            graph_dict[edge[2]["edge_name"]]["cause"] = [edge[0]]
            graph_dict[edge[2]["edge_name"]]["effect"] = [edge[1]]
            graph_dict[edge[2]["edge_name"]]["type"] = "CausalEdge"
            for prop in edge[2]:
                if prop != "edge_name":
                    graph_dict[edge[2]["edge_name"]][prop] = edge[2][prop]
                if prop == "creator":
                    # Try to append the current edge if the "created" property already
                    # exists within the creators dict. Will fail if not.
                    try:
                        creators[edge[2][prop][0]]["created"].append(edge[2]["edge_name"])
                    # Create first "created" property with this node. After that further
                    # edge can be appended within the try statement.
                    except KeyError:
                        creators[edge[2][prop][0]] = {"created": [edge[2]["edge_name"]]}
        # Add type to creators within creators dict
        for creator in creators:
            creators[creator]["type"] = "Creator"
        # Append creators dict to graph_dict
        if creators is not {}:
            graph_dict.update(creators)
        return graph_dict


    def export_gml(self, path):
        """Saves a cg graph to a given path as a .gml-file.

        :param path: Path to the directory under which the .gml-file will be saved.
        :type path: str
        """
        # Convert cg Graph to NX Graph
        g_nx = self.write()
        # Write gml file to path
        nx.write_gml(g_nx, f'{path}.gml')


    def export_graphml(self, path):
        """Saves a cg graph to a given path as a .graphml-file.

        :param path: Path to the directory under which the .graphml-file will be saved.
        :type path: str
        """
        # Convert cg Graph to NX Graph
        g_nx = self.write()
        # Write gml file to path
        nx.write_graphml(g_nx, f'{path}.graphml')


class Tigramite_ReadWrite():
    """This Class handles all methods with reference to Tigramite
    """
    def __init__(self, store, logger) -> None:
        self.store = store
        self.logger = logger


    def read(self, node_names: list, edge_names: dict, link_matrix: np.ndarray, q_matrix: np.ndarray, timestep_len_s: int) -> dict:
        """Returns a properties dictionary for the whole tigra graph.

        :param node_names: List of all nodes in the tigramite graph.
        :type node_names: list
        :param edge_names: Dict of all edges with their cause/ effect pairs.
        :type edge_names: dict
        :param link_matrix: The tigramite link matrix. Contains edges and their timelag.
        :type link_matrix: np.ndarray
        :param timestep_len_s: Tigramite timestep length.
        :type timestep_len_s: int
        :return: Properties dictionary of the graph
        :rtype: dict
        """
        graph_dict = {}
        # Compare number of nodes in link_matrix with the number of node_names
        if len(link_matrix) != len(node_names):
            self.logger.error("Too few nodes in the link matrix or the list of node names.")
            return False
        # Add nodes without their properties to graph_dict
        for nodes in node_names:
            graph_dict[nodes] = {"type": "CausalNode"}
        # Handle all edges, also add missing node properties
        for node_ind, matrix in enumerate(link_matrix):
            # Get indices of cause/effect pair and timelag
            possibly_edge = np.argwhere(matrix)
            # Only handle matrices with edges and timelags
            for edge in possibly_edge:
                cause = node_names[node_ind]
                effect = node_names[edge[0]]
                # Get time_lag and convert it with timestep_len_s to cg timeframe
                discrete_time_lag = edge[1]
                time_lag = discrete_time_lag * timestep_len_s
                # Get confidence
                confidence = q_matrix[node_ind, edge[0], edge[1]]
                # Get edge_name (dict key) with pair of cause and effect (values)
                try:
                    edge_name = list(edge_names.keys())[list(edge_names.values()).index({"cause": cause, "effect": effect})]
                except ValueError:
                    self.logger.error(f"There is no edge with cause {cause} and effect {effect}")
                    return False
                # Add edge with its cause, effect, confidence and timelag to graph_dict
                graph_dict[edge_name] = {}
                graph_dict[edge_name].update({"cause": [cause]})
                if confidence != 0.0:
                    graph_dict[edge_name].update({"confidence": float(confidence)})
                graph_dict[edge_name].update({"effect": [effect]})
                if time_lag != 0.0:
                    graph_dict[edge_name].update({"time_lag_s": float(time_lag)})
                graph_dict[edge_name].update({"type": "CausalEdge"})
                # Add node properties "affected_by" and "caused_by"
                graph_dict[cause].setdefault("caused_by", []).append(edge_name)
                graph_dict[effect].setdefault("affected_by", []).append(edge_name)
        # Return the filled graph_dict
        return graph_dict


    def write(self, graph_dict) -> Tuple[list, dict, np.ndarray, np.ndarray, int]:
        """Creates a Tigramite graph from a cg graph. Right now, this method only can handle
        edges, nodes, timelags and confidence.

        :param graph_dict: Properties dict of a cg graph.
        :type graph_dict: dict
        :return: Tuple with the links as a boolean matrix, the variable names as a list of
        strings, the edges as dict with its cause and effect and integer containing the
        tigra timestep length.
        :rtype: Tuple[np.ndarray, list, dict, int]
        """
        if len(graph_dict) <= 1:
            raise ValueError("You can't draw an empty graph or a graph with only one node using Tigramite!")

        list_of_edges = []
        list_cg_timelags = []
        list_tigra_timelags = []
        list_edge_confidence = []
        node_names = []
        edge_names = {}
        # Get list of cg timelags:
        for individual in graph_dict:
            individual_type = graph_dict[individual]["type"]
            if individual_type == "CausalEdge":
                # Get timelag or None
                time_lag_s = graph_dict[individual].get("time_lag_s", None)
                if time_lag_s is not None:
                    list_cg_timelags.append(time_lag_s)
        # Get timestep length (smallest timelag in list_cg_timelags)
        try:
            timestep_len_s = min(list_cg_timelags)
        except ValueError:
            timestep_len_s = 1

        for individual in graph_dict:
            individual_type = graph_dict[individual]["type"]
            individual_name = individual
            # Fill list of node names
            if individual_type == "CausalNode":
                node_names.append(individual_name)
            # Fill list of edges, incl. their tigramite timelag
            if individual_type == "CausalEdge":
                cause = graph_dict[individual].get("cause", [None])[0]
                effect = graph_dict[individual].get("effect", [None])[0]
                # If timelag exists for current edge, convert it to tigramite timeframe.
                # If it doesnt exist, set it to 0. After that add it to list_tigra_timelags
                time_lag_s = round(graph_dict[individual].get("time_lag_s", 0)/timestep_len_s)
                list_tigra_timelags.append(time_lag_s)
                # Get confidence for current edge. set it to 0 (edge present) if it does not exist
                confidence = graph_dict[individual].get('confidence', 0)
                list_edge_confidence.append(confidence)
                # Add edge with its timelag to list_of_edges
                list_of_edges.append((cause, effect, time_lag_s))
                edge_names[individual_name] = {}
                edge_names[individual_name] = {"cause": cause, "effect": effect}

        num_of_nodes = len(node_names)
        # graph consists of nodes only
        if len(edge_names) == 0:
            link_matrix = np.zeros((num_of_nodes, num_of_nodes, 5))
            q_matrix = np.ones((num_of_nodes, num_of_nodes, 5))
            return (node_names, [], link_matrix, q_matrix, timestep_len_s)
        # if there are edges, create list of edge indices with their timelags
        edge_indices = [(node_names.index(cause), node_names.index(effect), timelag)
                            for (cause, effect, timelag) in list_of_edges]
        # Init link_matrix with the proper dimension and fill it with zeros for now.
        link_matrix = np.zeros((num_of_nodes, num_of_nodes, max(list_tigra_timelags)+1))
        # Set 1 at the right indices to give information about the timelag value
        cause_ind, effect_ind, time_ind = zip(*edge_indices)
        link_matrix[cause_ind, effect_ind, time_ind] = 1
        # Init q_matrix with the proper dimension and fill it with ones (edges not present) for now
        q_matrix = np.ones((num_of_nodes, num_of_nodes, max(list_tigra_timelags)+1))
        q_matrix[cause_ind, effect_ind, time_ind] = list_edge_confidence
        return (node_names, edge_names, link_matrix, q_matrix, timestep_len_s)
