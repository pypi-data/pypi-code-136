from enum import Enum


class TransformationHttpMethod(str, Enum):
    PUT = "PUT"
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
