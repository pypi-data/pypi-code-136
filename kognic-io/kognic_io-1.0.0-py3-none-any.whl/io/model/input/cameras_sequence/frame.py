from typing import List, Mapping, Union

from kognic.io.model.input.abstract.sequence_frame import SequenceFrame
from kognic.io.model.input.resources import Image, VideoFrame


class Frame(SequenceFrame):
    images: List[Image] = []
    video_frames: List[VideoFrame] = []
    metadata: Mapping[str, Union[int, float, str, bool]] = {}
