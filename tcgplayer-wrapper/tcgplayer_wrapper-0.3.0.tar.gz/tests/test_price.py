"""
The Price test module.

This module contains tests for Price objects.
"""
import pytest

from tcgplayer.exceptions import ServiceError
from tcgplayer.service import TCGPlayer


def test_group_prices(session: TCGPlayer):
    """Test using the group prices endpoint with a valid group id."""
    results = session.list_group_prices(group_id=2324)
    result = [x for x in results if x.product_id == 175065]
    assert len(result) == 1
    assert result[0].product_id == 175065

    assert result[0].low_price == 99.99
    assert result[0].mid_price == 99.99
    assert result[0].high_price == 99.99
    assert result[0].market_price == 90.79
    assert result[0].direct_low_price is None
    assert result[0].sub_type_name == "Normal"


def test_invalid_group_prices(session: TCGPlayer):
    """Test using the group prices endpoint with an invalid group id."""
    with pytest.raises(ServiceError):
        session.list_group_prices(group_id=-1)


def test_product_prices(session: TCGPlayer):
    """Test using the product prices endpoint with a valid product id."""
    results = session.product_prices(product_id=175065)
    assert results[0].product_id == 175065

    assert results[0].low_price == 99.99
    assert results[0].mid_price == 99.99
    assert results[0].high_price == 99.99
    assert results[0].market_price == 90.79
    assert results[0].direct_low_price is None
    assert results[0].sub_type_name == "Normal"


def test_invalid_product_prices(session: TCGPlayer):
    """Test using the product prices endpoint with an invalid product id."""
    with pytest.raises(ServiceError):
        session.product_prices(product_id=-1)
