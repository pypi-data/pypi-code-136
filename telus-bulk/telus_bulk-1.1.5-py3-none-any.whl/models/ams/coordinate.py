from typing import Any, Optional

from fastapi_camelcase import CamelModel
from pydantic import Field


class Coordinate(CamelModel):
    srs_code: str = Field(..., alias="srsCode")
    latitude: float
    longitude: float
    location_accuracy_score: Optional[str] = Field(
        default=None, alias="locationAccuracyScore"
    )
    location_provider: Optional[Any] = Field(default=None, alias="locationProvider")
    location_update_ts: Optional[str] = Field(default=None, alias="locationUpdateTs")
