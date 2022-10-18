from abc import ABC

from kognic.io.model.base_serializer import BaseSerializer


class SequenceFrame(BaseSerializer, ABC):
    frame_id: str
    relative_timestamp: int
