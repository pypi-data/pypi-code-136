from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.forms import (
    CharField,
    Form,
    HiddenInput,
    IntegerField,
    PasswordInput,
)

from users.utils import get_hash

User = get_user_model()


class PasswordChangeForm(Form):
    password = CharField(label="Nowe hasło", widget=PasswordInput())
    repeat_password = CharField(label="Potwórz hasło", widget=PasswordInput())
    user = IntegerField(widget=HiddenInput(), required=False)
    key = CharField(widget=HiddenInput(), required=False)

    def clean_password(self):
        try:
            validate_password(self.cleaned_data["password"])
        except ValidationError as e:
            raise e

        return self.cleaned_data["password"]

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")
        user_pk = cleaned_data.get("user")
        key = cleaned_data.get("key")

        if user_pk and key:
            user = User.objects.filter(pk=user_pk).first()
            if user:
                hash = get_hash(user)

                if not user.is_active:
                    raise ValidationError("User's account is not activated!")

                if hash != key:
                    raise ValidationError("Data verification failed!")

                cleaned_data["user"] = user
            else:
                raise ValidationError("User does not exists!")
        else:
            raise ValidationError("User/key not provided!")

        if password and repeat_password:
            if password != repeat_password:
                raise ValidationError("Passwords are not equal!")
        else:
            raise ValidationError("Passwords not provided!")

        return cleaned_data
