import os
from importlib import abc
from pathlib import Path
from torch.utils.cpp_extension import load
_hdtorchcuda = load(
    name='hdtorchcuda',
    extra_cflags=['-O3'],
    is_python_module=True,
    sources=[
        os.path.join(Path(__file__).parent, 'cuda', 'hdtorch.cpp'),
        os.path.join(Path(__file__).parent, 'cuda', 'hdtorch_cu.cu')
    ]
)

import hdtorch.HDutil as HDutil
import hdtorch.HDmodel as HDmodel
import hdtorch.HDencoding as HDencoding
import hdtorch.HDVecGenerators as HDVecGenerators
from hdtorch.version import __version__

from hdtorch.HDutil import (
    ham_sim,
    cos_dist,
    cos_sim,
    dot_sim,
    xor_bipolar,
    rotateVec,
    normalizeAndDiscretizeData
)


from hdtorch.HDmodel import (
    HD_classifier
)

__all__ = [
    "HDutil",
    "HDmodel",
    "HDencoding",
    "HDVecGenerators",
    "ham_sim",
    "cos_dist",
    "cos_sim",
    "dot_sim",
    "xor_bipolar",
    "rotateVec",
    "normalizeAndDiscretizeData",
    "HD_classifier"
]

pack =    _hdtorchcuda.pack
unpack =  _hdtorchcuda.unpack
hcount =  _hdtorchcuda.hcount
vcount =  _hdtorchcuda.vcount
_hcount = _hdtorchcuda._hcount
