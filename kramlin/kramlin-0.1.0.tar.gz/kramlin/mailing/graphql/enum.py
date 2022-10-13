import strawberry
from enum import Enum


@strawberry.enum
class EmailServerTypeEnum(Enum):
    SMTP = "SMTP"


@strawberry.enum
class EmailConnectionSecurityEnum(Enum):
    NONE = "NONE"
    SSL = "SSL"
    TLS = "TLS"


__all__ = [
    'EmailServerTypeEnum',
    'EmailConnectionSecurityEnum'
]
