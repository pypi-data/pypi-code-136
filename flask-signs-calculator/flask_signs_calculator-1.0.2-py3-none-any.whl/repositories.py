from flask import current_app as app
from flask_geo.adapters import City
from flask_geo.domain import Country, ICityRepository, ICountryRepository
from flask_geo.validators import (CityNameValidator, CountryCodeValidator,
                         TimezoneValidator)

from .models import CityModel, CountryModel


class CityRepository(ICityRepository):

    def get_by_name(self, name: str) -> City | None:
        city = app.db_session.query(CityModel).filter_by(name=name).first()
        validator = CityNameValidator(city.name).set_next(
            TimezoneValidator(city.timezone))
        if city and validator.is_valid():
            return self.to_dataclass(city)

    def to_dataclass(self, model: CityModel) -> City:
        return City(
            id=model.id,
            name=model.name,
            timezone=model.timezone,
            latitude=model.latitude,
            longitude=model.longitude,
        )


class CountryRepository(ICountryRepository):

    def get_by_code(self, code: str) -> Country | None:
        country = app.db_session.query(CountryModel).filter_by(code=code).first()
        if country and CountryCodeValidator(country.code).is_valid():
            return self.to_dataclass(country)

    def all(self) -> list[Country]:
        countries = []
        for country in app.db_session.query(CountryModel).all():
            countries.append(self.to_dataclass(country))
        return countries

    def to_dataclass(self, model: CountryModel) -> Country:
        return Country(
            id=model.id,
            code=model.code,
            name=model.name,
            states=model.states,
            cities=model.cities,
        )
