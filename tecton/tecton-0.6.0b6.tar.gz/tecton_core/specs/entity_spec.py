from __future__ import annotations

from typing import Tuple

from typeguard import typechecked

from tecton_core import id_helper
from tecton_core.specs import utils
from tecton_proto import args
from tecton_proto import data

__all__ = [
    "EntitySpec",
]


@utils.frozen_strict
class EntitySpec:
    name: str
    id: str
    join_keys: Tuple[str, ...]

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.entity_pb2.Entity) -> EntitySpec:
        return cls(
            name=proto.fco_metadata.name,
            id=id_helper.IdHelper.to_string(proto.entity_id),
            join_keys=utils.get_tuple_from_repeated_field(proto.join_keys),
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.entity_pb2.Entity) -> EntitySpec:
        raise NotImplementedError
