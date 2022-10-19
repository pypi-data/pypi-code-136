"""Calculate Kolmogorov-Smirnov's Statistics on two groups of cells, testing whether their expression distributions for a given gene are significantly different.
"""
# imports
from scipy.stats import ks_2samp
from scipy.sparse import issparse
from numpy import array

def stats(adata, group_column, group_mutant, group_normal, gene, layer = None):
    """Calculate Kolmogorov-Smirnov's Statistics on two groups of cells for a given gene.

    Parameters
    ----------
    adata: anndata object
        Object containing single cell RNA-seq data.
    group_column: string
        A column in adata.obs containing group labels.
    group_mutant: string
        Name of the first group.
    group_normal: string
        Name of the second group.
    gene: string
        Gene name to perform statistical analysis on.
    layer: string
        Name of the adata layer to be used for calculation. Default is None. If default adata.X will be used for calculation.

    Returns
    -------
    ks: KstestResult object
        The object contains KS statistic and pvalue for a given gene.
    """

    d1 = adata[adata.obs[group_column] == group_mutant, gene]
    d2 = adata[adata.obs[group_column] == group_normal, gene]

    if layer is not None:
        d1 = d1.layers[layer]
        d2 = d2.layers[layer]
    else:
        d1 = d1.X
        d2 = d2.X

    if issparse(d1):
        d1 = d1.toarray()
        d2 = d2.toarray()

    d1 = array(d1).flatten()
    d2 = array(d2).flatten()

    ks = ks_2samp(d1, d2)

    return(ks)

# run when file is directly executed
if __name__ == '__main__':
    from .adata import dummy
    # create a dummy anndata object
    adata = dummy()
    ks = stats(adata, 'cell_type', 'Monocyte', 'B', gene = adata.var.index[0], layer = 'log_transformed')
    print(ks)