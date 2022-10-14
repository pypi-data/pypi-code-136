from .singleton import Singleton


class DefaultType(Singleton, value_as_bool=False):
    """
    Use `Default`. This class is an implementation detail, to ensure that there is ever only
    one `Default` value. I based this off how None works in Python [ie: type(None) is NoneType]
    """
    pass


Default = DefaultType()
"""
You can use this as the default value in a method if you want a distinction between the user
passing in `None` and the user not passing in anything
(and in this case, you want to discover/generate/lookup a 'default' value to use).

You can also use this as a placeholder in a list, if it makes sense that there is
a sensible `default` value that can be used in the spot the place holder is at.
This is used when doing an `OrderedDefaultSet`, for example. 

This sensible default can come from a parent object, an environmental variable,
or global default set of values... or some other place.
"""
