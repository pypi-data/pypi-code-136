from __future__ import annotations
import json
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from dicom_cnn.series.series import Series

class Study:

    study_instance_uid = None
    series: List[Series] = []

    def __init__(self, study_instance_uid):
        self.study_instance_uid = study_instance_uid

    def add_series(self, series: Series):
        series_instance_uid = series.get_series_instance_uid()
        study_instance_uid = series.get_study_instance_uid()

        if(study_instance_uid != self.study_instance_uid):
            raise('Series does not belongs to study instance uid')
        elif (not self.is_known_series_instance_uid(series_instance_uid)):
            raise('already known series')
        else:
            self.series.append(series)

    def is_known_series_instance_uid(self, series_instance_uid: str) -> bool:
        for series in self.series:
            if (series.get_series_instance_uid() == series_instance_uid):
                return True
        return False
    
    def toJSON(self):
        first_series = self.series[0]
        series_details = json.load(first_series.toJSON())
        return json.dumps({
            'PatientID' : series_details['PatientID'],
            'PatientName' : series_details['PatientName'],
            'PatientBirthDate' : series_details['PatientBirthDate'],
            'PatientSex' : series_details['PatientSex'],
            "AccessionNumber" : series_details['AccessionNumber'],
            "StudyDate" : series_details['StudyDate'],
            "StudyTime" : series_details['StudyTime'],
            "StudyDescription" : series_details['StudyDescription'],
            "StudyInstanceUID" : series_details['StudyInstanceUID'],
            'Series' : [ json.load(series.toJSON()) for series in self.series]
    })
