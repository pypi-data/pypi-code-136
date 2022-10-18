"""Find hydrated waters in structure."""
import json
from pathlib import Path
from typing import Any

# third-party imports
import gemmi  # type: ignore
import pandas as pd
from loguru import logger

# module imports
from .common import APP
from .common import METADATA_FILE
from .common import NAME
from .common import NEIGHBOR_FILE
from .common import RCSB_CACHE
from .config import read_config


MAX_NEIGHBORS = 6


def add_mark(
    n: int, mark: gemmi.NeighborSearch.Mark, st: gemmi.Model
) -> dict[str, Any]:
    """Return numbered dictionary of mark info."""
    mark_dict = {}
    mark_dict[f"image_idx_{n}"] = mark.image_idx
    chain = st[mark.chain_idx]
    mark_dict[f"chain_{n}"] = chain.name
    res = chain[mark.residue_idx]
    mark_dict[f"residue_{n}"] = res.seqid
    mark_dict[f"resname_{n}"] = res.name
    atom = res[mark.atom_idx]
    mark_dict[f"atom_type_{n}"] = atom.element.name
    mark_dict[f"atom_{n}"] = atom.serial
    # mark_dict[f"x_{n}"] = round(mark.x, 2)
    # mark_dict[f"y_{n}"] = round(mark.y, 2)
    # mark_dict[f"z_{n}"] = round(mark.z, 2)
    return mark_dict


@APP.command()
def water_neighbors(rcsb_id: str) -> dict[str, Any]:
    """Find neighbors of waters in structure file."""
    conf = read_config(NAME)
    cache_dir = conf["rcsb_cache"]["dir"]
    min_dist = conf["find"]["min_dist"]
    populate_radius = conf["find"]["populate_radius"]
    neighbor_radius = conf["find"]["neighbor_radius"]
    # special_point_radius = conf["find"]["special_point_radius"]
    inpath = RCSB_CACHE.rcsb_cache(rcsb_id, file_type="cif", cache_dir=cache_dir)
    st = gemmi.read_structure(str(inpath))
    if len(st) > 1:
        logger.warning(f"Multi-structure file {rcsb_id} has {len(st)} parts.")
    meta_dict = {}
    meta_dict["structures"] = len(st)
    meta_dict["mass"] = round(st[0].calculate_mass(), 1)
    meta_dict["hydrogens"] = st[0].count_hydrogen_sites()
    meta_dict["atoms"] = st[0].count_atom_sites()
    ns = gemmi.NeighborSearch(st[0], st.cell, populate_radius).populate(include_h=False)
    n_waters = 0
    max_marks = 0
    nbr_dict = {}
    for chain in st[0]:
        for res in chain:
            if res.is_water():
                for atom in res:
                    row_dict = {
                        "chain": chain.name,
                        "residue": res.seqid,
                        "atom": atom.serial,
                        "occ_no": round(atom.occ, 2),
                        "b_iso": round(atom.b_iso, 1),
                        "neighbors": 0,
                    }
                    n_marks = 0
                    for mark in ns.find_neighbors(
                        atom, min_dist=min_dist, max_dist=neighbor_radius
                    ):
                        if n_marks < MAX_NEIGHBORS:
                            row_dict.update(add_mark(n_marks, mark, st[0]))
                        n_marks += 1
                    row_dict["neighbors"] = n_marks
                    max_marks = max(max_marks, n_marks)
                    nbr_dict[n_waters] = row_dict
                n_waters += 1
    meta_dict["n_waters"] = n_waters
    meta_dict["max_neighbors"] = max_marks
    neighbors = pd.DataFrame.from_dict(nbr_dict, orient="index")
    dir_path = Path(rcsb_id)
    dir_path.mkdir(exist_ok=True)
    neighbors.to_csv(dir_path / NEIGHBOR_FILE, sep="\t")
    with (dir_path / METADATA_FILE).open("w") as f:
        json.dump(meta_dict, f, sort_keys=True, indent=4)
    return meta_dict
