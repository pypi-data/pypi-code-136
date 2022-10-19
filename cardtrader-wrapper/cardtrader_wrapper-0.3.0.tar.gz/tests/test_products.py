"""
The Product test module.

This module contains tests for Product objects.
"""
from cardtrader.service import CardTrader


def test_products_by_expansion(session: CardTrader):
    """Test using the product list by expansion endpoint."""
    results = session.products_by_expansion(expansion_id=1)
    result = [x for x in results if x.product_id == 135198328]
    assert len(result) == 1
    assert results[0].product_id == 135198328

    assert result[0].quantity == 20
    assert result[0].description is None
    assert result[0].blueprint_id == 49464
    assert result[0].expansion is not None
    assert result[0].graded is None
    assert result[0].tag is None
    assert result[0].bundle_size == 4
    assert result[0].on_vacation is False
    assert result[0].seller is not None
    assert result[0].name == "Pilgrim's Eye"
    assert result[0].price is not None
    assert result[0].properties is not None


def test_products_by_blueprint(session: CardTrader):
    """Test using the product list by blueprint endpoint."""
    results = session.products_by_blueprint(blueprint_id=1)
    result = [x for x in results if x.product_id == 127886155]
    assert len(result) == 1
    assert result[0].product_id == 127886155

    assert result[0].quantity == 1
    assert result[0].description == "TBS #1"
    assert result[0].blueprint_id == 1
    assert result[0].expansion is not None
    assert result[0].graded is None
    assert result[0].tag is None
    assert result[0].bundle_size == 1
    assert result[0].on_vacation is False
    assert result[0].seller is not None
    assert result[0].name == "Rampaging Brontodon"
    assert result[0].price is not None
    assert result[0].properties is not None
