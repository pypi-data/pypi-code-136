from typing import List, Mapping, Union, Optional

from kognic.io.model import UnixTimestampNs
from kognic.io.model.ego import EgoVehiclePose
from kognic.io.model.input.abstract.sequence_frame import SequenceFrame
from kognic.io.model.input.resources import PointCloud, Image, VideoFrame


class Frame(SequenceFrame):
    point_clouds: List[PointCloud]
    ego_vehicle_pose: Optional[EgoVehiclePose] = None
    metadata: Mapping[str, Union[int, float, str, bool]] = {}
    unix_timestamp: Optional[UnixTimestampNs] = None
