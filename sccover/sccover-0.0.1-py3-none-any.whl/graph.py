#!/usr/bin/env python3

import numba
import numpy as np

from anndata import AnnData
from scipy.sparse import csr_matrix
from typing import Tuple


def random_sampling(adata, target_reduction: float = 0.1, key: str = "random_set"):
    """
    Basic random subsampling.
    """
    adata.obs[key] = (np.random.random(adata.n_obs) < target_reduction).astype(int)


def vertex_cover_base(graph: csr_matrix, n_hops: int = 1) -> np.ndarray:
    """
    Runs vertex cover algorithm on a csr-shaped adjacency graph. Returns for each
    point the index of its reference anchor.
    """
    if isinstance(graph, np.ndarray):
        graph = csr_matrix(graph)
    assert isinstance(graph, csr_matrix), f"Unknown graph type: {type(graph).__name__}."
    return _vertex_cover_njit(graph.indptr, graph.indices, n_hops)


def vertex_cover(
    adata: AnnData,
    n_hops: int = 1,
    key: str = "sccover",
    graph_key: str = "distances",
) -> None:
    """
    Adds vertex cover information to AnnData cells, writing them in the .obs
    field. Anchor information contains for each cell the index of the closest
    anchor.
    """
    assert (
        "distances" in adata.obsp
    ), f"No neighbors graph found in AnnData object under .obsp['{graph_key}'].\
    Please ensure scanpy.pp.neighbors has been called."
    N_csr = adata.obsp[graph_key]
    adata.obs[f"{key}_ref"] = _vertex_cover_njit(N_csr.indptr, N_csr.indices, n_hops)
    adata.obs[f"{key}_set"] = [
        int(ref == i) for i, ref in enumerate(adata.obs[f"{key}_ref"])
    ]


@numba.njit
def _vertex_cover_njit(
    ptr: np.ndarray,
    ind: np.ndarray,
    hops: int = 1,
) -> np.ndarray:
    # ptr, ind: CSR matrix representation
    # of an adjacency matrix
    n = ptr.shape[0] - 1
    anchors = np.zeros(n, dtype="int") - 1
    for v in range(n):
        if anchors[v] > -1:
            continue
        # If v not visited, it's a new anchor
        # Mark its hops-neighbors as v-anchored
        neighbors = [(v, 0)]
        while len(neighbors):
            nb, d = neighbors.pop(0)
            anchors[nb] = v
            if d < hops:
                M = ptr[nb + 1] if nb + 1 < n else n
                for nb2 in ind[ptr[nb] : M]:
                    if anchors[nb2] > -1:
                        continue
                    anchors[nb2] = v
                    neighbors.append((nb2, d + 1))
    return anchors


def get_closest_anchor(
    adata: AnnData,
    key_set: str = "sccover_set",
    graph_key: str = "distances",
    key: str = "sccover",
    use_dist: bool = False,
) -> None:
    """
    Writes for each cell its nearest element within a set of cells.
    """
    assert (
        "distances" in adata.obsp
    ), f"No neighbors graph found in AnnData object under .obsp['{graph_key}'].\
    Please ensure scanpy.pp.neighbors has been called."
    assert key_set in adata.obs, "Please make sure to run vertex_cover first."
    N_csr = adata.obsp[graph_key]
    ref_anchor, dist_to_anchor = _get_closest_anchor_njit(
        N_csr.indptr,
        N_csr.indices,
        N_csr.data,
        np.array(adata.obs[key_set]),
        use_dist=use_dist,
    )
    adata.obs[f"{key}_ref"] = ref_anchor
    adata.obs[f"{key}_dist"] = dist_to_anchor


def _insert_sorted(l, t) -> None:
    """
    Inserts t = (x, w) in list l so that l stays sorted by w.
    """
    if len(l) == 0:
        l.insert(0, t)
        return
    m, M = 0, len(l) - 1
    _, w = t
    _, wm = l[m]
    _, wM = l[M]
    while True:
        if w <= wm:
            l.insert(m, t)
            break
        if w >= wM:
            l.insert(M + 1, t)
            break
        mid = int(0.5 * (M + m))  # rounded down
        _, wmid = l[mid]
        if wmid <= wm:
            M, wM = mid, wmid
        else:
            m, wm = mid, wmid


# TODO: njit later
def _get_closest_anchor_njit(
    ptr: np.ndarray,
    ind: np.ndarray,
    data: np.ndarray,
    set_indices: np.ndarray,
    use_dist: bool = False,
) -> Tuple[np.ndarray, np.ndarray]:
    # ptr, ind: CSR matrix representation
    # of an adjacency matrix
    if not use_dist:
        data[:] = 1
    n = set_indices.shape[0]
    anchors = np.zeros(n, dtype="int") - 1
    dist_to_anchor = np.zeros(n, dtype="float")
    for v in range(n):
        # If v not visited, add it as an anchor
        if set_indices[v]:
            anchors[v] = v
            continue
        # Mark its neighbors as visited
        visited = np.zeros((n,), dtype="bool")
        distances = np.zeros((n,), dtype="float")
        visited[v] = True
        to_visit = [(v, 0)]
        while len(to_visit):
            current, d = to_visit.pop(0)
            M = ptr[current + 1] if current + 1 < n else n
            neighbors, neighbors_d = ind[ptr[current] : M], data[ptr[current] : M]
            neighbors, neighbors_d = (
                neighbors[np.argsort(neighbors_d)],
                np.sort(neighbors_d),
            )
            for nb, d2 in zip(neighbors, neighbors_d):
                if set_indices[nb]:
                    anchors[v] = nb
                    dist_to_anchor[v] = d + d2
                    to_visit = []
                    break
                if visited[nb] and d + d2 >= distances[nb]:
                    continue
                _insert_sorted(to_visit, (nb, d + d2))
                distances[nb] = d + d2
                visited[nb] = True
    return anchors, dist_to_anchor
