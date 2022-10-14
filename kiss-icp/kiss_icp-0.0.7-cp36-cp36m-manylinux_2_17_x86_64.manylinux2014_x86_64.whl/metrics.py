from typing import List, Tuple

import numpy as np

from kiss_icp.pybind import kiss_icp_pybind


def sequence_error(
    gt_poses: List[np.ndarray], results_poses: List[np.ndarray]
) -> Tuple[float, float]:
    """Sptis the sequence error for a given trajectory in camera coordinate frames."""
    return kiss_icp_pybind._kitti_seq_error(gt_poses, results_poses)


def absolute_trajectory_error(
    gt_poses: List[np.ndarray], results_poses: List[np.ndarray]
) -> Tuple[float, float]:
    """Sptis the sequence error for a given trajectory in camera coordinate frames."""
    return kiss_icp_pybind._absolute_trajectory_error(gt_poses, results_poses)
