from functools import lru_cache

import pandas as pd
from ALLCools.mcds import MCDS

from ..annot import CEMBAEpiRetroCellAnnotation
from ..files import *
from ..genome import mm10


class CEMBAEpiRetro(AutoPathMixIn):
    """CEMBA EpiRetro-seq data."""

    def __init__(self):
        self.CEMBA_EPI_RETRO_ZARR_PATH = CEMBA_EPI_RETRO_ZARR_PATH
        self.CEMBA_EPI_RETRO_CELL_TYPE_ANNOTATION_PATH = CEMBA_EPI_RETRO_CELL_TYPE_ANNOTATION_PATH
        self.CEMBA_EPI_RETRO_MAPPING_METRIC_PATH = CEMBA_EPI_RETRO_MAPPING_METRIC_PATH

        # for gene plots
        self.CEMBA_EPI_RETRO_GENE_CHUNK_ZARR_PATH = CEMBA_EPI_RETRO_GENE_CHUNK_ZARR_PATH

        self._mapping_metric = None
        self._mc_gene_mcds = None

        # validate path or auto change prefix
        self._check_file_path_attrs()
        return

    def get_epi_retro_mapping_metric(self):
        if self._mapping_metric is None:
            self._mapping_metric = pd.read_hdf(self.CEMBA_EPI_RETRO_MAPPING_METRIC_PATH)
        return self._mapping_metric

    def get_epi_retro_annot(self):
        return CEMBAEpiRetroCellAnnotation(self.CEMBA_EPI_RETRO_CELL_TYPE_ANNOTATION_PATH,
                                           self.get_epi_retro_mapping_metric())

    def _open_gene_mcds(self):
        self._mc_gene_mcds = MCDS.open(self.CEMBA_EPI_RETRO_GENE_CHUNK_ZARR_PATH)

    @lru_cache(maxsize=200)
    def get_gene_frac(self, gene, mc_type='CHN'):
        if self._mc_gene_mcds is None:
            self._open_gene_mcds()

        # check if gene is gene name:
        try:
            gene_name = gene
            gene_id = mm10.gene_name_to_id(gene)
        except KeyError:
            gene_id = gene
            gene_name = mm10.gene_id_to_name(gene)

        gene_data = self._mc_gene_mcds['geneslop2k-vm23_da_frac_fc'].sel(
            {'mc_type': mc_type, 'geneslop2k-vm23': gene_id}
        ).to_pandas()
        return gene_data
