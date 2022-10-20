import json

from dateutil.parser import parse, ParserError
from unittest.mock import MagicMock

from django.conf import settings


def is_faculty(user):
    if user.is_staff or user.is_superuser:
        return True
    return False


def objects_key_by(iter, key):
    index = {}
    for obj in iter:
        value = getattr(obj, key)
        index[value] = obj
    return index


def parse_date_string(date_string, raise_exception=False):
    try:
        return parse(date_string)
    except (TypeError, ParserError):
        if not raise_exception:
            return
        raise


def masked_dict(obj) -> dict:
    """
    To mask sensitive key / value in log entries.
    masks the value of specified key.

    obj: a dict or a string representation of a dict, or None

    example:
        2022-10-07 20:03:01,455 INFO member_press.client.Client.register_user() request: path=/api/user/v1/account/registration/, data={
            "name": "__Pat_SelfReg-07",
            "username": "__Pat_SelfReg-07",
            "email": "pat.mcguire+Pat_SelfReg-07@cabinetoffice.gov.uk",
            "password": "*** -- REDACTED -- ***",
            "terms_of_service": true
        }

    """

    def redact(key: str, obj):
        if key in obj:
            obj[key] = "*** -- REDACTED -- ***"
        return obj

    obj = obj or {}
    obj = dict(obj)
    for key in settings.MEMBERPRESS_SENSITIVE_KEYS:
        obj = redact(key, obj)
    return obj


class StepwiseJSONEncoder(json.JSONEncoder):
    """
    a custom encoder class.
    - smooth out bumps mostly related to test data.
    - ensure text returned is utf-8 encoded.
    - velvety smooth error handling, understanding that we mostly use
      this class for generating log data.
    """

    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding="utf-8")
        if isinstance(obj, MagicMock):
            return ""
        try:
            return json.JSONEncoder.default(self, obj)
        except Exception:
            # obj probably is not json serializable.
            return ""
