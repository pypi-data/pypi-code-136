from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from datetime import datetime
from typing import TypedDict


class BirthDateTimeError(Exception):
    pass


class BirthDateTime:

    def __init__(self, birth_datetime: datetime) -> None:
        self.__birth_datetime = birth_datetime

    @property
    def date(self) -> str:
        return str(self.__birth_datetime.date())

    @property
    def time(self) -> str:
        return str(self.__birth_datetime.time())

    @classmethod
    def create(cls, birth_datetime: datetime):
        if birth_datetime < datetime.now():
            return cls(birth_datetime)
        raise BirthDateTimeError('Invalid birth datetime')


class SignsCalculatorResult(TypedDict):
    label: str
    sign: str
    icon: str


class ISignsCalculator(ABC):

    @abstractproperty
    def sun(self) -> SignsCalculatorResult:
        raise NotImplementedError()

    @abstractproperty
    def ascendant(self) -> SignsCalculatorResult:
        raise NotImplementedError()
