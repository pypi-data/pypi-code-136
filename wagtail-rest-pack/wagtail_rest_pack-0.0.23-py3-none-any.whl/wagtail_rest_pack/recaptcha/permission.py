import logging

from rest_framework.exceptions import ValidationError
from rest_framework.permissions import BasePermission

from .models import get_recaptcha_instance

logger = logging.getLogger(__name__)

class AuthenticatedOrRecaptcha(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return True
        try:
            get_recaptcha_instance().verify(request)
            return True
        except ValidationError as e:
            logger.error(e)
            return False

