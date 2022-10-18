from datetime import datetime
from typing import Dict

from kognic.io.model.base_serializer import BaseSerializer
from kognic.io.util import ts_to_dt


class Annotation(BaseSerializer):
    input_uuid: str
    annotation_type: str
    created: datetime
    content: Dict

class PartialAnnotation(BaseSerializer):
    input_uuid: str
    annotation_type: str
    created: datetime
    uri: str

    def to_annotation(self, content: Dict) -> Annotation:
        return Annotation(input_uuid=self.input_uuid, annotation_type=self.annotation_type, created=self.created,
                          content=content)
