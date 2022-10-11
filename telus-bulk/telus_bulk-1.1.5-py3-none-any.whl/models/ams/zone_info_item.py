from email.policy import default
from typing import Optional

from fastapi_camelcase import CamelModel
from pydantic import Field

from telus_bulk.models.ams.zone_attribute import ZoneAttributes


class ZoneInfoItem(CamelModel):
    zone_type: Optional[str] = Field(default=None, alias="zoneType")
    zone_name: Optional[str] = Field(default=None, alias="zoneName")
    zone_attributes: Optional[ZoneAttributes] = Field(None, alias="zoneAttributes")
