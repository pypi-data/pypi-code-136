import torch
import math
from . import _hdtorchcuda
from .HDVecGenerators import generateBasisHDVectors
from .HDutil import rotateVec, xor_bipolar, ham_sim, cos_sim, dot_sim
from .HDencoding import  *

__all__ = [
    "HD_classifier",
]

class HD_classifier:
    """Basic HD classifier with generic parameters and learning and prediction funtions
    
    Creates a simple HD classifier model with learning and prediction functions
    
    Args:
        HDParams: an HDParams object that initializes the classifier
    """

    def __init__(self, HDParams):

        self.numFeat      = HDParams["numFeat"]
        self.D            = HDParams["D"]
        self.packed       = HDParams["packed"]
        self.device       = HDParams["device"]
        self.bindingStrat = HDParams["encodingStrat"]
        self.HDFlavor     = HDParams["HDFlavor"]
        self.normType     = 'Norm&Discr'  #has to be 'Norm&Discr' for HD computing
        self.similarityType   = HDParams["similarityType"]
        
        if self.HDFlavor == 'bipol' and self.packed:
            raise TypeError('Model cannot be bipol and packed simultanously')

        # initializes model vectors
        self.modelVectors = torch.zeros((HDParams["numClasses"], self.D), device=self.device)
        if self.packed:
            self.modelVectorsNorm= torch.zeros((HDParams["numClasses"], math.ceil(self.D/32)), device = self.device, dtype=torch.int32)
        else:
            self.modelVectorsNorm= torch.zeros((HDParams["numClasses"], self.D), device = self.device, dtype=torch.int8)
        self.numAddedVecPerClass = torch.zeros(HDParams["numClasses"], device=self.device, dtype=torch.int32)

        #initialized basis vectors for featur IDs and feature values
        self.featureIDs = generateBasisHDVectors(HDParams["IDVecType"],self.numFeat,HDParams["D"],self.packed,self.device)
        self.featureIDs[self.featureIDs==0] = -1 if self.HDFlavor=='bipol' else 0
        
        self.featureLevelValues = generateBasisHDVectors(HDParams["levelVecType"],HDParams["numSegmentationLevels"],HDParams["D"],self.packed,self.device)
        self.featureLevelValues[self.featureLevelValues==0] = -1 if self.HDFlavor=='bipol' else 0
        
    def distanceFunction(self, vA, vB):
        """Calculate similarity between two vectors.

        Potential distances are 'hamming', 'cosing', 'dot', but default one is 'hamming' as HD vectors are usually binary.

        Args:
            vA: First hypervectors to be compared.
            vB: Second hypervectors to be compared.

        Returns:
            Similarity (not distance, despite name) between two vectors.
        """
        if self.similarityType == 'hamming':
            out= ham_sim(vA, vB, self.D, self.HDFlavor, self.packed)
        elif self.similarityType == 'cosine':
            out = cos_sim(vA, vB, self.packed)
        elif self.similarityType == 'dot':
            out = dot_sim(vA, vB, self.packed)
        else:
            print('No valid similarity distance chosen, using Hamming instead')
            out = ham_sim(vA, vB, self.D, self.HDFlavor, self.packed)
        return out


    def givePrediction(self, data, encoded=False):
        """Predict class to which input data belongs.

        If the input data has not been encoded into HD space, project data. Then, compare data with class vectors
        via the selected distance function and return the closest class.

        Args:
            data: Array of data for which to predict class. My be already encoded into HD space or not.
            encoded: Boolean value indicating if data has been already encoded into HD space.
        Returns:
            A vector of predicted classes, and the distance from each classes for each encoded data point.
        """
        #if data was not encoded to HD space then encode is now
        if not encoded:
            (temp, tempPacked) = encode_data_to_vectors(data, self.featureIDs, self.featureLevelValues, self.HDFlavor,  self.packed, self.bindingStrat, self.D)
            temp = temp if not self.packed else tempPacked
            data = temp.view(-1,1,temp.shape[-1])
        else:
            data = data.view(-1,1,data.shape[-1])

        #measure distance from model vectors
        distances = self.distanceFunction(data, self.modelVectorsNorm.unsqueeze(0))

        #find minimum
        minVal = torch.argmin(distances,-1)

        return (minVal.squeeze(), distances.squeeze())
    
    def trainModelVecOnData(self, data, labels):
        """Learn HD class vectors for from training data and labels.
        
        trainModelVecOnData will project each data point into HD space, bind it with the feature hypervector,
        then bundle all bound hypervectors of the same class into a class vector. After learning self.modelVectors,
        self.modelVectorsNorm and self.numAddedVecPerClass are updated.
        
        Args:
            data: Array of data from which to learn class vectors
            labels: Array of labels from which to learn class vectors
        """
        # number of clases
        numLabels = self.modelVectors.shape[0]
    
        # Encode data
        (temp, packedTemp) = encode_data_to_vectors (data, self.featureIDs, self.featureLevelValues, self.HDFlavor, self.packed, self.bindingStrat, self.D)
        temp = temp if not self.packed else packedTemp
        
        #go through all data windows and add them to model vectors
        for l in range(numLabels):
            t = temp[labels==l,:]
            if(t.numel() != 0 and self.packed):
                self.modelVectors[l, :] += _hdtorchcuda.vcount(temp[labels==l],self.D) #temp[labels==l].sum(0)
            elif not self.packed:
                self.modelVectors[l] += temp[labels==l].sum(0)
            self.numAddedVecPerClass[l] +=  (labels==l).sum().cpu() #count number of vectors added to each subclass
    
        # normalize model vectors to be binary (or bipolar) again
        if self.HDFlavor == 'binary' and self.packed:
                _hdtorchcuda.pack(self.modelVectors > (self.numAddedVecPerClass.unsqueeze(1)>>1),self.modelVectorsNorm)
        elif self.HDFlavor == 'binary' and not self.packed:
                self.modelVectorsNorm = self.modelVectors > (self.numAddedVecPerClass.unsqueeze(1)>>1)
        elif self.HDFlavor == 'bipol':
            self.modelVectorsNorm = torch.where(self.modelVectors>0,1,-1)
