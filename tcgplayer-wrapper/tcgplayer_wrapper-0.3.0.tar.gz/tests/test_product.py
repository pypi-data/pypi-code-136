"""
The Product test module.

This module contains tests for Product objects.
"""
import pytest

from tcgplayer.exceptions import ServiceError
from tcgplayer.service import TCGPlayer


def test_group_products(session: TCGPlayer):
    """Test using the group products endpoint with a valid category and group id."""
    results = session.list_group_products(category_id=1, group_id=87)
    result = [x for x in results if x.product_id == 86]
    assert len(result) == 1
    assert result[0].product_id == 86
    assert result[0].name == "Abyssal Nightstalker"
    assert result[0].clean_name == "Abyssal Nightstalker"
    assert result[0].image_url == "https://tcgplayer-cdn.tcgplayer.com/product/86_200w.jpg"
    assert result[0].category_id == 1
    assert result[0].group_id == 87
    assert (
        result[0].url
        == "https://www.tcgplayer.com/product/86/magic-portal-second-age-abyssal-nightstalker"
    )


def test_invalid_group_products(session: TCGPlayer):
    """Test using the group products endpoint with an invalid category and group id."""
    with pytest.raises(ServiceError):
        session.list_group_products(category_id=-1, group_id=-1)


def test_group_products_invalid_category(session: TCGPlayer):
    """Test using the group products endpoint with a valid group and invalid category id."""
    with pytest.raises(ServiceError):
        session.list_group_products(category_id=-1, group_id=87)


def test_group_products_invalid_group(session: TCGPlayer):
    """Test using the group products endpoint with a valid category and invalid group id."""
    with pytest.raises(ServiceError):
        session.list_group_products(category_id=1, group_id=-1)


def test_product(session: TCGPlayer):
    """Test using the product endpoint with a valid product id."""
    result = session.product(product_id=86)
    assert result.product_id == 86

    assert result.name == "Abyssal Nightstalker"
    assert result.clean_name == "Abyssal Nightstalker"
    assert result.image_url == "https://tcgplayer-cdn.tcgplayer.com/product/86_200w.jpg"
    assert result.category_id == 1
    assert result.group_id == 87
    assert (
        result.url
        == "https://www.tcgplayer.com/product/86/magic-portal-second-age-abyssal-nightstalker"
    )


def test_invalid_product(session: TCGPlayer):
    """Test using the product endpoint with an invalid product id."""
    with pytest.raises(ServiceError):
        session.product(product_id=-1)
