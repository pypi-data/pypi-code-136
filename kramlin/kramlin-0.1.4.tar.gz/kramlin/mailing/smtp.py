from typing import Union, Optional

from django.core.mail.backends.smtp import EmailBackend

from kramlin.mailing.graphql.enum import EmailConnectionSecurityEnum
from kramlin.mailing.graphql.types import EmailSMTPSettings


class SMTPManager:

    def __init__(
        self,
        username: str = None,
        password: str = None,
        email: str = None,
        address: str = None,
        port: int = 587,
        connectionSecurity: Optional[Union[EmailConnectionSecurityEnum, str]] = EmailConnectionSecurityEnum.NONE,
    ):
        self.username: str = username
        self.password: str = password
        self.email: str = email
        self.address: str = address
        self.port: int = port
        if connectionSecurity and type(connectionSecurity) == str:
            connectionSecurity = (
                EmailConnectionSecurityEnum.SSL if connectionSecurity == 'SSL' else
                EmailConnectionSecurityEnum.TLS if connectionSecurity == 'TLS' else
                EmailConnectionSecurityEnum.NONE
            )
        self.connectionSecurity: EmailConnectionSecurityEnum = connectionSecurity

    def get_backend(self, fail_silently=False) -> EmailBackend:
        return EmailBackend(
            host=self.address,
            port=self.port,
            username=self.username,
            password=self.password,
            use_ssl=self.connectionSecurity == EmailConnectionSecurityEnum.SSL,
            use_tls=self.connectionSecurity == EmailConnectionSecurityEnum.TLS,
            fail_silently=fail_silently,
        )

    def graphql(self) -> EmailSMTPSettings:
        return EmailSMTPSettings(
            username=self.username,
            password=self.password,
            email=self.email,
            address=self.address,
            port=self.port,
            connectionSecurity=self.connectionSecurity,
        )

    def dict(self) -> dict:
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "address": self.address,
            "port": self.port,
            "connectionSecurity": (
                self.connectionSecurity.value if self.connectionSecurity else EmailConnectionSecurityEnum.NONE.value
            )
        }


__all__ = [
    'SMTPManager',
]
