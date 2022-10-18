from typing import TypeVar, Generic, Optional

from django.db.models import Model, Q, QuerySet
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

from dry_django.selectors.generic import BaseModelSelector

_DjangoModelTypeVar = TypeVar("_DjangoModelTypeVar", bound=Model)


#################################
#################################
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  DEPRECATED WILL BE REMOVED   #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#################################
#################################


class DeprecatedUUIDSelectorMixin(BaseModelSelector[_DjangoModelTypeVar], Generic[_DjangoModelTypeVar]):
    @classmethod
    def get_by_uuid(
        cls, *, uuid: str, select_related: Optional[tuple[str]] = None, prefetch_related: Optional[tuple[str]] = None
    ) -> _DjangoModelTypeVar:
        query = Q(uuid=uuid)
        try:
            return cls.wrap_queryset_with_select_and_prefetch_related(
                cls.model.objects, select_related=select_related, prefetch_related=prefetch_related
            ).get(query)
        except cls.model.DoesNotExist:
            raise ObjectDoesNotExist(_("%s with uuid = %s not found.") % (cls.model.__name__, uuid))

    @classmethod
    def list_get_by_uuids(
        cls,
        *,
        uuids: list[str],
        select_related: Optional[tuple[str]] = None,
        prefetch_related: Optional[tuple[str]] = None,
    ) -> QuerySet:
        return cls.wrap_queryset_with_select_and_prefetch_related(
            cls.model.objects, select_related=select_related, prefetch_related=prefetch_related
        ).filter(uuid__in=uuids)
