"""Useful functions for using in templates"""
from functools import reduce

def get_value(variable):
    """If the variable is a callable, it will be called.
    
    :TODO: If the variable is a date or datetime object, it will
    return formatted result.

    This is useful in templates to avoid having to check
    whether a variable is callable or not.
    """
    if callable(variable):
        return get_value(variable())

    return variable


def get_chained_attr(obj, attr):
    """Similar to getattr, but can also do chained lookups
    using double underscores.

    Example:
    
        get_chained_attr(obj, 'foo__bar')
    """
    return reduce(getattr, attr.split('__'), obj)


def get_list_display(attr, model_instance, admin_instance):
    """Function for resolving list headers.

    :param attr: The attribute to resolve.
        + if it's a callable, it will called
        + if it's a string containing double-underscores ('__'),
          first lookup will be done on the db object,
          then on the admin instance.
        + if it's a string without double-underscores,
          first lookup will be done on the admin instance,
          then on the model instance.
        + if it's anything else, it will be returned as is.

    :param model_instance: instance of the model class.

    :param admin_instance: instance of the admin class.
    """
    found = False

    if callable(attr):
        value = get_value(attr(model_instance))
        found = True
    elif not isinstance(attr, str):
        value = get_value(attr)
        found = True

    if not found and '__' in attr:
        # double-underscore means it's most probably a field
        try:
            value = get_value(get_chained_attr(model_instance, attr))
        except AttributeError:
            pass
        else:
            found = True

    if not found:
        if hasattr(admin_instance, attr):
            value = get_value(getattr(admin_instance, attr)(model_instance))
        elif hasattr(model_instance, attr):
            value = get_value(getattr(model_instance, attr))
        else:
            raise ValueError("List header called '%s' couldn't be resolved.\n"
                "Make sure it's either a model field, or an attribute of etither "
                "the model class or the admin class"
                % attr
            )

    return value
