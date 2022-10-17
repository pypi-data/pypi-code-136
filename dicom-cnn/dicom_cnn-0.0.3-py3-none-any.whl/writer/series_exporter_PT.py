from __future__ import annotations
import enum
from typing import TYPE_CHECKING
from dicom_cnn.writer.series_exporter import SeriesExporter
if TYPE_CHECKING:
    from dicom_cnn.series.series_pt import SeriesPT

import numpy as np
import SimpleITK as sitk

class UnitPT(enum.Enum):

    RAW = 'raw'
    SUV = 'suv'
    SUL = 'sul'


class SeriesExporterPT(SeriesExporter):
  
    unit = UnitPT.SUV

    series: SeriesPT = None

    def convert_to(self, unit: str):
        if(unit not in list(UnitPT)):
            raise('Unknown PT Export Unit')
        self.unit = unit

    def get_array(self) -> np.ndarray:
        """Override series exporter to calculate image matrix to be exported according to choosen unit

        Returns:
            np.ndarray: _description_
        """
        if(self.unit == UnitPT.RAW):
            return self.series.get_numpy_array()
        elif (self.unit == UnitPT.SUV):
            return self.series.get_suv_numpy_array()
        elif (self.unit == UnitPT.SUL):
            return self.series.get_sul_numpy_array()

    def get_sitk_image(self) -> sitk.Image:
        sitk_img = sitk.GetImageFromArray(self.get_array())
        sitk_img.SetDirection(self.series.get_series_direction())
        sitk_img.SetOrigin(self.series.get_image_origin())
        sitk_img.SetSpacing(self.series.get_pixel_spacing())

        #If DICOM original value has been converted to SUV/SUL, data are calculated as 32bits float
        if(self.unit == UnitPT.RAW): sitk_img = sitk.Cast(sitk_img, sitk.sitkInt16)
        else: sitk_img = sitk.Cast(sitk_img, sitk.sitkFloat64)
        
        return sitk_img

