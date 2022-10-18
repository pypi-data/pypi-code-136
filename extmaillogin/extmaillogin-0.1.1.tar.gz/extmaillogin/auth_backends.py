from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class ExternalEmailAuthBackend(BaseBackend):
    def authenticate(self, request, ext_email=""):
        if ext_email:
            user_model = get_user_model()
            try:
                user = user_model.objects.get(email=ext_email)
                return user
            except user_model.DoesNotExist:
                return None
        return None

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
