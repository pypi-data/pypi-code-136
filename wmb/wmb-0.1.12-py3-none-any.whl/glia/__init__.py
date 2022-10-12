from functools import lru_cache

import numpy as np
import pandas as pd

from ..annot import GliamCTCellAnnotation

AGE_PALETTE = {'E16': '#d24f38',
               'P0': '#b0775e',
               'P7': '#d4a63e',
               'P14': '#cdcd9b',
               'P28': '#6f813c',
               'P120': '#97d54e'}
SEX_PALETTE = {'M': 'steelblue', 'F': 'orange'}
REGION_PALETTE = {
    'VC': '#ed5f74',
    'Retina': '#38c37b',
    'dLGN': '#b879dd',
}


class GliaMCT:
    def __init__(self):
        self.metadata = '/gale/netapp/glia1/analysis_hl/study/BasicCellFilter/Glia.snmCT.CellMetadata.csv.gz'
        self.GLIA_MCT_MCDS_PATH = '/gale/netapp/glia1/dataset/DVC.snmCT.mcds'
        self.GLIA_MCT_RNA_GENE_CHUNK_PATH = '/gale/netapp/glia1/dataset/DVC.snmCT.rna_feature_chunk.zarr'
        self.GLIA_MCT_MC_GENE_CHUNK_PATH = '/gale/netapp/glia1/dataset/DVC.snmCT.gene_frac_feature_chunk.zarr'
        self.GLIA_MCT_ANNOTATION_PATH = '/gale/netapp/glia1/analysis_hl/study/Clustering/' \
                                        'Summary/GLIA.snmCT.Annotations.zarr'
        self.GLIA_ALLC_PATH = '/gale/netapp/glia1/analysis_hl/bulk/PrepareFileList/total_allc.tsv.gz'
        self.AGE_PALETTE = AGE_PALETTE
        self.SEX_PALETTE = SEX_PALETTE
        self.REGION_PALETTE = REGION_PALETTE

        self._gene_dataset = None
        self._rna_dataset = None
        self._per_cell_million_rna_reads = None

        from ..genome import MM10GenomeRef
        self._mm10 = MM10GenomeRef(annot_version='GENCODE_vm22')

    def get_glia_metadata(self):
        return pd.read_csv(self.metadata, index_col=0)

    def get_glia_annot(self):
        return GliamCTCellAnnotation(self.GLIA_MCT_ANNOTATION_PATH)

    def _open_gene_mcds(self):
        from ALLCools.mcds import MCDS
        mcds = MCDS.open(self.GLIA_MCT_MC_GENE_CHUNK_PATH)
        self._gene_dataset = mcds

    @lru_cache(maxsize=200)
    def get_gene_mc_frac(self, gene, mc_type='CHN'):
        if self._gene_dataset is None:
            self._open_gene_mcds()

        # check if gene is gene name:
        try:
            gene_id = self._mm10.gene_name_to_id(gene)
        except KeyError:
            gene_id = gene

        gene_data = self._gene_dataset['geneslop2k_da_frac_fc'].sel(
            mc_type=mc_type, geneslop2k=gene_id
        ).to_pandas()
        return gene_data

    def _open_rna_zarr(self):
        from ALLCools.mcds import MCDS
        self._rna_dataset = MCDS.open(self.GLIA_MCT_RNA_GENE_CHUNK_PATH)
        self._per_cell_million_rna_reads = self.get_glia_metadata()['FinalRNAReads'] / 1e6

    @lru_cache(maxsize=200)
    def get_gene_rna(self, gene, normalize=True, log1p=True):
        if self._rna_dataset is None:
            self._open_rna_zarr()

        # check if gene is gene name:
        try:
            gene_id = self._mm10.gene_name_to_id(gene)
        except KeyError:
            gene_id = gene

        gene_data = self._rna_dataset['gene_da_fc'].sel(gene=gene_id).to_pandas()

        if normalize:
            gene_data = gene_data / self._per_cell_million_rna_reads
        if log1p:
            gene_data = np.log1p(gene_data)

        return gene_data


glia = GliaMCT()
