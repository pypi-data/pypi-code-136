from typing import Optional

from kognic.io.model.base_serializer import BaseSerializer
from kognic.io.model.input.cameras.frame import Frame
from kognic.io.model.input.metadata.metadata import AllowedMetaData
from kognic.io.model.input.sensor_specification import SensorSpecification


class Cameras(BaseSerializer):
    external_id: str
    frame: Frame
    sensor_specification: Optional[SensorSpecification] = None
    metadata: AllowedMetaData
