import os
from pathlib import Path
import re
from typing import Optional

import numpy as np
from pyntcloud import PyntCloud
from scipy.spatial.transform.rotation import Rotation as R

from kiss_icp.config import KISSConfig, load_config
from kiss_icp.datasets.cache import get_cache, memoize


class NewerCollegeDataset:
    def __init__(
        self,
        data_dir,
        config: Path,
        max_range: Optional[float] = None,
        no_cache: Optional[bool] = None,
        *_,
        **__,
    ):
        self.config = load_config(config)
        self.config.data.max_range = max_range if max_range else self.config.data.max_range
        self.data_source = os.path.join(data_dir, "")
        self.scan_folder = os.path.join(self.data_source, "raw_format/ouster_scan")
        self.pose_file = os.path.join(self.data_source, "ground_truth/registered_poses.csv")
        self.sequence_id = os.path.basename(data_dir)

        # Load scan files and poses
        self.scan_files = self.get_pcd_filenames(self.scan_folder)
        self.gt_poses = self.load_gt_poses(self.pose_file)

        # Cache
        self.use_cache = False if no_cache else self.config.use_cache
        self.cache = get_cache(directory=os.path.join(self.__class__.__name__, self.sequence_id))

        # Visualization Options
        self.use_global_visualizer = True

    def __len__(self):
        return len(self.scan_files)

    def __getitem__(self, idx):
        file_path = os.path.join(self.scan_folder, self.scan_files[idx])
        return self.getitem(file_path, self.config.data)

    @memoize()
    def getitem(self, scan_file: str, config: KISSConfig.data):
        points = PyntCloud.from_file(scan_file).points[["x", "y", "z"]].to_numpy()
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

    @staticmethod
    def get_pcd_filenames(scans_folder):
        # cloud_1583836591_182590976.pcd
        regex = re.compile("^cloud_(\d*_\d*)")

        def get_cloud_timestamp(pcd_filename):
            m = regex.search(pcd_filename)
            secs, nsecs = m.groups()[0].split("_")
            return int(secs) * int(1e9) + int(nsecs)

        return sorted(os.listdir(scans_folder), key=get_cloud_timestamp)

    @staticmethod
    def load_gt_poses(file_path: str):
        """Taken from pyLiDAR-SLAM/blob/master/slam/dataset/nhcd_dataset.py"""
        ground_truth_df = np.genfromtxt(str(file_path), delimiter=",", dtype=np.float64)
        xyz = ground_truth_df[:, 2:5]
        qxyzw = ground_truth_df[:, 5:]

        num_poses = qxyzw.shape[0]
        poses = np.eye(4, dtype=np.float64).reshape(1, 4, 4).repeat(num_poses, axis=0)
        poses[:, :3, :3] = R.from_quat(qxyzw).as_matrix()
        poses[:, :3, 3] = xyz

        T_CL = np.eye(4, dtype=np.float32)
        T_CL[:3, :3] = R.from_quat([0.0, 0.0, 0.924, 0.383]).as_matrix()
        T_CL[:3, 3] = np.array([-0.084, -0.025, 0.050], dtype=np.float32)
        poses = np.einsum("nij,jk->nik", poses, T_CL)
        poses = np.einsum("ij,njk->nik", np.linalg.inv(poses[0]), poses)
        return poses
