import typing as t

from sarus_data_spec.protobuf.attribute_pb2 import Attribute
from sarus_data_spec.protobuf.bounds_pb2 import Bounds
from sarus_data_spec.protobuf.constraint_pb2 import (
    ConstraintKind,
    VariantConstraint,
)
from sarus_data_spec.protobuf.dataset_pb2 import Dataset
from sarus_data_spec.protobuf.manager_pb2 import Manager
from sarus_data_spec.protobuf.marginals_pb2 import Marginals
from sarus_data_spec.protobuf.path_pb2 import Path
from sarus_data_spec.protobuf.predicate_pb2 import Predicate
from sarus_data_spec.protobuf.relation_pb2 import Relation
from sarus_data_spec.protobuf.scalar_pb2 import Scalar
from sarus_data_spec.protobuf.schema_pb2 import Schema
from sarus_data_spec.protobuf.size_pb2 import Size
from sarus_data_spec.protobuf.statistics_pb2 import Distribution, Statistics
from sarus_data_spec.protobuf.status_pb2 import Status
from sarus_data_spec.protobuf.transform_pb2 import Transform
from sarus_data_spec.protobuf.type_pb2 import Type
from sarus_data_spec.protobuf.utilities import (
    copy,
    dejson,
    deserialize,
    dict_deserialize,
    dict_serialize,
    from_base64,
    json,
    json_deserialize,
    json_serialize,
    message,
    message_type,
    serialize,
    to_base64,
    type_name,
    unwrap,
    wrap,
)


def python_proto_factory(string_to_deserialize: str, name: str) -> t.Any:
    proto_type = message(type_name=name)
    proto = from_base64(string_to_deserialize, proto_type)

    if name == type_name(Path):
        import sarus_data_spec.path as path_module

        proto = t.cast(Path, proto)
        return path_module.Path(proto)

    elif name == type_name(Type):
        import sarus_data_spec.type as type_module

        proto = t.cast(Type, proto)
        return type_module.Type(proto)

    raise NotImplementedError(f'current {name} not implemented yet')
