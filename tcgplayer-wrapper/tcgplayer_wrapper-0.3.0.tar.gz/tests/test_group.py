"""
The Groups test module.

This module contains tests for Group objects.
"""

from datetime import date

import pytest

from tcgplayer.exceptions import ServiceError
from tcgplayer.service import TCGPlayer


def test_category_groups(session: TCGPlayer):
    """Test using the category groups endpoint with a valid category id."""
    results = session.list_category_groups(category_id=1)
    result = [x for x in results if x.group_id == 1882]
    assert len(result) == 1
    assert result[0].group_id == 1882

    assert result[0].name == "Amonkhet"
    assert result[0].abbreviation == "AKH"
    assert result[0].is_supplemental is False
    assert result[0].published_on == date(2017, 4, 28)
    assert result[0].category_id == 1


def test_invalid_category_groups(session: TCGPlayer):
    """Test using the category groups endpoint with an invalid category id."""
    with pytest.raises(ServiceError):
        session.list_category_groups(category_id=-1)


def test_group(session: TCGPlayer):
    """Test using the group endpoint with a valid group id."""
    result = session.group(group_id=1)
    assert result.group_id == 1

    assert result.name == "10th Edition"
    assert result.abbreviation == "10E"
    assert result.is_supplemental is False
    assert result.published_on == date(2007, 7, 13)
    assert result.category_id == 1


def test_invalid_group(session: TCGPlayer):
    """Test using the group endpoint with an invalid group id."""
    with pytest.raises(ServiceError):
        session.group(group_id=-1)
