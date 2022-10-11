from flask import Blueprint, jsonify, abort, Response, current_app as app

bp = Blueprint('geo_api', __name__, url_prefix='/geo/api/v1')


@bp.get('/cities/<string:country_code>')
def cities(country_code) -> Response:
    country = app.geo.country_repository.get_by_code(country_code)
    if country:
        return jsonify([city.name for city in country.cities])
    return abort(404)
