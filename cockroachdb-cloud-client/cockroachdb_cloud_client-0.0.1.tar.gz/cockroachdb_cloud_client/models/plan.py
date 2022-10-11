from enum import Enum


class Plan(str, Enum):
    DEDICATED = "DEDICATED"
    CUSTOM = "CUSTOM"
    SERVERLESS = "SERVERLESS"

    def __str__(self) -> str:
        return str(self.value)
