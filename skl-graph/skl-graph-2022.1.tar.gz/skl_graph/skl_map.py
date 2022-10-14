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

"""
Skeleton Map Creation and Manipulation.

Definitions
-----------
A map is a Numpy ndarray representing one or several object over a background. It exists in several variants:
- Boolean  map: ndarray of type bool            where the object(s) are labeled True and the background is False.
- Binary   map: ndarray of type int8  or uint8  where the object(s) are labeled 1 and the background is 0.
- Labeled  map: ndarray of type int64 or uint64 where the objects   are labeled from 1 with successive integers,
and the background is 0.
- Topology map: ndarray of type int8  or uint8  where each object site (pixel, voxel...) has a value between 0 and
3^D - 1, where D is the number of dimensions of the array, and the background is 3^D. The values correspond to the
number of neighboring sites belonging to the object with the weakest connectivity (8 in 2-D, 26 in 3-D...).

These variants are abbreviated omp, ymp, lmp, and tmp, respectively, to be used as a variable name postfix, e.g.,
edge_ymp.

For maps that can be of signed or unsigned types, the signed version is usually preferred to make them subtractable.

A skeleton map, normally abbreviated as skl_map, is a 2- or 3-dimensional boolean or binary map in which no site (pixel
or voxel) with value True, respectively 1, can be set to False, respectively 0, without breaking the skeleton
connectivity (in the weakest sense) or shortening a branch.

Simple example usage:
>>> import matplotlib.pyplot as pyplot
>>> import numpy
>>> import skimage.data as data
>>> import skimage.util as util
>>> object_map = util.invert(data.horse())
>>> # --- SKL Map
>>> from skl_map import SKLMapFromObjectMap, PruneSKLMapBasedOnWidth
>>> skl_map, width_map = SKLMapFromObjectMap(object_map, with_width=True)
>>> pruned_map = skl_map.copy()
>>> PruneSKLMapBasedOnWidth(pruned_map, width_map, 20)
>>> # --- End of SKLGraph-based section
>>> _, axes = pyplot.subplots(nrows=1, ncols=4)
>>> axes[0].matshow(object_map, cmap="gray")
>>> axes[1].matshow(skl_map, cmap="gray")
>>> axes[2].matshow(width_map, cmap="hot")
>>> axes[3].matshow(pruned_map, cmap="gray")
>>> for ax, title in zip(axes, ("Object", "Skeleton", "Width", "Pruned Skeleton")):
>>>     ax.set_title(title)
>>>     ax.set_axis_off()
>>> pyplot.tight_layout()
>>> pyplot.show()
"""

from typing import List, Optional, Tuple, Union

import numpy as nmpy
import scipy.ndimage as spim
import skimage.morphology as skmp

import skl_graph.brick.topology_map as tymp


array_t = nmpy.array


def SKLMapFromObjectMap(
    object_map: array_t, with_width: bool = False
) -> Union[array_t, Tuple[array_t, array_t]]:
    """Returns the skeleton map of an object map, optionally with the width map (see `SkeletonWidthMapFromObjectMap`).

    Works for multiple objects if skmp.thin and skmp.skeletonize_3d do.

    Parameters
    ----------
    object_map : numpy.ndarray
    with_width : bool

    Returns
    -------
    Union[array_t, Tuple[array_t, array_t]]

    """
    # TODO: check doc of skmp.thin and skmp.skeletonize_3d
    # TODO: check returned dtype of thin/skeletonize, make returned dtype coherent if needed
    #
    if object_map.ndim == 2:
        # Doc says it removes every pixel up to breaking connectivity
        output = skmp.thin(object_map)
        output[
            output > 1
        ] = 1  # In case the skeleton is marked with 255, which converts to -1 in int8
        output = output.astype(nmpy.int8, copy=False)
    elif object_map.ndim == 3:
        output = skmp.skeletonize_3d(object_map)
        output[
            output > 1
        ] = 1  # In case the skeleton is marked with 255, which converts to -1 in int8
        output = output.astype(nmpy.int8, copy=False)
        # Doc does not tell anything about every pixel being necessary or not
        TurnThickSKLMapIntoSKLMap(output)
    else:
        raise ValueError(f"{object_map.ndim}: Invalid map dimension; Expected: 2 or 3")

    if with_width:
        return output, SkeletonWidthMapFromObjectMap(object_map)
    return output


def SkeletonWidthMapFromObjectMap(object_map: array_t) -> array_t:
    """Width map of an object map.

    The width map is a distance map where the values on the object(s) skeleton are equal to twice the distance to the
    object border, which can be interpreted as the local object width.

    Parameters
    ----------
    object_map : numpy.ndarray

    Returns
    -------
    numpy.ndarray

    """
    return 2.0 * spim.distance_transform_edt(object_map) + 1.0


_CENTER_3x3 = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
_CROSS_3x3 = nmpy.array(((0, 1, 0), (1, 1, 1), (0, 1, 0)), dtype=nmpy.uint8)
_CROSS_3x3x3 = nmpy.array((_CENTER_3x3, _CROSS_3x3, _CENTER_3x3), dtype=nmpy.uint8)
_CROSS_FOR_DIM = (None, None, _CROSS_3x3, _CROSS_3x3x3)


def TurnThickSKLMapIntoSKLMap(skl_map: array_t) -> None:
    """Removes all sites (pixels or voxels) that do not break the skeleton connectivity (in the weakest sense) or
    shorten a branch.

    Removing a site means setting it to zero.

    Works for multi-skeletons.

    Parameters
    ----------
    skl_map : numpy.ndarray

    Returns
    -------
    None

    """
    cross = _CROSS_FOR_DIM[skl_map.ndim]
    LabeledMap = tymp.LABELING_FCT_FOR_DIM[skl_map.ndim]
    background_label = tymp.TMapBackgroundLabel(skl_map)
    padded_map = nmpy.pad(skl_map, 1, "constant")

    def FixLocalMap_n(
        _topo_map: array_t,
        _n_neighbors: int,
    ) -> bool:
        #
        skel_has_been_modified_ = False

        center = padded_map.ndim * (1,)
        for coords in zip(*nmpy.where(_topo_map == _n_neighbors)):
            lm_slices = tuple(slice(coord - 1, coord + 2) for coord in coords)
            local_map = padded_map[lm_slices]
            local_part_map = _topo_map[lm_slices]
            if (local_part_map[cross] == background_label).any():
                local_map[center] = 0

                _, n_components = LabeledMap(local_map)
                if n_components == 1:
                    skel_has_been_modified_ = True
                else:
                    local_map[center] = 1

        return skel_has_been_modified_

    excluded_n_neighbors = {
        0,
        1,
        2 * skl_map.ndim,
        background_label,
    }
    skel_has_been_modified = True
    while skel_has_been_modified:
        skel_has_been_modified = False

        topo_map = tymp.TopologyMapOfMap(padded_map, full_connectivity=False)
        included_n_neighbors = set(nmpy.unique(topo_map)).difference(
            excluded_n_neighbors
        )

        for n_neighbors in sorted(included_n_neighbors, reverse=True):
            skel_has_been_modified = skel_has_been_modified or FixLocalMap_n(
                topo_map,
                n_neighbors,
            )

    if skl_map.ndim == 2:
        skl_map[:, :] = padded_map[1:-1, 1:-1]
    else:
        skl_map[:, :, :] = padded_map[1:-1, 1:-1, 1:-1]


def PruneSKLMapBasedOnWidth(
    skl_map: array_t, width_map: array_t, min_width: float
) -> None:
    """Prunes the skeleton map so that the resulting skeleton corresponds everywhere to object portions wider than the
    passed minimal width.

    Works for multi-skeletons.

    Parameters
    ----------
    skl_map : numpy.ndarray
    width_map : numpy.ndarray
    min_width : float

    Returns
    -------
    None

    """
    while True:
        topo_map = tymp.TopologyMapOfMap(skl_map)
        end_positions = nmpy.where(topo_map == 1)
        distances = width_map[end_positions]

        tiny_distances = distances < min_width
        if tiny_distances.any():
            extra_positions = tuple(site[tiny_distances] for site in end_positions)
            skl_map[extra_positions] = 0
        else:
            break


def CheckSkeletonMap(
    skl_map: array_t,
    mode: Optional[str] = "single",
    behavior: Optional[str] = "exception",
) -> Optional[List[str]]:
    """Raises an exception or returns a list of invalid properties if the passed map is not a valid skeleton map.

    The map dtype is not strictly checked: only floating point types raise an exception (but int64, for example, does
    not although the chosen definition for skeleton map only mentions boolean and 8-bit integer types). The other
    aspects of a valid skeleton map are described in the module documentation.

    Parameters
    ----------
    skl_map : numpy.ndarray
    mode : str, optional
        Can be "single" (the default) to check that `skl_map` is a valid skeleton map with a unique connected component,
        or "multi" if multiple connected components are allowed. It can also be None to skip validation.
    behavior : str, optional
        Can be "exception" (the default) to trigger an exception raising if the map is invalid, or "report" to just
        return None if the map is valid or a list of strings describing the invalid properties.

    Returns
    -------
    List[str], optional

    """
    if mode is None:
        return None

    if mode == "single":
        invalidities = _SingleSkeletonMapInvalidities(skl_map)
    elif mode == "multi":
        invalidities = _MultiSkeletonMapInvalidities(skl_map)
    else:
        raise ValueError(f'{mode}: Invalid "mode" value')

    if invalidities is None:
        return None
    elif behavior == "exception":
        invalidities = "\n    ".join(invalidities)
        raise ValueError(f"Invalid {mode}-skeleton:\n    {invalidities}")
    elif behavior == "report":
        return invalidities
    else:
        raise ValueError(f'{behavior}: Invalid "behavior" value')


def _SingleSkeletonMapInvalidities(skl_map: array_t) -> Optional[List[str]]:
    """Returns a list of invalid properties, if any, of the passed map when expecting a skeleton with a single connected
    component.

    Parameters
    ----------
    skl_map : numpy.ndarray

    Returns
    -------
    List[str], optional

    """
    output = _MultiSkeletonMapInvalidities(skl_map)
    if output is None:
        output = []

    _, n_components = tymp.LABELING_FCT_FOR_DIM[skl_map.ndim](skl_map)
    if n_components > 1:
        output.append(
            f"{n_components}: Too many connected components in map; Expected: 1"
        )

    if (output is None) or (output.__len__() == 0):
        return None
    return output


def _MultiSkeletonMapInvalidities(skl_map: array_t) -> Optional[List[str]]:
    """Returns a list of invalid properties, if any, of the passed map when expecting a skeleton with one or more
    connected components.

    Parameters
    ----------
    skl_map : numpy.ndarray

    Returns
    -------
    List[str], optional

    """
    output = []

    if nmpy.issubdtype(skl_map.dtype, nmpy.floating):
        output.append(
            f"{skl_map.dtype}: Invalid map dtype; Expected: {nmpy.bool} or variants of {nmpy.integer}"
        )

    if skl_map.ndim not in (2, 3):
        output.append(f"{skl_map.ndim}: Invalid map dimension; Expected: 2 or 3")

    unique_values = nmpy.unique(skl_map)
    if not nmpy.array_equal(unique_values, (0, 1)):
        output.append(
            f"{unique_values}: Too many unique values in map; Expected: 0 and 1"
        )

    if (output is None) or (output.__len__() == 0):
        return None
    return output
