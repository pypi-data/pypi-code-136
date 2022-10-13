from __future__ import annotations

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

    @classmethod
    @typechecked
    def from_data_proto(cls, proto: data.new_transformation_pb2.NewTransformation) -> TransformationSpec:
        return cls(
            name=proto.fco_metadata.name,
            id=id_helper.IdHelper.to_string(proto.transformation_id),
            transformation_mode=proto.transformation_mode,
            user_function=utils.get_field_or_none(proto, "user_function"),
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, proto: args.new_transformation_pb2.NewTransformationArgs) -> TransformationSpec:
        return cls(
            name=proto.info.name,
            id=id_helper.IdHelper.to_string(proto.transformation_id),
            transformation_mode=proto.transformation_mode,
            user_function=utils.get_field_or_none(proto, "user_function"),
        )
