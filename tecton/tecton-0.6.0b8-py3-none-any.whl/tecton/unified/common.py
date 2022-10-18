from __future__ import annotations

import datetime
from typing import Dict
from typing import Optional

import attrs
from typeguard import typechecked

from tecton_core import id_helper
from tecton_proto import args
from tecton_proto import common
from tecton_proto import data


@attrs.frozen
class TectonObjectInfo:
    """A public SDK dataclass containing common metadata used for all Tecton Objects."""

    id: str
    name: str
    description: Optional[str]
    tags: Dict[str, str]
    owner: Optional[str]
    created_at: Optional[datetime.datetime]
    workspace: Optional[str]

    @classmethod
    @typechecked
    def from_args_proto(cls, basic_info: args.basic_info_pb2.BasicInfo, id: common.id_pb2.Id) -> TectonObjectInfo:
        return cls(
            id=id_helper.IdHelper.to_string(id),
            name=basic_info.name,
            description=basic_info.description if basic_info.HasField("description") else None,
            tags=basic_info.tags,
            owner=basic_info.owner if basic_info.HasField("owner") else None,
            created_at=None,  # created_at is only filled for remote (i.e. applied) Tecton objects.
            workspace=None,  # workspace is only filled for remote (i.e. applied) Tecton objects.
        )

    @classmethod
    @typechecked
    def from_data_proto(cls, metadata: data.fco_metadata_pb2.FcoMetadata, id: common.id_pb2.Id) -> TectonObjectInfo:
        return cls(
            id=id_helper.IdHelper.to_string(id),
            name=metadata.name,
            description=metadata.description if metadata.HasField("description") else None,
            tags=metadata.tags,
            owner=metadata.owner if metadata.HasField("owner") else None,
            created_at=metadata.created_at.ToDatetime(),
            workspace=metadata.workspace,
        )
