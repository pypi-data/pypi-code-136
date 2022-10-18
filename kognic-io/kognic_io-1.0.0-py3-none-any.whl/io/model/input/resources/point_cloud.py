from typing import Optional

from kognic.io.model.input.resources.resource import Resource

lidar_sensor_default = "lidar"


class PointCloud(Resource):
    filename: str
    resource_id: Optional[str] = None
    sensor_name: str = lidar_sensor_default
