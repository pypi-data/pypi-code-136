from flask import (Blueprint, render_template, request, Response, redirect,
                   url_for)
from datetime import datetime
from .repositories import CityRepository
from .forms import SignsCalculatorForm
from .adapters import SignsCalculator
from .domain import BirthDateTime
from .utils import parse_date, parse_time

bp = Blueprint(
    'signs_calculator',
    __name__,
    url_prefix='/calculadora-astrologica',
    template_folder='templates',
    static_folder='static',
)


@bp.get('/')
def index() -> Response:
    return render_template('signs_calculator/index.html',
                           form=SignsCalculatorForm())


@bp.post('/resultado')
def result() -> Response:
    city = CityRepository().get_by_name(request.form['city'])
    calculator = SignsCalculator(create_birth_datetime(), city)
    return render_template(
        'signs_calculator/result.html',
        result=[calculator.sun, calculator.ascendant],
    )
    return redirect(url_for('.index', error_message='Dados invalidos'))


def create_birth_datetime() -> BirthDateTime:
    year, month, day = parse_date(request.form['birth_date'])
    hour, minute = parse_time(request.form['birth_time'])
    if request.form.get('not_know_the_time'):
        hour, minute = (12, 0)
    return BirthDateTime.create(datetime(year, month, day, hour, minute))
