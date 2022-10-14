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

import matplotlib.pyplot as pl_
import numpy as nmpy

import skl_graph.skl_map as mp_
from skl_graph.skl_fgraph import skl_graph_t
from skl_graph.skl_graph import plot_mode_e


# fmt: off
skl_maps = (
    ((0, 1, 0),
     (0, 1, 0),
     (1, 0, 1)),

    ((0, 1, 0),
     (1, 0, 1),
     (0, 1, 0)),

    ((0, 1, 0),
     (1, 0, 1),
     (0, 1, 0),
     (1, 0, 1),
     (0, 1, 0)),

    ((0, 1, 0),
     (1, 0, 1),
     (0, 1, 0),
     (0, 1, 0),
     (1, 0, 1),
     (0, 1, 0)),

    ((0, 1, 0),
     (1, 0, 1),
     (0, 1, 0),
     (0, 1, 0),
     (0, 1, 0),
     (1, 0, 1),
     (0, 1, 0)),

    ((0, 1, 1, 1, 0),
     (1, 0, 0, 0, 1),
     (0, 1, 1, 1, 0),
     (0, 0, 1, 0, 0)),

    ((0, 1, 0),
     (1, 0, 1),
     (1, 0, 1),
     (1, 0, 1),
     (0, 1, 0),
     (0, 1, 0)),
)
map_names = ("Eiffel Tour", "Lozenge", "Touching Lozenges", "Touuuching Lozenges", "Linked Lozenges", "Lozenge w/ BNode", "Racket")
# fmt: on


skl_maps = (nmpy.array(skl_map, dtype=nmpy.bool_) for skl_map in skl_maps)
for map_name, skl_map in zip(map_names, skl_maps):
    mp_.CheckSkeletonMap(skl_map, mode="multi")
    skl_graph = skl_graph_t.FromSKLMap(skl_map)

    skl_graph.ShowInvalidities()
    print("")

    figure, axes = skl_graph.Plot(
        mode=plot_mode_e.SKL,
        should_block=False,
        should_return_figure=True,
        should_return_axes=True,
    )
    axes.set_title(map_name)
    axes = figure.add_subplot(1, 5, 5)
    axes.set_axis_off()
    axes.matshow(skl_map, cmap="cool")

    pl_.show()
