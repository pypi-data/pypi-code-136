import glob
import os
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

from kiss_icp.config import KISSConfig, load_config
from kiss_icp.datasets.cache import get_cache, memoize


class NuscenesDataset:
    def __init__(
        self,
        data_dir: Path,
        sequence: int,
        config: Path,
        max_range: Optional[float] = None,
        no_cache: Optional[bool] = None,
        *_,
        **__
    ):
        # Config stuff
        self.sequence_id = str(int(sequence)).zfill(4)
        self.config = load_config(config)
        self.config.data.max_range = max_range if max_range else self.config.data.max_range
        self.nusc_sequence_dir = os.path.join(data_dir, self.sequence_id)
        self.velodyne_dir = os.path.join(self.nusc_sequence_dir, "velodyne/")

        # Read stuff
        self.calibration = self.read_calib_file(os.path.join(self.nusc_sequence_dir, "calib.txt"))
        self.gt_poses = self.load_poses(os.path.join(self.nusc_sequence_dir, "poses.txt"))
        self.scan_files = sorted(glob.glob(self.velodyne_dir + "*.bin"))

        # Cache
        self.use_cache = False if no_cache else self.config.use_cache
        self.cache = get_cache(directory=os.path.join(self.__class__.__name__, self.sequence_id))

    def __len__(self):
        return len(self.scan_files)

    def __getitem__(self, idx):
        return self.read_point_cloud(self.scan_files[idx], self.config.data)

    @memoize()
    def read_point_cloud(self, scan_file: str, config: KISSConfig.data):
        points = np.fromfile(scan_file, dtype=np.float32).reshape((-1, 4))[:, :3]
        points = self._preprocess(points, config) if config.preprocess else points
        return points.astype(np.float64)

    @staticmethod
    def _preprocess(points, config: KISSConfig.data):
        points = points[np.linalg.norm(points, axis=1) <= config.max_range]
        points = points[np.linalg.norm(points, axis=1) >= config.min_range]
        return points

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
