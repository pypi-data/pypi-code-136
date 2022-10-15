from datetime import datetime, timedelta


def today(date_type="str"):
    _today = datetime.today().date()
    if date_type == "str":
        _today = str(_today)
    return _today


def yesterday(date_type="str"):
    _yesterday = datetime.today().date() - timedelta(days=1)
    if date_type == "str":
        _yesterday = str(_yesterday)
    return _yesterday
