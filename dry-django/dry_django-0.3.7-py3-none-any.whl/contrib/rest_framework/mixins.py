from typing import Any, Union, Type, Optional

from django.core.exceptions import (
    ObjectDoesNotExist,
    ValidationError,
)
from django.db import IntegrityError
from django.db.models import QuerySet, Model
from django.http import QueryDict
from django.utils.translation import gettext_lazy as _
from django_filters import FilterSet
from rest_framework import exceptions as rest_exceptions
from rest_framework.pagination import BasePagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status as http_statuses

from dry_django.contrib.rest_framework.utils import get_error_message
from dry_django.contrib.rest_framework.pagination import LimitOffsetPagination
from dry_django.selectors.generic import ModelSelector
from dry_django.services import ModelService

DEFAULT_FILTERS_SET_CLASS_NAME = "FilterSet"
DEFAULT_PAGINATION_CLASS = LimitOffsetPagination


class ApiErrorsMixin:
    """
    Миксина для трансформации исключений Python и Django в соответствующие исключения DRF,
    иначе они будут возвращать 500 код ответа, что не желательно.

    Миксина предназначена для использования в связке с APIView.
    """

    expected_exceptions = {
        ObjectDoesNotExist: rest_exceptions.NotFound,
        IntegrityError: rest_exceptions.ValidationError,
        ValueError: rest_exceptions.ValidationError,
        ValidationError: rest_exceptions.ValidationError,
        PermissionError: rest_exceptions.PermissionDenied,
    }

    def handle_exception(self, exc):
        if isinstance(exc, tuple(self.expected_exceptions.keys())):
            drf_exception_class = self.expected_exceptions[exc.__class__]
            drf_exception = drf_exception_class(get_error_message(exc))

            return super().handle_exception(drf_exception)

        return super().handle_exception(exc)


class ApiFiltersMixin:
    """
    Миксина для уменьшения шаблонного кода при работе с фильтрацией данных
    в get запросах.
    Определяет метод get_validated_filters для представлений на основе APIView,
    который позволяет получить словарь с провалидированными фильтрами на основе
    параметров запроса (get параметров).
    """

    def get_filtered_queryset(
        self, queryset: QuerySet[Any], *, filterset_class: Optional[Union[str, Type[FilterSet]]] = None
    ) -> QuerySet[Any]:
        """
        Возвращает QuerySet с фильтрами на основе параметров запроса (get параметров).
        Для валидации используется filterset_class.

        :param queryset: QuerySet для фильтрации
        :param filterset_class: Класс или имя класса FilterSet, если используется
            имя класса, то по нему ищется класс сериалайзера объявленный внутри класса представления.

        :return: Отфильтрованный на базе фильтров QuerySet
        """
        if filterset_class is None:
            filterset_class = DEFAULT_FILTERS_SET_CLASS_NAME
        if not isinstance(filterset_class, str) and not issubclass(filterset_class, FilterSet):
            raise TypeError(_("filterset_class must be str or class inherited from" " django_filters.FilterSet"))

        if isinstance(filterset_class, str):
            filterset_class = getattr(self, filterset_class, None)
            if filterset_class is None:
                return queryset

        if filterset_class is None or self.request is None:
            return queryset

        if not issubclass(filterset_class, FilterSet):
            raise TypeError(_("filterset_class must be inherited from" " django_filters.FilterSet class"))

        filterset = filterset_class(queryset=queryset, data=self.request.query_params, request=self.request)
        return filterset.qs


class ApiPaginatedResponseMixin:
    """
    Миксина для обеспечения функционала по пагинации List запросов,
    выполняемых через метод get в представлениях на базе APIView
    """

    def get_paginated_response(
        self,
        queryset,
        *,
        pagination_class: Type[BasePagination] = None,
        serializer_class: Type[Serializer] = None,
        serializer_context: dict[str, Any] = None,
        filterset_class: Optional[Union[str, Type[FilterSet]]] = None,
        as_raw_data: bool = False,
    ) -> Response:
        if pagination_class is None:
            pagination_class = getattr(self, "Pagination", None)
            if pagination_class is None:
                pagination_class = DEFAULT_PAGINATION_CLASS
        if not issubclass(pagination_class, BasePagination):
            raise AttributeError(
                _("pagination_class must be inherited from" " rest_framework.pagination.BasePagination class.")
            )

        if serializer_class is None:
            serializer_class = getattr(self, "OutputSerializer", None)
            if serializer_class is None:
                raise AttributeError(
                    _(
                        "serializer_class set as None by default,"
                        " but view class don't implements OutputSerializer class."
                    )
                )
        if not issubclass(serializer_class, Serializer):
            raise AttributeError(
                _("serializer_class must be inherited from" " rest_framework.serializers.Serializer class.")
            )

        paginator = pagination_class()
        if getattr(self, "get_filtered_queryset", None) is not None:
            queryset = self.get_filtered_queryset(queryset=queryset, filterset_class=filterset_class)

        page = paginator.paginate_queryset(queryset=queryset, request=self.request, view=self)

        if serializer_context is None:
            serializer_context = {}
        serializer_context.setdefault("request", self.request)

        if page is not None:
            serializer = serializer_class(page, many=True, read_only=True, context=serializer_context)
            if as_raw_data:
                return paginator.get_paginated_data(serializer.data)
            return paginator.get_paginated_response(serializer.data)

        serializer = serializer_class(queryset, many=True, read_only=True, context=serializer_context)
        if as_raw_data:
            return serializer.data
        return Response(data=serializer.data)


class ApiDefaultMixin(ApiPaginatedResponseMixin, ApiFiltersMixin, ApiErrorsMixin):
    """
    Миксина с набором базовых миксин необходимого для большинства APIView  представлений
    """

    def get_request_data_as_list(self, request):
        request_data = request.data
        if isinstance(request_data, QueryDict):
            request_data = [element for element in request_data.values()]
        return request_data


##############################################
#   Generic Operations Mixins
##############################################


class ModelLogicBaseAPIMixin:
    selector_class: Type[ModelSelector]
    service_class: Type[ModelService]


class _ModelRetrieveBase(ModelLogicBaseAPIMixin):
    retrieve_serializer: Type[Serializer]

    def serialize_obj(self, obj: Model) -> dict:
        return self.retrieve_serializer(obj, read_only=True).data

    def get_object(self, request: Request, *args, **kwargs):
        return self.selector_class().get(pk=args[0])


class ModelListAPIMixin(ApiPaginatedResponseMixin, ModelLogicBaseAPIMixin):
    list_item_serializer: Optional[Type[Serializer]] = None

    def get(self, request, *args, **kwargs):
        return self.get_paginated_response(
            queryset=self.get_list_items_queryset(request, *args, **kwargs), serializer_class=self.list_item_serializer
        )

    def get_list_items_queryset(self, request: Request, *args, **kwargs):
        return self.selector_class().list_all()


class ModelRetrieveAPIMixin(ApiPaginatedResponseMixin, _ModelRetrieveBase, ModelLogicBaseAPIMixin):
    def get(self, request, *args, **kwargs):
        obj = self.get_object(request, *args, **kwargs)
        return Response(self.serialize_obj(obj))


class ModelCreateAPIMixin(ApiPaginatedResponseMixin, _ModelRetrieveBase, ModelLogicBaseAPIMixin):
    create_request_body_serializer: Type[Serializer]

    def post(self, request, *args, **kwargs):
        request_data = self.parse_request_body_for_create(request, *args, **kwargs)
        obj = self.perform_create(request, *args, request_data=request_data, **kwargs)
        return Response(self.serialize_obj(obj))

    def parse_request_body_for_create(self, request, *args, **kwargs) -> dict:
        data = request.data
        if data is None:
            return {}
        serializer = self.create_request_body_serializer(data)
        serializer.is_valid(raise_exception=True)
        return serializer.data

    def perform_create(self, request: Request, *args, request_data: dict, **kwargs) -> Model:
        service = self.service_class()
        service.create(**request_data)
        return service.instance


class ModelUpdateAPIMixin(ApiPaginatedResponseMixin, _ModelRetrieveBase, ModelLogicBaseAPIMixin):
    update_request_body_serializer: Type[Serializer]

    def put(self, request, *args, **kwargs):
        obj = self.get_object(request, *args, **kwargs)
        request_data = self.parse_request_body_for_update(request, *args, **kwargs)
        obj = self.perform_update(obj, request, *args, request_data=request_data, **kwargs)
        return Response(self.serialize_obj(obj), status=http_statuses.HTTP_200_OK)

    def parse_request_body_for_update(self, request, *args, **kwargs) -> dict:
        data = request.data
        if data is None:
            return {}
        serializer = self.update_request_body_serializer(data)
        serializer.is_valid(raise_exception=True)
        return serializer.data

    def perform_update(self, obj: Model, request: Request, *args, request_data: dict, **kwargs) -> Model:
        service = self.service_class(instance=obj)
        service.update(**request_data)
        return service.instance


class ModelDestroyAPIMixin(ApiPaginatedResponseMixin, _ModelRetrieveBase, ModelLogicBaseAPIMixin):
    def delete(self, request, *args, **kwargs):
        obj = self.get_object(request, *args, **kwargs)
        self.perform_destroy(obj, request, *args, **kwargs)
        return Response(status=http_statuses.HTTP_204_NO_CONTENT)

    def perform_destroy(self, obj: Model, request: Request, *args, **kwargs) -> None:
        service = self.service_class(instance=obj)
        service.destroy()
