from flask import current_app as app, url_for
from flatlib import const, chart, datetime, geopos
from flask_geo.domain import ICity

from .domain import ISignsCalculator, BirthDateTime, Result


RESULTS_TYPES = [
    {'label': 'Signo', 'const': const.SUN},
    {'label': 'Ascendente', 'const': const.ASC},
]


COMPLETE_RESULTS_TYPES = RESULTS_TYPES + [
    {'label': 'Lua', 'const': const.MOON},
    {'label': 'Mercúrio', 'const': const.MERCURY},
    {'label': 'Vênus', 'const': const.VENUS},
    {'label': 'Marte', 'const': const.MARS},
    {'label': 'Júpiter', 'const': const.JUPITER},
    {'label': 'Saturno', 'const': const.SATURN},
    {'label': 'Nó Norte', 'const': const.NORTH_NODE},
    {'label': 'Nó Sul', 'const': const.SOUTH_NODE},
    {'label': 'Sizígia', 'const': const.SYZYGY},
    {'label': 'Pars Fortuna', 'const': const.PARS_FORTUNA},
]


SIGNS_TRANSLATED = {
    'Aries': 'Áries',
    'Taurus': 'Touro',
    'Gemini': 'Gêmeos',
    'Cancer': 'Cancer',
    'Leo': 'Leão',
    'Virgo': 'Virgem',
    'Libra': 'Libra',
    'Scorpio': 'Escorpião',
    'Sagittarius': 'Sagitario',
    'Capricorn': 'Capricornio',
    'Aquarius': 'Aquário',
    'Pisces': 'Peixes',
}


class SignsCalculator(ISignsCalculator):

    def __init__(self, birth_datetime: BirthDateTime, city: ICity) -> None:
        utcoffset = city.get_utcoffset()
        birth_datetime = datetime.Datetime(
            birth_datetime.date.replace('-', '/'), birth_datetime.time,
            utcoffset)
        birth_geopos = geopos.GeoPos(city.latitude, city.longitude)
        self.chart = chart.Chart(birth_datetime, birth_geopos)

    def get_results(self, complete: bool = False) -> list[Result]:
        result = [Result(t['label'], **self.get_result_for(t['const'])) for t in RESULTS_TYPES]
        if complete:
            result = [Result(t['label'], **self.get_result_for(t['const'])) for t in COMPLETE_RESULTS_TYPES]
        return result

    def get_result_for(self, sign_type: str) -> dict:
        sign = self.chart.get(sign_type).sign
        with app.app_context():
            return {
                'sign': SIGNS_TRANSLATED[sign],
                'icon_url': url_for('signs_calculator.static', filename=f'signs_calculator/signs_icons/{sign.lower()}_small.webp'),
            }
