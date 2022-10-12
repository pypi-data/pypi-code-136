import requests as _requests


def urltext(url:str):
    try:
        result = requests.get(url).text
    except BaseException:
        result = None
    return result
