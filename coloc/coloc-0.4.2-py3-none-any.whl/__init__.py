"""An implementation of the COLOC method for colocalization of GWAS and/or eQTL
signals by Giambartolomei et al. 

https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1004383
"""

from coloc.coloc import (
    coloc, moloc, ascii_bar, print_coloc_result, print_moloc_result
)