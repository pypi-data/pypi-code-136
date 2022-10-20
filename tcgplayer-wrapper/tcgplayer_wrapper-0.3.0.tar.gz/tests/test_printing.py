"""
The Category Printing test module.

This module contains tests for Printing objects.
"""
import pytest

from tcgplayer.exceptions import ServiceError
from tcgplayer.service import TCGPlayer


def test_category_printings(session: TCGPlayer):
    """Test using the category printing endpoint with a valid category id."""
    results = session.list_category_printings(category_id=1)
    result = [x for x in results if x.printing_id == 1]
    assert len(result) == 1
    assert result[0].printing_id == 1

    assert result[0].name == "Normal"
    assert result[0].display_order == 1


def test_invalid_category_printings(session: TCGPlayer):
    """Test using the category printing endpoint with an invalid category id."""
    with pytest.raises(ServiceError):
        session.list_category_printings(category_id=-1)
