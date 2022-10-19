#!/usr/bin/env python3

import numpy as np

from anndata import AnnData


def info(adata: AnnData, key_set: str = "sccover_set") -> None:
    """
    Displays basic vertex cover info.
    """
    assert key_set in adata.obs, "Please make sure to run vertex_cover first."
    vc = adata.obs[key_set]
    print(f"Total number of cells: {adata.n_obs}")
    print(
        f"Vertex cover cells number: {np.sum(vc)} ({int(np.sum(vc)/adata.n_obs*1000)/10}%)"
    )
