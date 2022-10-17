from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dicom_cnn.writer.series_exporter import SeriesExporter


from SimpleITK import sitk 

class NiftiWriter():

    def __init__(self, path: str) :
        self.path= path

    def set_mask(self):
        sitk_image= sitk.ReadImage(self.path)