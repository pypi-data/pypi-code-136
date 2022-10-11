from typing import Any, List, Dict, Optional, Literal

from fastapi_camelcase import CamelModel
from pydantic import Field

from telus_bulk.models.ams.coordinate import Coordinate
from telus_bulk.models.ams.e911_address import E911Address
from telus_bulk.models.ams.fms_address import FmsAddress
from telus_bulk.models.ams.reference_id import ReferenceId
from telus_bulk.models.ams.reference_ids import ReferenceIds
from telus_bulk.models.ams.zone_info_item import ZoneInfoItem
from telus_bulk.models.worker_job.place import PlaceAMS


class AddressDetailModel(CamelModel):
    address_id: str
    address_type: Optional[str]
    reference_id: Optional[ReferenceId]
    reference_ids: Optional[ReferenceIds]
    unit: Any
    floor: Any
    street_number_prefix: Any
    street_number: Optional[str]
    street_number_suffix: Any
    dir_prefix: Any
    street_type_prefix: Any
    street_name: Optional[str]
    street_type_suffix: Any
    dir_suffix: Any
    city: Optional[str]
    province: str
    postal_code: Optional[str] = Field(default="N/A")
    country: Optional[Literal["USA", "CAN"]] = Field(default="CAN")
    coid: Optional[str]
    serviceable: Optional[str]
    serviceable_code: Optional[str]
    building_type: Optional[str]
    premise_count_flag: Optional[Any]
    premise_count_date: Optional[Any]
    postal_code_updt_ts: Optional[Any]
    res_line_count: Optional[str]
    bus_line_count: Optional[str]
    mdu_sfu_count: Optional[str]
    project_sub_type: Optional[Any]
    first_nation_ind: Optional[str]
    exception_code: Optional[Any]
    nap_addr_assoc: Optional[Any]
    coordinate: Optional[Coordinate]
    zone_info: Optional[List[ZoneInfoItem]]
    fms_address: Optional[FmsAddress]
    e911_address: Optional[E911Address]
    tag: Optional[List]
    location_comments: Optional[Dict[str, Any]]

    def to_csq_item(self) -> PlaceAMS:
        return PlaceAMS(
            id=self.address_id,
            city=self.city,
            country=self.country,
            postcode=self.postal_code,
            state_or_province=self.province,
            street_dir=self.dir_prefix,
            street_name=self.street_name,
            street_nr=self.street_number,
            street_type=self.street_type_prefix,
            street_type_suffix=self.street_type_suffix,
            street_type_prefix=self.street_type_prefix,
            street_number_prefix=self.street_number_prefix,
            street_number_suffix=self.street_number_suffix,
            dir_suffix=self.dir_suffix,
            dir_prefix=self.dir_prefix,
            floor=self.floor,
            unit=self.unit,
            address_type=self.address_type,
            coordinate=self.coordinate,
        )
