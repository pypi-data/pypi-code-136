"""
Helper functions for mapping model fields to a dictionary of default
keyword arguments that should be used for their equivalent serializer fields.
"""
import inspect

from django.db import models
from django.utils.text import capfirst
from yangson.datatype import DataType, Decimal64Type, EnumerationType
from yangson.schemanode import SchemaNode, InternalNode

NUMERIC_FIELD_TYPES = (
    models.IntegerField, models.FloatField, models.DecimalField, models.DurationField,
)


class ClassLookupDict:
    """
    Takes a dictionary with classes as keys.
    Lookups against this object will traverses the object's inheritance
    hierarchy in method resolution order, and returns the first matching value
    from the dictionary or raises a KeyError if nothing matches.
    """

    def __init__(self, mapping):
        self.mapping = mapping

    def __getitem__(self, key):
        if hasattr(key, '_proxy_class'):
            # Deal with proxy classes. Ie. BoundField behaves as if it
            # is a Field instance when using ClassLookupDict.
            base_class = key._proxy_class
        else:
            base_class = key.__class__

        for cls in inspect.getmro(base_class):
            if cls in self.mapping:
                return self.mapping[cls]
        raise KeyError('Class %s not found in lookup.' % base_class.__name__)

    def __setitem__(self, key, value):
        self.mapping[key] = value


def get_field_kwargs(field_name, model_field):
    """
    Creates a default instance of a basic non-relational field.
    """
    kwargs = {}
    ...
    # validator_kwarg = list(model_field.validators)

    # The following will only be used by ModelField classes.
    # Gets removed for everything else.
    kwargs['model_field'] = model_field
    kwargs['required'] = model_field.mandatory

    if model_field.name:
        kwargs['label'] = capfirst(model_field.name)

    if model_field.default:
        kwargs['default'] = model_field.default

    if isinstance(model_field.type, Decimal64Type):
        decimal_places = getattr(model_field.type, 'fraction_digits', 18)
        kwargs['decimal_places'] = decimal_places
        kwargs['max_digits'] = 19

    if isinstance(model_field.type, EnumerationType):
        choices = tuple(getattr(model_field.type, 'enum', {}))
        kwargs['choices'] = choices

    return kwargs

def get_nested_relation_kwargs(relation_info):
    kwargs = {}
    if relation_info.to_many:
        kwargs['many'] = True
    return kwargs
