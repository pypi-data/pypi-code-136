from typing import List

from kognic.io.model.input.abstract import BaseInputWithIMUData
from kognic.io.model.input.lidars_sequence.frame import Frame
from kognic.io.model.input.metadata.metadata import AllowedMetaData


class LidarsSequence(BaseInputWithIMUData):
    external_id: str
    frames: List[Frame]
    metadata: AllowedMetaData
