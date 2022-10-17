'''
Created on Apr 8, 2022

@author: wsimon
'''

import torch
from . import _hdtorchcuda


__all__ = [
    "ham_sim",
    "cos_dist",
    "cos_sim",
    "dot_sim",
    "xor_bipolar",
    "rotateVec",
    "normalizeAndDiscretizeData"
]

## HD VECTOR DISTANCE FUNCTIONS
def ham_sim(vA, vB, D, HDFlavor, IsPacked): # ?? replaced ham_dist_arr with ham_sim
    """Calculate relative hamming similarity between two hypervectors

    ham_dist will perform a bitwise xor if the two hypervectors are in binary form, else it will compare their values and
    return 1 if the values are different.

    Args:
        vA: First hypervectors to be compared.
        vB: Second hypervectors to be compared.
        D: Hypervector dimension D (if packed then it should be original dimension not packed).
        HDFlavor: Type of vectors: 'binary' or 'bipolar'.
        IsPacked: 1 of vectors are packed and 0 if not.

    Returns:
        The count of bits in the hypervectors that are different divided by the hypervectors size.
    """
    vC = torch.bitwise_xor(vA,vB) if HDFlavor == 'binary' else vA != vB
    if IsPacked:
        out= _hdtorchcuda.hcount(vC)/int(D/32) # ?? Check if works ok
    else:
        vC.sum(2,dtype=torch.int16)/D
    return  out

def cos_dist(vA, vB, IsPacked):
    """Calculate cosine distance  between two hypervectors

    Args:
        vA: First hypervectors to be compared.
        vB: Second hypervectors to be compared.
        IsPacked: 1 of vectors are packed and 0 if not.

    Returns:
        The cosine distance between the input hypervectors.
    """
    if not IsPacked:  # check if it works ??  - before was written: cos_dist_arr currently only works with unpacked hypervectors.
        vA=vA.unpack
        vB=vB.unpack

    output = torch.dot(vA, vB) / (torch.sqrt(torch.dot(vA,vA)) * torch.sqrt(torch.dot(vB,vB)))
    #outTensor = torch.tensor(1.0-output) #because we use later that if value is 0 then vectors are the same
    return output

def cos_sim(vA, vB, IsPacked): # ?? replace in code cos_dist with cos_sim
    """Calculate cosine similarity between two hypervectors

    Args:
        vA: First hypervectors to be compared.
        vB: Second hypervectors to be compared.
        IsPacked: 1 of vectors are packed and 0 if not.

    Returns:
        The cosine similarity between the input hypervectors.
    """
    # invert value from cos_dist - if vectors are similar (1) cos distance would be 0
    return torch.tensor(1-cos_dist(vA, vB, IsPacked))

def dot_sim(vA, vB, IsPacked):
    """Calculate dot product similarity between two hypervectors

    Args:
        vA: First hypervectors to be compared.
        vB: Second hypervectors to be compared.
        IsPacked: 1 of vectors are packed and 0 if not.
    Returns:
        The dot product similarity between the input hypervectors.
    """
    if not IsPacked:  # check if it works ??  - before was written: cos_dist_arr currently only works with unpacked hypervectors.
        vA=vA.unpack
        vB=vB.unpack

    output = torch.dot(vA, vB)
    return output


## HD BASIC OPERATIONS

def xor_bipolar( vec_a, vec_b):
    """Xor between two bipolar vectors.

    Implements a xor function between two bipolar vectors conisting of values (-1,1).
    Returns a vector containing values (-1,1).

    Args:
        vec_a: Vector of bipolar bytes consisting of values (-1,1).
        vec_b: Vector of bipolar bytes consisting of values (-1,1).


    Returns:
        Vector of bipolar bytes consisting of values (-1,1).
    """
    #vec_c = (torch.sub(vec_a, vec_b) != 0).short()  # 1
    vec_c = torch.sub(vec_a, vec_b)
    vec_c [vec_c!=0]= 1
    vec_c[vec_c == 0] = -1
    return vec_c

def rotateVec(mat,shifts):
    """Rotate vector array by n spaces (row-based).

    Rotates the rows of a 2D-array by the value given in the shifts vector. This is used for binding features
    via feature permutation as described in XXX.

    Args:
        mat: A 2D-array of values of shape [n,m].
        shifts: Vector of shift values of length n, which will be used to shift the mat array.


    Returns:
        The values of the mat array shifted accordingly.
    """
    n_rows, n_cols = mat.shape
    arange1 = torch.arange(n_cols,device=mat.device).view(( 1,n_cols)).repeat((n_rows,1))
    arange2 = (arange1.unsqueeze(0) - shifts.unsqueeze(2)) % n_cols
    return torch.gather(mat.unsqueeze(0).expand(shifts.shape[0],-1,-1),2,arange2)


# DATA PREPARATION FUNCTIONS

def normalizeAndDiscretizeData(data, min_val, max_val, numBins, typeNorm='Norm&Discr'):
    """Normalize or/and discretize data.

    Normalizes the input data to between 0 and 1 based on the passed minimum and maximum values. Then, discretizes the values
    to a given number of bins. Default is to both normalize and discretize.

    Args:
        data: The data tensor to be normalized.
        min_val: The value that will be normalized to 0
        max_val: The value that will be normalized to 1
        numBins: The number of bins in which to discretize data.
        type: Weather only normalization or also discretization is performed. Type has to have words 'norm', 'Norm', 'discr' or 'Discr' in name. Default is to both normalize and discretize.

    Returns:
        The normalized pr/and discretized data.
    """
    #normalize and discretize train adn test data
    dataNorm = (data - min_val) / (max_val - min_val)

    if ('Norm' in typeNorm) | ('norm' in typeNorm):
        out= dataNorm
    if ('Discr' in typeNorm) | ('discr' in typeNorm):
        dataDisc = torch.floor((numBins - 1) * dataNorm)
        #check for outliers
        dataDisc[dataDisc >= numBins] = numBins - 1
        dataDisc[dataDisc < 0] = 0
        dataDisc[torch.isnan(dataDisc)] = 0
        #discr values to int
        out= dataDisc.to(int)
    return out


