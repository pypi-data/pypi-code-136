from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class ValidatePasswordMixin:
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise e

        return value


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ("key", "user_id")


class StandardRegistrationSerializer(
    serializers.Serializer, ValidatePasswordMixin
):
    email = serializers.EmailField()
    password = serializers.CharField()
    repeat_password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(email=data["email"]).exists():
            raise ValidationError(
                _("User associated with this email already exists!")
            )

        if data["password"] != data["repeat_password"]:
            raise ValidationError(_("Passwords are not equal!"))

        return data

    def save(self):
        user = User.objects.create(
            username=self.validated_data["email"],
            email=self.validated_data["email"],
            password=make_password(self.validated_data["password"]),
            is_active=False,
            account_type=User.Type.standard,
        )

        return user


class StandardLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer, ValidatePasswordMixin):
    current_password = serializers.CharField()
    new_password = serializers.CharField()
    repeat_new_password = serializers.CharField()

    def validate(self, data):
        if data["new_password"] != data["repeat_new_password"]:
            raise ValidationError(_("Passwords are not equal!"))

        return data


class RemindPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        if not User.objects.filter(email=data["email"]).exists():
            raise ValidationError(
                _("User associated with this email does not exists!")
            )
        else:
            user = User.objects.get(email=data["email"])

            if not user.is_active:
                raise ValidationError(_("User's account is not activated!"))
            if user.account_type != User.Type.standard:
                raise ValidationError(
                    _("Action not allowed for user's account type!")
                )

        return data


class SocialAuthSerializer(serializers.Serializer):
    token = serializers.CharField()
