from enum import Enum


class CMEKStatus(str, Enum):
    DISABLED = "DISABLED"
    DISABLING = "DISABLING"
    DISABLE_FAILED = "DISABLE_FAILED"
    ENABLED = "ENABLED"
    ENABLING = "ENABLING"
    ENABLE_FAILED = "ENABLE_FAILED"
    ROTATING = "ROTATING"
    ROTATE_FAILED = "ROTATE_FAILED"
    REVOKED = "REVOKED"
    REVOKING = "REVOKING"
    REVOKE_FAILED = "REVOKE_FAILED"

    def __str__(self) -> str:
        return str(self.value)
