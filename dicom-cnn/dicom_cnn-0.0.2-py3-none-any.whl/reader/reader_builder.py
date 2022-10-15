from typing import TypeVar
from dicom_cnn.instance.dicom_instance import DicomInstance
from dicom_cnn.reader.dicom_instance_file_reader import DicomInstancePyDicomFactory

ReaderBuilder = TypeVar('ReaderBuilder')
class ReaderBuilder:

    storage_endpoint :str = None
    location :str = None
    read_pixel :bool = False
    
    def set_storage_endpoint(self, storage_endpoint :str) -> ReaderBuilder :
        self.storage_endpoint = storage_endpoint
        return self
    
    def set_location(self, location :str) -> ReaderBuilder:
        self.location = location
        return self

    def with_pixels(self) -> ReaderBuilder:
        self.read_pixel = True
        return self

    def get_instance(self) -> DicomInstance :

        if(self.storage_endpoint == ReaderBuilder.File) : 
            dicom_file_reader = DicomInstancePyDicomFactory()
            dicom_file_reader.set_location(self.location)
            return dicom_file_reader.read(self.read_pixel)


ReaderBuilder.Orthanc = "Orthanc"
ReaderBuilder.File = "File"