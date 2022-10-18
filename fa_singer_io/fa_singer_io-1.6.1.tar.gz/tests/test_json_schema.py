from fa_purity import (
    JsonValue,
)
from fa_purity.frozen import (
    freeze,
)
from fa_purity.json.factory import (
    from_unfolded_dict,
)
from fa_purity.json.primitive.core import (
    PrimitiveTypesList,
)
from fa_singer_io.json_schema.factory import (
    datetime_schema,
    from_json,
    from_prim_type,
    opt_datetime_schema,
    opt_prim_type,
)

MOCK_SCHEMA = from_json(
    from_unfolded_dict(
        freeze(
            {
                "properties": freeze(
                    {"foo": JsonValue(from_prim_type(int).encode())}
                )
            }
        )
    )
)


def test_mock_schema() -> None:
    valid = freeze({"foo": JsonValue(123)})
    invalid = freeze({"foo": JsonValue("text")})
    assert MOCK_SCHEMA.unwrap().validate(valid).unwrap() is None
    assert MOCK_SCHEMA.unwrap().validate(invalid).unwrap_fail()


def test_from_prim_type() -> None:
    for t in PrimitiveTypesList:
        assert from_prim_type(t)


def test_opt_prim_type() -> None:
    for t in PrimitiveTypesList:
        assert opt_prim_type(t)


def test_datetime_schema() -> None:
    assert datetime_schema()


def test_opt_datetime_schema() -> None:
    assert opt_datetime_schema()
