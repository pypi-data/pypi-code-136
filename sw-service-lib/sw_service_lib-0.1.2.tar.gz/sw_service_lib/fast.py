from fastapi import Request

from .client import Client, new_client


def fetch_client_from_request(request: Request) -> Client:
    auth_token = request.headers.get("x-strangeworks-access-token")
    return new_client(auth_token)
