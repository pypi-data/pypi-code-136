"""
The Exceptions test module.

This module contains tests for Exceptions.
"""

import pytest

from cardtrader.exceptions import AuthenticationError, ServiceError
from cardtrader.service import CardTrader
from cardtrader.sqlite_cache import SQLiteCache


def test_unauthorized():
    """Test a 401 Unauthorized raises an AuthenticationError."""
    session = CardTrader("Invalid", cache=SQLiteCache("tests/cache.sqlite", expiry=None))
    with pytest.raises(AuthenticationError):
        session.info()


def test_not_found(session: CardTrader):
    """Test a 404 Not Found raises a ServiceError."""
    with pytest.raises(ServiceError):
        session._get_request(endpoint="/invalid")


def test_timeout(access_token: str):
    """Test a TimeoutError for slow responses."""
    session = CardTrader(access_token, timeout=0.1, cache=None)
    with pytest.raises(ServiceError):
        session.info()
