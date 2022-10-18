from typing import List, Optional

from kognic.io.model import UnixTimestampNs, BaseSerializer
from kognic.io.model.input.resources.point_cloud import PointCloud


class Frame(BaseSerializer):
    point_clouds: List[PointCloud]
    unix_timestamp: Optional[UnixTimestampNs] = None
