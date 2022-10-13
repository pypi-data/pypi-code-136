from email.policy import default
from typing import Optional
from fastapi_camelcase import CamelModel
from pydantic import Field


class ReferenceIds(CamelModel):
    lpds_id: Optional[str] = Field(default=None, alias="LPDS_ID")
    fms_id: Optional[str] = Field(default=None, alias="FMS_ID")
