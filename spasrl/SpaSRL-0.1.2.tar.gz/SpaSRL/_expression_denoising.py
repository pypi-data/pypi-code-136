# -*- coding: utf-8 -*-

from typing import Optional
from anndata import AnnData

import numpy as np
from scipy.sparse import issparse, csr_matrix


def expression_denoising(
    adata: AnnData,
    representation_key: Optional[str] = None,
    inplace: bool = True,
) -> Optional[AnnData]:
    '''
    Denoise the gene expression matrix using representation matrix.
    
    Parameters
    ----------
    adata
        Annotated data matrix.
    representation_key
        If not specified, it looks `.uns['representation']` for self-representation learning settings
        (default storage place for :func:`~SpaSRL.run_SRL`).
        If specified, it looks `.uns[representation_key]` for self-representation learning settings.
    inplace
        Write to ``adata`` instead of returning a copy .
    
    Returns
    -------
    Depending on ``inplace``, returns or updates ``adata`` with the following fields updated.
    
    .X
        The denoised gene expression matrix.
    .layers['original']
        The original gene expression matrix.
    '''
    
    adata = adata if inplace else adata.copy()
    
    if representation_key is None:
        representation_key = 'representation'
    
    if representation_key not in adata.uns:
        raise ValueError(f'Did not find .uns["{representation_key}"].')
    
    conns_key = adata.uns[representation_key]['connectivities_key']
    
    
    adata.layers['original'] = adata.X.copy()
    
    adata.X = csr_matrix(np.matmul(
        adata.obsp[conns_key].toarray(),
        adata.X.toarray() if issparse(adata.X) else adata.X,
    ))
    
    return None if inplace else adata



















