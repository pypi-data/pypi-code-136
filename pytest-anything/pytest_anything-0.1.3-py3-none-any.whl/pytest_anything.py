import pytest


@pytest.fixture(scope="session")
def Anything():
    """`Anything` is always Anything."""
    return type.__new__(
        type,
        "Anything",
        (object,),
        {
            "__repr__": lambda self: self.__class__.__name__,
            "__eq__": lambda _, __: True,
        },
    )()


@pytest.fixture(scope="session")
def Something():
    SomethingMeta = type.__new__(
        type,
        "Something",
        (type,),
        {
            "__repr__": lambda cls: cls.__name__,
            "__eq__": lambda _, other: other is not None,
        },
    )

    class Something(metaclass=SomethingMeta):
        """`Something` is not None.
        You can call Something with a test to specialize your assertion.
        """

        def __init__(self, special):
            self.special = special

        def __repr__(self):
            return f"{self.__class__.__name__}({self.special})"

        def __eq__(self, other):
            return self.special(other)

    return Something
