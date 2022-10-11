from enum import Enum


class LogExportStatus(str, Enum):
    DISABLED = "DISABLED"
    DISABLING = "DISABLING"
    DISABLE_FAILED = "DISABLE_FAILED"
    ENABLED = "ENABLED"
    ENABLING = "ENABLING"
    ENABLE_FAILED = "ENABLE_FAILED"

    def __str__(self) -> str:
        return str(self.value)
