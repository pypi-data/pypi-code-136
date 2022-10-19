"""
The Blueprint test module.

This module contains tests for Blueprint objects.
"""

from cardtrader.service import CardTrader


def test_blueprints(session: CardTrader):
    """Test using the blueprint endpoint with a valid expansion id."""
    results = session.blueprints(expansion_id=1)
    result = [x for x in results if x.blueprint_id == 6]
    assert len(result) == 1
    assert result[0].blueprint_id == 6

    assert result[0].name == "Ghalta, Primal Hunger"
    assert result[0].version is None
    assert result[0].game_id == 1
    assert result[0].category_id == 1
    assert result[0].expansion_id == 1
    assert result[0].card_market_id == 366585
    assert result[0].tcg_player_id == 180397
    assert result[0].scryfall_id == "b2a93747-720a-4ddf-8325-36db78e0a584"
    assert result[0].fixed_properties is not None
    assert result[0].editable_properties is not None


def test_null_pricing_ids(session: CardTrader):
    """Test the blueprint endpoint a blueprint that has a null pricing id."""
    results = session.blueprints(expansion_id=2591)
    result = [x for x in results if x.blueprint_id == 169160]
    assert len(result) == 1
    assert result[0].blueprint_id == 169160

    assert result[0].card_market_id == 650781
    assert result[0].tcg_player_id == 234001
    assert result[0].scryfall_id is None
