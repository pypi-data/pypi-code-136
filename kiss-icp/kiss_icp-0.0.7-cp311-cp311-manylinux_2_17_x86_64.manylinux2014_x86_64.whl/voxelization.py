import numpy as np

from kiss_icp.pybind import kiss_icp_pybind


def voxel_down_sample(points: np.ndarray, voxel_size: float):
    _points = kiss_icp_pybind._Vector3dVector(points)
    return np.asarray(kiss_icp_pybind._voxel_down_sample(_points, voxel_size))
