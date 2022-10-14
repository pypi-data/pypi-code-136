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

import pathlib as ph_
import tempfile as tf_

import matplotlib.pyplot as pl_
import numpy as np_
import scipy.ndimage as im_
import skimage.measure as ms_

import skl_graph.skl_map as mp_
from skl_graph.skl_fgraph import skl_graph_t
from skl_graph.skl_graph import plot_mode_e

import sknw as sk_


COLORMAP_FOR_IMG = "inferno"
COLORMAP_FOR_DIFF = "gray"


def _HorseData():
    """"""
    import skimage.data as sd_
    import skimage.morphology as my_
    import skimage.util as su_

    space_dim = 2

    object_map = su_.invert(sd_.horse())
    disk = my_.disk(9)
    object_map[10 : (10 + disk.shape[0]), 20 : (20 + disk.shape[1])][disk] = True

    return space_dim, object_map, "multi"


def _RandomData(dim_as_str: str):
    """"""
    _SetRandomSeedForSession()

    if dim_as_str == "2d":
        space_dim = 2
        array_shape = (100, 100)
        threshold_fct = lambda img: img.median()
        struct_elm_shape = (3, 3)
    elif dim_as_str == "3d":
        space_dim = 3
        array_shape = (80, 80, 50)
        threshold_fct = lambda img: 0.75 * np_.amax(image)
        struct_elm_shape = (3, 3, 3)
    else:
        raise ValueError(f"{dim_as_str}: Unknown data specification")

    image = np_.random.random(array_shape)
    image = im_.gaussian_filter(image, 1)

    multi_map = image > threshold_fct(image)
    lbl_multi_map, _ = im_.label(
        multi_map,
        structure=np_.ones(struct_elm_shape, dtype=np_.uint8),
        output=np_.uint,
    )

    cc_props = ms_.regionprops(lbl_multi_map)
    largest_cc_idx = np_.argmax([cc_prop.area for cc_prop in cc_props]).item()
    lbl_multi_map[lbl_multi_map != cc_props[largest_cc_idx].label] = 0
    object_map = lbl_multi_map > 0

    return space_dim, object_map, "single"


def _SetRandomSeedForSession() -> None:
    """Sets a random seed limited to current session.

    The purpose is to allow the generation of different random data in consecutive tests while allowing to generate the
    same data sequence again for debugging purposes. This would be done by deleting the file "skl_graph_demo_seed.lock"
    in the temporary folder.

    Returns
    -------

    """
    try:
        with tf_.NamedTemporaryFile() as doc_accessor:
            doc_name = ph_.Path(doc_accessor.name)
            tmp_folder = doc_name.parents[0]
    except:
        print("Unable to set a random seed for current session")
        tmp_folder = None

    if tmp_folder is not None:
        seed_lock = tmp_folder.joinpath("skl_graph_demo_seed.lock")
        if not seed_lock.exists():
            np_.random.seed(0)
            seed_lock.touch()


def _PrepareImagePlots(all_axes, images, colormaps, titles) -> None:
    """"""
    for axes, img, cmap, title in zip(all_axes.flat, images, colormaps, titles):
        axes.matshow(img, cmap=cmap)
        axes.set_title(title)
        axes.set_axis_off()
    pl_.tight_layout(pad=0.3)


def Main(data, just_test) -> None:
    """"""
    # --- Generation of object map
    if data == "horse":
        space_dim, object_map, skl_validity_mode = _HorseData()
    elif data in ("2d", "3d"):
        space_dim, object_map, skl_validity_mode = _RandomData(data)
    else:
        obj_map_path = ph_.Path(__file__).parent / (data +".npz")
        if obj_map_path.is_file():
            object_map = np_.load(obj_map_path)["obj_map"]
            space_dim = object_map.ndim
            skl_validity_mode = "multi"
        else:
            raise FileNotFoundError(obj_map_path)

    # --- From object map to skeleton graph
    np_.savez_compressed("/tmp/object_map", object_map=object_map)
    skl_map, skl_width_map = mp_.SKLMapFromObjectMap(object_map, with_width=True)
    mp_.CheckSkeletonMap(skl_map, mode=skl_validity_mode)
    skl_graph = skl_graph_t.FromSKLMap(skl_map, width_map=skl_width_map)

    sknw_graph = sk_.build_sknw(skl_map)

    # --- Checking correctness of skeleton graph
    binary_correctness, topology_correctness = skl_graph.Correctness(skl_map)
    print(
        f"Rebuilt skeleton = Binary? Topological? "
        f"{binary_correctness} {topology_correctness}"
    )

    # --- Some info about skeleton graphs
    graph_is_valid = skl_graph.is_valid
    print(
        f"Obj map area={np_.count_nonzero(object_map)}\n\n"
        f"Graph validity={graph_is_valid}"
    )
    if graph_is_valid:
        print(skl_graph)
    else:
        skl_graph.ShowInvalidities()
    print(dir(sknw_graph))

    # --- No display
    if just_test:
        return

    # --- Various rebuilt maps
    object_map = object_map.astype(np_.uint8)
    rebuilt_skl_map = skl_graph.RebuiltSkeletonMap()
    rebuilt_skl_mww = skl_graph.RebuiltSkeletonMap(with_width=True)
    rebuilt_obj_map = skl_graph.RebuiltObjectMap()

    if space_dim == 3:
        object_map = np_.amax(object_map, axis=2)
        rebuilt_skl_map = np_.amax(rebuilt_skl_map, axis=2)
        rebuilt_skl_mww = np_.amax(rebuilt_skl_mww, axis=2)
        rebuilt_obj_map = np_.amax(rebuilt_obj_map, axis=2)

    # --- Show various maps
    images = (
        rebuilt_skl_map + object_map,
        rebuilt_skl_map + rebuilt_obj_map,
        rebuilt_skl_map,
        rebuilt_skl_mww,
    )
    colormaps = (COLORMAP_FOR_IMG, COLORMAP_FOR_IMG, COLORMAP_FOR_IMG, COLORMAP_FOR_IMG)
    titles = (
        "Rebuilt Skl Over Obj",
        "Rebuilt Skl Over Rebuilt Obj",
        "Rebuilt Skl",
        "Rebuilt Skl WW",
    )
    _, axes = pl_.subplots(2, 2)
    _PrepareImagePlots(axes, images, colormaps, titles)

    images = (object_map, rebuilt_obj_map, object_map - rebuilt_obj_map)
    colormaps = (COLORMAP_FOR_IMG, COLORMAP_FOR_IMG, COLORMAP_FOR_DIFF)
    titles = ("Object", "Rebuilt", "Error")
    _, axes = pl_.subplots(1, images.__len__())
    _PrepareImagePlots(axes, images, colormaps, titles)

    # --- Plot skeleton graph
    if space_dim == 2:
        axes_1 = skl_graph.Plot(
            mode=plot_mode_e.Networkx, should_block=False, should_return_axes=True
        )
        axes_2 = skl_graph.Plot(
            mode=plot_mode_e.Graphviz, should_block=False, should_return_axes=True
        )
        axes_1.set_title("Networkx Mode")
        axes_2.set_title("Graphviz Mode")
    axes_1 = skl_graph.Plot(
        mode=plot_mode_e.SKL_Curve,
        w_directions=True,
        should_block=False,
        should_return_axes=True,
    )
    axes_2 = skl_graph.Plot(
        mode=plot_mode_e.SKL_Polyline,
        w_directions=True,
        should_block=False,
        should_return_axes=True,
    )
    axes_3 = skl_graph.Plot(should_block=False, should_return_axes=True)
    axes_1.set_title("Curve Mode")
    axes_2.set_title("Polyline Mode")
    axes_3.set_title("Default Mode")

    if space_dim == 2:
        # From: https://github.com/Image-Py/sknw (previously: https://github.com/yxdragon/sknw)
        sk_.draw_graph(object_map, sknw_graph, cn=255, ce=128)
        pl_.title("SKNW")
        pl_.gca().set_axis_off()
        pl_.tight_layout(pad=0.3)


if __name__ == "__main__":
    #
    import sys as sy_

    if sy_.argv.__len__() == 1:
        print("Call with arguments: horse|2d|3d [noplot]")
        sy_.exit(0)
    test_and_exit = (sy_.argv.__len__() > 2) and (sy_.argv[2] == "noplot")

    Main(sy_.argv[1], test_and_exit)
    if not test_and_exit:
        pl_.show()
