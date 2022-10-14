import glob
import os
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
from scipy.spatial.transform.rotation import Rotation as R
from trimesh import transform_points

from kiss_icp.config import KISSConfig, load_config
from kiss_icp.datasets.cache import get_cache, memoize


__ALL_SEQUENCES__ = [
    "kaist/KAIST01",
    "kaist/KAIST02",
    "kaist/KAIST03",
    "dcc/DCC01",
    "dcc/DCC02",
    "dcc/DCC03",
    "riverside/Riverside01",
    "riverside/Riverside02",
    "riverside/Riverside03",
    "sejong/Sejong01",
    "sejong/Sejong02",
    "sejong/Sejong03",
]


class MulranDataset:
    def __init__(
        self,
        data_dir: Path,
        config: Path,
        max_range: Optional[float] = None,
        no_cache: Optional[bool] = None,
        *_,
        **__,
    ):
        # Config stuff
        self.config = load_config(config)
        self.config.data.max_range = max_range if max_range else self.config.data.max_range
        self.sequence_id = os.path.basename(data_dir)
        self.sequence_dir = os.path.realpath(data_dir)
        self.velodyne_dir = os.path.join(self.sequence_dir, "Ouster/")

        # Use this rotation matrix to have a forward looking X axi
        self.R = np.eye(4)
        self.R[:3, :3] = R.from_euler("xyz", [0.0, 0.0, 180.0], degrees=True).as_matrix()
        self.scan_files = sorted(glob.glob(self.velodyne_dir + "*.bin"))
        self.scan_timestamps = [int(os.path.basename(t).split(".")[0]) for t in self.scan_files]

        # Cache
        self.use_cache = False if no_cache else self.config.use_cache
        self.cache = get_cache(directory=os.path.join(self.__class__.__name__, self.sequence_id))

        # Load poses after cache is created
        self.gt_poses = self.load_gt_poses(os.path.join(self.sequence_dir, "global_pose.csv"))

    def __len__(self):
        return len(self.scan_files)

    def __getitem__(self, idx):
        return self.read_point_cloud(self.scan_files[idx], self.config.data)

    @memoize()
    def read_point_cloud(self, file_path: str, config: KISSConfig.data):
        points = np.fromfile(file_path, dtype=np.float32).reshape((-1, 4))[:, :3]
        points = transform_points(points, self.R)
        timestamps = self.get_timestamps()
        if points.shape[0] != timestamps.shape[0]:
            # MuRan has some broken point clouds, just fallback to no timestamps
            return points.astype(np.float64), np.ones(points.shape[0])
        if config.preprocess:
            points, timestamps = self._preprocess(points, timestamps, config)
        return points.astype(np.float64), timestamps

    @staticmethod
    def _preprocess(points, timestamps, config: KISSConfig.data):
        ranges = np.linalg.norm(points, axis=1)
        filter_ = np.logical_and(ranges <= config.max_range, ranges >= config.min_range)
        return points[filter_], timestamps[filter_]

    @staticmethod
    def get_timestamps():
        H = 64
        W = 1024
        return (np.floor(np.arange(H * W) / H) / W).reshape(-1, 1)

    @memoize()
    def load_gt_poses(self, poses_file: str):
        """MuRan has more poses than scans, therefore we need to match 1-1 timestamp with pose"""

        def read_csv(poses_file: str):
            poses = pd.read_csv(poses_file, sep=",", header=None)
            timestamps = np.asarray(poses[0])
            poses = poses.drop(poses.columns[0], axis=1)  # drop the timestamp valie
            n = poses.shape[0]
            poses = np.concatenate(
                (poses, np.zeros((n, 3), dtype=np.float32), np.ones((n, 1), dtype=np.float32)),
                axis=1,
            )
            poses = poses.reshape((n, 4, 4))  # [N, 4, 4]
            return poses, timestamps

        # Read the csv file
        poses, timestamps = read_csv(poses_file)
        # Extract only the poses that has a matching Ouster scan
        poses = poses[[np.argmin(abs(timestamps - t)) for t in self.scan_timestamps]]

        # Convert from global coordinate poses to local poses
        first_pose = poses[0, :, :]
        poses = np.linalg.inv(first_pose) @ poses

        # Apply calibration obtainbed from calib_base2ouster.txt
        T_lidar_to_base = np.eye(4, dtype=np.float32)
        T_lidar_to_base[:3, 3] = np.array([1.7042, -0.021, 1.8047])
        T_lidar_to_base[:3, :3] = R.from_euler(
            "xyz", [0.0001, 0.0003, 179.6654], degrees=True
        ).as_matrix()
        T_lidar_to_base = self.R @ T_lidar_to_base
        T_base_to_lidar = np.linalg.inv(T_lidar_to_base)
        return T_lidar_to_base @ poses @ T_base_to_lidar
