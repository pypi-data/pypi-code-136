from typing import List, Optional

from kognic.io.model.base_serializer import BaseSerializer
from kognic.io.model.ego.utils import UnixTimestampNs
from kognic.io.model.input.resources.image import Image
from kognic.io.model.input.resources.point_cloud import PointCloud


class Frame(BaseSerializer):
    point_clouds: List[PointCloud]
    images: List[Image]
    unix_timestamp: Optional[UnixTimestampNs] = None
