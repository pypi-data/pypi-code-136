import googletrans
from datetime import datetime


def translate(text: str, dest: str = 'pt') -> str:
    return googletrans.Translator().translate(text, dest=dest).text


def parse_date(string_date: str) -> tuple[int]:
    result_date = datetime.strptime(string_date, '%Y-%m-%d')
    return result_date.year, result_date.month, result_date.day


def parse_time(string_time: str) -> tuple[int]:
    string_time = ':'.join(string_time.split(':')[:2])
    result_time = datetime.strptime(string_time, '%H:%M')
    return result_time.hour, result_time.minute
