#!/usr/bin/env python
# coding: utf-8

from nopea.exceptions import MaxLengthError
from nopea.managers import RelatedManager


class Unresolved:
    pass


class DbField(object):
    def __new__(cls, *args, **kwargs):
        if len(args) > 0:
            cls.adaptor = args[0].adaptor
            cls.fieldname = cls.__name__.lower()
        return super().__new__(cls)

    def __init__(self):
        self.value = Unresolved()

    def make_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_drop_column_query(self, base=None):
        # Must be a function for sqlite
        return self.adaptor.get_drop_column_query(self, base)


class PkField(DbField):

    def __init__(self):
        self.fieldname = 'id'

    @property
    def partial_create_table_query(self):
        return self.adaptor.get_pkfield_create_query()


class IntegerField(DbField):

    def __init__(self, default=None):
        self.default = default

    @property
    def partial_create_table_query(self):
        return self.adaptor.get_integer_field_create_query(self)

    @property
    def add_column_query(self):
        return self.adaptor.get_integer_field_create_column_query(self)


class CharField(DbField):

    def __init__(self, max_length, default=None):
        if not isinstance(max_length, int) or max_length < 1:
            raise MaxLengthError("On CharFields max_length must be set and it must be a positive integer")
        self.max_length = max_length
        self.default = default

    @property
    def partial_create_table_query(self):
        return self.adaptor.get_char_field_create_query(self)

    @property
    def add_column_query(self):
        return self.adaptor.get_charfield_create_column_query(self)


class TextField(DbField):

    def __init__(self, default=""):
        self.default = default

    @property
    def partial_create_table_query(self):
        return self.adaptor.get_text_field_create_query(self)

    @property
    def add_column_query(self):
        return self.adaptor.get_text_field_create_column_query(self)


class BooleanField(DbField):

    def __init__(self, default):
        self.default = default

    @property
    def partial_create_table_query(self):
        return self.adaptor.get_boolean_field_create_query(self.default)

    @property
    def add_column_query(self):
        return self.adaptor.get_boolean_field_create_column_query(self)


class DateTimeField(DbField):

    def __init__(self, default=None):
        self.default = default

    @property
    def partial_create_table_query(self):
        return self.adaptor.get_datetime_field_create_query(self.default)

    @property
    def add_column_query(self):
        raise NotImplementedError("Still not implemented")


class ForeignKey(DbField):

    def __init__(self, reference_class, reverse_name=None, lazy=False, on_delete=''):
        self.reference_class = reference_class
        self.reverse_name = reverse_name
        self.lazy = lazy
        self.on_delete = on_delete

    def set_related_manager(self, target):
        if not self.reverse_name:
            self.reverse_name = target.__class__.__name__.lower() + '_set'
        setattr(self.reference_class, self.reverse_name, RelatedManager(target, self.fieldname, self.reverse_name))

    def make_value(self, value):
        if not self.lazy:
            if value:
                reference_obj = self.reference_class.objects.filter(id=value)
                if not reference_obj.exists():
                    self.value = None
                self.value = reference_obj[0]
        else:
            self.value = ReverseLazy(value, self.reference_class)

    def __get__(self, instance, owner):
        return self

    def get_value(self):
        if self.lazy:
            return self.value().id
        return self.value

    @property
    def partial_create_table_query(self):
        return self.adaptor.get_foreignkey_field_create_query_base()

    @property
    def partial_create_table_query_extension(self):
        return self.adaptor.get_foreignkey_field_create_query_extension(self.reference_class, self.on_delete)

    @property
    def add_column_query(self):
        raise NotImplementedError("Still not implemented")


class ReverseLazy:
    def __init__(self, value, reference_class):
        self.value = value
        self.reference_class = reference_class

    def __call__(self):
        if self.value:
            reference_obj = self.reference_class.objects.filter(id=self.value)
            if not reference_obj.exists():
                return None
            return reference_obj[0]
        return self
