import os.path
import requests

from lotr_api.exceptions import LimitExceededException
from lotr_api.response import Response

BASE_URL = "https://the-one-api.dev/v2"
LOOKUPS = {
    "neq": "!=",
    "gt": ">",
    "gte": ">=",
    "lt": "<",
    "lte": "<=",
}


def get_response(path, token, **filters):
    url = os.path.join(BASE_URL, f"{path}?")
    built_filters = __build_filters(**filters)
    url += built_filters

    response, response_json = get(url, token)

    response = Response(
        status=response.status_code, path=path, **response_json, filters=filters
    )
    response.set_token(token)
    return response


def get(url, token):
    try:
        response = requests.get(url, headers={"Authorization": f"Bearer {token}"})
        response.raise_for_status()
    except requests.RequestException as exc:
        if exc.response.status_code == 423:
            raise LimitExceededException() from exc
        raise exc
    return response, response.json()


def __build_filters(**filters):
    query_items = list()
    for key, value in filters.items():
        try:
            lookup_key, lookup_operation = key.split("__")
            try:
                parsed_lookup_operation = LOOKUPS[lookup_operation]
            except KeyError:
                continue
            query_items.append(f"{key}{parsed_lookup_operation}{value}")
        except ValueError:
            query_items.append(f"{key}={value}")
    return "&".join(query_items)
