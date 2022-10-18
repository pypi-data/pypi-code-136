from typing import Optional

from kognic.io.model.input.abstract import BaseInputWithIMUData
from kognic.io.model.input.lidars_and_cameras.frame import Frame
from kognic.io.model.input.metadata.metadata import AllowedMetaData
from kognic.io.model.input.sensor_specification import SensorSpecification


class LidarsAndCameras(BaseInputWithIMUData):
    external_id: str
    frame: Frame
    calibration_id: str
    sensor_specification: Optional[SensorSpecification] = None
    metadata: AllowedMetaData
