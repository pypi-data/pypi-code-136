"""
The Exceptions test module.

This module contains tests for Exceptions.
"""

import pytest

from tcgplayer.exceptions import AuthenticationError, ServiceError
from tcgplayer.service import TCGPlayer


def test_unauthorized():
    """Test 401 Unauthorized raises an AuthenticationError."""
    session = TCGPlayer("Invalid", "Invalid", "Invalid", cache=None)
    with pytest.raises(AuthenticationError):
        session.list_categories()


def test_not_found(session: TCGPlayer):
    """Test 404 Not Found raises a ServiceError."""
    with pytest.raises(ServiceError):
        session._get_request(endpoint="/invalid")


def test_timeout(client_id, client_secret, access_token: str):
    """Test a TimeoutError for slow responses."""
    session = TCGPlayer(
        client_id=client_id,
        client_secret=client_secret,
        access_token=access_token,
        timeout=0.1,
        cache=None,
    )
    with pytest.raises(ServiceError):
        session.list_categories()
