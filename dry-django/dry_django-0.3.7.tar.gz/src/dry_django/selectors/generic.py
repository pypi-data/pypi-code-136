from typing import TypeVar, Generic, Optional, Union, Mapping

from django.db.models import Model, Q, QuerySet
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from dry_core.selectors.generics import Selector


_DjangoModelTypeVar = TypeVar("_DjangoModelTypeVar", bound=Model)


class ModelSelector(Selector[_DjangoModelTypeVar], Generic[_DjangoModelTypeVar]):
    select_related: Optional[Union[list, tuple]] = None
    prefetch_related: Optional[Union[list, tuple]] = None

    def __init__(
        self, select_related: Optional[Union[list, tuple]] = None, prefetch_related: Optional[Union[list, tuple]] = None
    ):
        self.select_related = select_related or self.select_related
        self.prefetch_related = prefetch_related or self.prefetch_related
        self.model_manager = self.model.objects

    def get(self, **kwargs) -> _DjangoModelTypeVar:
        filtered_kwargs = self._filter_kwargs_from_service_fields(kwargs)
        query = Q(**filtered_kwargs)
        try:
            return self.wrap_queryset_with_select_and_prefetch_related(self.model_manager, **kwargs).get(query)
        except self.model.DoesNotExist:
            raise ObjectDoesNotExist(_("%s with params: '%s' not found.") % (self.model.__name__, filtered_kwargs))

    async def aget(self, **kwargs) -> _DjangoModelTypeVar:
        filtered_kwargs = self._filter_kwargs_from_service_fields(kwargs)
        query = Q(**filtered_kwargs)
        try:
            return await self.wrap_queryset_with_select_and_prefetch_related(self.model_manager, **kwargs).aget(query)
        except self.model.DoesNotExist:
            raise ObjectDoesNotExist(_("%s with params: '%s' not found.") % (self.model.__name__, filtered_kwargs))

    def list_all(self, **kwargs) -> QuerySet:
        return self.wrap_queryset_with_select_and_prefetch_related(self.model_manager, **kwargs).all()

    def list_filter(self, **kwargs) -> QuerySet:
        return self.wrap_queryset_with_select_and_prefetch_related(self.model_manager, **kwargs).filter(
            **self._filter_kwargs_from_service_fields(kwargs)
        )

    ################################
    #       Utils & helpers
    ################################

    def wrap_queryset_with_select_and_prefetch_related(self, queryset: QuerySet, **kwargs) -> QuerySet:
        select_related_fields = self._get_select_related_fields_taking_into_kwargs(**kwargs)
        prefetch_related_fields = self._get_prefetch_related_fields_taking_into_kwargs(**kwargs)
        result_queryset = queryset
        if select_related_fields:
            result_queryset = queryset.select_related(*select_related_fields)
        if prefetch_related_fields:
            result_queryset = queryset.prefetch_related(*prefetch_related_fields)
        return result_queryset

    def _get_select_related_fields_taking_into_kwargs(self, **kwargs):
        return kwargs.get("select_related", self.select_related)

    def _get_prefetch_related_fields_taking_into_kwargs(self, **kwargs):
        return kwargs.get("prefetch_related", self.prefetch_related)

    @staticmethod
    def _filter_kwargs_from_service_fields(kwargs: Mapping) -> Mapping:
        return {key: value for key, value in kwargs if key not in ("select_related", "prefetch_related")}


#################################
#################################
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  DEPRECATED WILL BE REMOVED   #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#################################
#################################


class BaseModelSelector(Selector[_DjangoModelTypeVar], Generic[_DjangoModelTypeVar]):
    default_select_related: tuple = ()
    default_prefetch_fields: tuple = ()

    @classmethod
    def _get_select_related_fields(cls, select_related: Optional[tuple[str]] = None) -> tuple[str]:
        return select_related if select_related else cls.default_select_related

    @classmethod
    def _get_prefetch_related_fields(cls, prefetch_related: Optional[tuple[str]] = None) -> tuple[str]:
        return prefetch_related if prefetch_related else cls.default_prefetch_fields

    @classmethod
    def wrap_queryset_with_select_and_prefetch_related(
        cls,
        queryset: QuerySet,
        select_related: Optional[tuple[str]] = None,
        prefetch_related: Optional[tuple[str]] = None,
    ) -> QuerySet:
        return queryset.select_related(*cls._get_select_related_fields(select_related=select_related)).prefetch_related(
            *cls._get_prefetch_related_fields(prefetch_related=prefetch_related)
        )

    @classmethod
    def list_all(
        cls, *, select_related: Optional[tuple[str]] = None, prefetch_related: Optional[tuple[str]] = None
    ) -> QuerySet:
        return cls.wrap_queryset_with_select_and_prefetch_related(
            cls.model.objects, select_related=select_related, prefetch_related=prefetch_related
        ).all()

    @classmethod
    def get_by_id(
        cls, *, id: str, select_related: Optional[tuple[str]] = None, prefetch_related: Optional[tuple[str]] = None
    ) -> _DjangoModelTypeVar:
        query = Q(id=id)
        try:
            return cls.wrap_queryset_with_select_and_prefetch_related(
                cls.model.objects, select_related=select_related, prefetch_related=prefetch_related
            ).get(query)
        except cls.model.DoesNotExist:
            raise ObjectDoesNotExist(_("%s with id = %s not found.") % (cls.model.__name__, id))

    @classmethod
    def list_get_by_ids(
        cls,
        *,
        ids: list[int],
        select_related: Optional[tuple[str]] = None,
        prefetch_related: Optional[tuple[str]] = None,
    ) -> QuerySet:
        return cls.wrap_queryset_with_select_and_prefetch_related(
            cls.model.objects, select_related=select_related, prefetch_related=prefetch_related
        ).filter(id__in=ids)
