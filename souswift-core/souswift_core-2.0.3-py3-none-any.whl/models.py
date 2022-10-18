from typing import Generic, TypeVar

import fastapi
import orjson
import pydantic
import pydantic.generics

from souswift_core.utils import string


def _orjson_dumps(val, *, default=None):
    return orjson.dumps(val, default=default).decode()


class Model(pydantic.BaseModel):
    class Config:
        allow_population_by_field_name = True
        json_loads = orjson.loads
        json_dumps = _orjson_dumps
        frozen = True

        @classmethod
        def alias_generator(cls, field: str):
            return string.to_camel(field.removesuffix('_'))


class FrozenModel(Model):
    """Same as Model, just for compatibility"""


T = TypeVar('T', bound=Model)


class Details(FrozenModel):
    last_id: int | None = None
    total_pages: int | None = None
    info: str | None = None
    total_left: int | None = None


class BaseResponse(pydantic.generics.GenericModel, Generic[T]):
    data: list[T]
    details: Details | None = pydantic.Field(default_factory=Details)


class Page(FrozenModel):
    last_id: int = fastapi.Query(0, ge=0)
    per_page: int = fastapi.Query(20, ge=5, le=100)


class BaseError(Model):
    title: str
    path: str
    status: int
    detail: str
