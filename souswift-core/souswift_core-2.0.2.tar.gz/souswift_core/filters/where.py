from __future__ import annotations

import typing
from dataclasses import dataclass
from enum import Enum

import sqlalchemy as sa
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy.sql.elements import BooleanClauseList

from souswift_core.filters import cp
from souswift_core.filters.base import Filter
from souswift_core.providers import Driver


def _attr(
    entity: type | sa.Table, field: str
) -> sa.Column | RelationshipProperty:
    try:
        result = getattr(entity, field, None) or getattr(
            typing.cast(sa.Table, entity).c, field, None
        )
    except AttributeError:
        raise AttributeError(f'{entity} does not have field {field}') from None
    else:
        if result is None:
            raise NotImplementedError
        return result


@dataclass
class Field(Filter):
    field: str
    value: typing.Any | None
    comp: cp.Comparison = cp.Equal()
    enum_value: bool = False
    sql_func: typing.Callable[[sa.Column], typing.Any] | None = None

    def similar_to(self, where: Filter) -> typing.TypeGuard[Field]:
        return (
            self.field == where.field
            if isinstance(where, type(self))
            else False
        )

    def __post_init__(self):
        if self.field == 'id':
            self.field = 'id_'
        if isinstance(self.value, bool) and not isinstance(self.comp, cp.Null):
            self.value = sa.true() if self.value else sa.false()
        if isinstance(self.value, Enum):
            if self.enum_value:
                self.value = self.value and self.value.value
            else:
                self.value = self.value and self.value.name

    def where(self, entity: type | sa.Table):
        return self.attr(entity)  # type: ignore

    def attr(self, entity: type | sa.Table):
        if not self:
            return True
        attr = self.retrieve_attr(entity)
        if self.sql_func:
            attr = self.sql_func(attr)  # type: ignore
        return self.comp.compare(attr, self.value)

    def retrieve_attr(self, entity: type | sa.Table):
        return _attr(entity, self.field)

    def __bool__(self):
        return self.value is not None


@dataclass(init=False)
class FilterJoins(Filter):
    operator: type[BooleanClauseList]
    filters: tuple[Filter, ...]

    def __init__(self, *filters: Filter) -> None:
        self.filters = filters

    def where(self, entity: type | sa.Table):
        return self.operator(*(f.where(entity) for f in self.filters))

    def __bool__(self):
        return True


class Or(FilterJoins):
    @property
    def operator(self):
        return sa.or_


class And(FilterJoins):
    @property
    def operator(self):
        return sa.and_


def _entity_from_foreign(attr: sa.Column | RelationshipProperty) -> type:
    return attr.entity.class_


@dataclass(frozen=True)
class ForeignField(Filter):
    field: str
    comp: cp.RelatedComp

    def where(self, entity: type):
        related_attr = _attr(entity, self.field)
        related_entity = _entity_from_foreign(related_attr)
        return self.comp.compare(related_entity, related_attr)

    def __bool__(self):
        return self.comp.__bool__()


class EmptyFilter(Filter):
    def __bool__(self):
        return True


class FilterIterator(Filter):
    def __init__(self, *filters: Filter):
        self._filter = And(*filters)

    def __bool__(self):
        return bool(self._filter)

    def where(self, entity: type | sa.Table):
        return self._filter.where(entity)

    def fields(self):
        return list(self._fields())

    def _fields(self, _filter: FilterJoins | None = None):
        if not _filter:
            _filter = self._filter
        for item in _filter.filters:
            if not item:
                continue
            if isinstance(item, FilterJoins):
                yield from self._fields(item)
            else:
                yield typing.cast(Field, item).field


class DateFilter:
    def __init__(self, driver: Driver):
        self._driver = driver

    @staticmethod
    def format(date_part: int):
        return str(date_part).zfill(2)

    def day(self, column: sa.Column):
        if self._driver is Driver.SQLITE:
            return sa.func.strftime('%d', column)
        return sa.extract('DAY', column)

    def month(self, column: sa.Column):
        if self._driver is Driver.SQLITE:
            return sa.func.strftime('%m', column)
        return sa.extract('MONTH', column)


class JSONFilter:
    def __init__(self, driver: Driver):
        self._driver = driver

    @property
    def contains(self):
        return (
            cp.AlwaysTrue()
            if self._driver is Driver.SQLITE
            else cp.JSONContains()
        )

    @property
    def empty(self):
        return (
            cp.AlwaysTrue()
            if self._driver is Driver.SQLITE
            else cp.EmptyJson()
        )
