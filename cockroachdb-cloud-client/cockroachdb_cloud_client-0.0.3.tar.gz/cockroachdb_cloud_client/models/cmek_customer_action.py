from enum import Enum


class CMEKCustomerAction(str, Enum):
    REVOKE = "REVOKE"

    def __str__(self) -> str:
        return str(self.value)
