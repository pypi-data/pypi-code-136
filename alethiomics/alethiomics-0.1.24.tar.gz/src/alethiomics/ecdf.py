"""Plot ECDF plot for two groups of cells for a given gene.
"""
# imports
from pandas import DataFrame, concat
from numpy import concatenate
from scipy.sparse import issparse
from plotnine import ggplot, aes, stat_ecdf, ylim, ylab, xlab, labs, ggtitle, theme_minimal, theme, element_text

# modules
def plot(adata, gene, group_column, group_mutant, group_normal, font_size = 14, layer = None):
    """Plot ECDF plot for two groups of cells.
    Parameters
    ----------
    adata: anndata object
        Object containing single cell RNA-seq data.
    gene: string
        Gene name.
    group_column: string
        A column in adata.obs containing group labels.
    group_mutant: string
        Name of the first group.
    group_normal: string
        Name of the second group.
    font_size: integer
        Font size for the text on the plot.
    layer: string
        Name of the adata layer to be used for calculation. Default is None. If default adata.X will be used for calculation.

    Returns
    -------
    p: ggplot object
        p contains ECDF plot for a given gene. To plot p use print(p).
    """

    gene_list = adata.var.index.tolist()
    
    if gene in gene_list:
        if not layer:
            if issparse(adata.X):
                df1 = DataFrame({
                    "expr" : concatenate(DataFrame.sparse.from_spmatrix(adata[adata.obs[group_column] == group_mutant, gene].X).to_numpy()), 
                    "cond" : group_mutant
                })
                df2 = DataFrame({
                    "expr" : concatenate(DataFrame.sparse.from_spmatrix(adata[adata.obs[group_column] == group_normal, gene].X).to_numpy()), 
                    "cond" : group_normal
                })
            else:
                df1 = DataFrame({
                    "expr" : concatenate(adata[adata.obs[group_column] == group_mutant, gene].X), 
                    "cond" : group_mutant
                })
                df2 = DataFrame({
                    "expr" : concatenate(adata[adata.obs[group_column] == group_normal, gene].X),
                    "cond" : group_normal
            })
        else:
            if issparse(adata.layers[layer]):
                df1 = DataFrame({
                    "expr" : concatenate(DataFrame.sparse.from_spmatrix(adata[adata.obs[group_column] == group_mutant, gene].layers[layer]).to_numpy()), 
                    "cond" : group_mutant
                })
                df2 = DataFrame({
                    "expr" : concatenate(DataFrame.sparse.from_spmatrix(adata[adata.obs[group_column] == group_normal, gene].layers[layer]).to_numpy()), 
                    "cond" : group_normal
                })
            else:
                df1 = DataFrame({
                    "expr" : concatenate(adata[adata.obs[group_column] == group_mutant, gene].layers[layer]), 
                    "cond" : group_mutant
                })
                df2 = DataFrame({
                    "expr" : concatenate(adata[adata.obs[group_column] == group_normal, gene].layers[layer]), 
                    "cond" : group_normal
                })

        df = concat([df1, df2])

        p = (
            ggplot(aes(x = 'expr', colour = 'cond'), df)
            + stat_ecdf()
            + ylim((0,1))
            + ylab("ECDF")
            + xlab("Expression")
            + labs(colour = "Groups")
            + ggtitle(gene)
            + theme_minimal()
            + theme(text = element_text(size = font_size))
        )

        return(p)
        
    else:
        print("Input gene is not present in the input dataset!")
        return(None)

# run when file is directly executed
if __name__ == '__main__':
    from .adata import dummy
    # create a dummy anndata object
    adata = dummy()
    p = plot(adata, 'Gene_1', 'cell_type', 'Monocyte', 'B', layer = 'log_transformed')
    print(p)
