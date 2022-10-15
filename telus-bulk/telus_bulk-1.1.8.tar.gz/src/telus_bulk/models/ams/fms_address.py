from email.policy import default
from typing import Optional
from fastapi_camelcase import CamelModel
from pydantic import Field


class FmsAddress(CamelModel):
    sa_no: Optional[str] = Field(default=None, alias="saNo")
    resc_cd: Optional[str] = Field(default=None, alias="rescCd")
    sa_house: Optional[str] = Field(default=None, alias="saHouse")
    sa_street_name: Optional[str] = Field(default=None, alias="saStreetName")
    sa_city_province_code: Optional[str] = Field(
        default=None, alias="saCityProvinceCode"
    )
    sa_postal_code: Optional[str] = Field(default="N/A", alias="saPostalCode")
    sa_clli_code: Optional[str] = Field(default=None, alias="saCLLICode")
    serv_coid: Optional[str] = Field(default=None, alias="servCoid")
    sa_clli_prov_cd: Optional[str] = Field(default=None, alias="saClliProvCd")
