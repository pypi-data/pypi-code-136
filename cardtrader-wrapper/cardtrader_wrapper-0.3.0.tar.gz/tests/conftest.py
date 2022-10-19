"""
The conftest module.

This module contains pytest fixtures.
"""

import os

import pytest

from cardtrader.service import CardTrader
from cardtrader.sqlite_cache import SQLiteCache


@pytest.fixture(scope="session")
def access_token():
    """Set the CardTrader access token fixture."""
    return os.getenv("CARDTRADER__ACCESS_TOKEN", default="Invalid")


@pytest.fixture(scope="session")
def session(access_token) -> CardTrader:
    """Set the CardTrader session fixture."""
    return CardTrader(access_token, cache=SQLiteCache("tests/cache.sqlite", expiry=None))
