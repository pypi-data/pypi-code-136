def docstring(value):
    if not isinstance(value, str):
        value = value.__doc__
    def _doc(func):
        func.__doc__ = value
        return func
    return _doc