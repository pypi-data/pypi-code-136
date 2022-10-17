"""
Created on Apr 8, 2022

@author: wsimon
"""

import math
import torch
from . import _hdtorchcuda
from .HDutil import xor_bipolar

__all__ = [
    "bind_feat_and_values_via_append",
    "bind_feat_and_values_via_permute",
    "bind_feat_and_values_via_xor",
    "encode_data_to_vectors"
]
def bind_feat_and_values_via_append(features, D, HD_flavor, basis_feat_vecs, basis_val_vecs, packed):
    """ Bind feature with its values using 'FeatAppend' approach.

    In 'FeatAppend' approach features representing different values for each feature are just
    appended next to each other instead of accumulating it in the same bits. This way one feature
    contributes to each bit, and thus knowing which feature is responsible for each bit, which can
    be useful for interpretability.

    Args:
        features: 2D array of discretized feature values (columns are features, rows are samples)
        D: hypervector dimension D
        HD_flavor: if vectors are 'bipolar' or 'binary'
        basis_feat_vecs: basis feature ID vectors
        basis_val_vecs: basis feature value vectors
        packed: weather vectors are 'packed' or not
        
    Returns:
        The encoded features to HD hypervectors for each sample. They are in uncompressed binary
        form, with each bit having type int8, unles, if the user specified packed mode when
        initializing the HD_classifier, then they are in the packed format.
    """
    data_bind= basis_val_vecs[features].view(features.shape[0], 1, -1)
    # bundle for all features
    if packed:
        out = _hdtorchcuda.vcount(data_bind, D)
    else:
        out = data_bind.sum(1, dtype=torch.int16)

    output = out.to(torch.int8)

    # converting to bipolar if needed
    if HD_flavor == 'bipol':
        output[output == 0] = -1

    return output

def bind_feat_and_values_via_permute(features, D, HD_flavor, basis_feat_vecs, basis_val_vecs, packed):
    """ Bind feature with its values using 'FeatPermute' approach.

    In 'FeatPermute' approach features ID vectors are shifted for value of that feature. This is
    interesting encoding whose advantages and disadvantages can be explored.

    Args:
        features: 2D array of discretized feature values (columns are features, rows are samples)
        D: hypervector dimension D
        HD_flavor: if vectors are 'bipolar' or 'binary'
        basis_feat_vecs: basis feature ID vectors
        basis_val_vecs: basis feature value vectors
        packed: weather vectors are 'packed' or not

    Returns:
        The encoded features to HD hypervectors for each sample. They are in uncompressed binary
        form, with each bit having type int8, unles, if the user specified packed mode when
        initializing the HD_classifier, then they are in the packed format.
    """
    num_feat = features.shape[1]

    data_bind= rotateVec(basis_feat_vecs, features)
    # bundle for all features
    if packed:
        out = _hdtorchcuda.vcount(data_bind, D)
    else:
        out = data_bind.sum(1, dtype=torch.int16)

    # normalize back to binary form
    num_feat = num_feat >> 1 if HD_flavor == 'binary' else 0
    output = torch.empty((features.shape[0], D), dtype=torch.int8, device=features.device)
    torch.gt(out, num_feat, out=output)

    # converting to bipolar if needed
    if HD_flavor == 'bipol':
        output[output == 0] = -1

    return output


def bind_feat_and_values_via_xor(features, D, HD_flavor, basis_feat_vecs, basis_val_vecs, packed):
    """ Bind feature with its values using most typical 'FeatXORVal' approach.

    In 'FeatXORVal' approach features representing different values for each feature are XOR-ed
    with ID vectors of correspontind features. This is a typical way to bind information of features
    and their values. In the end such binded vectors for each feature are bundled (summed and
    normalized) for to combine for all features together.

    Args:
        features: 2D array of discretized feature values (columns are features, rows are samples)
        D: hypervector dimension D
        HD_flavor: if vectors are 'bipolar' or 'binary'
        basis_feat_vecs: basis feature ID vectors
        basis_val_vecs: basis feature value vectors
        packed: weather vectors are 'packed' or not

    Returns:
        The encoded features to HD hypervectors for each sample. They are in uncompressed binary
        form, with each bit having type int8, unles, if the user specified packed mode when
        initializing the HD_classifier, then they are in the packed format.
    """
    num_feat = features.shape[1]

    if HD_flavor == 'binary':
        data_bind=torch.bitwise_xor(basis_feat_vecs.unsqueeze(0), basis_val_vecs[features])
    elif HD_flavor == 'bipol' and not packed:
        data_bind=xor_bipolar(basis_feat_vecs.unsqueeze(0), basis_val_vecs[features])

    # bundle for all features
    if packed:
        out = _hdtorchcuda.vcount(data_bind, D)
    else:
        out = data_bind.sum(1, dtype=torch.int16)

    # normalize back to binary form
    f = num_feat >> 1 if HD_flavor == 'binary' else 0
    output = torch.empty((features.shape[0], D), dtype=torch.int8, device=features.device)
    torch.gt(out, f, out=output)

    # converting to bipolar if needed
    if HD_flavor == 'bipol':
        output[output == 0] = -1

    return output

def encode_data_to_vectors(data, basis_feat_vecs, basis_val_vecs, HD_flavor, packed, type_encoding, D):
    """ Encode training data into HD space via selected binding function

    EncodeDataToVectors is expecting data to be discretized into a range of values equal to the
    number of values present in in the featureLevelValues array. The input data will be used to
    index featureLevelValues, with the return value being bound to the featureID
    corresponding to the feature.

    Args:
        data: 2D array of discretized feature values (columns are features, rows are samples)
        basis_feat_vecs: basis feature ID vectors
        basis_val_vecs: basis feature value vectors
        HD_flavor: if vectors are 'bipolar' or 'binary'
        packed: weather vectors are 'packed' or not
        type_encoding: strategy how to bind feature values with feature indices
        D: hypervector dimension D

    Returns:
        The encoded features to HD hypervectors for each sample. They are in uncompressed binary
        form, with each bit having type int8, unles, if the user specified packed mode when
        initializing the HD_classifier, then they are in the packed format.
    """

    # Select bindingFunction
    binding_function = bind_feat_and_values_via_append  if type_encoding == 'featAppend'  \
                  else bind_feat_and_values_via_permute if type_encoding == 'featPermute' \
                  else bind_feat_and_values_via_xor     if type_encoding == 'featXORVal'  \
                  else None

    # bind features with their values
    output=binding_function(data, D, HD_flavor, basis_feat_vecs, basis_val_vecs, packed)


    # packing if needed
    if packed:
        packed_output = torch.full(
            (data.shape[0], math.ceil(D / 32)),
            -1,
            dtype=torch.int32,
            device=data.device)
        _hdtorchcuda.pack(output, packed_output)
    else:
        packed_output = -1

    return output, packed_output
