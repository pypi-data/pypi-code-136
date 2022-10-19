from enum import Enum
from typing import List

import attr
from marshmallow3_annotations.ext.attrs import AttrsSchema
from dl_common.models.datasource import Common_Dashboard_DatasourceFields, DatasourcesNames


class PowerBI_MetadataScanningLevel(Enum):
    basic = "basic"
    advanced = "advanced"


@attr.s(auto_attribs=True, kw_only=True)
class PowerBIToken:
    access_token: str = attr.ib()
    refresh_token: str = attr.ib()


@attr.s(auto_attribs=True, kw_only=True)
class PowerBI_Group:
    id: str = attr.ib()
    isOnDedicatedCapacity: bool = attr.ib()
    isReadOnly: bool = attr.ib()
    name: str = attr.ib()
    type: str = attr.ib()


class PowerBI_GroupSchema(AttrsSchema):
    class Meta:
        target = PowerBI_Group
        register_as_scheme = True


@attr.s(auto_attribs=True, kw_only=True)
class PowerBI(Common_Dashboard_DatasourceFields, PowerBIToken):
    name: str = attr.ib(default='')
    metadata_scanning_level: str = attr.ib(
        default=PowerBI_MetadataScanningLevel.basic.value)
    allowed_groups: List[PowerBI_Group] = attr.ib(default=[])
    datasource_type: str = attr.ib(
        default=DatasourcesNames.POWERBI, init=False)


class PowerBI_TokensSchema(AttrsSchema):
    class Meta:
        target = PowerBIToken
        register_as_scheme = True


class PowerBI_AddDatasourceSchema(AttrsSchema):
    class Meta:
        target = PowerBI
        register_as_scheme = True
