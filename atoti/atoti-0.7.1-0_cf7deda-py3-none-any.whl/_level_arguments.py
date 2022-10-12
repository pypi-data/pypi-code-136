from typing import Tuple

from atoti_core import ColumnCoordinates

from .order._order import Order
from .type import DataType

LevelArguments = Tuple[str, ColumnCoordinates, DataType, Order]
