from ._inner import (
    InnerJsonSchema,
)
from dataclasses import (
    dataclass,
)
from decimal import (
    Decimal,
)
from enum import (
    Enum,
)
from fa_purity import (
    FrozenDict,
    FrozenList,
    JsonObj,
    JsonValue,
    Result,
    ResultE,
)
from fa_purity.json.primitive import (
    PrimitiveTypes,
)
from fa_purity.json.transform import (
    to_raw,
)
from fa_singer_io.json_schema.core import (
    JsonSchema,
)
from jsonschema import (
    Draft4Validator,
    SchemaError,
)
from typing import (
    FrozenSet,
)


class SupportedType(Enum):
    array = "array"
    boolean = "boolean"
    integer = "integer"
    null = "null"
    number = "number"
    object = "object"
    string = "string"


_encode_type = {
    bool: SupportedType.boolean,
    int: SupportedType.integer,
    type(None): SupportedType.null,
    Decimal: SupportedType.number,
    float: SupportedType.number,
    str: SupportedType.string,
}


@dataclass(frozen=True)
class JSchemaFactory:
    @staticmethod
    def from_json(raw: JsonObj) -> ResultE[JsonSchema]:
        raw_dict = to_raw(raw)  # type: ignore[misc]
        try:
            Draft4Validator.check_schema(raw_dict)  # type: ignore[misc]
            validator = Draft4Validator(raw_dict)  # type: ignore[misc]
            draft = InnerJsonSchema(raw, validator)
            return Result.success(JsonSchema(draft))
        except SchemaError as err:  # type: ignore[misc]
            return Result.failure(err)

    @classmethod
    def multi_type(
        cls, types: FrozenSet[PrimitiveTypes]
    ) -> ResultE[JsonSchema]:
        if len(types) == 0:
            return Result.failure(Exception("Must specify a type"))
        _types: FrozenList[JsonValue] = tuple(
            JsonValue(_encode_type[t].value) for t in types
        )
        raw = {"type": JsonValue(_types) if len(_types) > 1 else _types[0]}
        return Result.success(cls.from_json(FrozenDict(raw)).unwrap())

    @classmethod
    def from_prim_type(cls, p_type: PrimitiveTypes) -> JsonSchema:
        raw = {"type": JsonValue(_encode_type[p_type].value)}
        return cls.from_json(FrozenDict(raw)).unwrap()

    @classmethod
    def opt_prim_type(cls, p_type: PrimitiveTypes) -> JsonSchema:
        return cls.multi_type(frozenset([p_type, type(None)])).unwrap()

    @classmethod
    def datetime_schema(cls) -> JsonSchema:
        json = {
            "type": JsonValue(_encode_type[str].value),
            "format": JsonValue("date-time"),
        }
        return cls.from_json(FrozenDict(json)).unwrap()

    @classmethod
    def opt_datetime_schema(cls) -> JsonSchema:
        base = cls.opt_prim_type(str).encode()
        json = {
            "type": base["type"],
            "format": JsonValue("date-time"),
        }
        return cls.from_json(FrozenDict(json)).unwrap()

    @staticmethod
    def obj_schema(props: FrozenDict[str, JsonSchema]) -> JsonSchema:
        _props = FrozenDict(
            {k: JsonValue(v.encode()) for k, v in props.items()}
        )
        raw = {
            "properties": JsonValue(_props),
            "required": JsonValue(tuple(JsonValue(k) for k in _props.keys())),
        }
        return JSchemaFactory.from_json(FrozenDict(raw)).unwrap()
