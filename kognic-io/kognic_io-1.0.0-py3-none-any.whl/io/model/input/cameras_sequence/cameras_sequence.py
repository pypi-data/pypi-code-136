from typing import List, Optional

from kognic.io.model.base_serializer import BaseSerializer
from kognic.io.model.input.cameras_sequence.frame import Frame
from kognic.io.model.input.metadata.metadata import AllowedMetaData, metadata_to_dict
from kognic.io.model.input.sensor_specification import SensorSpecification


class CamerasSequence(BaseSerializer):
    external_id: str
    frames: List[Frame]
    sensor_specification: Optional[SensorSpecification] = None
    metadata: AllowedMetaData
