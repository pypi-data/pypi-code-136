import numpy
from dicom_cnn.instance.dicom_enums import Modalities
from dicom_cnn.instance.dicom_instance import DicomInstance, DicomInstancePT
from dicom_cnn.reader.abstract_dicom_reader import AbstractDicomReader
from dicom_cnn.orthanc.apis import OrthancApis


class DicomInstanceOrthancFactory(AbstractDicomReader):

    orthanc_apis: OrthancApis

    def __init__(self) -> None:
        super().__init__()
        self.orthanc_apis = OrthancApis()
    
    def set_orthanc_server(self, url : str):
        self.orthanc_apis.set_orthanc_server(url)
    
    def set_orthanc_port(self, port :int):
        self.orthanc_apis.set_orthanc_port(port)

    def read(self, readPixel: bool) -> DicomInstance:

        dicom_metadata = self.orthanc_apis.get_instance_metadata(
            self.data_location)
        pixels = None
        if (readPixel):
            pixels = self.orthanc_apis.get_instance_numpy(self.data_location)

        modality = dicom_metadata.get('0008,0060', {}).get('Value', None)
        if (modality == Modalities.PT.value):
            return DicomInstancePyDicomReaderPT(dicom_metadata, pixels).get_instance()
        else:
            return DicomInstancePyDicomReader(dicom_metadata, pixels).get_instance()


class DicomInstancePyDicomReader():

    dicom_metadata: dict
    pixels: numpy.ndarray
    dicom_instance: DicomInstance

    def __init__(self, dicom_metadata: dict, pixels: numpy.ndarray) -> None:
        self.dicom_metadata = dicom_metadata
        self.pixels = pixels
        self.dicom_instance = DicomInstance()
        pass

    def get_instance(self) -> DicomInstance:
        self.dicom_instance.study_date = DicomInstance.parse_dicom_date(
            self.dicom_metadata.get('0008,0020', {}).get('Value', None))
        self.dicom_instance.study_time = DicomInstance.parse_dicom_time(
            self.dicom_metadata.get('0008,0030', {}).get('Value', None))
        self.dicom_instance.study_description = self.dicom_metadata.get(
            '0008,1030', {}).get('Value', None)
        self.dicom_instance.series_description = self.dicom_metadata.get(
            '0008,103e', {}).get('Value', None)
        self.dicom_instance.series_number = self.dicom_metadata.get(
            '0020,0011', {}).get('Value', None)
        self.dicom_instance.patient_name = self.dicom_metadata.get(
            '0010,0010', {}).get('Value', None)
        self.dicom_instance.patient_id = self.dicom_metadata.get(
            '0010,0020', {}).get('Value', None)
        self.dicom_instance.patient_birthdate = None if (self.dicom_metadata.get('0010,0030', {}).get(
            'Value', None) == None) else DicomInstance.parse_dicom_date(self.dicom_metadata['0010,0030']['Value'])
        self.dicom_instance.patient_sex = None if (self.dicom_metadata.get('0010,0040', {}).get('Value', None) == 'O' or self.dicom_metadata.get(
            '0010,0040', {}).get('Value', None) == None) else self.dicom_metadata['0010,0040']['Value']
        self.dicom_instance.patient_weight = None if self.dicom_metadata.get('0010,1030', {}).get('Value', None) == None else int(self.dicom_metadata['0010,1030']['Value'])
        self.dicom_instance.patient_size = None if self.dicom_metadata.get('0010,1020', {}).get('Value', None) == None else float(self.dicom_metadata['0010,1030']['Value'])
        self.dicom_instance.study_instance_uid = self.dicom_metadata.get('0020,000d', {}).get('Value', None)
        self.dicom_instance.series_date = None if (self.dicom_metadata.get('0008,0021', {}).get('Value', None) == None) else DicomInstance.parse_dicom_date(self.dicom_metadata['0008,0021']['Value'])
        self.dicom_instance.series_time = None if (self.dicom_metadata.get('0008,0031', {}).get('Value', None) == None) else DicomInstance.parse_dicom_time(self.dicom_metadata['0008,0031']['Value'])
        self.dicom_instance.sop_instance_uid = self.dicom_metadata.get('0008,0018', {}).get('Value', None)
        self.dicom_instance.frame_of_reference_uid = self.dicom_metadata.get('0020,0052', {}).get('Value', None)
        self.dicom_instance.modality = self.dicom_metadata.get('0008,0060', {}).get('Value', None)
        self.dicom_instance.slice_thickness = None if self.dicom_metadata.get('0018,0050', {}).get('Value', None) == None else float(self.dicom_metadata['0018,0050']['Value'])
        self.dicom_instance.protocol_name = self.dicom_metadata.get('0018,1030', {}).get('Value', [None])
        self.dicom_instance.acquisition_date = None if (self.dicom_metadata.get('0008,0022', {}).get(
            'Value', None) == None) else DicomInstance.parse_dicom_date(self.dicom_metadata['0008,0022']['Value'])
        self.dicom_instance.acquisition_time = None if (self.dicom_metadata.get('0008,0032', {}).get(
            'Value', None) == None) else DicomInstance.parse_dicom_time(self.dicom_metadata['0008,0032']['Value'])
        self.dicom_instance.columns = None if self.dicom_metadata.get('0028,0011', {}).get('Value', None) == None else int(self.dicom_metadata['0028,0011']['Value'])
        self.dicom_instance.rows = None if self.dicom_metadata.get('0028,0010', {}).get('Value', None) == None else int(self.dicom_metadata['0028,0010']['Value'])
        self.dicom_instance.content_date = None if (self.dicom_metadata.get('0008,0023', {}).get('Value', None) == None) else DicomInstance.parse_dicom_date(self.dicom_metadata['0008,0023']['Value'])
        self.dicom_instance.accession_number = self.dicom_metadata.get('0008,0050', {}).get('Value', None)
        self.dicom_instance.sop_class_uid = self.dicom_metadata.get('0008,0016', {}).get('Value', None)
        self.dicom_instance.series_instance_uid = self.dicom_metadata.get('0020,000e', {}).get('Value', None)
        self.dicom_instance.pixel_spacing = self.__get_pixel_spacing()
        self.dicom_instance.image_position = self.__get_image_position()
        self.dicom_instance.image_orientation = self.__get_image_orientation()
        self.dicom_instance.rescale_slope = None if self.dicom_metadata.get('0028,1053', {}).get('Value', None) == None else float(self.dicom_metadata['0028,1053']['Value'])
        self.dicom_instance.rescale_intercept = None if self.dicom_metadata.get('0028,1052', {}).get('Value', None) == None else float(self.dicom_metadata['0028,1052']['Value'])
        self.dicom_instance.manufacturer = self.dicom_metadata.get('0008,0070', {}).get('Value', None)
        self.dicom_instance.pixels = self.__get_image_nparray()
        return self.dicom_instance

    def __get_image_orientation(self) -> list:
        image_orientation = self.dicom_metadata.get(
            '0020,0037', {}).get('Value', None)
        if(image_orientation == None): return None
        image_orientation_list = image_orientation.split('\\')
        image_orientation_list_int = [int(i) for i in image_orientation_list]
        return image_orientation_list_int

    def __get_image_position(self) -> list:
        image_position = self.dicom_metadata.get('0020,0032', {}).get('Value', None)
        if(image_position == None): return None
        image_possition_list = image_position.split('\\')
        image_possition_list_float = [float(i) for i in image_possition_list]
        return image_possition_list_float
    
    def __get_pixel_spacing(self) -> list:
        pixel_spacing = self.dicom_metadata.get('0028,0030', {}).get('Value', None)
        if(pixel_spacing == None): return None
        spacing_list = pixel_spacing.split('\\')
        spacing_list_float = [float(i) for i in spacing_list]
        return spacing_list_float
    
    def __get_image_nparray(self) -> numpy.ndarray:
        """get instance image ndarray (taking account rescale slope and intercept)
        Returns:
            [ndarray]: [return instance image ndarray]
        """
        if (type(self.pixels) == numpy.ndarray): return self.pixels[0,:,:,0]
        return None

class DicomInstancePyDicomReaderPT(DicomInstancePyDicomReader):

    dicom_instance: DicomInstancePT

    def __init__(self, dicom_metadata: dict, pixels: numpy.ndarray) -> None:
        super().__init__(dicom_metadata, pixels)
        self.dicom_instance = DicomInstancePT()
        pass

    def get_instance(self) -> DicomInstancePT:
        super().get_instance()

        radiophramaceutical_dict = self.dicom_metadata['0054,0016']['Value'][0]
        self.dicom_instance.radiopharmaceutical_start_time = None if (radiophramaceutical_dict.get('0018,1072', {}).get(
            'Value', None) == None) else DicomInstance.parse_dicom_time(radiophramaceutical_dict['0018,1072']['Value'])
        self.dicom_instance.radiopharmaceutical_start_datetime = None if (radiophramaceutical_dict.get('0018,1078', {}).get(
            'Value', None) == None) else DicomInstance.parse_dicom_datetime(radiophramaceutical_dict['0018,1078']['Value'])
        self.dicom_instance.radiopharmaceutical_stop_time = None if (radiophramaceutical_dict.get('0018,1073', {}).get(
            'Value', None) == None) else DicomInstance.parse_dicom_time(radiophramaceutical_dict['0018,1073']['Value'])
        self.dicom_instance.radionuclide_totale_dose = radiophramaceutical_dict.get('0018,1074', {}).get('Value', None)
        self.dicom_instance.radionuclide_half_life = None if radiophramaceutical_dict.get('0018,1075', {}).get('Value', None) == None else float(radiophramaceutical_dict['0018,1075']['Value'])
        self.dicom_instance.correction_image = self.__get_correction_image()
        self.dicom_instance.philips_suv_factor = self.dicom_metadata.get(
            '7053,1000', {}).get('Value', None)
        self.dicom_instance.philips_bqml_factor = self.dicom_metadata.get(
            '7053,1009', {}).get('Value', None)
        self.dicom_instance.units = self.dicom_metadata.get(
            '0054,1001', {}).get('Value', None)
        self.dicom_instance.decay_correction = self.dicom_metadata.get(
            '0054,1102', {}).get('Value', None)
        return self.dicom_instance

    def __get_correction_image(self) -> list:
        correction_image = self.dicom_metadata.get('0028,0051', {}).get('Value', None)
        if correction_image == None: return None
        return correction_image.split('\\')
