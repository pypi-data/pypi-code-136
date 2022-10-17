import numpy as np

class Instance_RTDose_pydicom(): 
    """A class to represent a RTDose Dicom File

    Args:
        Instance ([type]): [description]
    """

    def get_image_nparray(self) -> np.ndarray:
        """get 3d matrix of rt dose, no rescale slope and intercept for RTDose

        Returns:
            [np.ndarray]: [return the 3D array from a RTDose file, shape (z,y,x) ]
        """
        return self.dicom_pixel


    def wrap_DHVSequence_in_dict(self) -> dict: 
        """wrap in dictionnary DVH Sequence of each ROI 
        dict = { (roi) 1 : {'ReferencedROINumber' : value
                                'DVHType' : value
                                'DoseUnits' : value
                                'DVHDoseScaling' : value
                                'DVHVolumeUnits':  value
                                'DVHNumberOfBins' : value
                                'DVHMinimumDose' : value
                                'DVHMaximumDose' : value
                                'DVHMeanDose' : value
                                'DVHData' : value},
                (roi) 2 : {'ReferencedROINumber' : value
                                'DVHType' : value
                                'DoseUnits' : value
                                'DVHDoseScaling' : value
                                'DVHVolumeUnits':  value
                                'DVHNumberOfBins' : value
                                'DVHMinimumDose' : value
                                'DVHMaximumDose' : value
                                'DVHMeanDose' : value
                                'DVHData' : value}, ...}

        Returns:
            [dict]: [return a dictionnary, with, for each ROI, DVHSequence in the RTDose file]
        """
        dictionnary = {}
        for i in range(len(self.dicomData.DVHSequence)) : 
            referenced_roi = int(self.dicomData.DVHSequence[i].DVHReferencedROISequence[0].ReferencedROINumber)
            dataset = {}
            dataset['ReferencedROINumber'] = referenced_roi
            dataset['DVHType'] = self.dicomData.DVHSequence[i].DVHType
            dataset['DoseUnits'] = self.dicomData.DVHSequence[i].DoseUnits  
            dataset['DVHDoseScaling'] = self.dicomData.DVHSequence[i].DVHDoseScaling 
            dataset['DVHVolumeUnits'] = self.dicomData.DVHSequence[i].DVHVolumeUnits 
            dataset['DVHNumberOfBins'] = self.dicomData.DVHSequence[i].DVHNumberOfBins 
            dataset['DVHMinimumDose'] = self.dicomData.DVHSequence[i].DVHMinimumDose
            dataset['DVHMaximumDose'] = self.dicomData.DVHSequence[i].DVHMaximumDose
            dataset['DVHMeanDose'] = self.dicomData.DVHSequence[i].DVHMeanDose
            dataset['DVHData'] = self.dicomData.DVHSequence[i].DVHData
            dictionnary[referenced_roi] = dataset 

        return dictionnary
