from enum import Enum


class ApiCloudProvider(str, Enum):
    GCP = "GCP"
    AWS = "AWS"

    def __str__(self) -> str:
        return str(self.value)
