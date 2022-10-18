from typing import List

from kognic.io.model.base_serializer import BaseSerializer
from kognic.io.model.input.resources.image import Image


class Frame(BaseSerializer):
    images: List[Image]
