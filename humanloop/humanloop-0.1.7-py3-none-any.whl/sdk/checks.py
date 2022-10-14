from humanloop.api.models.user import UserResponse
from humanloop.sdk.init import _get_client


def server_health() -> dict:
    client = _get_client()
    return client.health_check()


def user() -> UserResponse:
    client = _get_client()
    return client.read_me()
