from enum import Enum


class QuantityUnitType(str, Enum):
    HOURS = "HOURS"
    REQUEST_UNITS = "REQUEST_UNITS"

    def __str__(self) -> str:
        return str(self.value)
