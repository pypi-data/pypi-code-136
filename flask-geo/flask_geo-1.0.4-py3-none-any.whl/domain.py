from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ICity(ABC):
    id: int
    name: str
    timezone: str
    latitude: float
    longitude: float

    @abstractmethod
    def get_utcoffset(self) -> str:
        raise NotImplementedError()


class ICityRepository(ABC):

    @abstractmethod
    def get_by_name(self, name: str) -> ICity | None:
        raise NotImplementedError()


@dataclass
class State:
    id: int
    code: str
    name: str
    cities: list[ICity]


@dataclass
class Country:
    id: int
    code: str
    name: str
    states: list[State]
    cities: list[ICity]


class ICountryRepository(ABC):

    @abstractmethod
    def get_by_code(self, code: str) -> Country | None:
        raise NotImplementedError()

    @abstractmethod
    def all(self) -> list[Country]:
        raise NotImplementedError()
