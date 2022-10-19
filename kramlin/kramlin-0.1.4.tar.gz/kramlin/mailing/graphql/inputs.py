import strawberry
from typing import Optional

from .enum import EmailConnectionSecurityEnum, EmailServerTypeEnum


@strawberry.input
class EmailSMTPSettingsInput:
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    port: Optional[int] = None
    connectionSecurity: Optional[EmailConnectionSecurityEnum] = None


@strawberry.input
class MailingConfigurationInput:
    enforceEmailVerification: Optional[bool] = None
    serverType: Optional[EmailServerTypeEnum] = None
    smtpSettings: Optional[EmailSMTPSettingsInput] = None


__all__ = [
    'EmailSMTPSettingsInput',
    'MailingConfigurationInput'
]
