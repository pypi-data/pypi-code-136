_singleton_instances = {}


def create_sentinel(name: str, value_as_bool: bool = True):
    """
        Convenience method.

        Creates a Singleton class, with class name set to passed in name.
        Allocated the singleton instance of that type, and returns the instance.

        Doing this:

        >>> MyGuard = create_sentinel('MyGuard')

        Is equivelent to doing this:

        >>> class MyGuardType(Singleton):
        ...     pass
        >>> MyGuard = MyGuardType()

        Except, you don't have an attribute set to the 'type'; you just have the sentinel object.
    """
    return type(name, (Singleton,), value_as_bool=value_as_bool)()


class Singleton:
    """
    This can be used as the superclass that should always be a Singleton no mater what.
    Example of something you may want to make a true singleton is a sentinel-type, like
    the `NoneType` that Python has.

    See the `default-type.Default` for an example of how you can use this,
    or the following code example:

    ```
    class DefaultType(Singleton):
        pass

    Default = DefaultType()
    ```

    Class Arguments:

    - name: You can provide a name for instances of the type, this is what they will return from
        `__repr__` for the object's description.

        By default, if you don't provide this we take the class name, and strip off the word
        `"Type"` and the end of class name (if present at end of class name). Whatever is left
        is what we return for by default for this `name` argument.

    - value_as_bool: Default's to `True`. The value provided here is what is returned from
        `__bool__`. This is what Python uses as the bool value for the object.
        Consider overriding this to False if you want to make a sentential type-objects.

        It seems like sentential type-objects normally want to be False like. 

        Similar to why `None` has False as it's bool-value.

        You can override by setting `value_as_bool=True` as a class argument, ie:

        ```python
        from guards import Singleton

        class MySingletonType(Singleton, value_as_bool=True)
            pass

        # Will now be `True` like when used as a bool.
        assert MySingletonType()

        ```

    """

    def __new__(cls, *args, **kwargs):
        singletons = _singleton_instances
        if cls not in singletons:
            singletons[cls] = super().__new__(cls, *args, **kwargs)
        return singletons[cls]

    def __init_subclass__(cls, name: str = None, value_as_bool: bool = False, **kwargs):
        super().__init_subclass__(**kwargs)
        if not name:
            name = cls.__name__
            if name.endswith("Type") and len(name) > 4:
                name = name[:-4]

        cls._name = name
        cls._value_as_bool = value_as_bool

    def __repr__(self):
        return self._name

    def __bool__(self):
        return self._value_as_bool

    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        return self

