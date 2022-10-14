import datetime
from functools import reduce
import os
from pathlib import Path
import sys
import time
from typing import List

import numpy as np
from tqdm import trange

from kiss_icp.config import KISSConfig, load_config, write_config
from kiss_icp.metrics import absolute_trajectory_error, sequence_error
from kiss_icp.odometry import Odometry
from kiss_icp.visualizer import RegistrationVisualizer, StubVisualizer


class OdometryPipeline:
    def __init__(
        self,
        dataset,
        config: Path,
        deskew: bool = False,
        visualize: bool = False,
        n_scans: int = -1,
        jump: int = 0,
    ):
        self._dataset = dataset
        self._n_scans = (
            len(self._dataset) - jump if n_scans == -1 else min(len(self._dataset) - jump, n_scans)
        )
        self._jump = jump
        self._first = jump
        self._last = self._jump + self._n_scans
        self.config: KISSConfig = load_config(config)
        self.config.data = self._dataset.config.data  # TODO(Nacho): Fix this config mess

        self.odometry = Odometry(config=self.config, deskew=deskew)
        self.times = []
        self.poses = self.odometry.poses

        # Visualizer
        self.visualizer = RegistrationVisualizer() if visualize else StubVisualizer()
        if hasattr(self._dataset, "use_global_visualizer"):
            self.visualizer.global_view = self._dataset.use_global_visualizer

    # Public interface  ------
    def run(self):
        self._run_pipeline()
        self._write_result_poses()
        self._write_cfg()
        return self._run_evaluation()

    # Private interface  ------
    def _run_pipeline(self):
        for idx in trange(self._first, self._last, unit=" frames", dynamic_ncols=True):
            frame, timestamps = self._next(idx)
            start_time = time.perf_counter_ns()
            in_frame, source = self.odometry.register_frame(frame, timestamps)
            self.times.append(time.perf_counter_ns() - start_time)
            self.visualizer.update(in_frame, source, self.odometry.local_map, self.poses[-1])

    def _next(self, idx):
        """TODO: re-arrange this logic"""
        dataframe = self._dataset[idx]
        try:
            frame, timestamps = dataframe
        except ValueError:
            frame = dataframe
            timestamps = np.zeros(frame.shape[0])
        return frame, timestamps

    def _write_poses(self, poses: List[np.ndarray], filename: str):
        def _to_kitti_format(poses: np.ndarray) -> np.ndarray:
            return np.array([np.concatenate((pose[0], pose[1], pose[2])) for pose in poses])

        np.savetxt(
            fname=filename,
            X=_to_kitti_format(
                self._dataset.apply_calibration(poses)
                if hasattr(self._dataset, "apply_calibration")
                else poses
            ),
        )

    @property
    def results_dir(self):
        return self._get_results_dir(self.config.out_dir)

    def _write_result_poses(self):
        self._write_poses(self.poses, f"{self.results_dir}/{self._dataset.sequence_id}.txt")

    def _get_fps(self):
        total_time_ns = reduce(lambda a, b: a + b, self.times)
        total_time = total_time_ns * 1e-9
        total_scans = self._n_scans - self._jump
        return float(total_scans / total_time)

    def _run_evaluation(self):
        if not hasattr(self._dataset, "gt_poses"):
            print("[WARNING] No GT poses available, skipping evaluation")
            return None, None

        # Dump always (calibrated) gt_poses to disk for re-evaluation
        gt_poses = self._dataset.gt_poses[self._first : self._last]
        self._write_poses(gt_poses, f"{self.results_dir}/{self._dataset.sequence_id}_gt.txt")

        # Run metrics evaluation
        avg_trans_error, avg_rot_error = sequence_error(gt_poses, self.poses)
        ate_rot, ate_trans = absolute_trajectory_error(gt_poses, self.poses)
        fps = int(np.floor(self._get_fps()))

        results_fn = f"{self.results_dir}/result_metrics.log"
        with open(results_fn, "w") as file:
            stdout = sys.stdout
            sys.stdout = file  # Change the standard output to the file we created.
            print(f"Results for {self._dataset.__class__.__name__}:{self._dataset.sequence_id}")
            print(f"AVG translational error:{avg_trans_error:.3f}")
            print(f"AVG rotational    error:{avg_rot_error:.3f}")
            print(f"ATE translation     [m]:{ate_trans:.3f}")
            print(f"ATE rotation      [rad]:{ate_rot:.3f}")
            print(f"AVG FPS           [fps]:{fps}")
            sys.stdout = stdout
        os.system(f"cat {results_fn}")
        return avg_trans_error, avg_rot_error

    def _write_cfg(self):
        config_file = os.path.join(self.results_dir, "config.yml")
        write_config(self.config, config_file)

    @staticmethod
    def _get_results_dir(out_dir: str):
        def get_current_timestamp() -> str:
            return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        results_dir = os.path.join(os.path.realpath(out_dir), get_current_timestamp())
        latest_dir = os.path.join(os.path.realpath(out_dir), "latest")
        os.makedirs(results_dir, exist_ok=True)
        os.unlink(latest_dir) if os.path.exists(latest_dir) else None
        os.symlink(results_dir, latest_dir)
        return results_dir
