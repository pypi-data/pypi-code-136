from enum import Enum as StandardEnum
from enum import Flag as StandardFlag
from enum import IntEnum as StandardIntEnum
from enum import IntFlag as StandardIntFlag
from types import DynamicClassAttribute as dynamic_attribute
from typing import Any, Dict, Iterator, Type, TypeVar, Union

from enum_extensions.constants import (
    DEFAULT_BOUND,
    DEFAULT_ENCODING,
    DEFAULT_ERRORS,
    DEFAULT_REVERSE,
)
from enum_extensions.enums import case_fold_name_next_value
from enum_extensions.string import case_fold_name, create_title
from enum_extensions.types import Nullable, is_null, null
from enum_extensions.typing import is_string

__all__ = ("Enum", "IntEnum", "StringEnum", "StrEnum", "Flag", "IntFlag")

E = TypeVar("E", bound="Enum")


class Enum(StandardEnum):
    """Derived from the standard [`enum.Enum`][enum.Enum], emulating functionality of the
    [`enum_extensions.Enum`][enum_extensions.enums.Enum].
    """

    @dynamic_attribute
    def title_name(self) -> str:
        """See [`title_name`][enum_extensions.enums.Enum.title_name]."""
        return create_title(self.name)

    @classmethod
    def fetch_case_fold_names(cls: Type[E]) -> Dict[str, E]:
        return {case_fold_name(name): member for name, member in cls.__members__.items()}

    @classmethod
    def is_empty(cls) -> bool:
        """See [`is_empty`][enum_extensions.enums.EnumType.is_empty]."""
        return not cls.__members__

    @classmethod
    def iter_members(cls: Type[E], reverse: bool = DEFAULT_REVERSE) -> Iterator[E]:
        """See [`iter_members`][enum_extensions.enums.EnumType.iter_members]."""
        return reversed(cls) if reverse else iter(cls)  # type: ignore

    @classmethod
    def from_name(cls: Type[E], name: str) -> E:
        """See [`from_name`][enum_extensions.enums.EnumType.from_name]."""
        return cls.fetch_case_fold_names()[case_fold_name(name)]

    @classmethod
    def from_value(cls: Type[E], value: Any, default: Nullable[Any] = null) -> E:  # type: ignore
        """See [`from_value`][enum_extensions.enums.EnumType.from_value]."""
        try:
            return cls(value)

        except ValueError:
            if is_null(default):
                raise

            return cls(default)

    @classmethod
    def from_data(cls: Type[E], data: Any, default: Nullable[Any] = null) -> E:  # type: ignore
        """See [`from_data`][enum_extensions.enums.EnumType.from_data]."""
        if is_string(data):
            try:
                return cls.from_name(data)

            except KeyError:
                pass

        return cls.from_value(data, default)


class IntEnum(StandardIntEnum, Enum):
    """Derived from the standard [`enum.IntEnum`][enum.IntEnum], emulating functionality of the
    [`enum_extensions.IntEnum`][enum_extensions.enums.IntEnum].
    """


buffer = Union[bytes, bytearray, memoryview]

S = TypeVar("S", bound="StringEnum")


class StringEnum(str, Enum):
    """Derived from the standard string enumeration, emulating functionality of the
    [`enum_extensions.StringEnum`][enum_extensions.enums.StringEnum].
    """

    def __new__(
        cls: Type[S], item: Any, encoding: str = DEFAULT_ENCODING, errors: str = DEFAULT_ERRORS
    ) -> S:
        if is_string(item):
            value = item

        else:  # pragma: no cover
            value = str(item, encoding, errors)

        member = str.__new__(cls, value)

        member._value_ = value

        return member

    _generate_next_value_ = case_fold_name_next_value  # type: ignore


StrEnum = StringEnum
"""An alias of [`StringEnum`][enum_extensions.standard.StringEnum]."""


F = TypeVar("F", bound="Flag")


class Flag(StandardFlag, Enum):
    """Derived from the standard [`enum.Flag`][enum.Flag], emulating functionality of the
    [`enum_extensions.Flag`][enum_extensions.flags.Flag].
    """

    @classmethod
    def from_names(cls: Type[F], *names: str) -> F:
        """See [`from_names`][enum_extensions.flags.FlagType.from_names]."""
        result = cls(0)

        for name in names:
            result |= cls.from_name(name)

        return result

    @classmethod
    def from_values(cls: Type[F], *values: int, bound: bool = DEFAULT_BOUND) -> F:
        """See [`from_values`][enum_extensions.flags.FlagType.from_values]."""
        result = cls(0)

        if bound:
            for value in values:
                result |= cls.from_value(value)

        else:
            for value in values:
                result |= cls.from_value(value, 0)

        return result

    @classmethod
    def from_multiple_data(
        cls: Type[F], *multiple_data: Union[int, str], bound: bool = DEFAULT_BOUND
    ) -> F:
        """See [`from_multiple_data`][enum_extensions.flags.FlagType.from_multiple_data]."""
        result = cls(0)

        if bound:
            for data in multiple_data:
                result |= cls.from_data(data)

        else:
            for data in multiple_data:
                result |= cls.from_data(data, 0)

        return result


class IntFlag(StandardIntFlag, Flag):  # type: ignore
    """Derived from the standard [`enum.IntFlag`][enum.IntFlag], emulating functionality of the
    [`enum_extensions.IntFlag`][enum_extensions.flags.IntFlag].
    """
