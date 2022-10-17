from flask import (Blueprint, render_template, request, Response, redirect,
                   url_for, current_app)
from datetime import datetime
from .forms import SignsCalculatorForm
from .adapters import SignsCalculator
from .domain import BirthDateTime, BirthDateTimeError
from .utils import parse_date, parse_time

bp = Blueprint(
    'signs_calculator',
    __name__,
    url_prefix='/calculadora-astrologica',
    template_folder='templates',
    static_folder='static',
)


@bp.get('/')
@bp.get('/completa')
def index() -> Response:
    return render_template(
        'signs_calculator/index.html',
        form=SignsCalculatorForm(),
        complete_result='true' if 'completa' in request.url else 'false')


@bp.post('/resultado')
def result() -> Response:
    city = current_app.geo.city_repository.get_by_name(request.form['city'])
    try:
        calculator = SignsCalculator(create_birth_datetime(), city)
    except BirthDateTimeError:
        return redirect(url_for('.index', error_message='Dados invalidos'))
    complete = True if request.form['complete_result'] == 'true' else False
    return render_template('signs_calculator/result.html',
                           result=calculator.get_results(complete=complete))


def create_birth_datetime() -> BirthDateTime:
    year, month, day = parse_date(request.form['birth_date'])
    hour, minute = parse_time(request.form['birth_time'])
    if request.form.get('not_know_the_time'):
        hour, minute = (12, 0)
    return BirthDateTime.create(datetime(year, month, day, hour, minute))
