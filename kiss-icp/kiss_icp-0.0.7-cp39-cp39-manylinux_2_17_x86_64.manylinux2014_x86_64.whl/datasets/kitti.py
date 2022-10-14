import glob
import os
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

from kiss_icp.config import KISSConfig, load_config
from kiss_icp.datasets.cache import get_cache, memoize

__CORRECT_KITTI_CALIBRATION__ = True
__ALL_SEQUENCES__ = [seq for seq in range(0, 11)]


class KITTIOdometryDataset:
    def __init__(
        self,
        data_dir,
        config: Path,
        sequence: int,
        max_range: Optional[float] = None,
        no_cache: Optional[bool] = None,
        *_,
        **__,
    ):
        self.config = load_config(config)
        self.config.data.correct_scan = __CORRECT_KITTI_CALIBRATION__
        self.config.data.max_range = max_range if max_range else self.config.data.max_range
        self.sequence_id = str(int(sequence)).zfill(2)

        self.kitti_sequence_dir = os.path.join(data_dir, "sequences", self.sequence_id)
        self.velodyne_dir = os.path.join(self.kitti_sequence_dir, "velodyne/")

        self.scan_files = sorted(glob.glob(self.velodyne_dir + "*.bin"))
        self.calibration = self.read_calib_file(os.path.join(self.kitti_sequence_dir, "calib.txt"))

        # Load GT Poses (if available)
        if sequence < 11:
            self.poses_fn = os.path.join(data_dir, f"poses/{self.sequence_id}.txt")
            self.gt_poses = self.load_poses(self.poses_fn)

        # Cache
        self.use_cache = False if no_cache else self.config.use_cache
        self.cache = get_cache(directory=os.path.join(self.__class__.__name__, self.sequence_id))

    def __getitem__(self, idx):
        return self.scans(idx)

    def __len__(self):
        return len(self.scan_files)

    def scans(self, idx):
        return self.read_point_cloud(self.scan_files[idx], self.config.data)

    def apply_calibration(self, poses: np.ndarray) -> np.ndarray:
        """Converts from Velodyne to Camera Frame"""
        Tr = np.eye(4, dtype=np.float64)
        Tr[:3, :4] = self.calibration["Tr"].reshape(3, 4)
        return Tr @ poses @ np.linalg.inv(Tr)

    @memoize()
    def read_point_cloud(self, scan_file: str, config: KISSConfig.data):
        points = np.fromfile(scan_file, dtype=np.float32).reshape((-1, 4))[:, :3]
        points = self._correct_scan(points) if config.correct_scan else points
        points = self._preprocess(points, config) if config.preprocess else points
        return points.astype(np.float64)

    def load_poses(self, poses_file):
        def _lidar_pose_gt(poses_gt):
            _tr = self.calibration["Tr"].reshape(3, 4)
            tr = np.eye(4, dtype=np.float64)
            tr[:3, :4] = _tr
            left = np.einsum("...ij,...jk->...ik", np.linalg.inv(tr), poses_gt)
            right = np.einsum("...ij,...jk->...ik", left, tr)
            return right

        poses = pd.read_csv(poses_file, sep=" ", header=None).values
        n = poses.shape[0]
        poses = np.concatenate(
            (poses, np.zeros((n, 3), dtype=np.float32), np.ones((n, 1), dtype=np.float32)), axis=1
        )
        poses = poses.reshape((n, 4, 4))  # [N, 4, 4]
        return _lidar_pose_gt(poses)

    @staticmethod
    def _preprocess(points, config: KISSConfig.data):
        """Remove the annoying reflections from the KITTI dataset."""
        __MIN_Z_TH__ = -2.9
        z = points[:, 2]
        points = points[z > __MIN_Z_TH__]
        points = points[np.linalg.norm(points, axis=1) <= config.max_range]
        points = points[np.linalg.norm(points, axis=1) >= config.min_range]
        return points

    @staticmethod
    def read_calib_file(file_path: str) -> dict:
        calib_dict = {}
        with open(file_path, "r") as calib_file:
            for line in calib_file.readlines():
                tokens = line.split(" ")
                if tokens[0] == "calib_time:":
                    continue
                # Only read with float data
                if len(tokens) > 0:
                    values = [float(token) for token in tokens[1:]]
                    values = np.array(values, dtype=np.float32)

                    # The format in KITTI's file is <key>: <f1> <f2> <f3> ...\n -> Remove the ':'
                    key = tokens[0][:-1]
                    calib_dict[key] = values
        return calib_dict

    @staticmethod
    def _correct_scan(scan: np.ndarray):
        """Corrects the calibration of KITTI's HDL-64 scan.

        Taken from PyLidar SLAM
        """
        xyz = scan[:, :3]
        n = scan.shape[0]
        z = np.tile(np.array([[0, 0, 1]], dtype=np.float32), (n, 1))
        axes = np.cross(xyz, z)
        # Normalize the axes
        axes /= np.linalg.norm(axes, axis=1, keepdims=True)
        theta = 0.205 * np.pi / 180.0

        # Build the rotation matrix for each point
        c = np.cos(theta)
        s = np.sin(theta)

        u_outer = axes.reshape(n, 3, 1) * axes.reshape(n, 1, 3)
        u_cross = np.zeros((n, 3, 3), dtype=np.float32)
        u_cross[:, 0, 1] = -axes[:, 2]
        u_cross[:, 1, 0] = axes[:, 2]
        u_cross[:, 0, 2] = axes[:, 1]
        u_cross[:, 2, 0] = -axes[:, 1]
        u_cross[:, 1, 2] = -axes[:, 0]
        u_cross[:, 2, 1] = axes[:, 0]
        eye = np.tile(np.eye(3, dtype=np.float32), (n, 1, 1))
        rotations = c * eye + s * u_cross + (1 - c) * u_outer
        corrected_scan = np.einsum("nij,nj->ni", rotations, xyz)
        return corrected_scan
