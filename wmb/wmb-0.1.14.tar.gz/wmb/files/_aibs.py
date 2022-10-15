"""
Notes:
    1. 3 10X samples has h5 missing manifest,
    2. 131 10X sample has manifest, missing h5. see AIBS_tenx_missing_info.txt
    3. SMART-seq data all has manifest
    4. 9895 SMART-seq cell has manifest, no data. see AIBS_SMART_missing_info.txt
    5. Need to clean up AIBS regions, get colors, standardize
    6. Current 10X sample metadata
        816: shared by Zizhen Yao
        688: files having h5 on Terra, but only 685 has metadata
"""

import pathlib

import wmb

PACKAGE_DIR = pathlib.Path(wmb.__path__[0])

# =================================
# AIBS SMART
# =================================

AIBS_SMART_CELL_METADATA_PATH = PACKAGE_DIR / 'files/AIBS.SMART.KeyCellMetadata.213261.csv.gz'
AIBS_SMART_CELL_FULL_METADATA_PATH = PACKAGE_DIR / 'files/AIBS.SMART.CellMetadata.213261.csv.gz'
AIBS_SMART_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/AIBS_SMART/AIBS.SMART.ordered.zarr'
AIBS_SMART_CELL_TYPE_ANNOTATION_PATH = '/gale/netapp/cemba3c/BICCN/wmb/aibs/AIBS.SMART.Annotations.zarr'

# Outliers
# /home/hanliu/project/cemba/study/MarkOutlier/AIBS_SMART 05/02/2022
AIBS_SMART_OUTLIER_IDS_PATH = PACKAGE_DIR / 'files/AIBS.SMART.DoubletsID.txt.gz'

# gene metadata
AIBS_SMART_GENE_MAP_PATH = PACKAGE_DIR / 'files/AIBS.SMART.GeneMap.csv'

# clustering

# =================================
# AIBS 10X v2 and v3
# =================================

AIBS_TENX_SAMPLE_METADATA_PATH = PACKAGE_DIR / 'files/AIBS.TENX.KeySampleMetadata.688.csv.gz'
AIBS_TENX_SAMPLE_FULL_METADATA_PATH = PACKAGE_DIR / 'files/AIBS.TENX.SampleMetadata.688.csv.gz'
AIBS_TENX_SAMPLE_TOTAL_METADATA_PATH = PACKAGE_DIR / 'files/AIBS.TENX.KeySampleMetadata.816.csv.gz'
AIBS_TENX_SAMPLE_TOTAL_FULL_METADATA_PATH = PACKAGE_DIR / 'files/AIBS.TENX.SampleMetadata.816.csv.gz'
AIBS_TENX_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/AIBS_TENX/AIBS.10X.ordered.zarr'
# zarr file created from the h5ad Zizhen shared on 08/2022, contains 4M cells pass QC,
# with her metadata and annots in AIBS_TENX_CELL_TYPE_ANNOTATION_V2_PATH
AIBS_TENX_V2_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/AIBS_TENX/AIBS.10X.v2.zarr'

AIBS_TENX_CELL_TYPE_ANNOTATION_PATH = '/gale/netapp/cemba3c/BICCN/wmb/aibs/AIBS.TENX.Annotations.zarr'
AIBS_TENX_CELL_TYPE_ANNOTATION_V2_PATH = '/gale/netapp/cemba3c/BICCN/wmb/aibs/AIBS.TENX.Annotations.v2.zarr'
AIBS_TENX_CELL_TYPE_ANNOTATION_V3_PATH = '/gale/netapp/cemba3c/BICCN/wmb/aibs/AIBS.TENX.Annotations.v3.zarr'

# Outliers
# /home/hanliu/project/cemba/study/MarkOutlier/AIBS_TENX 05/02/2022
AIBS_TENX_OUTLIER_IDS_PATH = PACKAGE_DIR / 'files/AIBS.TENX.DoubletsID.txt.gz'

# gene metadata
AIBS_TENX_GENE_MAP_PATH = PACKAGE_DIR / 'files/AIBS.TENX.GeneMap.csv'

# Gene chunk zarr path
AIBS_SMART_GENE_CHUNK_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/wmb/GeneChunks/AIBS.SMART'
AIBS_TENX_GENE_CHUNK_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/wmb/GeneChunks/AIBS.TENX'
AIBS_TENX_GENE_CHUNK_V2_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/wmb/GeneChunks/AIBS.TENX.V2'

# Cluster Aggregation
AIBS_SMART_CLUSTER_L4_SUM_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/wmb/aibs/AIBS.SMART.L4Agg.zarr'
AIBS_TENX_CLUSTER_L4_SUM_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/wmb/aibs/AIBS.TENX.L4Agg.zarr'

AIBS_SMART_CLUSTER_L4Region_SUM_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/wmb/aibs/AIBS.SMART.L4RegionAgg.zarr'
AIBS_TENX_CLUSTER_L4Region_SUM_ZARR_PATH = '/gale/netapp/cemba3c/BICCN/wmb/aibs/AIBS.TENX.L4RegionAgg.zarr'
