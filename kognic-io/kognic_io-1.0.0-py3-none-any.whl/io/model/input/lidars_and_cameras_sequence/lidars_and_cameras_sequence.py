from typing import List, Optional

from kognic.io.model.input.abstract import BaseInputWithIMUData
from kognic.io.model.input.lidars_and_cameras_sequence.frame import Frame
from kognic.io.model.input.metadata.metadata import AllowedMetaData
from kognic.io.model.input.sensor_specification import SensorSpecification


class LidarsAndCamerasSequence(BaseInputWithIMUData):
    external_id: str
    frames: List[Frame]
    calibration_id: str
    sensor_specification: Optional[SensorSpecification] = None
    metadata: AllowedMetaData
