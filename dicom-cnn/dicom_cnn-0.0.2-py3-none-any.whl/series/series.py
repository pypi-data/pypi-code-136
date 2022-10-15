import json
from dicom_cnn.instance.dicom_instance import DicomInstance
from typing import List
import numpy as np
from dicom_cnn.writer.series_exporter import SeriesExporter
class Series():

    instances :List[DicomInstance] = []
    
    def __init__(self, instances :List[DicomInstance]):
        self.instances = instances
        self.instances.sort(key = lambda instance_array:int(instance_array.get_image_position()[2]))
        if(not self.is_instances_belongs_same_series()) : raise "Instances does not belongs to the same series"

    def is_instances_belongs_same_series(self)-> bool:
        series_instance_uids = []
        for instance in self.instances : 
            series_instance_uid = instance.get_series_instance_uid()
            series_instance_uids.append(series_instance_uid)
        if len(set(series_instance_uids)) == 1: return True
        else: return False
    
    def get_series_instance_uid(self) -> str:
        return self.instances[0].get_series_instance_uid()

    def get_study_instance_uid(self) -> str:
        return self.instances[0].get_study_instance_uid()
        
    def get_number_of_instance(self) -> int:
        return len(self.instances)

    def get_numpy_array(self) -> np.ndarray:
        pixel_data = [instance.get_image_nparray() for instance in self.instances]
        np_array = np.stack(pixel_data, axis=0)
        return np_array

    def get_all_sop_instance_uid(self)-> List[str]:
        sops = []
        for instance in self.instances : 
            sops.append(instance.get_sop_instance_uid())
        return sops
    
    def get_size_matrix(self) -> tuple :
        rows = self.instances[0].get_rows()
        columns = self.instances[0].get_columns()
        slices = self.get_number_of_instance()
        return (rows, columns, slices)
            
    def is_z_spacing_constant(self) -> bool : 
        spacings = self.get_image_spacings()
        initial_z_spacing = round(abs(spacings[0] - spacings[1]), 1)
        for i in range(1,len(spacings)):
            z_spacing = round(abs(spacings[i - 1] - spacings[i]), 1)
            if z_spacing < initial_z_spacing - float(0.1) or z_spacing > initial_z_spacing + float(0.1) :
                return False

        return True
    
    def get_series_direction(self) -> tuple :
        orientation = self.instances[0].get_image_orientation()
        return (orientation[0], orientation[1], orientation[2], orientation[3], orientation[4], orientation[5], 0.0, 0.0, 1.0)

    def get_image_origin(self) -> tuple:
        image_origin = self.instances[0].get_image_position()
        return (image_origin[0], image_origin[1], image_origin[2])

    def get_image_spacings(self) -> List[float]:
        spacings = []
        initial_z_spacing = self.instances[0].get_pixel_spacing()
        z_positions = [ instance.get_image_position()[2] for instance in self.instances]
        initial_z_spacing = np.round(abs(z_positions[0] - z_positions[1]), 1)
        spacings.append(initial_z_spacing)
        for i in range(1,len(z_positions)):
            z_spacing = np.round(abs(z_positions[i - 1] - z_positions[i]), 1)
            spacings.append(z_spacing)  
        return spacings

    def get_z_spacing(self) -> list:
        return np.mean(self.get_image_spacings())

    def get_pixel_spacing(self) -> tuple:
        pixel_spacing = self.instances[0].get_pixel_spacing()
        return (pixel_spacing[0], pixel_spacing[1], self.get_z_spacing())

    def get_average_image_spacing (self) -> str:
        return np.mean(self.get_image_spacings())

    def get_exporter(self) -> SeriesExporter :
        return SeriesExporter(self)

    def toJSON(self):
        first_instance = self.instances[0]
        return json.dumps({
            'PatientID' : first_instance.get_patient_id(),
            'PatientName' : first_instance.get_patient_name(),
            'PatientBirthDate' : first_instance.get_patient_birthdate().strftime("%mMd%Y"),
            'PatientSex' : first_instance.get_patient_sex(),
            "AccessionNumber" : first_instance.get_accession_number(),
            "StudyDate" : first_instance.get_study_date().strftime("%mMd%Y"),
            "StudyTime" : first_instance.get_study_time().strftime("%H:%M:%S"),
            "StudyDescription" : first_instance.get_study_description(),
            "StudyInstanceUID" : first_instance.get_study_instance_uid(),
            "Manufacturer" :  first_instance.get_manufacturer(),
            "Modality" :  first_instance.get_modality(),
            "SeriesDate" : first_instance.get_series_date().strftime("%mMd%Y"),
            "SeriesTime" : first_instance.get_series_time().strftime("%H:%M:%S"),
            "SeriesDescription" : first_instance.get_series_description(),
            "SeriesInstanceUID" : first_instance.get_series_instance_uid(),
            "SeriesNumber" : first_instance.get_series_number(),
            "StationName" : "SYMBIA"
        })
