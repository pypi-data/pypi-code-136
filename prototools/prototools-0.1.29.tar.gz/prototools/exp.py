import inspect
import sys


def retrieve_argname(var: object) -> str:
    """Retrieve the name of the argument passed to the function.

    Args:
        var (object): The argument passed to the function.
    Returns:
        str: The name of the argument.

    Example:

        >>> def foo(a):
                n = retrieve_argname(a)
        ...     return f"{n}'s value is {a}"
        ...
        >>> x = 42
        >>> foo(x)
        'x's value is 42
    """
    callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
    return [
        var_name for var_name, var_val in callers_local_vars if var_val is var
    ][0]


def retrive_varname(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [
        var_name for var_name, var_val in callers_local_vars if var_val is var
    ][0]


def return_names(name=None):
    if not name:
        raise ValueError("Argument 'name' is required")
    return [n for n in sys.modules[name].__dict__ if not n.startswith("__")]


class Maybe:
    """
    Example:

        >>> from prototools.exp import Maybe
        >>> f = lambda x: x + 3
        >>> r = Maybe(2)|f|f
        >>> print(r)
        8
    """

    def __init__(self, value=None, containes_value=True):
        self.value = value
        self.contains_value = containes_value

    def bind(self, func):
        if not self.contains_value:
            return Maybe(None, False)
        try:
            result = func(self.value)
            return Maybe(result)
        except:
            return Maybe(None, False)

    def __or__(self, func):
        return self.bind(func)

    def __str__(self):
        if self.contains_value and self.value is not None:
            return str(self.value)
        else:
            return "Nothing"

    def get(self):
        return self.value
