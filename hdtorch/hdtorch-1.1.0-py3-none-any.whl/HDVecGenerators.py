'''
Created on May 11, 2022

@author: wsimon
'''
import os, math
import torch
from . import _hdtorchcuda
import numpy as np

__all__ = [
    "generateBasisVectors_Random",
    "generateBasisVectors_Sandwich",
    "generateBasisVectors_ScaleRand",
    "generateBasisVectors_ScaleNoRand",
    "generateBasisVectors_ScaleWithRadius",
    "generateBasisHDVectors"
]
    

def generateBasisVectors_Random(numVectors, HDdim):
    """Generating basis hypervectors using 'random' initialization.
    
    Generating numVectors vectors using indpendant and random initialization.
    
    Args:
        numVectors: Number of vectors to be generated.
        HDdim: Dimensionsionality of hypervectors.
        
    
    Returns:
        Generated numVectors hypervectors using 'random' initialization.
        
    """

    return torch.randint(0,2,(numVectors, HDdim)).to(torch.int8)

def generateBasisVectors_Sandwich(numVectors, HDdim):
    """Generating basis hypervectors using 'sandwich' initialization.
    
    Generating numVectors vectors using so called 'sandwich' initialization. This means that every two neighbouring vectors have half of the vector the same, but the rest of the vector is random. In this vector are only similar (50%) with neighbouring vectors but not with the ones further.
    
    Args:
        numVectors: Number of vectors to be generated.
        HDdim:  Dimensionsionality of hypervectors.
        
    
    Returns:
        Generated numVectors hypervectors using 'sandwich' initialization.
        
    """

    vect_matrix = torch.zeros(numVectors, HDdim).to(torch.int8)
    #randomly generate every second vector
    for i in range(numVectors):
        if i % 2 == 0:
            vect_matrix[i, :] = torch.randint(0,2,(HDdim,))
    #the rest of the vectors create by using parts of previous and next vector
    for i in range(numVectors - 1):
        if i % 2 == 1:
            vect_matrix[i, 0:int(HDdim / 2)] = vect_matrix[i - 1, 0:int(HDdim / 2)]
            vect_matrix[i, int(HDdim / 2):HDdim] = vect_matrix[i + 1, int(HDdim / 2):HDdim]
    vect_matrix[numVectors - 1, 0:int(HDdim / 2)] = vect_matrix[numVectors - 2, 0:int(HDdim / 2)]
    vect_matrix[numVectors - 1, int(HDdim / 2):HDdim] = torch.randn(int(HDdim / 2))
    vect_matrix = vect_matrix>0 
    return vect_matrix

def generateBasisVectors_ScaleRand(numVectors, HDdim, scaleFact):
    """Generating basis hypervectors using 'scale' initialization with randomly chosen flipped bits.
    
    Generating numVectors vectors using so called 'scale' or 'level' initialization, so that distance in values vectors will represent is mapped to similarity between those vectors.   
    Every subsequent vector is created by randomly flipping HDdim/(numVectors*scaleFact) elements. 
    
    
    Args:
        numVectors: Number of vectors to be generated.
        HDdim:  Dimensionsionality of hypervectors.
        scaleFact: Determines how many vectors is changed between neighbouring vectors, if 1 then every time HDdim/numVectors bits are flipped
    
    Returns:
        Generated numVectors hypervectors using 'scale' initialization.
        
    """
    
    vect_matrix = torch.zeros(numVectors, HDdim).to(torch.int8)
        
    #calculate how many bits will be flipped for each next vector
    numValToFlip=int(np.floor(HDdim/(scaleFact*numVectors)))

    #generate first one as random
    vect_matrix[0, :] = torch.randint(0,2,(HDdim,))
    #iteratively the further they are flip more bits
    for i in range(1,numVectors):
        vect_matrix[i, :]=vect_matrix[i-1, :]
        #choose random positions to flip
        # posToFlip=random.sample(range(1,HDdim),numValToFlip)
        posToFlip = torch.randint(1,HDdim, (numValToFlip,))
        vect_matrix[i,posToFlip] = 1-vect_matrix[i,posToFlip]
    return vect_matrix

    

def generateBasisVectors_ScaleNoRand(numVectors, HDdim, scaleFact):
    """Generating basis hypervectors using 'scale' initialization with calefully chosen flipped bits.
    
    Generating numVectors vectors using so called 'scale' or 'level' initialization, so that distance in values vectors will represent is mapped to similarity between those vectors.   
    Every subsequent vector is created by flipping next HDdim/(numVectors*scaleFact) elements, e.g. from i-th to i+d bit and not randomly choosing bits to flip.
    
    
    Args:
        numVectors: Number of vectors to be generated.
        HDdim:  Dimensionsionality of hypervectors.
        scaleFact: Determines how many vectors is changed between neighbouring vectors, if 1 then every time HDdim/numVectors bits are flipped
    
    Returns:
        Generated numVectors hypervectors using 'scale' initialization.
        
    """
    #calculate how many bits will be flipped for each next vector
    numValToFlip = math.floor(HDdim / (scaleFact * numVectors))

    # initialize vectors
    vect_matrix = torch.randint(0,2,(numVectors, HDdim)).to(torch.int8)
    
    # iteratively  flip more bits the further they are
    for i in range(1, numVectors):
        vect_matrix[i] = vect_matrix[0]
        vect_matrix[i, 0: i * numValToFlip] = 1 - vect_matrix[0, 0: i * numValToFlip]
    
    return vect_matrix
    
def generateBasisVectors_ScaleWithRadius(numVectors, HDdim, radius):
    """Generating basis hypervectors using radius limited 'scale' initialization.
    
    Generating numVectors vectors using so called 'scale' or 'level' initialization, but only for vectors that are closer then 'radius' distance. This way vectors closer than 'radius' are similar proportionally to their distance (the furthr they are less similar are vectors), but after 'radius' they are orthogonal. 
    This is useful in case we need to generate many vectors, so that they wouldn't be all too similar (because num bits to flip between neighbouring ones would be too small percentage).
    
    
    Args:
        numVectors: Number of vectors to be generated.
        HDdim:  Dimensionsionality of hypervectors.
        radius: After what distance vectors are not longer similar proportionally to distance, but orthogonal
    
    Returns:
        Generated numVectors hypervectors using 'scale' with 'radius' initialization.
        
    """

    #calculate number of completly random vectors - every radius-th vector, called axes vectors
    numAxes=int(math.ceil(numVectors /radius)+1)
    #calculate how many bits to flip for those that are in 'radius' distance and generated using 'scale' approach
    numValToFlip=int(math.floor(HDdim/radius))
    #randomly generate every radius-th vector
    axesVecs = torch.randint(0, 2, (numAxes, HDdim)).to(torch.int8)
    vect_matrix = torch.zeros(numVectors, HDdim).to(torch.int8)
    #screate using 'scale' approach vctors between those randomly generated 
    for i in range(0,numVectors):
        modi=i%radius
        if ( modi ==0):
            vect_matrix[i, :]=axesVecs[int(i/radius),:]
        else:
            vect_matrix[i, 0:HDdim-modi*numValToFlip]= axesVecs[int(i/radius),0:HDdim-modi*numValToFlip] #first part is from prvious axes vec
            vect_matrix[i, HDdim-modi * numValToFlip:] = axesVecs[int(i / radius)+1, HDdim-modi * numValToFlip:] #second part is from next axes vec
    return vect_matrix
    
def generateBasisHDVectors(initType, numVec, HDDim, packed, device):
    """Generating basis hypervectors that will be used for encoding.
    
    Generating 'numVectors' 'HDDim'-dimensional basis hypervectors. Several options to initialize them are possible: 'random', 'sandwich', 
    'ScaleRand', 'ScaleNoRand' and 'ScaleWithRadius'. 
    
    
    Args:
        initType: Method to use to generate hypervectors.
        numVec: Number of vectors to generate.
        HDdim:  Dimensionsionality of hypervectors.
        packed: Weather to return vectors in original or 'packed' form. 
        device: The desired device of returned tensor. 
    
    Returns:
        Generated numVectors hypervectors using 'scale' with 'radius' initialization.
        
    """
    if initType == 'sandwich':
        hdVec = generateBasisVectors_Sandwich(numVec, HDDim)
    elif initType == 'random':
        hdVec = generateBasisVectors_Random(numVec, HDDim)
    elif "scaleNoRand" in initType:
        hdVec = generateBasisVectors_ScaleNoRand(numVec, HDDim, int(initType[11:]))
    elif "scaleRand" in initType:
        hdVec = generateBasisVectors_ScaleRand(numVec, HDDim, int(initType[9:]))
    elif "scaleWithRadius" in initType:
        hdVec = generateBasisVectors_ScaleWithRadius(numVec, HDDim, int(initType[15:]))
    else:
        raise TypeError(f'Unrecognized initType {initType}')
        
    if not packed:
        return hdVec.to(device).to(torch.int8)
    else:
        hdVecPacked = _hdtorchcuda.pack(hdVec.to(device).to(torch.int8))
        return hdVecPacked

