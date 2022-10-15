from abc import ABC, abstractmethod

from dicom_cnn.instance.dicom_instance import DicomInstance


class AbstractDicomReader(ABC):

    data_location: str

    def set_location(self, data_location) -> None:
        self.data_location = data_location

    @abstractmethod
    def read(self, readPixel: bool) -> DicomInstance:
        pass
