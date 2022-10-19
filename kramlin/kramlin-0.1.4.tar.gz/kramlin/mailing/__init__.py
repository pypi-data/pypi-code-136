#  Copyright © 2022 Traboda CyberLabs Private Limited.
#  All Rights Reserved.
from typing import Optional, Union, List

from .graphql.types import MailingConfiguration
from .smtp import SMTPManager
from kramlin.mailing.graphql.enum import EmailServerTypeEnum
from kramlin.mailing.graphql.inputs import EmailSMTPSettingsInput


class MailingManager:
    def __init__(
        self,
        enforceEmailVerification: Optional[bool] = False,
        serverType: Optional[EmailServerTypeEnum] = EmailServerTypeEnum.SMTP,
        smtpSettings: Optional[Union[EmailSMTPSettingsInput, dict]] = None
    ):
        self.enforceEmailVerification = enforceEmailVerification
        self.serverType: EmailServerTypeEnum = serverType
        self.smtpSettings: Optional[SMTPManager] = None
        if smtpSettings:
            if smtpSettings and type(smtpSettings) == dict:
                self.smtpSettings = EmailSMTPSettingsInput(**smtpSettings)
            self.smtpSettings = SMTPManager(
                username=smtpSettings.username,
                password=smtpSettings.password,
                email=smtpSettings.email,
                address=smtpSettings.address,
                port=smtpSettings.port,
                connectionSecurity=smtpSettings.connectionSecurity
            )

    def get_from_email(self):
        if self.serverType == EmailServerTypeEnum.SMTP and self.smtpSettings:
            return self.smtpSettings.email

    def get_email_backend(self, fail_silently=False):
        if self.serverType == EmailServerTypeEnum.SMTP and self.smtpSettings:
            return self.smtpSettings.get_backend(fail_silently=fail_silently)

    def send_email(
        self,
        subject: str,
        message: str,
        recipient_list: List[str],
        html_message: Optional[str] = None,
        fail_silently: Optional[bool] = False,
    ) -> int:
        backend = self.get_email_backend(fail_silently=fail_silently)
        from_email = self.get_from_email()

        from django.core.mail import EmailMultiAlternatives

        mail = EmailMultiAlternatives(
            connection=backend,
            from_email=from_email,
            to=recipient_list,
            subject=subject,
            body=message,
        )
        if html_message:
            mail.attach_alternative(html_message, "text/html")
        return mail.send()

    def graphql(self) -> MailingConfiguration:
        return MailingConfiguration(
            enforceEmailVerification=self.enforceEmailVerification,
            serverType=self.serverType,
            smtpSettings=self.smtpSettings.graphql() if self.smtpSettings else None,
        )

    def dict(self):
        return {
            "enforceEmailVerification": self.enforceEmailVerification,
            "serverType": self.serverType.value if self.serverType else EmailServerTypeEnum.SMTP.value,
            "smtpServer": self.smtpSettings.dict(),
        }


__all__ = [
    "MailingManager",
]
