from typing import Any, Optional, List, Dict, Set, Union

from rest_framework import serializers


def create_serializer_class(name, fields):
    return type(name, (serializers.Serializer,), fields)


def inline_serializer(*, fields, data=None, **kwargs):
    serializer_class = create_serializer_class(name="", fields=fields)

    if data is not None:
        return serializer_class(data=data, **kwargs)

    return serializer_class(**kwargs)


class QueryFieldsSetupMixin(serializers.Serializer):
    """
    Миксина для обеспечения управления полями сериалайзера для вывода на основе
    переменных query (get) запроса в адресной строке
    """

    def __init__(self, *args, fields: Optional[Union[tuple, list]] = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._fields_to_serialize = fields

    def get_field_names(self, *args, **kwargs):
        fields_to_serialize = self._fields_to_serialize
        if fields_to_serialize is None:
            default_fields_config = getattr(self.Meta, "default_fields", None)
            if default_fields_config is not None:
                fields_to_serialize = tuple(default_fields_config)
        if fields_to_serialize is None:
            fields_to_serialize = super().get_field_names(*args, **kwargs)
        return self.update_fields_to_serialize_by_request_query_params(fields_to_serialize)

    def update_fields_to_serialize_by_request_query_params(self, fields_to_serialize: Union[list, tuple]) -> list[str]:
        if not self.check_serializer_context():
            return fields_to_serialize

        direct_fields_list = self.get_direct_fields_list()
        if direct_fields_list is not None:
            return self.get_validated_fields(direct_fields_list)
        else:
            expand_fields = self.get_fields_to_expand() or []
            exclude_fields = self.get_fields_to_exclude() or []

            new_fields = [field for field in fields_to_serialize if field not in exclude_fields]
            new_fields += [field for field in expand_fields if field not in new_fields]
            return self.get_validated_fields(new_fields)

    def get_serializer_available_fields(self) -> Set[str]:
        return set(list(getattr(self.Meta, "fields", [])))

    def get_validated_fields(self, fields: List[str]) -> List[str]:
        available_fields = self.get_serializer_available_fields()
        return [field for field in fields if field in available_fields]

    def get_request_query_params(self) -> Dict[str, Any]:
        return getattr(self.get_request_from_context(), "query_params", {})

    def get_field_from_query_param_value(self, query_param: str) -> Optional[List[str]]:
        query_param_value: str = self.get_request_query_params().get(query_param, None)
        if query_param_value is None:
            return None
        return [field.strip().lower() for field in query_param_value.split(",") if field.strip()]

    def get_fields_to_expand(self) -> Optional[List[str]]:
        return self.get_field_from_query_param_value(query_param="expand")

    def get_fields_to_exclude(self) -> Optional[List[str]]:
        return self.get_field_from_query_param_value(query_param="exclude")

    def get_direct_fields_list(self) -> Optional[List[str]]:
        return self.get_field_from_query_param_value(query_param="fields")

    def get_request_from_context(self):
        return self.context.get("request", None)

    def check_serializer_context(self) -> bool:
        if self.get_request_from_context():
            return True
        return False


class DefaultOutputSerializer(QueryFieldsSetupMixin, serializers.Serializer):
    pass


class DefaultOutputModelSerializer(QueryFieldsSetupMixin, serializers.ModelSerializer):
    """
    Обычный сериалийзер для вывода информации о сущности на основе модели
    """

    pass


class DefaultCreateSerializer(serializers.Serializer):
    pass


class DefaultSetSerializer(serializers.Serializer):
    pass


class DefaultUpdateSerializer(serializers.Serializer):
    pass
