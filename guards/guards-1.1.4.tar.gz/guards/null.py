from typing import Union, TypeVar
from .singleton import Singleton


class NullType(Singleton):
    """
    Used to indicate something accepts `Null` via a type-hint.

    Use `Null` when you need it, this is just the type/class.

    `Null` will evaluate to False, similar to how `None` works.

    Example:
    ```python
        from null_type import Null

        class SomeClass:
            nullable_str = 'default-str'
            some_int = 3

            def json_dict(self):
                json_dict = {}
                if self.nullable_str is not None:
                    json_dict['nullable_str'] = self.nullable_str
                if self.some_int is not None:
                    json_dict['some_int'] = self.some_int

                return {k: v if v is not Null else None for k, v in json_dict.items()}

        obj = SomeClass()
        obj.nullable_str = Null
        obj.some_int = None

        # When getting the json_dict value of object, the original None value in some_int is
        # absent, and None replaced the Null; which is what was intended.
        # Now when json_dict is converted to json-string, python will convert the `None` to json
        # `null` value.
        assert obj.json_dict() == {'nullable_str': None}
    ```
    """
    pass


Null = NullType()
"""
Sentinel object used to represent NULL values to/from APIs, or other similar places.

Useful for when you need to know the difference between None and Null,
such as using None to indicate no value, and Null to indicate a null value.

Example: Useful in models that represent Json values, in that you can tell if the original Json
had any value defined at all vs a null value. 

```python
from null_type import Null

class SomeClass:
    nullable_str = 'default-str'
    some_int = 3

    def json_dict(self):
        json_dict = {}
        if self.nullable_str is not None:
            json_dict['nullable_str'] = self.nullable_str
        if self.some_int is not None:
            json_dict['some_int'] = self.some_int

        return {k: v if v is not Null else None for k, v in json_dict.items()}

obj = SomeClass()
obj.nullable_str = Null
obj.some_int = None

# When getting the json_dict value of object, the original None value in some_int is absent,
# and None replaced the Null; which is what was intended.
# Now when json_dict is converted to json-string, python will convert the `None` to json `null` value.
assert obj.json_dict() == {'nullable_str': None}
```
"""

T = TypeVar('T')

Nullable = Union[T, NullType]
""" Used in type-hints to wrap other type-hints to declare that it could be that
    type or `Null` value. Indicates that a value of Null could be assigned.

    You can use it like so:

    >>> from null_type import Nullable, Null
    >>>
    >>> nullable_string: Nullable[str]
    >>>
    >>> # You can assign a `str` or a `Null` and it will be type-correct:
    >>> nullable_string = "hello!"
    >>> nullable_string = Null
"""
