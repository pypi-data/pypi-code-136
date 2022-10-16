from datetime import date

from boatrace.models.stadium_tel_code import StadiumTelCode


def format_stadium_tel_code_for_query_string(stadium_tel_code: StadiumTelCode):
    return str(stadium_tel_code.value).zfill(2)


def format_date_for_query_string(date: date):
    return date.strftime("%Y%m%d")
