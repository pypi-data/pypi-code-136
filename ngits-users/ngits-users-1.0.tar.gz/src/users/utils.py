from hashlib import sha256

import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import get_template
from django.urls import reverse
from django.utils.translation import gettext as _
from rest_framework.exceptions import ParseError

User = get_user_model()


def get_hash(user):
    # strftime used because changing is_active flag trims date_joined miliseconds
    secret = "{}-{}".format(
        user.date_joined.strftime("%Y-%m-%d %H:%M:%S"), user.username
    ).encode()
    return sha256(secret).hexdigest()


class EmailManager:
    EMAIL_TEMPLATES = {
        "registration": {
            "text_template": "registration_email.txt",
            "html_template": "registration_email.html",
            "url": "verify",
            "title": settings.REGISTRATION_EMAIL_SUBJECT,
        },
        "remind": {
            "text_template": "change_password_email.txt",
            "html_template": "change_password_email.html",
            "url": "remind_password_confirm",
            "title": settings.REMIND_EMAIL_SUBJECT,
        },
    }

    @classmethod
    def send(self, user, protocol, host):
        hash = get_hash(user)

        URL = "{}://{}{}?user={}&key={}".format(
            protocol,
            host,
            reverse(self.EMAIL_TEMPLATES[self.template]["url"]),
            user.pk,
            hash,
        )
        context = {"url": URL}
        text_template = get_template(
            self.EMAIL_TEMPLATES[self.template]["text_template"]
        )
        html_template = get_template(
            self.EMAIL_TEMPLATES[self.template]["html_template"]
        )

        send_mail(
            subject=self.EMAIL_TEMPLATES[self.template]["title"],
            message=text_template.render(context),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            html_message=html_template.render(context),
        )


class StandardRegistration(EmailManager):
    @classmethod
    def send_auth_email(self, user_id, protocol, host):
        user = User.objects.get(pk=user_id)
        self.template = "registration"
        self.send(user, protocol, host)


class RemindPassword(EmailManager):
    @classmethod
    def send_email(self, user_email, protocol, host):
        user = User.objects.get(email=user_email)
        self.template = "remind"
        self.send(user, protocol, host)


class GoogleAuthorization:
    URL = "https://www.googleapis.com/oauth2/v2/userinfo?access_token={}"

    @classmethod
    def get_user_data(self, token):
        res = requests.get(self.URL.format(token))
        if res.status_code == 401:
            raise ParseError(_("Google authorization failed!"))

        return res.json()


class FacebookAuthorization:
    URL = "https://graph.facebook.com/me?fields=name,email&access_token={}"

    @classmethod
    def get_user_data(self, token):
        res = requests.get(self.URL.format(token))
        return res.json()
