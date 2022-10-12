from __future__ import (
    annotations,
)

from .._utils import (
    all_keys_in,
)
from dataclasses import (
    dataclass,
)
from fa_purity import (
    FrozenDict,
    Result,
    ResultE,
)
from fa_purity.json.value.transform import (
    Unfolder,
)
from fa_purity.pure_iter.factory import (
    from_flist,
)
from fa_singer_io.json_schema import (
    JSchemaFactory,
    JsonSchema,
)
from fa_singer_io.singer.errors import (
    MissingKeys,
)
from typing import (
    FrozenSet,
    Optional,
    Tuple,
)


def _check_keys(
    properties: Optional[FrozenSet[str]],
    key_properties: FrozenSet[str],
    bookmark_properties: Optional[FrozenSet[str]],
) -> ResultE[None]:
    if properties is None:
        return (
            Result.failure(
                Exception(
                    "If not properties then not key_properties nor bookmark_properties at SingerSchema"
                )
            )
            if (bool(key_properties) or bool(bookmark_properties))
            else Result.success(None)
        )
    check_keys = all_keys_in(properties, key_properties).alt(
        lambda m: MissingKeys(m, "schema properties")
    )
    check_bookmarks = all_keys_in(properties, bookmark_properties).alt(
        lambda m: MissingKeys(m, "schema properties")
    )
    return check_keys.bind(lambda _: check_bookmarks).alt(Exception)


@dataclass(frozen=True)
class _Private:
    pass


@dataclass(frozen=True)
class Property:
    schema: JsonSchema
    key_property: bool
    bookmark_property: bool


@dataclass(frozen=True)
class SingerSchema:
    _private: _Private
    stream: str
    schema: JsonSchema
    key_properties: FrozenSet[str]
    bookmark_properties: Optional[FrozenSet[str]]

    @staticmethod
    def new(
        stream: str,
        schema: JsonSchema,
        key_properties: FrozenSet[str],
        bookmark_properties: Optional[FrozenSet[str]],
    ) -> ResultE[SingerSchema]:
        raw = schema.encode()
        props = raw.get("properties", None)
        properties = (
            frozenset(Unfolder(props).to_json().unwrap())
            if props is not None
            else None
        )
        return _check_keys(
            properties, key_properties, bookmark_properties
        ).map(
            lambda _: SingerSchema(
                _Private(), stream, schema, key_properties, bookmark_properties
            )
        )

    @staticmethod
    def obj_schema(
        stream: str, props: FrozenDict[str, Property]
    ) -> SingerSchema:
        schema = FrozenDict({k: v.schema for k, v in props.items()})
        key_properties = (
            from_flist(tuple(props.items()))
            .filter(lambda k: k[1].key_property)
            .map(lambda t: t[0])
            .transform(lambda i: frozenset(i))
        )
        bookmark_properties = (
            from_flist(tuple(props.items()))
            .filter(lambda k: k[1].bookmark_property)
            .map(lambda t: t[0])
            .transform(lambda i: frozenset(i))
        )
        return SingerSchema.new(
            stream,
            JSchemaFactory.obj_schema(schema),
            key_properties,
            bookmark_properties,
        ).unwrap()
