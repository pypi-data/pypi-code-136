from __future__ import annotations

from typing import Optional

from typeguard import typechecked

from tecton_core import id_helper
from tecton_core.specs import utils
from tecton_proto import args
from tecton_proto import data

__all__ = [
    "TransformationSpec",
]


@utils.frozen_strict
class TransformationSpec:
    name: str
    id: str
    transformation_mode: args.new_transformation_pb2.TransformationMode
    user_function: args.user_defined_function_pb2.UserDefinedFunction
    description: Optional[str]
    owner: Optional[str]
    tags: Optional[str]

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.new_transformation_pb2.NewTransformation) -> TransformationSpec:
        return cls(
            name=proto.fco_metadata.name,
            id=id_helper.IdHelper.to_string(proto.entity_id),
            transformation_mode=data.transformation_mode,
            user_function=utils.get_field_or_none(proto, "user_function"),
            description=utils.get_field_or_none(proto.fco_metadata, "description"),
            owner=utils.get_field_or_none(proto.fco_metadata, "owner"),
            tags=utils.get_field_or_none(proto.fco_metadata, "tags"),
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.new_transformation_pb2.NewTransformation) -> TransformationSpec:
        raise NotImplementedError
