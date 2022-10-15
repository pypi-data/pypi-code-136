from email.policy import default
from typing import Any, Optional

from fastapi_camelcase import CamelModel
from pydantic import Field


class ReferenceId(CamelModel):
    fms_id: Optional[str] = Field(default=None, alias="fmsId")
    loc_building_id: Optional[str] = Field(default=None, alias="locBuildingId")
    loc_grp_id: Optional[Any] = Field(default=None, alias="locGrpId")
