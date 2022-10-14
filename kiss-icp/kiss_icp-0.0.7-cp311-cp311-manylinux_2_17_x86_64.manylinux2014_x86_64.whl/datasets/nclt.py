import os
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
from scipy import interpolate
from scipy.spatial.transform import Rotation

from kiss_icp.config import KISSConfig, load_config
from kiss_icp.datasets.cache import get_cache, memoize


class NCLTDataset:
    """Adapted from PyLidar-SLAM"""

    def __init__(
        self,
        data_dir: Path,
        config: Path,
        max_range: Optional[float] = None,
        no_cache: Optional[bool] = None,
        *_,
        **__,
    ):
        self.config = load_config(config)
        self.config.data.max_range = max_range if max_range else 50.0  # Override default 100.0m
        self.sequence_id = os.path.basename(data_dir)
        self.sequence_dir = os.path.join(os.path.realpath(data_dir), "")
        self.scans_dir = os.path.join(self.sequence_dir, "velodyne_sync")
        scan_files = np.array(sorted(os.listdir(str(self.scans_dir))), dtype=np.str)
        poses_file = f"ground_truth/groundtruth_{self.sequence_id}.csv"
        self.poses_file = os.path.realpath(os.path.join(self.sequence_dir, "..", poses_file))

        self.timestamps, timestamp_filter = self.load_valid_timestamps(self.poses_file, scan_files)
        self.scan_files = scan_files[timestamp_filter]
        self.gt_poses = self.load_gt_poses(self.poses_file)

        # Cache
        self.use_cache = False if no_cache else self.config.use_cache
        self.cache = get_cache(directory=os.path.join(self.__class__.__name__, self.sequence_id))

        # Visualization Options
        self.use_global_visualizer = True

    def __len__(self):
        return len(self.scan_files)

    def __getitem__(self, idx):
        return self.read_point_cloud(
            os.path.join(self.scans_dir, self.scan_files[idx]), self.config.data
        )

    @memoize()
    def read_point_cloud(self, file_path: str, config: KISSConfig.data):
        def _convert(x_s, y_s, z_s):
            # Copied from http://robots.engin.umich.edu/nclt/python/read_vel_sync.py
            scaling = 0.005
            offset = -100.0

            x = x_s * scaling + offset
            y = y_s * scaling + offset
            z = z_s * scaling + offset
            return x, y, z

        binary = np.fromfile(file_path, dtype=np.int16)
        x = np.ascontiguousarray(binary[::4])
        y = np.ascontiguousarray(binary[1::4])
        z = np.ascontiguousarray(binary[2::4])
        x = x.astype(np.float32).reshape(-1, 1)
        y = y.astype(np.float32).reshape(-1, 1)
        z = z.astype(np.float32).reshape(-1, 1)
        x, y, z = _convert(x, y, z)
        # Flip to have z pointing up
        points = np.concatenate([x, -y, -z], axis=1)
        points = self._preprocess(points, config) if config.preprocess else points
        return points.astype(np.float64)

    @staticmethod
    def _preprocess(points, config: KISSConfig.data):
        points = points[np.linalg.norm(points, axis=1) <= config.max_range]
        points = points[np.linalg.norm(points, axis=1) >= config.min_range]
        return points

    @staticmethod
    def load_valid_timestamps(poses_file: str, scan_files: np.ndarray):
        # Ground truth timestamps and LiDARs don't match, interpolate
        gt_t = pd.read_csv(poses_file, sep=",").values[:, 0]
        # Limit the sequence to timestamps for which a ground truth exists
        timestamps = np.array(
            [os.path.basename(file).split(".")[0] for file in scan_files], dtype=np.int64
        )
        filter_ = (timestamps > np.min(gt_t)) * (timestamps < np.max(gt_t))
        return timestamps[filter_], filter_

    def load_gt_poses(self, poses_file: str):
        ground_truth = pd.read_csv(poses_file, sep=",").values

        # Ground truth timestamps and LiDARs don't match, interpolate
        gt_t = ground_truth[:, 0]
        t_min = np.min(gt_t)
        t_max = np.max(gt_t)
        inter = interpolate.interp1d(
            ground_truth[:, 0], ground_truth[:, 1:], kind="nearest", axis=0
        )

        # Limit the sequence to timestamps for which a ground truth exists
        gt = inter(self.timestamps)
        gt_tr = gt[:, :3]
        gt_euler = gt[:, 3:][:, [2, 1, 0]]
        gt_rot = Rotation.from_euler("ZYX", gt_euler).as_matrix()

        gt = np.eye(4, dtype=np.float32).reshape(1, 4, 4).repeat(gt.shape[0], axis=0)
        gt[:, :3, :3] = gt_rot
        gt[:, :3, 3] = gt_tr

        gt = np.einsum(
            "nij,jk->nik",
            gt,
            np.array(
                [
                    [1.0, 0.0, 0.0, 0.0],
                    [0.0, -1.0, 0.0, 0.0],
                    [0.0, 0.0, -1.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0],
                ],
                dtype=np.float32,
            ),
        )
        gt = np.einsum(
            "ij,njk->nik",
            np.array(
                [
                    [1.0, 0.0, 0.0, 0.0],
                    [0.0, -1.0, 0.0, 0.0],
                    [0.0, 0.0, -1.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0],
                ],
                dtype=np.float32,
            ),
            gt,
        )

        return gt
