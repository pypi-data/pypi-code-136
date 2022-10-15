from ..files import *
from ..annot import CEMBAATACCellAnnotation
import pandas as pd


class CEMBAATAC(AutoPathMixIn):
    """
    CEMBA ATAC-seq data
    """

    def __init__(self):
        self.CEMBA_ATAC_ZARR_PATH = CEMBA_ATAC_ZARR_PATH
        self.CEMBA_ATAC_CELL_TYPE_ANNOTATION_PATH = CEMBA_ATAC_CELL_TYPE_ANNOTATION_PATH
        self.CEMBA_ATAC_CLUSTER_FULL_NAME_PATH = CEMBA_ATAC_CLUSTER_FULL_NAME_PATH
        self.CEMBA_ATAC_MAPPING_METRIC_PATH = CEMBA_ATAC_MAPPING_METRIC_PATH

        self.CEMBA_ATAC_CLUSTER_L4_SUM_ZARR_PATH = CEMBA_ATAC_CLUSTER_L4_SUM_ZARR_PATH
        self.CEMBA_ATAC_CLUSTER_L4Region_SUM_ZARR_PATH = CEMBA_ATAC_CLUSTER_L4Region_SUM_ZARR_PATH

        self._full_name_map = pd.read_csv(self.CEMBA_ATAC_CLUSTER_FULL_NAME_PATH,
                                          index_col=0, sep='\t').squeeze()
        self._mapping_metric = None

        # validate path or auto change prefix
        self._check_file_path_attrs()
        return

    def get_atac_mapping_metric(self):
        if self._mapping_metric is None:
            self._mapping_metric = pd.read_hdf(self.CEMBA_ATAC_MAPPING_METRIC_PATH)
        return self._mapping_metric

    def get_atac_annot(self):
        return CEMBAATACCellAnnotation(self.CEMBA_ATAC_CELL_TYPE_ANNOTATION_PATH,
                                       self.get_atac_mapping_metric())

    def get_cluster_full_name(self, name):
        return self._full_name_map.loc[name]

