from enum import Enum


class Currency(str, Enum):
    USD = "USD"
    CRDB_CLOUD_CREDITS = "CRDB_CLOUD_CREDITS"

    def __str__(self) -> str:
        return str(self.value)
