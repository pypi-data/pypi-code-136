from typing import Any, List, Iterable

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def only_one_field_set_validator(instance: Any, fields: List[str], raise_exception: bool = False) -> bool:
    """
    Проверяет, что instance имеет ровно одно установленное поле из fields,
    в случае если это не так генерирует ValidationError c нужным сообщением об ошибке
    :param instance:
    :param fields:
    :param raise_exception
    :return:
    """
    found_non_empty_field = False

    for field in fields:
        if getattr(instance, field, None) is not None:
            if found_non_empty_field:
                if raise_exception:
                    raise ValidationError(
                        _("Only one of %(fields)s must be set for %(instance_class)s")
                        % {"instance_class": type(instance).__name__, "fields": ", ".join(fields)}
                    )
                else:
                    return False
            else:
                found_non_empty_field = True

    if not found_non_empty_field:
        if raise_exception:
            raise ValidationError(
                _("At least one of %(fields)s must be set for %(instance_class)s")
                % {"instance_class": type(instance).__name__, "fields": ", ".join(fields)}
            )
        else:
            return False

    return True


def no_more_than_fields_set_validator(
    instance: Any, fields: List[str], count: int = 1, raise_exception: bool = False
) -> bool:
    """
    Проверяет, что instance имеет не больше count установленных полей из fields,
    в случае если это не так генерирует ValidationError c нужным сообщением об ошибке
    :param instance:
    :param fields:
    :param count:
    :param raise_exception
    :return:
    """
    found_non_empty_fields_count = 0

    for field in fields:
        if getattr(instance, field, None) is not None:
            found_non_empty_fields_count += 1
            if found_non_empty_fields_count > count:
                if raise_exception:
                    raise ValidationError(
                        _("No more than %(count)s of %(fields)s must be set for %(instance_class)s")
                        % {"instance_class": type(instance).__name__, "fields": ", ".join(fields), "count": count}
                    )
                else:
                    return False
    return True


def instances_field_value_validator(
    instances_list: Iterable[Any], field: str, value: Any, raise_exception: bool = True
) -> bool:
    """
    Проверяет, что каждый instance из списка содержит в себе определённое поле с определённым значением.
    В противном случае генерирует сообщение об ошибке ValidationError либо возвращает False
    :param instances_list:
    :param field:
    :param value:
    :param raise_exception:
    :return:
    """
    for instance in instances_list:
        instance_field = getattr(instance, field, None)
        if not instance_field or instance_field != value:
            if raise_exception:
                raise ValidationError(
                    _("Values of field %(field)s of instances in list are not the same as required")
                    % {
                        "field": field,
                    }
                )
            else:
                return False
    return True
