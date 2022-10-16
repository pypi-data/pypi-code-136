import os

GPU_ENABLE = os.environ.get("JJY_GPU_ENABLE", "True")
# GPU_ENABLE = "False"

GPU_MODE = True
if GPU_ENABLE.lower() == "false":
    GPU_ENABLE = False
else:
    GPU_ENABLE = True

import numpy as np

xp = np


if GPU_ENABLE is True:

    try:
        import cupy as cp

        xp = cp
        xp.cuda.Device(0).use()
        GPU_MODE = True
    except ImportError:
        GPU_ENABLE = False
        GPU_MODE = False


# import jax.numpy as xp



# a = [1,2,3]
# # # a = list(a)
# b = xp.prod(np.asarray(a))
# print(b)
# c = xp.ones(int(b))
# print(c)

# def enable_gpu():
#     global xp
#     try:
#         import cupy as cp
#
#         xp = cp
#     except ImportError:
#
#         gpu_enable = False
#         raise ImportError("Cupy 설치해주세요~~")
#
#
# def disable_gpu():
#     global xp
#     try:
#         import numpy as np
#         xp = np
#     except ImportError:
#
#         gpu_enable = False
#         raise ImportError("Numpy 설치해주세요~~")



def get_array_module(x):
    """Returns the array module for `x`.
    Args:
        x (dezero.Variable or numpy.ndarray or cupy.ndarray): Values to
            determine whether NumPy or CuPy should be used.
    Returns:
        module: `cupy` or `numpy` is returned based on the argument.
    """

    if not GPU_ENABLE:
        return np
    xp = cp.get_array_module(x)
    return xp


def as_numpy(x):
    """Convert to `numpy.ndarray`.
    Args:
        x (`numpy.ndarray` or `cupy.ndarray`): Arbitrary object that can be
            converted to `numpy.ndarray`.
    Returns:
        `numpy.ndarray`: Converted array.
    """

    if np.isscalar(x):
        return np.array(x)
    elif isinstance(x, np.ndarray):
        return x
    return cp.asnumpy(x)


def as_cupy(x):
    """Convert to `cupy.ndarray`.
    Args:
        x (`numpy.ndarray` or `cupy.ndarray`): Arbitrary object that can be
            converted to `cupy.ndarray`.
    Returns:
        `cupy.ndarray`: Converted array.
    """

    if not GPU_ENABLE:
        raise Exception('CuPy cannot be loaded. Install CuPy!')
    return cp.asarray(x)
