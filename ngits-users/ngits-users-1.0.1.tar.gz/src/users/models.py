from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Type(models.IntegerChoices):
        anonymous = 0
        standard = 1
        google = 2
        facebook = 3

    account_type = models.SmallIntegerField(
        choices=Type.choices,
        default=Type.standard,
    )
