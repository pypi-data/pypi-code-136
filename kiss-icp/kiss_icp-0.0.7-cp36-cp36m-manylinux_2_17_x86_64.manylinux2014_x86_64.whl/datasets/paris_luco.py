import glob
import os
from pathlib import Path
from typing import Optional

import numpy as np
from plyfile import PlyData

from kiss_icp.config import KISSConfig, load_config
from kiss_icp.datasets.cache import get_cache, memoize


class ParisLucoDataset:
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
        self.velodyne_dir = os.path.join(self.sequence_dir, "frames/")

        self.scan_files = sorted(glob.glob(self.velodyne_dir + "*.ply"))

        # Load poses after cache is created
        self.gt_poses = self.load_gt_poses(os.path.join(self.sequence_dir, "gt_traj_lidar.txt"))

        # Cache
        self.use_cache = False if no_cache else self.config.use_cache
        self.cache = get_cache(directory=os.path.join(self.__class__.__name__, self.sequence_id))

    def __len__(self):
        return len(self.scan_files)

    def __getitem__(self, idx):
        return self.read_point_cloud(self.scan_files[idx], self.config.data)

    @memoize()
    def read_point_cloud(self, file_path: str, config: KISSConfig.data):
        plydata = PlyData.read(file_path)
        x = np.asarray(plydata.elements[0].data["x"]).reshape(-1, 1)
        y = np.asarray(plydata.elements[0].data["y"]).reshape(-1, 1)
        z = np.asarray(plydata.elements[0].data["z"]).reshape(-1, 1)
        points = np.concatenate([x, y, z], axis=1)
        timestamps = np.asarray(plydata.elements[0].data["timestamp"])
        timestamps = timestamps / np.max(timestamps)
        if config.preprocess:
            points, timestamps = self._preprocess(points, timestamps, config)
        return points.astype(np.float64), timestamps

    @staticmethod
    def _preprocess(points, timestamps, config: KISSConfig.data):
        ranges = np.linalg.norm(points, axis=1)
        filter_ = np.logical_and(ranges <= config.max_range, ranges >= config.min_range)
        return points[filter_], timestamps[filter_]

    def load_gt_poses(self, file_path):
        gt_poses = []
        for xyz in np.loadtxt(file_path):
            T = np.eye(4)
            T[:3, 3] = xyz
            gt_poses.append(T)
        return gt_poses

    def apply_calibration(self, poses):
        """ParisLucoDataset only has a x, y, z trajectory, so we must will em all"""
        new_poses = []
        for pose in poses:
            T = pose.copy()
            T[:3, :3] = np.eye(3)
            new_poses.append(T)
        return new_poses
