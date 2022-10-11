from enum import Enum


class LogExportType(str, Enum):
    AWS_CLOUDWATCH = "AWS_CLOUDWATCH"
    GCP_CLOUD_LOGGING = "GCP_CLOUD_LOGGING"

    def __str__(self) -> str:
        return str(self.value)
