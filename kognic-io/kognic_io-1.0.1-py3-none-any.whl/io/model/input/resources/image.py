from typing import Optional

from kognic.io.model.base_serializer import BaseSerializer
from kognic.io.model.input.resources.resource import Resource

camera_sensor_default = "CAM"


class ImageMetadata(BaseSerializer):
    shutter_time_start_ns: int
    shutter_time_end_ns: int


class Image(Resource):
    filename: str
    resource_id: Optional[str] = None
    sensor_name: str = camera_sensor_default
    metadata: Optional[ImageMetadata] = None
