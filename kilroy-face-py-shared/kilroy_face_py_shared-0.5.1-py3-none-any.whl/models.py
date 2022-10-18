from abc import ABC

from humps import camelize
from pydantic import BaseModel, Extra


class SerializableModel(BaseModel, ABC):
    def json(self, *args, by_alias: bool = True, **kwargs) -> str:
        return super().json(*args, by_alias=by_alias, **kwargs)

    class Config:
        allow_population_by_field_name = True
        alias_generator = camelize
        extra = Extra.allow
