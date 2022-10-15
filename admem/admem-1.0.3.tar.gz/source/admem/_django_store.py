# Copyright (c) 2022 Mario S. Könz; License: MIT
import dataclasses as dc
import enum
import typing as tp

from django.db import models

from ._decorator import BACKEND_LINKER
from ._protocols import T


@dc.dataclass
class DjangoStore:
    identifier: str

    def dump(self, dc_obj: tp.Any) -> models.Model:
        django_model: type[models.Model] = BACKEND_LINKER.backend_class(dc_obj)
        kwgs, m2m = self.dataclass_to_django(dc_obj)
        dj_obj, created = django_model.objects.using(self.identifier).update_or_create(
            **kwgs
        )

        for key, vals in m2m.items():
            # remove old ones
            if not created:
                getattr(dj_obj, key).clear()
            for val in vals:
                getattr(dj_obj, key).add(self.dump(val))

        return dj_obj  # type: ignore

    def load(self, dataclass: type[T], **filter_kwgs: tp.Any) -> T:
        django_model: type[models.Model] = BACKEND_LINKER.backend_class(dataclass)
        instance = (
            django_model.objects.using(self.identifier).filter(**filter_kwgs).first()
        )
        return self.django_to_dataclass(instance)  # type: ignore

    def dataclass_to_django(self, dc_obj: models.Model) -> tp.Any:
        django_model: type[models.Model] = BACKEND_LINKER.backend_class(dc_obj)
        kwgs = {}
        m2m = {}
        for field in dc.fields(dc_obj):
            key = field.name
            val = getattr(dc_obj, key)
            if type(val) in BACKEND_LINKER.dc_to_backend:
                val = self.dump(val)
            if isinstance(val, enum.Enum):
                val = val.value

            # pylint: disable=protected-access
            dj_model = django_model._meta.get_field(key)
            if isinstance(dj_model, models.ManyToManyField):
                m2m[key] = val
            else:
                kwgs[key] = val

        return kwgs, m2m

    def django_to_dataclass(self, dj_obj: models.Model) -> tp.Any:
        dataclass = BACKEND_LINKER.backend_to_dc[type(dj_obj)]
        obj_kwgs = {}
        for field in dc.fields(dataclass):
            key = field.name
            val = getattr(dj_obj, key)
            if type(val) in BACKEND_LINKER.backend_to_dc:
                val = self.django_to_dataclass(val)
            field = [field for field in dc.fields(dataclass) if field.name == key][0]
            if issubclass(field.type, enum.Enum):
                val = field.type(val)
            # pylint: disable=protected-access
            if isinstance(dj_obj._meta.get_field(key), models.ManyToManyField):
                val = {self.django_to_dataclass(x) for x in val.all()}

            obj_kwgs[field.name] = val
        return dataclass(**obj_kwgs)
