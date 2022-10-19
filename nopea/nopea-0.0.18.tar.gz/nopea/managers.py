#!/usr/bin/env python
# coding: utf-8

from nopea.queryset import QuerySet
from nopea.exceptions import TooManyResultsError, UnknownFieldError


def check_fieldnames(func):
    def wrapper(*args, **kwargs):
        for field in kwargs.keys():
            field = field.split('__')[0]
            if field not in args[0].base.fieldnames:
                raise UnknownFieldError(f"Table {args[0].base.tablename} has no field {field}")
        return func(*args, **kwargs)
    return wrapper


class Manager:

    def __init__(self, base):
        self.base = base
        self.adaptor = self.base.adaptor

    @check_fieldnames
    def filter(self, *args, **kwargs):
        query_set = QuerySet(self.base)
        return query_set.filter(*args, **kwargs)

    @check_fieldnames
    def exclude(self, *args, **kwargs):
        query_set = QuerySet(self.base)
        return query_set.exclude(*args, **kwargs)

    def all(self):
        return self.filter()

    def first(self):
        return self.all().first()

    def last(self):
        return self.all().last()

    def count(self):
        return self.filter().count()

    def exists(self):
        return self.count() > 0

    @check_fieldnames
    def create(self, *args, **kwargs):
        query, query_args = self.adaptor.get_insert_query(self.base, kwargs)
        _, _id = self.adaptor.execute_query(query, query_args)
        return self.get(id=_id)

    def get(self, *args, **kwargs):
        result = self.filter(*args, **kwargs)()

        if len(result) <= 1:
            try:
                return result[0]
            except IndexError:
                raise IndexError("No %s object found" % self.base.__class__.__name__)
        raise TooManyResultsError('To many results for get(): %s' % len(result))

    @check_fieldnames
    def get_or_create(self, *args, **kwargs):
        try:
            return (False, self.get(*args, **kwargs))
        except IndexError:
            return (True, self.create(*args, **kwargs))

    def bulk_create(self, objects):
        self.adaptor.bulk_create(objects, self.base)


class RelatedManager(Manager):

    def __init__(self, target, fieldname, reverse_name):
        self.id = None
        self.base = target
        self.fieldname = fieldname
        target.related_managers[reverse_name] = self

    def filter(self, *args, **kwargs):
        field_filter = {self.fieldname: self.id}
        return super().filter(**field_filter).filter(*args, **kwargs)

    def exclude(self, *args, **kwargs):
        field_filter = {self.fieldname: self.id}
        return super().filter(**field_filter).exclude(*args, **kwargs)

    def bulk_create(self, *args, **kwargs):
        raise NotImplementedError("bulk_create cannot be used on RelatedManagers")
