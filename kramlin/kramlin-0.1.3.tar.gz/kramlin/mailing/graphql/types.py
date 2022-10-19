import strawberry
from typing import Optional

from .enum import EmailConnectionSecurityEnum


@strawberry.type
class EmailSMTPSettings:
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    port: Optional[int] = None
    connectionSecurity: Optional[EmailConnectionSecurityEnum] = None


@strawberry.type
class MailingConfiguration:
    enforceEmailVerification: Optional[bool] = None
    serverType: Optional[str] = None
    smtpSettings: Optional[EmailSMTPSettings] = None


__all__ = [
    'EmailSMTPSettings',
    'MailingConfiguration'
]
