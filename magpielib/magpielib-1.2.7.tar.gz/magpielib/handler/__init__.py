import json
from urllib import parse


def gen_get_url(uri, arguments):
    """获取get 生成 url
    """
    flag = '&' if '?' in uri else '?'
    for key, value in arguments.items():
        if isinstance(value, str):
            continue
        arguments[key] = json.dumps(value)
    uri_p = uri + '%s%s' % (flag, parse.urlencode(arguments))
    return uri_p
