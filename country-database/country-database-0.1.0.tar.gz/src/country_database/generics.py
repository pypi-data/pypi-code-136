from dataclasses import dataclass
from dataclasses import fields
from dataclasses import is_dataclass
from typing import Type
from typing import TypeVar

from .dataloader import CountryCode
from .dataloader import DataLoader
from .dataloader import default_dataloader
from .property import Property


@dataclass(frozen=True)
class CountryPropertiesBase(CountryCode):
    _dataloader: "DataLoader"
    locale: str

    def __post_init__(self):
        # trick: hide "_dataloader" from asdict output
        self.__dataclass_fields__.pop("_dataloader", None)

    def lookup(self, name: str) -> Property:
        """Lookup a property value of the current country, with default locale `en`.

        Args:
            name: name of the property

        Returns:
            The named property.
        """
        return Property(
            loader=self._dataloader,
            country_code=self.alpha3_code,
            name=name,
            locale=self.locale,
        )

    def to_locale(self, locale: str):
        return load_country_generic(
            type(self),
            self.alpha3_code,
            locale=locale,
            loader=self._dataloader,
        )


T_CountryProperties = TypeVar("T_CountryProperties", bound=CountryPropertiesBase)
T_CountryIndex = TypeVar("T_CountryIndex", bound=dataclass)


def load_country_generic(
    country_cls: Type[T_CountryProperties],
    fuzzy_code: str,
    locale: str = "en",
    loader: DataLoader = default_dataloader,
) -> T_CountryProperties:
    """Load a country from the database.

    Args:
        fuzzy_code: can be alpha-3 code, alpha-2 code, or numeric code.
        locale: the default locale of the property values.
        country_cls: a dataclass representing a country with named properties.
        loader: the dataloader.

    Returns:
        The country data.

    Raises:
        KeyError: if the country is not found.
    """
    code = loader.lookup_country_code(fuzzy_code)
    if code is None:
        raise KeyError(f"Country code `{fuzzy_code}` not found")

    if not is_dataclass(country_cls):
        raise ValueError(f"country_cls `{country_cls}` must be a frozen dataclass")

    # memo_key = (alpha3_code, locale)
    # if memo_key in __memo:
    #     return __memo[memo_key]

    kwargs = {
        "_dataloader": loader,
        "locale": locale,
        "alpha2_code": code.alpha2_code,
        "alpha3_code": code.alpha3_code,
        "numeric_code": code.numeric_code,
    }
    for fld in fields(country_cls):
        if fld.name in kwargs:
            continue

        kwargs[fld.name] = Property(
            loader=loader,
            country_code=code.alpha3_code,
            name=fld.name,
            locale=locale,
        )

    data = country_cls(**kwargs)
    # __memo[memo_key] = data
    return data


def load_countries_generic(
    index_cls: Type[T_CountryIndex],
    locale: str = "en",
    loader: DataLoader = default_dataloader,
) -> T_CountryIndex:
    orig_index_cls = index_cls
    country_cls = None

    # Unfold generic types.
    if hasattr(index_cls, "__origin__"):
        orig_index_cls = getattr(index_cls, "__origin__")
        generic_args = getattr(index_cls, "__args__", tuple())
        assert (
            len(generic_args) == 1
        ), "only generic types with 1 parameter are allowed in this context"
        country_cls = generic_args[0]

    if not is_dataclass(orig_index_cls):
        raise ValueError(f"`{orig_index_cls}` must be a dataclass")

    kwargs = {}
    for fld in fields(orig_index_cls):
        kwargs[fld.name] = load_country_generic(
            country_cls or fld.type,
            fld.name,
            locale=locale,
            loader=loader,
        )

    return index_cls(**kwargs)
