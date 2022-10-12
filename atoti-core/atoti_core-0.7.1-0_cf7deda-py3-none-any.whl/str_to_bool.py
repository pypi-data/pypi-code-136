_TRUE_VALUES = tuple(str(value).lower() for value in [True, 1])
_FALSE_VALUES = tuple(str(value).lower() for value in [False, 0])

# Stricter version of the deprecated `distutils.strtobool()`.
# See https://www.python.org/dev/peps/pep-0632/.
def str_to_bool(value: str) -> bool:
    """Convert a string to a boolean."""
    value = value.lower()

    if value in _TRUE_VALUES:
        return True

    if value in _FALSE_VALUES:
        return False

    raise ValueError(
        f"Expected one of {_TRUE_VALUES} or {_FALSE_VALUES} but received {value}."
    )
