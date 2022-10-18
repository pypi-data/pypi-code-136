from typing import Dict, List

from kognic.io.model.base_serializer import BaseSerializer
from kognic.io.model.input.abstract import BaseInputWithIMUData
from kognic.io.model.input.lidars.frame import Frame
from kognic.io.model.input.metadata.metadata import AllowedMetaData


class Lidars(BaseInputWithIMUData):
    external_id: str
    frame: Frame
    metadata: AllowedMetaData
