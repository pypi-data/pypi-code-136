from typing import List, Dict, Any, Callable


class Tag:
    """A simple `Tag` decorator to tag functions.

    Keeps a list of all tagged functions which can be used to group the
    functions later. A function can be tagged with multiple tags.

    Args:
        tagname: Name of the tag

    Example:
        imp = Tag("imp")
        useless = Tag("useless")

        @imp
        def foo():
            return "foo"

        def bar():
            return "bar"

        @imp
        @useless
        def floo():
            return "floo"


        imp.members == {"foo": foo, "floo": floo}
        useless.members == {"floo": floo}

    """
    def __init__(self, name: str):
        self._name = name
        self._members: Dict[str, Callable] = {}

    @property
    def name(self) -> str:
        return self._name

    @property
    def names(self) -> List[str]:
        return [*self._members.keys()]

    @property
    def members(self) -> Dict[str, Callable]:
        return self._members

    def add(self, f: Callable):
        """Add a function :code:`f` to members

        Args:
            f: Function to add

        """
        if f not in self._members:
            if isinstance(f, property):
                self._members[f.fget.__name__] = f
            else:
                self._members[f.__name__] = f

    def remove(self, fname: str):
        """Remove a function named :code:`fname` to members

        Args:
            f: Function to add

        """
        if fname in self._members:
            self._members.pop(fname)
        else:
            raise AttributeError(f"No such member {fname}")

    def __iter__(self):
        return self._members.__iter__()

    def __call__(self, f: Callable) -> Callable:
        """Add a function `f` to members self being called as a decorator.

        Args:
            f: Function to add

        """
        if f not in self._members:
            if isinstance(f, property):
                self._members[f.fget.__name__] = f
            else:
                self._members[f.__name__] = f
        return f
