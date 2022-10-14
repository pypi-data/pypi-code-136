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

from __future__ import annotations

from collections import namedtuple as namedtuple_t
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import matplotlib.pyplot as pl_
import numpy as np_
import scipy.interpolate as in_
import skimage.measure as ms_

import skl_graph.brick.topology_map as bymp
import skl_graph.brick.elm_id as id_
import skl_graph.brick.hierarchy as hrcy
from skl_graph.brick.constants import UNTESTED_VALIDITY
from skl_graph.brick.node import branch_node_t, end_node_t, node_t


array_t = np_.ndarray
# ww_length=width-weighted length
# sq_lengths=squared lengths; Interest: all integers
edge_lengths_t = namedtuple_t("edge_lengths_t", "length ww_length lengths sq_lengths")


class raw_edge_t:
    #
    __slots__ = (
        "dim",
        "sites",
    )

    dim: int
    sites: Tuple[array_t, ...]

    def __init__(self):
        #
        for slot in self.__class__.__slots__:
            setattr(self, slot, None)

    @classmethod
    def NewWithSites(cls, sites: Tuple[array_t, ...]) -> raw_edge_t:
        #
        instance = cls()

        instance.dim = sites.__len__()
        instance.sites = _ReOrderedSites(sites)

        return instance

    @property
    def n_sites(self) -> int:
        #
        return self.sites[0].size

    def __str__(self) -> str:
        """"""
        return (
            f"{self.__class__.__name__}:\n"
            f"    Sites[{self.dim}-D]={self.sites[0].size}"
        )


class edge_t(raw_edge_t):
    #
    __slots__ = (
        "uid",
        "lengths",
        "widths",
        "invalidities",
        "_cache",
    )

    uid: str
    lengths: edge_lengths_t
    widths: array_t
    invalidities: List[str]  # Use brick.constants.UNTESTED_VALIDITY as initial value
    _cache: Dict[str, Any]

    def __init__(self):
        #
        super().__init__()
        self.invalidities = UNTESTED_VALIDITY
        self._cache = {}

    @classmethod
    def NewWithDetails(
        cls,
        sites: Tuple[array_t, ...],
        adjacent_node_uids: Sequence[str],
        width_map: array_t = None,
    ) -> edge_t:
        #
        raw_edge = raw_edge_t.NewWithSites(sites)
        ip_edge = _in_progress_edge_t.NewFromRaw(raw_edge)

        ip_edge.SetUID(adjacent_node_uids)
        ip_edge.AddWidths(width_map)
        ip_edge.SetLengths(ip_edge.widths)

        return ip_edge.AsEdge()

    @property
    def is_probably_valid(self) -> bool:
        """Partial validity test.

        Missing validity test: The end sites must be found in the adjacent nodes position/sites, which can only be
        tested at the graph level. See HasValidEndSites.

        Returns
        -------
        bool

        """
        output = True
        self.invalidities = []

        n_sites = self.sites[0].size
        length = self.lengths.length
        sq_lengths = self.lengths.sq_lengths
        if length < n_sites - 1:
            output = False
            self.invalidities.append(
                f"{length}: Computed length cannot be smaller "
                f"than number of sites - 1={n_sites - 1}"
            )
        if np_.any(sq_lengths == 0):
            output = False
            self.invalidities.append("Has repeated sites")
        if np_.any(sq_lengths > self.dim):
            output = False
            self.invalidities.append("Has site gaps")

        return output

    def HasValidEndSites(
        self,
        origin: Union[end_node_t, branch_node_t],
        destination: Union[end_node_t, branch_node_t],
    ) -> bool:
        """"""
        end_sites = self.end_sites
        n_found_end_sites = [0, 0]

        for node in (origin, destination):
            for e_idx in (0, 1):
                if isinstance(node, end_node_t):
                    end_site_found = np_.array_equal(end_sites[e_idx], node.position)
                else:
                    end_site = np_.reshape(end_sites[e_idx], (self.dim, 1))
                    end_site_found = any(
                        np_.all(end_site == np_.array(node.sites), axis=0)
                    )
                if end_site_found:
                    n_found_end_sites[e_idx] += 1

        if origin.uid == destination.uid:
            n_expected = 2
        else:
            n_expected = 1

        return n_found_end_sites == [n_expected, n_expected]

    @property
    def end_sites(self) -> Tuple[Tuple[Any, ...]]:
        """"""
        return tuple(
            tuple(self.sites[idx_][_s_idx] for idx_ in range(self.dim))
            for _s_idx in (0, -1)
        )

    def AsPolyline(self, max_distance: float = None) -> Tuple[float, array_t]:
        """
        Implementation of the Ramer–Douglas–Peucker algorithm
        https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm
        """
        cache_entry = self.AsPolyline.__name__

        if cache_entry not in self._cache:
            self._cache[cache_entry] = {}

        if max_distance is None:
            if self._cache[cache_entry].__len__() > 0:
                max_distance = min(self._cache[cache_entry].keys())
            else:
                max_distance = 1.0

        if max_distance not in self._cache[cache_entry]:
            output = np_.zeros(self.n_sites, dtype=np_.bool)
            output[0] = True
            output[-1] = True

            sites_as_array = np_.array(self.sites).T
            segments = [(0, self.n_sites - 1)]
            while segments.__len__() > 0:
                first_idx, last_idx = segments.pop()
                first_point = sites_as_array[first_idx, :]
                along_line = sites_as_array[last_idx, :] - first_point
                al_norm = np_.linalg.norm(along_line)  # al=along line

                highest_distance = 0.0
                idx_of_hd = first_idx  # hd=highest distance
                for idx in range(first_idx + 1, last_idx):
                    distance = _DistanceToLine(
                        sites_as_array[idx, :], first_point, along_line, al_norm
                    )
                    if distance > highest_distance:
                        idx_of_hd = idx
                        highest_distance = distance

                if highest_distance > max_distance:
                    output[idx_of_hd] = True
                    segments.extend(((first_idx, idx_of_hd), (idx_of_hd, last_idx)))

            self._cache[cache_entry][max_distance] = (
                max_distance,
                np_.nonzero(output)[0],
            )

        return self._cache[cache_entry][max_distance]

    def AsCurve(self) -> Optional[tuple]:
        """"""
        cache_entry = self.AsCurve.__name__

        if cache_entry not in self._cache:
            if self.n_sites > 1:
                arc_lengths = np_.cumsum([0] + self.lengths.sq_lengths.tolist())
                self._cache[cache_entry] = tuple(
                    in_.PchipInterpolator(arc_lengths, self.sites[idx_])
                    for idx_ in range(self.dim)
                )
            else:
                self._cache[cache_entry] = None

        return self._cache[cache_entry]

    def OriginDirection(self) -> Optional[array_t]:
        """"""
        return self._Direction(self.OriginDirection)

    def FinalDirection(self) -> Optional[array_t]:
        """"""
        return self._Direction(self.FinalDirection)

    def _Direction(self, where: Callable) -> array_t:
        """"""
        where = where.__name__
        if where not in self._cache:
            self._SetEndPointDirections()

        return self._cache[where]

    def _SetEndPointDirections(self) -> None:
        #
        cache_entry_o = self.OriginDirection.__name__
        cache_entry_f = self.FinalDirection.__name__

        as_curve = self.AsCurve()
        if as_curve is None:
            self._cache[cache_entry_o] = None
            self._cache[cache_entry_f] = None
        else:
            max_arclength = as_curve[0].x.item(-1)
            o_dir, f_dir = [], []
            for d_idx in range(self.dim):
                directions = as_curve[d_idx]((0, max_arclength), 1)
                o_dir.append(directions[0])
                f_dir.append(directions[1])
            self._cache[cache_entry_o] = np_.array(o_dir, dtype=np_.float64) / (
                -np_.linalg.norm(o_dir)
            )
            self._cache[cache_entry_f] = np_.array(
                f_dir, dtype=np_.float64
            ) / np_.linalg.norm(f_dir)

    def __str__(self) -> str:
        """"""
        if (self._cache is None) or (self._cache.__len__() == 0):
            cached_values = "None yet"
        else:
            cached_values = ", ".join(self._cache.keys())

        return _EdgeCommonDescription(self) + f"\n    Cached values: {cached_values}"


class _in_progress_edge_t(raw_edge_t):
    #
    __slots__ = (
        "uid",
        "lengths",
        "widths",
    )

    uid: str
    lengths: edge_lengths_t
    widths: array_t

    @classmethod
    def NewFromRaw(cls, raw_edge: raw_edge_t) -> _in_progress_edge_t:
        #
        instance = cls()

        for slot in hrcy.AllSlotsOfClass(raw_edge.__class__):
            setattr(instance, slot, getattr(raw_edge, slot))

        return instance

    def AsEdge(self) -> edge_t:
        #
        output = edge_t()

        for slot in hrcy.AllSlotsOfClass(self.__class__):
            setattr(output, slot, getattr(self, slot))

        return output

    def SetUID(self, adjacent_node_uids: Sequence[str]) -> None:
        """"""
        if adjacent_node_uids.__len__() != 2:
            raise RuntimeError(
                f"{adjacent_node_uids.__len__()}: Incorrect number of adjacent node uids"
            )

        node_uid_0, node_uid_1 = adjacent_node_uids
        if node_uid_0 > node_uid_1:
            node_uid_0, node_uid_1 = node_uid_1, node_uid_0

        uid_components = [
            id_.EncodedNumber(coord)
            for coord in node_uid_0.split(id_.COORDINATE_SEPARATOR)
        ]
        uid_components.append(id_.COORDINATE_SEPARATOR)
        uid_components.extend(
            id_.EncodedNumber(coord)
            for coord in node_uid_1.split(id_.COORDINATE_SEPARATOR)
        )

        self.uid = "".join(uid_components)

    def SetLengths(self, widths: array_t) -> None:
        """
        Passing widths instead of using self.widths ensures that this method will not be called before setting
        self.widths, should it be set.
        """
        sites_as_array = np_.array(self.sites)
        segments = np_.diff(sites_as_array, axis=1)
        sq_lengths = (segments ** 2).sum(axis=0)
        lengths = np_.sqrt(sq_lengths)
        length = lengths.sum().item()

        if widths is None:
            ww_length = -1.0
        else:
            ww_length = (0.5 * (widths[1:] + widths[:-1]) * lengths).sum().item()

        self.lengths = edge_lengths_t(
            length=length, ww_length=ww_length, lengths=lengths, sq_lengths=sq_lengths
        )

    def AddWidths(self, width_map: array_t) -> None:
        #
        if width_map is not None:
            self.widths = width_map[self.sites]

    def AppendBranchNode(
        self,
        b_coords: array_t,
        node: node_t,
        adjacent_node_uids: List[str],
        force_after: bool = False,
    ) -> None:
        #
        adjacent_node_uids.append(node.uid)

        space_dim = self.dim
        first_site = tuple(self.sites[idx_][0] for idx_ in range(space_dim))
        sq_distance = (np_.subtract(first_site, b_coords) ** 2).sum()

        if self.n_sites > 1:
            # 0 <: so that if the edge is a self-loop ending at the same site, it does not put twice the site in a row
            if 0 < sq_distance <= space_dim:
                self.sites = tuple(
                    np_.hstack((b_coords[idx_], self.sites[idx_]))
                    for idx_ in range(space_dim)
                )
            else:
                self.sites = tuple(
                    np_.hstack((self.sites[idx_], b_coords[idx_]))
                    for idx_ in range(space_dim)
                )
        elif force_after:
            self.sites = tuple(
                np_.hstack((self.sites[idx_], b_coords[idx_]))
                for idx_ in range(space_dim)
            )
        else:
            self.sites = tuple(
                np_.hstack((b_coords[idx_], self.sites[idx_]))
                for idx_ in range(space_dim)
            )

    def __str__(self) -> str:
        """"""
        return _EdgeCommonDescription(self)


def _EdgeCommonDescription(edge: Union[edge_t, _in_progress_edge_t]) -> str:
    """"""
    origin = tuple(edge.sites[idx][0] for idx in range(edge.dim))
    if edge.lengths is None:
        raw_length = "Not computed yet"
        ww_length = raw_length
    else:
        raw_length = round(edge.lengths.length, 2)
        ww_length = round(edge.lengths.ww_length, 2)

    return (
        f"{edge.__class__.__name__}[{edge.uid}]:\n"
        f"    Sites[{edge.dim}-D]={edge.sites[0].size}\n"
        f"    Origin: {origin}\n"
        f"    Lengths: Raw={raw_length}, WW={ww_length}"
    )


def RawEdges(
    skl_map: array_t, b_node_lmap: array_t
) -> Tuple[Sequence[raw_edge_t], array_t]:
    """"""
    edge_map = skl_map.astype(np_.int8)
    edge_map[b_node_lmap > 0] = 0
    edge_lmap, n_edges = bymp.LABELING_FCT_FOR_DIM[skl_map.ndim](edge_map)

    edge_props = ms_.regionprops(edge_lmap)

    edges = n_edges * [raw_edge_t()]
    for props in edge_props:
        sites = props.image.nonzero()
        for d_idx in range(skl_map.ndim):
            sites[d_idx].__iadd__(props.bbox[d_idx])
        edges[props.label - 1] = raw_edge_t.NewWithSites(sites)

    return edges, edge_lmap


def EdgesFromRawEdges(
    raw_edges: Sequence[raw_edge_t],
    e_nodes: Sequence[end_node_t],
    b_nodes: Sequence[branch_node_t],
    edge_lmap: array_t,
    e_node_lmap: array_t,
    b_node_lmap: array_t,
    width_map: array_t = None,
) -> Tuple[Tuple[edge_t], List[List[str]]]:
    #
    edge_tmap = bymp.TopologyMapOfMap(edge_lmap > 0)
    # ip_=in progress
    ip_edges = [_in_progress_edge_t.NewFromRaw(edge) for edge in raw_edges]

    # ep=edge end point; Keep < 2 since ==0 (length-1 edges) and ==1 (other edges) are needed
    # Do not use list multiplication since the same list then used for all the elements
    node_uids_per_edge = [[] for _ in ip_edges]
    for ep_coords in zip(*(edge_tmap < 2).nonzero()):
        edge_idx = edge_lmap[ep_coords] - 1
        edge = ip_edges[edge_idx]
        e_node_label = e_node_lmap[ep_coords]

        if e_node_label > 0:
            # End node-to-X edge (i.e., edge end point is also an end node)
            node_uids_per_edge[edge_idx].append(e_nodes[e_node_label - 1].uid)
            if edge.n_sites == 1:
                # End node-to-branch node edge (and there is a unique non-zero value in b_neighborhood)
                nh_slices_starts, b_neighborhood = _LMapNeighborhood(
                    b_node_lmap, ep_coords
                )
                b_node_label = np_.amax(b_neighborhood)
                b_coords = np_.transpose((b_neighborhood == b_node_label).nonzero())[0]
                edge.AppendBranchNode(
                    np_.add(nh_slices_starts, b_coords),
                    b_nodes[b_node_label - 1],
                    node_uids_per_edge[edge_idx],
                )
        else:
            nh_slices_starts, b_neighborhood = _LMapNeighborhood(b_node_lmap, ep_coords)
            force_after = False
            # Looping only for length-1, b-to-b edges
            for b_coords in zip(*b_neighborhood.nonzero()):
                b_node_label = b_neighborhood[b_coords]
                edge.AppendBranchNode(
                    np_.add(nh_slices_starts, b_coords),
                    b_nodes[b_node_label - 1],
                    node_uids_per_edge[edge_idx],
                    force_after=force_after,
                )
                force_after = not force_after

    for edge, adjacent_node_uids in zip(ip_edges, node_uids_per_edge):
        edge.SetUID(adjacent_node_uids)
        edge.AddWidths(width_map)
        edge.SetLengths(edge.widths)

    edges = tuple(edge.AsEdge() for edge in ip_edges)

    return edges, node_uids_per_edge


def Plot(
    edges: Iterable[Tuple[str, str, edge_t]],
    transformation: Callable[[array_t], array_t],
    vector_transf: Callable[[array_t], array_t],
    axes: pl_.axes.Axes,
    mode: str = "site",  # "site", "polyline", "curve"
    max_distance: float = 1.0,
    w_directions: bool = False,
) -> None:
    #
    # space_dim = edges[0][2].dim  # Does not work since 'MultiEdgeDataView' object is not subscriptable
    space_dim = 2
    for _, _, edge in edges:
        space_dim = edge.dim
        break

    plot_fct = axes.plot if space_dim == 2 else axes.plot3D
    plot_style = "k." if mode == "site" else "k"

    for origin, destination, edge in edges:
        if mode == "curve":
            as_curve = edge.AsCurve()
            if as_curve is None:
                sites = list(edge.sites)
            else:
                max_arc_length = as_curve[0].x.item(-1)
                step = 0.125
                arc_lengths = np_.arange(0.0, max_arc_length + 0.5 * step, step)
                sites = [as_curve[idx_](arc_lengths) for idx_ in range(space_dim)]
        elif mode == "polyline":
            polyline_idc = edge.AsPolyline(max_distance=max_distance)[1]
            sites = [edge.sites[idx_][polyline_idc] for idx_ in range(space_dim)]
        elif mode == "site":
            sites = list(edge.sites)
        else:
            raise ValueError(
                f"{mode}: Invalid plotting mode; Valid modes: 'site', 'polyline', 'curve'"
            )
        sites[0], sites[1] = sites[1], transformation(sites[0])

        line_style = ":" if origin == destination else "-"
        plot_fct(*sites, plot_style + line_style, linewidth=2, markersize=7)

        if w_directions:
            origin_direction = edge.OriginDirection()
            if origin_direction is not None:
                dir_sites = tuple(
                    np_.hstack((sites[idx_][0], sites[idx_][-1]))
                    for idx_ in range(space_dim)
                )
                directions = list(zip(origin_direction, edge.FinalDirection()))
                directions[0], directions[1] = (
                    directions[1],
                    vector_transf(directions[0]),
                )
                axes.quiver(*dir_sites, *directions, color="b", linewidth=2)


def _ReOrderedSites(sites: Tuple[array_t, ...]) -> Tuple[array_t, ...]:
    """
    If the number of sites is 1 or 2, the input argument is returned (i.e., no copy is made).

    Parameters
    ----------
    sites

    Returns
    -------

    """
    n_sites = sites[0].size
    if n_sites < 3:
        return sites

    dim = sites.__len__()

    self_loop = all(sites[idx][0] == sites[idx][-1] for idx in range(dim))
    if self_loop:
        sites = tuple(sites[idx][:-1] for idx in range(dim))
        n_sites -= 1
        self_origin = np_.fromiter(
            (sites[idx][0] for idx in range(dim)), dtype=sites[0].dtype
        )
        self_origin = np_.reshape(self_origin, (1, dim))
    else:
        self_origin = None

    sites_as_array = np_.transpose(np_.array(sites))
    reordered_coords = [np_.array([sites[idx][0] for idx in range(sites.__len__())])]
    unvisited_slc = np_.ones(n_sites, dtype=np_.bool)
    unvisited_slc[0] = False
    unvisited_sites = None
    end_point = None
    pre_done = False
    post_done = False

    while unvisited_slc.any():
        if post_done:
            neighbor_idc = ()
        else:
            end_point = reordered_coords[-1]
            neighbor_idc, unvisited_sites = _NeighborIndices(
                dim, sites_as_array, unvisited_slc, end_point
            )

        if (neighbor_idc.__len__() == 1) or post_done:
            also_grow_first = (reordered_coords.__len__() > 1) and not pre_done
            if not post_done:
                c_idx = neighbor_idc[0]
                reordered_coords.append(unvisited_sites[c_idx, :])
                unvisited_slc[np_.where(unvisited_slc)[0][c_idx]] = False
            if also_grow_first:
                end_point = reordered_coords[0]
                neighbor_idc, unvisited_sites = _NeighborIndices(
                    dim, sites_as_array, unvisited_slc, end_point
                )
                if neighbor_idc.__len__() == 1:
                    c_idx = neighbor_idc[0]
                    reordered_coords = [unvisited_sites[c_idx, :]] + reordered_coords
                    unvisited_slc[np_.where(unvisited_slc)[0][c_idx]] = False
                elif neighbor_idc.__len__() == 0:
                    pre_done = True  # End point has been reached
                else:
                    raise RuntimeError(
                        f"{neighbor_idc.__len__()} neighbors when only 1 is expected\n"
                        f"{sites}\n{reordered_coords}\n{unvisited_slc}\n{end_point}"
                    )
        elif neighbor_idc.__len__() == 2:
            if reordered_coords.__len__() == 1:
                idx1, idx2 = neighbor_idc
                reordered_coords = [unvisited_sites[idx1, :]] + reordered_coords
                reordered_coords.append(unvisited_sites[idx2, :])
                true_map = np_.where(unvisited_slc)[0]
                unvisited_slc[true_map[idx1]] = False
                unvisited_slc[true_map[idx2]] = False
            else:
                raise RuntimeError(
                    f"2 neighbors when only 1 is expected\n"
                    f"{sites}\n{reordered_coords}\n{unvisited_slc}\n{end_point}"
                )
        elif neighbor_idc.__len__() == 0:
            post_done = True  # End point has been reached
        else:
            raise RuntimeError(
                f"{neighbor_idc.__len__()} neighbors when only 1 or 2 are expected\n"
                f"{sites}\n{reordered_coords}\n{unvisited_slc}\n{end_point}"
            )

    reordered_coords = np_.array(reordered_coords)
    if self_loop:
        self_origin_idx = np_.argwhere(
            np_.all(reordered_coords == self_origin, axis=1)
        ).item()
        if self_origin_idx > 0:
            reordered_coords = np_.roll(reordered_coords, -self_origin_idx, axis=0)
        reordered_coords = np_.vstack((reordered_coords, self_origin))
    reordered_coords = tuple(reordered_coords[:, _idx] for _idx in range(dim))

    return reordered_coords


def _NeighborIndices(
    dim: int, sites: array_t, unvisited_slc: array_t, end_point: array_t
) -> Tuple[array_t, array_t]:
    """"""
    unvisited_sites = sites[unvisited_slc, :]

    distances = np_.fabs(unvisited_sites - np_.reshape(end_point, (1, dim)))
    neighbor_idc = np_.nonzero(np_.all(distances <= 1, axis=1))[0]

    return neighbor_idc, unvisited_sites


def _DistanceToLine(
    point: array_t, on_line: array_t, along_line: array_t, al_norm: float
) -> float:
    #
    if al_norm == 0.0:
        return np_.linalg.norm(point - on_line)

    return np_.linalg.norm(np_.cross(point - on_line, along_line)) / al_norm


def _LMapNeighborhood(lmap: array_t, site: Tuple[int, ...]) -> Tuple[array_t, array_t]:
    #
    slices_starts = tuple(max(site[idx_] - 1, 0) for idx_ in range(site.__len__()))
    slices = tuple(
        slice(slices_starts[idx_], min(site[idx_] + 2, lmap.shape[idx_]))
        for idx_ in range(site.__len__())
    )
    neighborhood = lmap[slices]

    return np_.array(slices_starts, dtype=np_.int64), neighborhood
