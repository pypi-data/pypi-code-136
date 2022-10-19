"""
The Category test module.

This module contains tests for Category objects.
"""
from cardtrader.service import CardTrader


def test_categories(session: CardTrader):
    """Test using the category list endpoint."""
    results = session.categories()
    result = [x for x in results if x.category_id == 1]
    assert len(result) == 1
    assert result[0].category_id == 1

    assert result[0].name == "Magic Single Card"
    assert result[0].game_id == 1
    assert result[0].properties is not None


def test_categories_with_game_id(session: CardTrader):
    """Test using the category list endpoint filtered by a valid game id."""
    results = session.categories(game_id=6)
    result = [x for x in results if x.category_id == 80]
    assert len(result) == 1
    assert result[0].category_id == 80

    assert result[0].name == "Flesh and Blood Single Card"
    assert result[0].game_id == 6
    assert result[0].properties is not None


def test_categories_with_invalid_game_id(session: CardTrader):
    """Test using the category list endpoint filtered by an invalid game id."""
    results = session.categories(game_id=-1)
    assert results == []
