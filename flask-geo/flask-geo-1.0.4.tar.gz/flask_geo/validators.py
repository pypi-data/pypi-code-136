from abc import ABC, abstractmethod
import pytz
import pycountry
import re


class IValidator(ABC):

    _next_validator = None

    def set_next(self, validator):
        self._next_validator = validator
        return validator

    @abstractmethod
    def is_valid(self) -> bool:
        if self._next_validator:
            self._next_validator.is_valid()
        return True


class TimezoneValidator(IValidator):

    def __init__(self, value: str) -> None:
        self.value = value

    def is_valid(self) -> bool:
        if self.value in pytz.all_timezones:
            return super().is_valid()
        return False


class CountryCodeValidator(IValidator):

    def __init__(self, value) -> None:
        self.value = value

    def is_valid(self) -> bool:
        country_codes = [country.alpha_2 for country in pycountry.countries]
        if self.value in country_codes:
            return super().is_valid()
        return False


class CityNameValidator(IValidator):

    def __init__(self, value: str) -> None:
        self.value = value

    def is_valid(self) -> bool:
        city_name_re = re.compile(r'^\D+, \D+$')
        if city_name_re.findall(self.value):
            return super().is_valid()
        return False
