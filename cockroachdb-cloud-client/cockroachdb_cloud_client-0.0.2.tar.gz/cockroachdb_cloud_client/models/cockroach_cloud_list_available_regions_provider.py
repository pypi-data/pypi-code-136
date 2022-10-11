from enum import Enum


class CockroachCloudListAvailableRegionsProvider(str, Enum):
    GCP = "GCP"
    AWS = "AWS"

    def __str__(self) -> str:
        return str(self.value)
