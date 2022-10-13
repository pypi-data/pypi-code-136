# -*- coding: utf-8 -*-

from typing import Optional
from anndata import AnnData

import numpy as np
from scipy.sparse import issparse


def get_meta_genes(
    adata: AnnData,
    n_meta_genes: Optional[int] = None,
    representation_key: Optional[str] = None,
    copy: bool = False,
) -> Optional[AnnData]:
    '''
    Get functional meta gene score matrix using discriminant matrix.
    
    Parameters
    ----------
    adata
        Annotated data matrix.
    n_meta_genes
        Number of meta genes to return.
    representation_key
        If not specified, it looks `.uns['representation']` for self-representation learning settings
        (default storage place for :func:`~SpaSRL.run_SRL`).
        If specified, it looks `.uns[representation_key]` for self-representation learning settings.
    copy
        Return a copy instead of writing to ``adata``.
    
    Returns
    -------
    Depending on ``copy``, returns or updates ``adata`` with the following fields updated.
    
    .obsm['meta_genes']
        The meta gene score matrix.
    '''
    
    adata = adata.copy() if copy else adata
    
    if representation_key is None:
        representation_key = 'representation'
    
    if representation_key not in adata.uns:
        raise ValueError(f'Did not find .uns["{representation_key}"].')
    
    n_discriminant = adata.uns[representation_key]['discriminant'].shape[1]
    
    if n_meta_genes is None:
        n_meta_genes = n_discriminant
    
    if n_meta_genes > n_discriminant:
        raise ValueError(f'Number of meta genes should be smaller than number of discriminant vectors {n_discriminant}.')
    
    
    adata_use = adata[:, adata.uns['representation']['var_names_use']]
    
    adata.obsm['meta_genes'] =  np.matmul(
        adata_use.X.toarray() if issparse(adata_use.X) else adata_use.X,
        adata_use.uns[representation_key]['discriminant'][:n_meta_genes, :].T,
    )
    
    return adata if copy else None



















