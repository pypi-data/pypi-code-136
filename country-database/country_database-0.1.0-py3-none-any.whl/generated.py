from dataclasses import dataclass

from .generics import CountryPropertiesBase
from .property import Property


@dataclass(frozen=True)
class CountryProperties(CountryPropertiesBase):
    name: Property
