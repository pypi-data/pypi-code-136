import json
import pydicom
import numpy
from pydicom.dicomdir import DicomDir
from dicom_cnn.instance.dicom_enums import Modalities
from dicom_cnn.instance.dicom_instance import DicomInstance, DicomInstancePT
from dicom_cnn.reader.abstract_dicom_reader import AbstractDicomReader

class DicomInstancePyDicomFactory(AbstractDicomReader):

    def read(self, readPixel: bool) -> DicomInstance:

        dicom_data = pydicom.read_file(
            self.data_location, stop_before_pixels=(not readPixel), force=True)
        if isinstance(dicom_data, DicomDir): raise('DICOMDIR File')

        dicom_metadata = json.loads(dicom_data.to_json())

        pixel_array = None

        if (readPixel):
            pixel_array = dicom_data.pixel_array
        
        modality = dicom_metadata.get('00080060', {}).get('Value', [None])[0]
        if(modality == Modalities.PT.value):
            dicom_instance_reader = DicomInstancePyDicomReaderPT(dicom_metadata, pixel_array)
            return dicom_instance_reader.get_instance()
        else : 
            dicom_instance_reader = DicomInstancePyDicomReader(dicom_metadata, pixel_array )
            return dicom_instance_reader.get_instance()

class DicomInstancePyDicomReader():

    dicom_metadata :dict
    pixels :numpy.array
    dicom_instance :DicomInstance

    def __init__(self, dicom_metadata :dict, pixels :numpy.array) -> None:
        self.dicom_metadata = dicom_metadata
        self.pixels = pixels
        self.dicom_instance = DicomInstance()
        pass
    
    def get_instance(self) -> DicomInstance : 
        self.dicom_instance.study_date = DicomInstance.parse_dicom_date(self.dicom_metadata.get('00080020', {}).get('Value', [None])[0])
        self.dicom_instance.study_time = DicomInstance.parse_dicom_time(self.dicom_metadata.get('00080030', {}).get('Value', [None])[0])
        self.dicom_instance.study_description = self.dicom_metadata.get('00081030', {}).get('Value', [None])[0]
        self.dicom_instance.series_description = self.dicom_metadata.get('0008103E', {}).get('Value', [None])[0]
        self.dicom_instance.series_number = self.dicom_metadata.get('00200011', {}).get('Value', [None])[0]
        self.dicom_instance.patient_name = self.dicom_metadata.get('00100010', {}).get('Value', [None])[0]['Alphabetic']
        self.dicom_instance.patient_id = self.dicom_metadata.get('00100020', {}).get('Value', [None])[0]
        self.dicom_instance.patient_birthdate = None if (self.dicom_metadata.get('00100030', {}).get('Value',[None])[0] == None) else DicomInstance.parse_dicom_date(self.dicom_metadata['00100030']['Value'][0])
        self.dicom_instance.patient_sex = None if (self.dicom_metadata.get('00100040', {}).get('Value', [None])[0] == 'O' or self.dicom_metadata.get('00100040', {}).get('Value', [None])[0] == None) else self.dicom_metadata['00100040']['Value'][0]
        self.dicom_instance.patient_weight = self.dicom_metadata.get('00101030', {}).get('Value', [None])[0]
        self.dicom_instance.patient_size = self.dicom_metadata.get('00101020', {}).get('Value',[None])[0]
        self.dicom_instance.study_instance_uid = self.dicom_metadata.get('0020000D', {}).get('Value', [None])[0]
        self.dicom_instance.series_date = None if (self.dicom_metadata.get('00080021', {}).get('Value', [None])[0] == None) else DicomInstance.parse_dicom_date(self.dicom_metadata['00080021']['Value'][0])
        self.dicom_instance.series_time = None if (self.dicom_metadata.get('00080031', {}).get('Value', [None])[0] == None) else DicomInstance.parse_dicom_time(self.dicom_metadata['00080031']['Value'][0])
        self.dicom_instance.sop_instance_uid = self.dicom_metadata.get('00080018', {}).get('Value', [None])[0]
        self.dicom_instance.frame_of_reference_uid = self.dicom_metadata.get('00200052', {}).get('Value', [None])[0]
        self.dicom_instance.modality = self.dicom_metadata.get('00080060', {}).get('Value', [None])[0]
        self.dicom_instance.slice_thickness = self.dicom_metadata.get('00180050', {}).get('Value', [None])[0]
        self.dicom_instance.protocol_name = self.dicom_metadata.get('00181030', {}).get('Value',[None])[0]
        self.dicom_instance.acquisition_date = None if (self.dicom_metadata.get('00080022', {}).get('Value', [None])[0] == None) else DicomInstance.parse_dicom_date(self.dicom_metadata['00080022']['Value'][0])
        self.dicom_instance.acquisition_time = None if (self.dicom_metadata.get('00080032', {}).get('Value', [None])[0] == None) else DicomInstance.parse_dicom_time(self.dicom_metadata['00080032']['Value'][0])
        self.dicom_instance.columns = self.dicom_metadata.get('00280011', {}).get('Value',[None])[0]
        self.dicom_instance.rows = self.dicom_metadata.get('00280010', {}).get('Value',[None])[0]
        self.dicom_instance.content_date = None if (self.dicom_metadata.get('00080023', {}).get('Value', [None])[0] == None) else  DicomInstance.parse_dicom_date(self.dicom_metadata['00080023']['Value'][0])
        self.dicom_instance.accession_number = self.dicom_metadata.get('00080050', {}).get('Value',[None])[0]
        self.dicom_instance.sop_class_uid = self.dicom_metadata.get('00080016', {}).get('Value',[None])[0]
        self.dicom_instance.series_instance_uid = self.dicom_metadata.get('0020000E', {}).get('Value',[None])[0]
        self.dicom_instance.pixel_spacing = self.dicom_metadata.get('00280030', {}).get('Value',[None])
        self.dicom_instance.image_position = self.dicom_metadata.get('00200032', {}).get('Value',[None])
        self.dicom_instance.image_orientation = self.dicom_metadata.get('00200037', {}).get('Value',[None])
        self.dicom_instance.rescale_slope = self.dicom_metadata.get('00281053', {}).get('Value',[None])[0]
        self.dicom_instance.rescale_intercept = self.dicom_metadata.get('00281052', {}).get('Value',[None])[0]
        self.dicom_instance.manufacturer = self.dicom_metadata.get('00080070', {}).get('Value',[None])[0]
        self.dicom_instance.pixels = self.pixels
        return self.dicom_instance

class DicomInstancePyDicomReaderPT(DicomInstancePyDicomReader):

    dicom_instance :DicomInstancePT

    def __init__(self, dicom_metadata :dict, pixels :numpy.array) -> None:
        self.dicom_metadata = dicom_metadata
        self.pixels = pixels
        self.dicom_instance = DicomInstancePT()
        pass

    def get_instance(self) -> DicomInstancePT : 
        super().get_instance()

        radiophramaceutical_dict = self.dicom_metadata['00540016']['Value'][0]
        self.dicom_instance.radiopharmaceutical_start_time = None if (radiophramaceutical_dict.get('00181072', {}).get('Value',[None])[0] == None) else DicomInstance.parse_dicom_time(radiophramaceutical_dict['00181072']['Value'][0])
        self.dicom_instance.radiopharmaceutical_start_datetime = None if (radiophramaceutical_dict.get('00181078', {}).get('Value',[None])[0] == None) else DicomInstance.parse_dicom_datetime(radiophramaceutical_dict['00181078']['Value'][0])
        self.dicom_instance.radiopharmaceutical_stop_time = None if (radiophramaceutical_dict.get('00181073', {}).get('Value',[None])[0] == None) else DicomInstance.parse_dicom_time(radiophramaceutical_dict['00181073']['Value'][0])
        self.dicom_instance.radionuclide_totale_dose = radiophramaceutical_dict.get('00181074', {}).get('Value', [None])[0]
        self.dicom_instance.radionuclide_half_life = radiophramaceutical_dict.get('00181075', {}).get('Value', [None])[0]
        self.dicom_instance.correction_image = self.dicom_metadata.get('00280051', {}).get('Value', [None])
        self.dicom_instance.philips_suv_factor = self.dicom_metadata.get('70531000', {}).get('Value', [None])[0]
        self.dicom_instance.philips_bqml_factor = self.dicom_metadata.get('70531009', {}).get('Value', [None])[0]
        self.dicom_instance.units = self.dicom_metadata.get('00541001', {}).get('Value', [None])[0]
        self.dicom_instance.decay_correction = self.dicom_metadata.get('00541102', {}).get('Value', [None])[0]
        self.dicom_instance.pixels = self.pixels
        return self.dicom_instance