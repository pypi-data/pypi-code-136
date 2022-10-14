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

# skl_fgraph=Skeleton graph with computable features; Derived from base skeleton graph.

from typing import Callable, Iterable, List, Optional, Tuple  # , SupportsFloat

import numpy as np_

from skl_graph.skl_graph import skl_graph_t as skl_nfgraph_t  # nf=no feature


class skl_graph_t(skl_nfgraph_t):
    #
    @property
    def highest_degree(self) -> int:
        return max(degree for ___, degree in self.degree)

    @property
    def highest_degree_w_nodes(self) -> Tuple[int, List[str]]:
        #
        max_degree = -1
        at_nodes = None
        for node, degree in self.degree:
            if degree > max_degree:
                max_degree = degree
                at_nodes = [node]
            elif degree == max_degree:
                at_nodes.append(node)

        return max_degree, at_nodes

    @property
    def edge_lengths(self) -> Tuple[float, ...]:
        #
        return tuple(
            edge.lengths.length for ___, ___, edge in self.edges.data("as_edge_t")
        )

    @property
    def length(self) -> float:
        #
        return sum(self.edge_lengths)

    @property
    def area_as_rw_x_l(self) -> Optional[float]:
        """Area as reduced width times length.

        Returns
        -------

        """
        if self.has_widths:
            return self.ReducedWidth() * self.length
        else:
            return None

    @property
    def edge_ww_lengths(self) -> Tuple[float, ...]:
        #
        return tuple(
            edge.lengths.ww_length for ___, ___, edge in self.edges.data("as_edge_t")
        )

    @property
    def ww_length(self) -> float:
        #
        return sum(self.edge_ww_lengths)

    def EdgeReducedWidths(
        self, reduce_fct: Callable[[Iterable[float]], float] = np_.mean
    ) -> Tuple[float, ...]:
        #
        return tuple(
            reduce_fct(edge.widths) for ___, ___, edge in self.edges.data("as_edge_t")
        )

    def ReducedWidth(
        self, reduce_fct: Callable[[Iterable[float]], float] = np_.mean
    ) -> float:
        #
        all_widths = []
        for ___, ___, edge in self.edges.data("as_edge_t"):
            all_widths.extend(edge.widths)

        return reduce_fct(all_widths)

    def HeterogeneousReducedWidth(
        self,
        edge_reduce_fct: Callable[[Iterable[float]], float] = np_.mean,
        final_reduce_fct: Callable[[Iterable[float]], float] = np_.mean,
    ) -> float:
        #
        return final_reduce_fct(self.EdgeReducedWidths(edge_reduce_fct))

    def __str__(self) -> str:
        """"""
        output = super().__str__()
        output += (
            f"\n"
            f"    Highest degree={self.highest_degree}\n\n"
            f"    Length={round(self.length, 2)}"
        )
        if self.has_widths:
            output += (
                f"\n"
                f"    Width: Hom={round(self.ReducedWidth(), 2)}, "
                f"Het={round(self.HeterogeneousReducedWidth(), 2)}\n"
                f"    Area: RWxL={round(self.area_as_rw_x_l, 2)}, "
                f"WWL={round(self.ww_length, 2)}"
            )

        return output
