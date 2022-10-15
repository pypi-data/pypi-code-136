import re
from urllib.parse import quote

_to_snake_pattern = re.compile(r'(?!^)([A-Z]+)')
_to_camel_pattern = re.compile(r'_([a-z])')


def to_snake(camel_string: str):
    return _to_snake_pattern.sub('_\1', camel_string)


def to_spaced(camel_string: str):
    return to_snake(camel_string).replace('_', ' ')


def to_camel(string: str):
    string = '_'.join(string.split())
    return _to_camel_pattern.sub(lambda match: match[1].upper(), string)


def urlstring(string: str):
    return quote(string.strip())
