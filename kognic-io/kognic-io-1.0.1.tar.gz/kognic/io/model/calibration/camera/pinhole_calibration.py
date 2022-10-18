from kognic.io.model.calibration.camera.common import BaseCameraCalibration, DistortionCoefficients
from kognic.io.model.calibration.common import CalibrationType


class PinholeCalibration(BaseCameraCalibration):
    calibration_type = CalibrationType.PINHOLE.value
    distortion_coefficients: DistortionCoefficients
