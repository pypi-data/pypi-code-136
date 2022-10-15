from typing import TypeVar, Any, Optional
import os


Value = TypeVar("Value")
_NOT_SET = object()


class Env:

    def __init__(
        self,
        name: Optional[str] = None,
        *,
        naming_separator: str = "_",
        nesting_separator: str = ":"
    ):
        self.name = name or ""
        self.naming_separator = naming_separator
        self.nesting_separator = nesting_separator

    def __add__(self, other) -> "Env":
        if isinstance(other, str):
            return Env(self._get_name(other))

        return NotImplemented

    def __repr__(self):
        return (
            f"{type(self).__name__}({self.name!r}, "
            f"naming_separator={self.naming_separator!r}, "
            f"nesting_separator={self.nesting_separator!r})"
        )

    def get(
        self,
        name: str,
        type_: Value = str,
        nested_type: Any = None,
        *,
        default: Value = _NOT_SET
    ) -> Value:
        full_name = self._get_name(name)

        try:
            raw_value = os.environ[full_name]
        except KeyError:
            if default is _NOT_SET:
                raise

            return default

        if nested_type is None:
            return type_(raw_value)
        else:
            return type_(nested_type(i) for i in raw_value.split(self.nesting_separator))

    def _get_name(self, name: str) -> str:
        return self.naming_separator.join((self.name, name)) if self.name else name
