"""
The Rarity test module.

This module contains tests for Rarity objects.
"""
import pytest

from tcgplayer.exceptions import ServiceError
from tcgplayer.service import TCGPlayer


def test_category_rarities(session: TCGPlayer):
    """Test using the category rarity endpoint with a valid category id."""
    results = session.list_category_rarities(category_id=1)
    result = [x for x in results if x.rarity_id == 3]
    assert len(result) == 1
    assert result[0].rarity_id == 3

    assert result[0].display_text == "Uncommon"
    assert result[0].db_value == "U"


def test_invalid_category_rarities(session: TCGPlayer):
    """Test using the category rarity endpoint with an invalid category id."""
    with pytest.raises(ServiceError):
        session.list_category_rarities(category_id=-1)
