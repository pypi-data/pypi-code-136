from typing import TypeVar, Any, Union, Dict, Tuple, Optional

from pydantic.main import BaseModel as PydanticModel

from .base import ModelProtocol
from .fields import ModelFieldsMixin
from .local_cache import ModelLocalCacheMixin

CreateSchemaType = TypeVar('CreateSchemaType', bound=PydanticModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=PydanticModel)


class Model(ModelProtocol, ModelLocalCacheMixin, ModelFieldsMixin):
    class Meta(ModelFieldsMixin.Meta):
        pass

    @classmethod
    def has_cache(cls):
        return False

    @classmethod
    async def get_or_create(cls, id_value: Any,
                            data: Union[CreateSchemaType, Dict[str, Any]], **kwargs) \
            -> Tuple[Optional['Model'], bool]:
        if instance := await cls.get(id_value, **kwargs):
            return instance, False
        else:
            return await cls.create(data, **kwargs), True
