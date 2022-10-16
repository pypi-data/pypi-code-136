import re
import unicodedata
import datetime
from urllib.parse import urlencode, parse_qs
from tornado import web, httputil


# Taken from: https://stackoverflow.com/a/41510011/1925257
RE_CAMEL = re.compile(r'''
        # Find words in a string. Order matters!
        [A-Z]+(?=[A-Z][a-z]) |  # All upper case before a capitalized word
        [A-Z]?[a-z]+ |  # Capitalized words / all lower case
        [A-Z]+ |  # All upper case
        \d+  # Numbers
    ''',
    re.VERBOSE
)

def split_camel(value):
    return RE_CAMEL.findall(value)


def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.

    Copied from django.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def get_display_name(obj):
    if isinstance(obj, str):
        value = obj
    elif callable(obj):
        value = obj.__name__
    else:
        value = str(obj)
    return ' '.join(value.split('_')).capitalize()


def replace_qs(source, *args):
    """Replaces parameters in the given querystring. 

    :param source: An instance of any of RequestHandler, HTTPServerRequest, dict 
        or str.
    :param args: Any number of tuples in the formats:
        ('param', 'value')
        ('param', ['value 1', 'value 2']) # set multiple values
        ('param', '') # remove param

    Usage:

        replace_qs(source='q=term', ('page', 1))
        -> q=term&page=1

        replace_qs('q=term', ('page', 1), ('q', ''))
        -> page=1 # q removed
    """

    if isinstance(source, str):
        querystring = source
    elif isinstance(source, web.RequestHandler):
        querystring = source.request.query
    elif isinstance(source, httputil.HTTPServerRequest):
        querystring = source.query
    elif isinstance(source, dict):
        pass
    else:
        raise ValueError("First argument to make_querystring must be an instance of "
            "either RequestHandler or HTTPServerRequest or a dict or a plain "
            "string querystring.")

    if isinstance(source, dict):
        pass
    else:
        param_map = parse_qs(querystring)

    for arg in args:
        # first remove params to be replaced
        param_map.pop(arg[0], None)

    for arg in args:
        if not arg[1]:
            param_map.pop(arg[0], None)
        else:
            if arg[0] in param_map:
                if isinstance(param_map[arg[0]], list):
                    param_map[arg[0]].append(arg[1])
                else:
                    param_map[arg[0]] = [param_map[arg[0]], arg[1]]
            else:
                param_map[arg[0]] = arg[1]

    return urlencode(param_map, doseq=True)


def pluralize(singular, plural, count):
    """Returns the plural if count is not 1::

        pluraize('item', 'items', 1) -> 'item'
        
        pluraize('item', 'items', 2) -> 'items'

        pluraize('item was', 'items were', 2) -> 'items were'

    :param singular: singular form (returned when count in 1)
    :param plural: pular form (returned when count is not 1)
    :param count: a number which denotes how many items
    """
    if count == 1:
        return singular
    return plural
