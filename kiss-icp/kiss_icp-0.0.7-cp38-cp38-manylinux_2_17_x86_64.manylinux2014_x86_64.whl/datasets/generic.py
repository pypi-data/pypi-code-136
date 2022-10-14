import importlib
import os
from pathlib import Path
import sys
from typing import Optional

import natsort
import numpy as np
from pyntcloud import PyntCloud
import trimesh

from kiss_icp.config import KISSConfig, load_config
from kiss_icp.datasets import supported_file_extensions
from kiss_icp.datasets.cache import get_cache, memoize


class GenericDataset:
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
        self.scans_dir = os.path.join(os.path.realpath(data_dir), "")
        self.scan_files = np.array(
            natsort.natsorted(
                [
                    fn
                    for fn in os.listdir(self.scans_dir)
                    if any(fn.endswith(ext) for ext in supported_file_extensions())
                ]
            ),
            dtype=np.str,
        )
        if len(self.scan_files) == 0:
            raise ValueError(f"Tried to read point cloud files in {self.scans_dir} but none found")
        self.file_extension = self.scan_files[0].split(".")[-1]
        if self.file_extension not in supported_file_extensions():
            raise ValueError(f"Supported formats are: {supported_file_extensions()}")
        # Trying to keep Open3D as optional since it's too big
        if self.file_extension == "pcd":
            try:
                self.o3d = importlib.import_module("open3d")
            except ModuleNotFoundError as err:
                print(
                    "pcd BINARY files requires open3d and is not installed on your system."
                    'run "pip install open3d"'
                )
                sys.exit(1)

        # Cache
        self.use_cache = False if no_cache else self.config.use_cache
        self.cache = get_cache(directory=os.path.join(self.__class__.__name__, self.sequence_id))

    def __len__(self):
        return len(self.scan_files)

    def __getitem__(self, idx):
        return self.read_point_cloud(
            os.path.join(self.scans_dir, self.scan_files[idx]), self.config.data
        )

    @memoize()
    def read_point_cloud(self, file_path: str, config: KISSConfig.data):
        if self.file_extension == "bin":
            points = np.fromfile(file_path, dtype=np.float32).reshape((-1, 4))[:, :3]
        elif self.file_extension == "pcd":
            points = np.asarray(self.o3d.io.read_point_cloud(file_path).points, dtype=np.float64)
        else:
            try:  # first try trimesh
                points = np.asarray(trimesh.load(file_path).vertices)
            except ValueError:  # then try pyntcloud
                points = PyntCloud.from_file(file_path).points[["x", "y", "z"]].to_numpy()

        points = self._preprocess(points, config) if config.preprocess else points
        return points.astype(np.float64)

    @staticmethod
    def _preprocess(points, config: KISSConfig.data):
        points = points[np.linalg.norm(points, axis=1) <= config.max_range]
        points = points[np.linalg.norm(points, axis=1) >= config.min_range]
        return points
