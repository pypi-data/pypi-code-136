"""Create a dummy AnnData object with all of the slots filled in. This module follows this online tutorial: https://anndata-tutorials.readthedocs.io/en/latest/getting-started.html
"""
# imports
from scipy.sparse import csr_matrix
from anndata import AnnData
from pandas import Categorical
from numpy.random import poisson, choice, normal, seed, rand
from numpy import float32, log1p
from scipy.sparse import issparse

def dummy(ncells = 100, ngenes = 2000):
    """Create a dummy AnnData object
    Parameters
    ----------
    None

    Returns
    -------
    adata: AnnData object
        AnnData object with the following fields filled with random values:
            - adata.X
            - adata.obs_names
            - adata.var_names
            - adata.obs["cell_type"]
            - adata.obsm["X_umap"]
            - adata.varm["gene_stuff"]
            - adata.uns["random"]
            - adata.layers["log_transformed"]
    """
    # create a dummy anndata object
    seed(1); rand(1)
    counts = csr_matrix(poisson(1, size=(ncells, ngenes)), dtype=float32)
    adata = AnnData(counts)
    adata.obs_names = [f"Cell_{i:d}" for i in range(adata.n_obs)]
    adata.var_names = [f"Gene_{i:d}" for i in range(adata.n_vars)]
    ct = choice(["B", "T", "Monocyte"], size=(adata.n_obs,))
    adata.obs["cell_type"] = Categorical(ct)  # Categoricals are preferred for efficiency
    adata.obsm["X_umap"] = normal(0, 1, size=(adata.n_obs, 2))
    adata.varm["gene_stuff"] = normal(0, 1, size=(adata.n_vars, 5))
    adata.uns["random"] = [1, 2, 3]
    adata.layers["log_transformed"] = log1p(adata.X)
    return(adata)

# run when file is directly executed
if __name__ == '__main__':
    # create a dummy anndata object
    adata = dummy()
    print("Dummy Data:")
    print(adata)
    print("Obs:")
    print(adata.obs)
    print("Vars:")
    print(adata.var)
    print("Is adata.X sparse?")
    print(issparse(adata.X))