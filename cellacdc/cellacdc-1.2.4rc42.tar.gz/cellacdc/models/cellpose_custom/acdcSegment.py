import os

from cellacdc.models.cellpose import acdcSegment as cp
from cellpose import models

class Model:
    def __init__(self, model_path: os.PathLike = '', net_avg=False, gpu=False):
        self.acdcCellpose = cp.Model()
        self.acdcCellpose.model = models.CellposeModel(
            gpu=gpu, net_avg=net_avg, pretrained_model=model_path
        )

    def segment(
            self, image,
            diameter=0.0,
            flow_threshold=0.4,
            cellprob_threshold=0.0,
            stitch_threshold=0.0,
            min_size=15,
            anisotropy=0.0,
            normalize=True,
            resample=True,
            segment_3D_volume=False            
        ):
        labels = self.acdcCellpose.segment(
            image,
            diameter=diameter,
            flow_threshold=flow_threshold,
            cellprob_threshold=cellprob_threshold,
            stitch_threshold=stitch_threshold,
            min_size=min_size,
            anisotropy=anisotropy,
            normalize=normalize,
            resample=resample,
            segment_3D_volume=segment_3D_volume  
        )
        return labels