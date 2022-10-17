from __future__ import annotations
from typing import List
from typing import TYPE_CHECKING

from dicom_cnn.instance.dicom_instance import DicomInstancePT
if TYPE_CHECKING:
    from dicom_cnn.writer.series_exporter_PT import SeriesExporterPT
    from dicom_cnn.series.series import Series 
import numpy as np
from datetime import datetime
import math
from dicom_cnn.series.series import Series

class SeriesPT(Series):

    instances: List[DicomInstancePT] = []

    def __init__(self, instances: List[DicomInstancePT]):
        super().__init__(instances)

    def get_minimum_acquisition_datetime(self) -> datetime:
        list = []
        for instance in self.instances:
            acquisition_date = instance.get_acquisition_date()
            acquisition_time = instance.get_acquisition_time()
            acquisition_datetime = datetime.combine(
                acquisition_date, acquisition_time)
            list.append(acquisition_datetime)
        return min(list)

    def calculate_suv_factor(self) -> float:
        first_instance = self.instances[0]
        units = first_instance.get_units()
        known_units = ['GML', 'BQML', 'CNTS']
        if units not in known_units:
            raise Exception('Unknown PET Units')

        if units == 'GML': return 1
        elif units == 'CNTS':
            philips_bqml_factor = first_instance.get_philips_bqml_factor()
            philips_suv_factor = first_instance.get_philips_suv_factor()
            if (philips_suv_factor != None):
                return philips_suv_factor
            if (philips_suv_factor == None and philips_bqml_factor == None):
                raise Exception('Missing Philips private Factors')

        patient_weight = first_instance.get_patient_weight()
        if patient_weight == None: raise Exception('Missing patient weight')
        patient_weight = patient_weight * 1000  # kg to g conversion

        serie_time = first_instance.get_series_time().replace(microsecond=0)
        serie_date = first_instance.get_series_date()
        series_datetime = datetime.combine(serie_date, serie_time)

        acquisition_datetime = self.get_minimum_acquisition_datetime().replace(microsecond=0)
        acquisition_date = first_instance.get_acquisition_date()

        decay_correction = first_instance.get_decay_correction()
        radionuclide_half_life = first_instance.get_radionuclide_half_life()
        total_dose = first_instance.get_radionuclide_total_dose()

        if( first_instance.get_radiopharmaceutical_start_datetime() ): radiopharmaceutical_start_date_time = first_instance.get_radiopharmaceutical_start_datetime().replace(microsecond=0)
        else : radiopharmaceutical_start_date_time = datetime.combine( acquisition_date, first_instance.get_radiopharmaceutical_start_time() ).replace(microsecond=0)
        
        if ( total_dose == None or acquisition_datetime == None or radionuclide_half_life == None):
            raise Exception('Missing Radiopharmaceutical data or acqusition datetime')

        # Determine Time reference of image acqusition
        acquisition_hour = series_datetime
        if ( (acquisition_datetime - series_datetime).total_seconds() < 0 and units == 'BQML'):
            acquisition_hour = acquisition_datetime

        # Calculate decay correction
        if decay_correction == 'START':
            delta = (acquisition_hour - radiopharmaceutical_start_date_time)
            delta = delta.total_seconds()
            if (delta < 0): raise("Acqusition time before injection time")
            decay_factor = math.exp(-delta * math.log(2) / radionuclide_half_life)

        # If decay corrected from administration time no decay correction to apply
        elif decay_correction == 'ADMIN': decay_factor = 1
        else: raise Exception('Unknown Decay Correction methode')

        suv_conversion_factor = 1 / \
            ((total_dose * decay_factor) / patient_weight)

        if units == 'CNTS':
            return philips_bqml_factor * suv_conversion_factor
        else:
            return suv_conversion_factor

    def calculate_sul_factor(self) -> float:
        first_instance = self.instances[0]
        patient_size = first_instance.get_patient_size()
        patient_sex = first_instance.get_patient_sex()
        patient_weight = first_instance.get_patient_weight()
        if (patient_sex == None or patient_size == None or patient_weight == None ):
            raise Exception('Missing Height or Weight to calculate SUL')
        bmi = patient_weight / pow(patient_size, 2)
        if patient_sex == 'F':
            return 9270 / (8780 + 244 * bmi)
        elif patient_sex == 'M':
            return 9270 / (6680 + 216 * bmi)
        else:
            raise Exception('Unknown Sex String')

    def is_corrected_attenuation(self) -> bool:
        corrected_image = self.instances[0].get_correction_image()
        if 'ATTN' in corrected_image:
            return True
        else:
            return False

    def get_suv_numpy_array(self) -> np.ndarray:
        raw_numpy = super().get_numpy_array()
        return (raw_numpy * self.calculate_suv_factor())

    def get_sul_numpy_array(self) -> np.ndarray:
        raw_numpy = super().get_numpy_array()
        return (raw_numpy * self.calculate_suv_factor() * self.calculate_sul_factor())

    def get_exporter(self) -> SeriesExporterPT :
        return SeriesExporterPT(self)
