from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dicom_cnn.reader.nifti_reader import NiftiReader 
    from dicom_cnn.writer.MaskToNifti import MaskBuilder
    
from radiomics.featureextractor import RadiomicsFeatureExtractor 
import SimpleITK as sitk 
from itertools import combinations
import numpy as np

class Radiomics():
    
    def __init__(self, mask: NiftiReader):
        self.mask= mask  
        
    def set_tep (self):
        '''
        Arguments
            size : pet image size
        '''
        pet_arr = np.random.randint(10, size=(self.mask.get_size())).transpose()
        pet_img = sitk.GetImageFromArray(pet_arr)
        pet_img.SetOrigin(self.mask.get_origin())
        pet_img.SetDirection(self.mask.get_direction())
        pet_img.SetSpacing(self.mask.get_spacing())
        return pet_img


    def get_center_of_mass (self) -> list :
        list_center = []
        number_of_roi = self.mask.get_array().shape[0]
        for i in  range(0, number_of_roi) : 
            center= self.roi_center(i)  
            list_center.append(center)
        return center  

    def roi_center (self, i) :
        center=[] 
        extractor = RadiomicsFeatureExtractor()
        results = extractor.execute(self.set_tep(), ((self.mask_path)), label =i)
        x, y, z = results['diagnostics_Mask-original_CenterOfMass']
        center.append([x,y,z])
        return center 
            
    def distance(self, coord_A:list, coord_B:list) -> float:        
        return np.sqrt((coord_A[0]-coord_B[0])**2 + (coord_A[1]-coord_B[1])**2 + (coord_A[2]-coord_B[2])**2)
     
    def calcul_distance_max(self) -> float:
         center = self.get_center_of_mass()
         if len(center) == 1 : #only 1 roi
             return 0
         else : 
             comb = combinations(center, 2)
             comb_liste = list(comb)
             liste_distance = []
             for combinaison in comb_liste : 
                 point_A = combinaison[0]
                 point_B = combinaison[1]
                 liste_distance.append(self.distance(point_A, point_B))
             maxi = np.max(liste_distance)
             return np.round(maxi,2)
     
    def calculate(self)  :
        extract= RadiomicsFeatureExtractor()
        radiomics= extract.execute(self.mask, self.set_tep)
        return radiomics
        
        
        
