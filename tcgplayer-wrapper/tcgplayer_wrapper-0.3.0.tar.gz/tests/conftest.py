"""
The conftest module.

This module contains pytest fixtures.
"""

import os

import pytest

from tcgplayer.exceptions import ServiceError
from tcgplayer.service import TCGPlayer
from tcgplayer.sqlite_cache import SQLiteCache


@pytest.fixture(scope="session")
def client_id():
    """Set the TCGPlayer client id fixture."""
    return os.getenv("TCGPLAYER__CLIENT_ID", default="Invalid")


@pytest.fixture(scope="session")
def client_secret():
    """Set the TCGPlayer client secret fixture."""
    return os.getenv("TCGPLAYER__CLIENT_SECRET", default="Invalid")


@pytest.fixture(scope="session")
def access_token():
    """Set the TCGPlayer access token fixture."""
    return os.getenv("TCGPLAYER__ACCESS_TOKEN", default="Invalid")


@pytest.fixture(scope="session")
def session(client_id, client_secret, access_token) -> TCGPlayer:
    """Set the TCGPlayer session fixture."""
    session = TCGPlayer(
        client_id, client_secret, access_token, cache=SQLiteCache("tests/cache.sqlite", expiry=None)
    )
    try:
        if not session.authorization_check():
            session.generate_token()
    except ServiceError:
        pass
    return session
