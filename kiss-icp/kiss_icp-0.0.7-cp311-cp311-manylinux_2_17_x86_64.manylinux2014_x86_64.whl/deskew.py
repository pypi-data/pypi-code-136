from abc import ABC

from kiss_icp.config import KISSConfig
from kiss_icp.pybind import kiss_icp_pybind


class StubCompensator(ABC):
    def __init__(self):
        pass

    def deskew_scan(self, frame, poses, timestamps):
        return frame


class MotionCompensator:
    def __init__(self, config: KISSConfig):
        self.scan_duration = 1 / config.data.lidar_frequency
        self.mid_pose_timestamp = 0.5  # TODO: Expose this

    # This could be an IMU estimation
    def velocity_estimation(self, poses):
        return kiss_icp_pybind._velocity_estimation(
            start_pose=poses[-2],
            finish_pose=poses[-1],
            scan_duration=self.scan_duration,
        )

    def deskew_scan(self, frame, poses, timestamps):
        if len(poses) < 2:
            return frame

        linear_velocity, angular_velocity = self.velocity_estimation(poses)
        return kiss_icp_pybind._deskew_scan(
            frame=kiss_icp_pybind._Vector3dVector(frame),
            timestamps=self.scan_duration * (timestamps - self.mid_pose_timestamp),
            linear_velocity=linear_velocity,
            angular_velocity=angular_velocity,
        )
