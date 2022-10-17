from __future__ import annotations
import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dicom_cnn.series.series import Series

import SimpleITK as sitk
import numpy as np

class SeriesExporter():

    series: Series = None

    def __init__(self, series: Series):
        self.series = series

    def get_array(self) -> np.ndarray:
        return self.series.get_numpy_array()

    def get_sitk_image(self) -> sitk.Image:
        sitk_img = sitk.GetImageFromArray(self.get_array())
        sitk_img.SetDirection(self.series.get_series_direction())
        sitk_img.SetOrigin(self.series.get_image_origin())
        sitk_img.SetSpacing(self.series.get_pixel_spacing())

        sitk_img = sitk.Cast(sitk_img, sitk.sitkInt16)
        return sitk_img

    def write_image_to_nifti(self, file_path, filename, compress = False) -> None:
        extension = '.nii'
        if(compress): extension = '.nii.gz'
        path = os.path.join(file_path, filename + extension)
        image_sitk = self.get_sitk_image()
        sitk.WriteImage(image_sitk, path)
