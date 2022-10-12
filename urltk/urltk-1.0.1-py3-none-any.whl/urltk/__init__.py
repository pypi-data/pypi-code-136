import requests as _requests


def urltext(url:str):
    try:
        result = _requests.get(url).text
    except BaseException:
        result = None
    return result
