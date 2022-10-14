import glob
import importlib
import os
from pathlib import Path
import sys
from typing import Optional

import natsort
import numpy as np
from scipy.spatial.transform import Rotation as R

from kiss_icp.config import KISSConfig, load_config
from kiss_icp.datasets.cache import get_cache, memoize


class ApolloDataset:
    def __init__(
        self,
        data_dir: Path,
        config: Path,
        max_range: Optional[float] = None,
        no_cache: Optional[bool] = None,
        *_,
        **__,
    ):
        try:
            self.o3d = importlib.import_module("open3d")
        except ModuleNotFoundError:
            print(
                'pcd files requires open3d and is not installed on your system run "pip install open3d"'
            )
            sys.exit(1)

        self.config = load_config(config)
        self.config.data.max_range = max_range if max_range else self.config.data.max_range
        self.scan_files = natsort.natsorted(glob.glob(f"{data_dir}/pcds/*.pcd"))
        self.gt_poses = self.readPoses(f"{data_dir}/poses/gt_poses.txt")
        self.sequence_id = os.path.basename(data_dir)

        # Cache
        self.use_cache = False if no_cache else self.config.use_cache
        self.cache = get_cache(directory=os.path.join(self.__class__.__name__, self.sequence_id))

    def __len__(self):
        return len(self.scan_files)

    def __getitem__(self, idx):
        return self.get_scan(self.scan_files[idx], self.config.data)

    @memoize()
    def get_scan(self, scan_file: str, config: KISSConfig.data):
        points = np.asarray(self.o3d.io.read_point_cloud(scan_file).points, dtype=np.float64)
        points = self._preprocess(points, config) if config.preprocess else points
        return points.astype(np.float64)

    @staticmethod
    def _preprocess(points, config: KISSConfig.data):
        points = points[np.linalg.norm(points, axis=1) <= config.max_range]
        points = points[np.linalg.norm(points, axis=1) >= config.min_range]
        return points

    @staticmethod
    def readPoses(file):
        data = np.loadtxt(file)
        id, time, t, q = np.split(data, [1, 2, 5], axis=1)
        r = R.from_quat(q).as_matrix()
        pose = np.zeros([r.shape[0], 4, 4])
        pose[:, :3, -1] = t
        pose[:, :3, :3] = r
        pose[:, -1, -1] = 1
        return pose
