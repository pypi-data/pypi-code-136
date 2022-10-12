import pathlib

import wmb

PACKAGE_DIR = pathlib.Path(wmb.__path__[0])

ENCODE_BLACKLIST_PATH = PACKAGE_DIR / "files/mm10-blacklist.v2.bed.gz"

GENCODE_MM10_vm22 = PACKAGE_DIR / "files/gencode.vM22.annotation.gene.flat.tsv.gz"
GENCODE_MM10_vm23 = PACKAGE_DIR / "files/modified_gencode.vM23.primary_assembly.annotation.gene.flat.tsv.gz"
MM10_TF_GENE_TABLE_PATH = '/ref/SCENIC/allTFs_mm.gene_info.csv'

MM10_MAIN_CHROM_SIZES_PATH = PACKAGE_DIR / "files/mm10.main.chrom.sizes"
MM10_MAIN_CHROM_NOCHRM_SIZES_PATH = PACKAGE_DIR / "files/mm10.main.chrom.nochrM.sizes"
MM10_MAIN_CHROM_NOCHRM_NOCHRY_SIZES_PATH = PACKAGE_DIR / "files/mm10.main.chrom.nochrM.nochrY.sizes"

CISTARGET_MGI_MOTIF_TF_TABLE_PATH = '/ref/SCENIC/v10nr_clust_public/snapshots/motifs-v10-nr.mgi-m0.00001-o0.0.tbl'
