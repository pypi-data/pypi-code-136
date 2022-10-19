"""
The Info test module.

This module contains tests for Info objects.
"""
from cardtrader.service import CardTrader


def test_info(session: CardTrader):
    """Test using the info endpoint."""
    result = session.info()
    assert result.info_id == 4263
    assert result.name == "BuriedInCode App 20220418050011"
