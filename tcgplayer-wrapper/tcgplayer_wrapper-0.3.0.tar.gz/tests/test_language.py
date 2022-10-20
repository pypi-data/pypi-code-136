"""
The Category Languages test module.

This module contains tests for Language objects.
"""
import pytest

from tcgplayer.exceptions import ServiceError
from tcgplayer.service import TCGPlayer


def test_category_languages(session: TCGPlayer):
    """Test using the category language endpoint with a valid category id."""
    results = session.list_category_languages(category_id=1)
    result = [x for x in results if x.language_id == 1]
    assert len(result) == 1
    assert result[0].language_id == 1

    assert result[0].name == "English"
    assert result[0].abbreviation == "EN"


def test_invalid_category_languages(session: TCGPlayer):
    """Test using the category language endpoint with an invalid category id."""
    with pytest.raises(ServiceError):
        session.list_category_languages(category_id=-1)
