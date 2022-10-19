"""Calculate Fisher's Statistics on two groups of cells, testing whether the number of expressed cells (not zero expression) has significantly changed between two groups.
"""
# imports
from pandas import DataFrame
from scipy.sparse import issparse
from pyranges.statistics import fisher_exact

def stats(adata, group_column, group_mutant, group_normal):
    """Calculate Fisher's Statistics on two groups of cells.
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

    Returns
    -------
    adata: anndata object
        Original anndata object with six new added columns in adata.var. Columns correspond to 1) fraction of non-zero cells in group_mutant, 2) fraction of non-zero cells in group_normal and 3) four other columns correspond to Fisher's test statistics, the most important of which is P. If Fisher stats was calculated before it will be overwritten with new values.
    """
    
    x = adata[adata.obs[group_column] == group_mutant].X
    y = adata[adata.obs[group_column] == group_normal].X
    
    if not issparse(adata.X):
        x = DataFrame(x == 0)
        y = DataFrame(y == 0)
        a = x.sum(axis = 0)
        b = y.sum(axis = 0)
    else:
        x = DataFrame.sparse.from_spmatrix(x != 0)
        y = DataFrame.sparse.from_spmatrix(y != 0)
        a = (x == 0).sum(axis = 0)
        b = (y == 0).sum(axis = 0)
    
    c = x.shape[0] - a
    d = y.shape[0] - b

    fish = fisher_exact(a, b, c, d, pseudocount=0)

    fish.index = adata.var.index
    
    adata.var['non_zero_mutant'] = (c / x.shape[0] * 100).tolist()
    adata.var['non_zero_normal'] = (d / y.shape[0] * 100).tolist()

    adata.var['OR'] = fish['OR']
    adata.var['P'] = fish['P']
    adata.var['PLeft'] = fish['PLeft']
    adata.var['PRight'] = fish['PRight']

    return(adata)

# run when file is directly executed
if __name__ == '__main__':
    from .adata import dummy
    # create a dummy anndata object
    adata = dummy()
    adata = stats(adata, 'cell_type', 'Monocyte', 'B')
    print(adata.var)
