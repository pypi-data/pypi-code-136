from functools import lru_cache

import numpy as np
import pandas as pd

from wmb.files import *
from ..annot import AIBSTENXCellAnnotation, AIBSSMARTCellAnnotation
from ..brain_region import brain
from ..genome import mm10


def _get_mapping_metric(path, pass_basic_qc_only=True):
    df = pd.read_csv(path, index_col=0)
    df.index.name = 'cell'
    if pass_basic_qc_only:
        df = df[df['PassBasicQC']].copy()
    return df


class AIBS(AutoPathMixIn):
    def __init__(self):
        self.AIBS_SMART_CELL_METADATA_PATH = AIBS_SMART_CELL_METADATA_PATH
        self.AIBS_SMART_CELL_FULL_METADATA_PATH = AIBS_SMART_CELL_FULL_METADATA_PATH
        self.AIBS_SMART_ZARR_PATH = AIBS_SMART_ZARR_PATH
        self.AIBS_SMART_OUTLIER_IDS_PATH = AIBS_SMART_OUTLIER_IDS_PATH
        self.AIBS_SMART_CELL_TYPE_ANNOTATION_PATH = AIBS_SMART_CELL_TYPE_ANNOTATION_PATH
        self.AIBS_SMART_GENE_MAP_PATH = AIBS_SMART_GENE_MAP_PATH

        self.AIBS_TENX_SAMPLE_METADATA_PATH = AIBS_TENX_SAMPLE_METADATA_PATH
        self.AIBS_TENX_SAMPLE_FULL_METADATA_PATH = AIBS_TENX_SAMPLE_FULL_METADATA_PATH
        self.AIBS_TENX_SAMPLE_TOTAL_METADATA_PATH = AIBS_TENX_SAMPLE_TOTAL_METADATA_PATH
        self.AIBS_TENX_SAMPLE_TOTAL_FULL_METADATA_PATH = AIBS_TENX_SAMPLE_TOTAL_FULL_METADATA_PATH

        self.AIBS_TENX_ZARR_PATH = AIBS_TENX_ZARR_PATH
        self.AIBS_TENX_V2_ZARR_PATH = AIBS_TENX_V2_ZARR_PATH

        self.AIBS_TENX_OUTLIER_IDS_PATH = AIBS_TENX_OUTLIER_IDS_PATH
        self.AIBS_TENX_CELL_TYPE_ANNOTATION_PATH = AIBS_TENX_CELL_TYPE_ANNOTATION_PATH
        self.AIBS_TENX_CELL_TYPE_ANNOTATION_V2_PATH = AIBS_TENX_CELL_TYPE_ANNOTATION_V2_PATH
        self.AIBS_TENX_CELL_TYPE_ANNOTATION_V3_PATH = AIBS_TENX_CELL_TYPE_ANNOTATION_V3_PATH
        self.AIBS_TENX_GENE_MAP_PATH = AIBS_TENX_GENE_MAP_PATH

        self.AIBS_SMART_GENE_CHUNK_ZARR_PATH = AIBS_SMART_GENE_CHUNK_ZARR_PATH
        self.AIBS_TENX_GENE_CHUNK_ZARR_PATH = AIBS_TENX_GENE_CHUNK_ZARR_PATH
        self.AIBS_TENX_GENE_CHUNK_V2_ZARR_PATH = AIBS_TENX_GENE_CHUNK_V2_ZARR_PATH

        self.AIBS_SMART_CLUSTER_L4_SUM_ZARR_PATH = AIBS_SMART_CLUSTER_L4_SUM_ZARR_PATH
        self.AIBS_TENX_CLUSTER_L4_SUM_ZARR_PATH = AIBS_TENX_CLUSTER_L4_SUM_ZARR_PATH
        self.AIBS_SMART_CLUSTER_L4Region_SUM_ZARR_PATH = AIBS_SMART_CLUSTER_L4Region_SUM_ZARR_PATH
        self.AIBS_TENX_CLUSTER_L4Region_SUM_ZARR_PATH = AIBS_TENX_CLUSTER_L4Region_SUM_ZARR_PATH

        # internal variables
        self._smart_gene_zarr = None
        self._smart_cell_million_reads = None
        self._smart_gene_index = None
        self._tenx_gene_zarr = None
        self._tenx_cell_million_reads = None
        self._tenx_gene_index = None

        # validate path or auto change prefix
        self._check_file_path_attrs()
        return

    def get_smart_gene_map(self):
        return pd.read_csv(self.AIBS_SMART_GENE_MAP_PATH, index_col=0, header=0).squeeze()

    def get_tenx_gene_map(self):
        return pd.read_csv(self.AIBS_TENX_GENE_MAP_PATH, index_col=0, header=0).squeeze()

    def get_smart_cell_metadata(self, pass_basic_qc_only=True, remove_outlier_ids=True):
        df = pd.read_csv(self.AIBS_SMART_CELL_METADATA_PATH, index_col=0)
        df.index.name = 'cell'
        if pass_basic_qc_only:
            df = df[df['PassBasicQC']].copy()
        if remove_outlier_ids:
            df = df.drop(self.get_smart_outlier_ids())

        df['MajorRegion'] = df['Substructure'].map(
            brain.map_dissection_region_to_major_region(region_type='AIBS_SMART'))
        df['SubRegion'] = df['Substructure'].map(brain.map_dissection_region_to_sub_region(region_type='AIBS_SMART'))
        return df

    def get_tenx_sample_metadata(self):
        df = pd.read_csv(self.AIBS_TENX_SAMPLE_METADATA_PATH, index_col=0)

        # three sample has missing values in the current manifest file, 05/08/2022
        df.fillna('nan', inplace=True)

        df.index.name = 'sample'

        df['MajorRegion'] = df['Structure'].map(brain.map_dissection_region_to_major_region(region_type='AIBS_TENX'))
        df['SubRegion'] = df['Structure'].map(brain.map_dissection_region_to_sub_region(region_type='AIBS_TENX'))
        return df

    def get_tenx_outlier_ids(self):
        ids = pd.read_csv(self.AIBS_TENX_OUTLIER_IDS_PATH, index_col=0, header=None).index
        ids.name = 'cell'
        return ids

    def get_smart_outlier_ids(self):
        ids = pd.read_csv(self.AIBS_SMART_OUTLIER_IDS_PATH, index_col=0, header=None).index
        ids.name = 'cell'
        return ids

    def get_smart_annot(self):
        return AIBSSMARTCellAnnotation(self.AIBS_SMART_CELL_TYPE_ANNOTATION_PATH,
                                       self.get_smart_cell_metadata())

    def get_tenx_annot(self, version='v3'):
        if version == 'v1':
            path = self.AIBS_TENX_CELL_TYPE_ANNOTATION_PATH
        elif version == 'v2':
            path = self.AIBS_TENX_CELL_TYPE_ANNOTATION_V2_PATH
        elif version == 'v3':
            path = self.AIBS_TENX_CELL_TYPE_ANNOTATION_V3_PATH
        else:
            raise ValueError('Unknown version: {}'.format(version))

        annot = AIBSTENXCellAnnotation(path,
                                       self.get_tenx_sample_metadata())
        if version == 'v2':
            annot.add_palette(palette=PALETTES['AIBS.TENX.Annot.V2'], da_name='L2_annot')
        return annot

    def _open_smart_zarr(self):
        import xarray as xr
        self._smart_gene_zarr = xr.open_zarr(self.AIBS_SMART_GENE_CHUNK_ZARR_PATH)
        self._smart_cell_million_reads = self._smart_gene_zarr['read_count'].to_pandas()
        self._smart_cell_million_reads /= 1000000
        self._smart_gene_index = self._smart_gene_zarr.get_index('gene')
        return

    def _open_tenx_zarr(self, version):
        import xarray as xr
        if version == 'v1':
            path = self.AIBS_TENX_GENE_CHUNK_ZARR_PATH
        elif version == 'v2':
            path = self.AIBS_TENX_GENE_CHUNK_V2_ZARR_PATH
        else:
            raise ValueError('Unknown version: {}'.format(version))

        self._tenx_gene_zarr = xr.open_zarr(path)
        self._tenx_cell_million_reads = self._tenx_gene_zarr['umi_count'].to_pandas()
        self._tenx_cell_million_reads /= 1000000
        self._tenx_gene_index = self._tenx_gene_zarr.get_index('gene')
        return

    @staticmethod
    def _standardize_gene_index(gene, dataset, gene_index):
        # check if gene is gene name:
        try:
            if dataset == 'smart':
                # current smart gene index is gene name
                if gene not in gene_index:
                    use_gene_text = mm10.gene_id_to_name(gene)
                else:
                    use_gene_text = gene
            else:
                # current tenx gene index is gene id base
                if gene not in gene_index:
                    use_gene_text = mm10.gene_name_to_id_base(gene)
                else:
                    use_gene_text = gene
                if use_gene_text not in gene_index:
                    raise KeyError
        except KeyError:
            raise KeyError(f'gene {gene} can not be recognized.')
        return use_gene_text

    @lru_cache(maxsize=200)
    def _get_gene_data(self, gene, normalize, log, dataset):
        if dataset == 'smart':
            gene_zarr = self._smart_gene_zarr
            cell_million_reads = self._smart_cell_million_reads
        elif dataset == 'tenx':
            gene_zarr = self._tenx_gene_zarr
            cell_million_reads = self._tenx_cell_million_reads
        else:
            raise ValueError('dataset must be smart or tenx, got {}'.format(dataset))

        # raw counts
        gene_data = gene_zarr['gene_da_fc'].sel(gene=gene).to_pandas()
        # normalize to CPM
        if normalize:
            gene_data /= cell_million_reads

        # log transform
        if log:
            gene_data = np.log1p(gene_data)

        return gene_data

    def get_tenx_gene_data(self, gene, normalize=True, log=True, version='v2'):
        if self._tenx_gene_zarr is None:
            self._open_tenx_zarr(version=version)

        gene_index = self._tenx_gene_index
        gene = self._standardize_gene_index(gene, 'tenx', gene_index)
        return self._get_gene_data(gene, normalize=normalize, log=log, dataset='tenx')

    def get_smart_gene_data(self, gene, normalize=True, log=True):
        if self._smart_gene_zarr is None:
            self._open_smart_zarr()

        gene_index = self._smart_gene_index
        gene = self._standardize_gene_index(gene, 'smart', gene_index)
        return self._get_gene_data(gene, normalize=normalize, log=log, dataset='smart')


aibs = AIBS()
