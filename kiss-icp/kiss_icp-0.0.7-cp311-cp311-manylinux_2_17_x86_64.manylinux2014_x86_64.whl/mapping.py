from typing import Tuple

import numpy as np

from kiss_icp.pybind import kiss_icp_pybind


class VoxelHashMap:
    def __init__(self, voxel_size: float, max_distance: float, max_points_per_voxel: int):
        self._internal_map = kiss_icp_pybind._VoxelHashMap(
            voxel_size=voxel_size,
            max_distance=max_distance,
            max_points_per_voxel=max_points_per_voxel,
        )

    def clear(self):
        return self._internal_map._clear()

    def empty(self):
        return self._internal_map._empty()

    def add_points(self, points: np.ndarray, pose: np.ndarray = np.eye(4)):
        """Add points to the inernal map representaion.

        The origin is needed to remove the far away poitns

        TODO(NACHO): Use similar overload API as we did for VDBFusion
        """
        self._internal_map._add_points(kiss_icp_pybind._Vector3dVector(points), pose)

    def point_cloud(self) -> np.ndarray:
        """Return the internal representaion as a np.array (pointcloud)."""
        return np.asarray(self._internal_map._point_cloud())

    def get_correspondences(
        self,
        points: np.ndarray,
        max_correspondance_distance: float,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Get the pair of {source, target} pointcloud of the same size."""
        _points = kiss_icp_pybind._Vector3dVector(points)
        source, target = self._internal_map._get_correspondences(
            _points, max_correspondance_distance
        )
        return np.asarray(source), np.asarray(target)

    def register_frame(
        self,
        points: np.ndarray,
        initial_guess: np.ndarray,
        max_correspondance_distance: float,
        kernel: float,
    ) -> np.ndarray:
        return self._internal_map._register_point_cloud(
            points=kiss_icp_pybind._Vector3dVector(points),
            initial_guess=initial_guess,
            max_correspondance_distance=max_correspondance_distance,
            kernel=kernel,
        )
