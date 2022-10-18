from abc import ABC
from typing import Optional

from kognic.io.model.base_serializer import BaseSerializer
from kognic.io.model.input.resources.resource import Resource

camera_sensor_default = "CAM"


class VideoTS(ABC, BaseSerializer):
    video_timestamp: int


class VideoFrame(Resource, VideoTS):
    filename: str
    resource_id: Optional[str] = None
    sensor_name: str = camera_sensor_default
    video_timestamp: int
