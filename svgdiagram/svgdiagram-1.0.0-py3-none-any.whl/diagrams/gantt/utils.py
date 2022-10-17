from datetime import date, datetime
import re


def str_to_date_datetime(date_string):
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_string):
        return date.fromisoformat(date_string)
    else:
        return datetime.fromisoformat(date_string)


def date_datetime_to_str(date_datetime):
    return date_datetime.isoformat()
