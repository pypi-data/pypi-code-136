"""
Helper functions for conversions
"""
import decimal
import datetime
from typing import Any


def convert_return_value_to_python_type(value) -> Any:
    """
    Convert return types to basic python types
    """
    if isinstance(value, decimal.Decimal):
        return float(value)

    if isinstance(value, datetime.datetime):
        return value.isoformat()

    if isinstance(value, datetime.date):
        return value.strftime("%Y-%m-%d")

    return value
