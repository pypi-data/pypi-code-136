from abc import ABC
from pathlib import Path
from typing import Optional

from pydantic import validator

from kognic.io.model.base_serializer import BaseSerializer


class Resource(ABC, BaseSerializer):
    filename: str
    resource_id: Optional[str]
    sensor_name: str

    @validator('resource_id', always=True)
    def validate_date(cls, value, values):
        if value is None:
            return str(Path(values["filename"]).expanduser())
        return value
