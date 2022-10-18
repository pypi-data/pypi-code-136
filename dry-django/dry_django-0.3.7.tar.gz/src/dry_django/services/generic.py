from typing import Generic, TypeVar

from django.db.models import Model
from dry_core.services import Service as _BaseService

from . import mixins


__all__ = [
    "ModelService",
]


_DjangoModelTypeVar = TypeVar("_DjangoModelTypeVar", bound=Model)


class ModelService(
    mixins.CreateServiceMixin[_DjangoModelTypeVar],
    mixins.UpdateServiceMixin[_DjangoModelTypeVar],
    mixins.DestroyServiceMixin[_DjangoModelTypeVar],
    mixins.ServiceModelInstanceMixin[_DjangoModelTypeVar],
    _BaseService[_DjangoModelTypeVar],
    Generic[_DjangoModelTypeVar],
):
    """
    Services for Django models with create, update, destroy operations
    """
