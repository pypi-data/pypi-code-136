from kognic.io.model.base_serializer import BaseSerializer
from kognic.io.model.calibration.camera.common import BaseCameraCalibration
from kognic.io.model.calibration.common import CalibrationType


class PrincipalPointDistortionCoefficients(BaseSerializer):
    k1: float
    k2: float


class PrincipalPoint(BaseSerializer):
    x: float
    y: float


class DistortionCenter(BaseSerializer):
    x: float
    y: float


class PrincipalPointDistortionCalibration(BaseCameraCalibration):
    calibration_type = CalibrationType.PRINCIPALPOINTDIST.value
    principal_point_distortion_coefficients: PrincipalPointDistortionCoefficients
    distortion_center: DistortionCenter
    principal_point: PrincipalPoint
