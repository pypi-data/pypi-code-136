from flatlib import const, chart, datetime, geopos

from .domain import ISignsCalculator, BirthDateTime, SignsCalculatorResult
from flask_geo.domain import ICity


class SignsCalculator(ISignsCalculator):

    def __init__(self, birth_datetime: BirthDateTime, city: ICity) -> None:
        utcoffset = city.get_utcoffset()
        birth_datetime = datetime.Datetime(birth_datetime.date.replace('-', '/'),
                                           birth_datetime.time, utcoffset)
        birth_geopos = geopos.GeoPos(city.latitude, city.longitude)
        self.chart = chart.Chart(birth_datetime, birth_geopos)

    @property
    def sun(self) -> SignsCalculatorResult:
        return {'label': 'Signo', **self.get_result_for(const.SUN)}

    @property
    def ascendant(self) -> SignsCalculatorResult:
        return {'label': 'Ascendente', **self.get_result_for(const.ASC)}

    def get_result_for(self, sign_type: str) -> dict:
        sign = self.chart.get(sign_type).sign
        base_url = '/calculadora-astrologica/static/signs_calculator/signs_icons'
        return {'sign': sign, 'icon_url': f'{base_url}/{sign.lower()}_small.webp'}
