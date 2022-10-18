from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import Field

from kognic.io.model.base_serializer import BaseSerializer


class InputStatus(str, Enum):
    Pending = "pending"
    Processing = "processing"
    Created = "created"
    Failed = "failed"
    InvalidatedBadContent = "invalidated:broken-input"
    InvalidatedSlamRerun = "invalidated:slam-rerun"
    InvalidatedDuplicate = "invalidated:duplicate"
    InvalidatedIncorrectlyCreated = "invalidated:incorrectly-created"


class Input(BaseSerializer):
    uuid: str = Field(alias='internalId')
    external_id: str
    batch: str = Field(alias='batchId')
    input_type: str
    status: InputStatus
    created: datetime
    annotation_types: List[str]
    calibration_id: Optional[str]
    view_link: Optional[str]
    error_message: Optional[str]
