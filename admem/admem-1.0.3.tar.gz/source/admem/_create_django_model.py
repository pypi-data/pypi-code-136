# Copyright (c) 2022 Mario S. Könz; License: MIT
import dataclasses as dc
import datetime
import enum
import types
import typing as tp

from django.db import models

from ._decorator import BACKEND_LINKER
from ._util import public_name

__all__ = ["CreateDjangoModel", "create_django_model"]


@dc.dataclass
class CreateDjangoModel:
    dataclass: type

    def __post_init__(self) -> None:
        # evaluate the Meta class
        pk_key, unique_together = self.extract_meta()
        # translate fields
        fields: dict[str, tp.Any] = self.translate_fields(pk_key)
        fields["Meta"] = self.generate_meta(unique_together)
        fields["__module__"] = fields["Meta"].app_label
        django_model = type(self.dataclass.__name__, (models.Model,), fields)
        BACKEND_LINKER.link(self.dataclass, django_model)

    def extract_meta(self) -> tuple[str | None, list[str] | None]:
        pk_key, unique_together = None, None
        if hasattr(self.dataclass, "Meta"):
            meta = self.dataclass.Meta  # type: ignore
            if hasattr(meta, "primary_key"):
                pk_key = meta.primary_key
            if hasattr(meta, "unique_together"):
                unique_together = meta.unique_together

        return pk_key, unique_together

    def translate_fields(
        self, pk_key: str | None
    ) -> "dict[str, models.Field[tp.Any, tp.Any]]":
        fields = {}
        for field in dc.fields(self.dataclass):
            django_field, opts = self.django_field_precursor(field.type)
            if field.name == pk_key:
                opts["primary_key"] = True
                if django_field is models.ForeignKey:
                    django_field = models.OneToOneField

            fields[field.name] = django_field(**opts)
        return fields

    def generate_meta(self, unique_together: list[str] | None) -> type:
        class Meta:
            app_label = public_name(self.dataclass, without_cls=True)
            db_table = public_name(self.dataclass)

        if unique_together:
            Meta.unique_together = unique_together  # type: ignore

        return Meta

    @classmethod
    def django_field_precursor(
        cls, type_: type
    ) -> "tuple[type[models.Field[tp.Any, tp.Any]], dict[str, tp.Any]]":
        # pylint: disable=too-many-return-statements,too-many-branches
        if type_ == str:
            return models.CharField, dict(max_length=1024)
        if type_ == int:
            return models.IntegerField, {}
        if type_ == float:
            return models.FloatField, {}
        if type_ == datetime.datetime:
            return models.DateTimeField, {}
        if type_ == datetime.date:
            return models.DateField, {}
        if type_ == datetime.time:
            return models.TimeField, {}
        if type_ == bytes:
            return models.BinaryField, dict(editable=True)
        if type_ == bool:
            return models.BooleanField, {}

        if isinstance(type_, types.GenericAlias):
            origin = tp.get_origin(type_)
            subtypes = tp.get_args(type_)
            if origin is set:
                assert len(subtypes) == 1
                subtype = subtypes[0]
                try:
                    fk_class = BACKEND_LINKER.backend_class(subtype)
                    assert issubclass(fk_class, models.Model)
                    return models.ManyToManyField, dict(to=fk_class, related_name="+")
                except KeyError:
                    pass

        if isinstance(type_, types.UnionType):
            target_type, none_type = tp.get_args(type_)
            if none_type is type(None):
                field, kwgs = cls.django_field_precursor(target_type)
                kwgs["blank"] = True
                kwgs["null"] = True
                return field, kwgs

        if issubclass(type_, enum.Enum):
            max_length = 256
            choices = []
            for val in type_.__members__.values():
                choices.append((val.value, val.value))
                assert len(val.value) < max_length

            return models.CharField, dict(max_length=max_length, choices=choices)

        try:  # try Foreign Key relation (many-to-one)
            fk_class = BACKEND_LINKER.backend_class(type_)
            assert issubclass(fk_class, models.Model)
            return models.ForeignKey, dict(
                to=fk_class, on_delete=models.CASCADE, related_name="+"
            )

        except KeyError:
            pass

        raise NotImplementedError(type_)


def create_django_model(dataclass: type) -> type:
    CreateDjangoModel(dataclass)
    return dataclass
