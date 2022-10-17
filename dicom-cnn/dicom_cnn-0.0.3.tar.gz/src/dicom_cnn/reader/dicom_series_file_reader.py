
import os
from dicom_cnn.instance.dicom_instance import DicomInstance
from dicom_cnn.reader.abstract_dicom_reader import AbstractDicomReader
from dicom_cnn.reader.dicom_instance_file_reader import DicomInstancePyDicomFactory
from dicom_cnn.series.series import Series
from dicom_cnn.series.series_pt import SeriesPT
from typing import List


class DicomSeriesFileReader(AbstractDicomReader):

    def read(self, readPixel: bool) -> Series:

        instances : List[DicomInstance] = []
        for name in os.listdir(self.data_location):
            path = os.path.join(self.data_location, name)
            instance_file_reader = DicomInstancePyDicomFactory()
            instance_file_reader.set_location(path)
            instance = instance_file_reader.read(readPixel)
            instances.append(instance)

        series = None
        if(instances[0].get_modality() == "PT"): series = SeriesPT(instances)
        else: series = Series(instances)

        series.get_series_instance_uid()

        return series
