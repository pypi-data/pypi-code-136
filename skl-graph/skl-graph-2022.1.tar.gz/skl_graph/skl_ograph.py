# Copyright CNRS/Inria/UNS
# Contributor(s): Eric Debreuve (since 2018)
#
# eric.debreuve@cnrs.fr
#
# This software is governed by the CeCILL  license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

# skl_ograph=Skeleton graph with specific operations, derived from skeleton graph with features

raise NotImplementedError("THIS MODULE IS A WORK-IN-PROGRESS: NOT USABLE YET")

# Derive an oedge_t (or other name) adding a field composition:
# composition: Holds the lengths of pieces composing the edge (can change while simplifying)

from skl_graph.skl_fgraph import skl_graph_t as skl_fgraph_t  # f=feature
# from skl_graph import EdgeID, NodeID


import networkx as nx_
import numpy as np_


array_t = np_.ndarray


class skl_graph_t(skl_fgraph_t):
    def PruneBasedOnWidths(self, min_width: float) -> None:
        #
        assert self.has_widths

        delete_list = []
        relabeling_dct = {}

        for node_0, node_1, edge_desc in self.edges.data("as_edge_t"):
            extremity = None
            if self.degree[node_0] == 1:
                extremity = node_0
            elif self.degree[node_1] == 1:
                extremity = node_1
            if extremity is None:
                continue

            assert (
                len(edge_desc["composition"]) == 1
            )  # /!\ Not made to work on already simplified graphs

            edge_coords_0 = edge_desc["sites"][0]
            edge_coords_1 = edge_desc["sites"][1]
            widths = edge_desc["widths"]
            n_edge_pixels = len(edge_coords_0)

            if (edge_coords_0[0], edge_coords_1[0]) == self.node[extremity].position:
                pixel_idx = 0
                idx_incr = 1
            else:
                pixel_idx = n_edge_pixels - 1
                idx_incr = -1

            while (0 <= pixel_idx < n_edge_pixels) and (widths[pixel_idx] < min_width):
                pixel_idx += idx_incr

            if (pixel_idx < 0) or (pixel_idx >= n_edge_pixels):
                delete_list.append(extremity)
            else:
                self.node[extremity].position = (
                    edge_coords_0[pixel_idx],
                    edge_coords_1[pixel_idx],
                )
                self.node[extremity].diameter = widths[pixel_idx]
                relabeling_dct[extremity] = NodeID(self.node[extremity].position)

                if idx_incr > 0:
                    valid_idc = slice(pixel_idx, n_edge_pixels)
                    extra_idc = slice(pixel_idx + 1)
                else:
                    valid_idc = slice(pixel_idx + 1)
                    extra_idc = slice(pixel_idx, n_edge_pixels)

                edge_piece = np_.array(
                    (edge_coords_0[extra_idc], edge_coords_1[extra_idc]), dtype=np_.float64
                )
                extra_widths = np_.array(widths[extra_idc], dtype=np_.float64)
                extra_lengths = np_.sqrt(
                    (np_.diff(edge_piece, axis=1) ** 2).sum(axis=0)
                )
                extra_w_lengths = extra_lengths * (
                    0.5 * (extra_widths[1:] + extra_widths[:-1])
                )

                edge_desc["sites"] = (
                    edge_coords_0[valid_idc],
                    edge_coords_1[valid_idc],
                )
                edge_desc["widths"] = widths[valid_idc]
                edge_desc[
                    "length"
                ] -= extra_lengths.sum().item()  # Conversion to float is necessary,
                edge_desc[
                    "w_length"
                ] -= (
                    extra_w_lengths.sum().item()
                )  # otherwise type np_.float64 contaminates all.
                if edge_desc["origin_node"] == extremity:
                    edge_desc["origin_node"] = relabeling_dct[extremity]

        if len(delete_list):
            self.remove_nodes_from(delete_list)
        if len(relabeling_dct):
            nx_.relabel_nodes(self, relabeling_dct, copy=False)

    def Simplify(self, min_edge_length: float) -> None:
        #
        while True:
            min_length = np_.Inf
            end_nodes = ()
            for node_label_0, node_label_1, edge in self.edges.data("as_edge_t"):
                degree_0 = self.degree[node_label_0]
                degree_1 = self.degree[node_label_1]

                if (degree_0 > 2) and (degree_1 > 2) and (edge.length < min_length):
                    edge_desc_list = self[node_label_0][node_label_1]
                    if len(edge_desc_list) > 1:
                        lengths_lower = [
                            description["length"] <= edge.length
                            for description in edge_desc_list.values()
                        ]
                        should_continue = all(lengths_lower)
                    else:
                        should_continue = True
                    if should_continue:
                        min_length = edge.length
                        end_nodes = (node_label_0, node_label_1)

            if min_length < min_edge_length:
                # /!\ management of edge descriptions is inexistant
                edges = []
                all_coords = [[], []]
                n_coords_per_piece = []
                for edge, description in self[end_nodes[0]][end_nodes[1]].items():
                    edges.append(edge)
                    sites = description["sites"]
                    all_coords[0].extend(sites[0])
                    all_coords[1].extend(sites[1])
                    n_coords_per_piece.append(len(sites[0]))

                all_coords = np_.array(all_coords, dtype=np_.float64)
                cum_n_coords_per_piece = np_.cumsum(n_coords_per_piece) - 1
                # Naming: actually "cumulative minus one" rather than "cumulative"

                centroid = all_coords.mean(axis=1, keepdims=True).round()
                closest_pixel_idx = (
                    ((all_coords - centroid) ** 2).sum(axis=0).argmin()
                )  # idx of first occurrence of min
                centroid = (
                    int(all_coords[0, closest_pixel_idx]),
                    int(all_coords[1, closest_pixel_idx]),
                )

                closest_edge_idx = cum_n_coords_per_piece.searchsorted(
                    closest_pixel_idx
                )
                shared_description = self[end_nodes[0]][end_nodes[1]][
                    edges[closest_edge_idx]
                ]
                # for edge in self[end_nodes[0]][end_nodes[1]].keys():
                #     if edge != edge_to_keep:
                #         self.remove_edge(end_nodes[0], end_nodes[1], key = edge)

                description = self.nodes[end_nodes[0]]
                description["position"] = centroid
                description["sites"] = ((centroid[0],), (centroid[1],))

                for neighbor in self[end_nodes[0]]:
                    if neighbor != end_nodes[1]:
                        for description in self[end_nodes[0]][neighbor].values():
                            pass
                            # use shared_description here
                            # description = {
                            #     "sites":           new_coords,
                            #     'origin_node': edge_0_node,
                            #     'length':           edge_0_desc['length']   + edge_1_desc['length']   + joint_length,
                            #     'w_length':         edge_0_desc['w_length'] + edge_1_desc['w_length'] + joint_w_length,
                            #     'widths':            widths,
                            #     'composition':      edge_0_desc['composition'] + (len(node_desc["sites"][0]),) + \
                            #                         edge_1_desc['composition']
                            # }

                for neighbor in self[end_nodes[1]]:
                    if (neighbor != end_nodes[0]) and (
                        neighbor not in self[end_nodes[0]]
                    ):
                        for edge, description in self[end_nodes[1]][neighbor].items():
                            # use shared_description here
                            # description = {
                            #     "sites":           new_coords,
                            #     'origin_node': edge_0_node,
                            #     'length':           edge_0_desc['length']   + edge_1_desc['length']   + joint_length,
                            #     'w_length':         edge_0_desc['w_length'] + edge_1_desc['w_length'] + joint_w_length,
                            #     'widths':            widths,
                            #     'composition':      edge_0_desc['composition'] + (len(node_desc["sites"][0]),) + \
                            #                         edge_1_desc['composition']
                            # }
                            self.add_edge(
                                end_nodes[0], neighbor, key=edge, **description
                            )

                self.remove_node(end_nodes[1])
            else:
                break

        while True:
            min_length = np_.Inf
            node_label = -1
            for node_label_0, node_label_1, edge in self.edges.data("as_edge_t"):
                degree_0 = self.degree[node_label_0]
                degree_1 = self.degree[node_label_1]

                if (
                    ((degree_0 == 1) or (degree_1 == 1))
                    and (degree_0 + degree_1 > 3)
                    and (edge.length < min_length)
                ):
                    min_length = edge.length
                    if degree_0 == 1:
                        node_label = node_label_0
                    else:
                        node_label = node_label_1

            if min_length < min_edge_length:
                self.remove_node(node_label)
            else:
                break

        graph_has_been_modified = True
        while graph_has_been_modified:
            graph_has_been_modified = False

            for node_label, node_desc in self.nodes.data("as_node_t"):
                if self.degree[node_label] != 2:
                    continue

                edge_0, edge_1 = self.edges(node_label, data=True)
                other_node_0, edge_0_node, edge_0_desc = edge_0
                other_node_1, edge_1_node, edge_1_desc = edge_1
                assert (other_node_0 == node_label) and (other_node_1 == node_label)
                # If this assertion fails one day, it means that NetworkX has changed the way it returns
                # adjacent edges. It will become necessary to test which of other_node_X and edge_X_node
                # is node_label.

                new_coords, joint_length, first_reversed, last_reversed = __EdgeOfGluedEdges__(
                    edge_0_desc["sites"],
                    edge_1_desc["sites"],
                    node_desc["sites"],
                    edge_0_desc["origin_node"] == node_label,
                    edge_1_desc["origin_node"] == node_label,
                )

                if self.has_widths:
                    joint_w_length = joint_length * np_.mean(node_desc["diameters"])
                    if first_reversed:
                        first_part = tuple(reversed(edge_0_desc["widths"]))
                    else:
                        first_part = edge_0_desc["widths"]
                    if last_reversed:
                        last_part = tuple(reversed(edge_1_desc["widths"]))
                    else:
                        last_part = edge_1_desc["widths"]
                    widths = first_part + node_desc["diameters"] + last_part
                else:
                    joint_w_length = 0
                    widths = None

                description = {
                    "sites": new_coords,
                    "origin_node": edge_0_node,
                    "length": edge_0_desc["length"]
                    + edge_1_desc["length"]
                    + joint_length,
                    "w_length": edge_0_desc["w_length"]
                    + edge_1_desc["w_length"]
                    + joint_w_length,
                    "widths": widths,
                    "composition": edge_0_desc["composition"]
                    + (len(node_desc["sites"][0]),)
                    + edge_1_desc["composition"],
                }

                self.add_edge(
                    edge_0_node,
                    edge_1_node,
                    EdgeID(edge_0_node, edge_1_node),
                    **description
                )
                self.remove_node(node_label)
                graph_has_been_modified = True
                break


def __EdgeOfGluedEdges__(
    edge_0_coords, edge_1_coords, node_coords, node_is_first_of_0, node_is_first_of_1
):
    #
    # Returns the glued sites and the length of the gluing joint
    #
    if node_is_first_of_0:
        first_part_0 = tuple(reversed(edge_0_coords[0]))
        first_part_1 = tuple(reversed(edge_0_coords[1]))
        first_reversed = True
    else:
        first_part_0 = edge_0_coords[0]
        first_part_1 = edge_0_coords[1]
        first_reversed = False

    if node_is_first_of_1:
        last_part_0 = tuple(reversed(edge_1_coords[0]))
        last_part_1 = tuple(reversed(edge_1_coords[1]))
        last_reversed = True
    else:
        last_part_0 = edge_1_coords[0]
        last_part_1 = edge_1_coords[1]
        last_reversed = False

    glued_coords = (
        first_part_0 + node_coords[0] + last_part_0,
        first_part_1 + node_coords[1] + last_part_1,
    )
    joint_length = float(
        np_.sqrt(
            (first_part_0[-1] - last_part_0[0]) ** 2
            + (first_part_1[-1] - last_part_1[0]) ** 2
        )
    )

    return glued_coords, joint_length, first_reversed, last_reversed
