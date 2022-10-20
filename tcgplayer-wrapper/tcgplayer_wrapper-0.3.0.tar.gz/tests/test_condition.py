"""
The Category Conditions test module.

This module contains tests for Condition objects.
"""
import pytest

from tcgplayer.exceptions import ServiceError
from tcgplayer.service import TCGPlayer


def test_category_conditions(session: TCGPlayer):
    """Test using the category conditions endpoint with a valid category id."""
    results = session.list_category_conditions(category_id=2)
    result = [x for x in results if x.condition_id == 1]
    assert len(result) == 1
    assert result[0].condition_id == 1

    assert result[0].name == "Near Mint"
    assert result[0].abbreviation == "NM"
    assert result[0].display_order == 1


def test_invalid_category_conditions(session: TCGPlayer):
    """Test using the category conditions endpoint with an invalid category id."""
    with pytest.raises(ServiceError):
        session.list_category_conditions(category_id=-1)
