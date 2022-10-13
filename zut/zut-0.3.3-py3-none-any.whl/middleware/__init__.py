import logging
from django.http import HttpResponseForbidden
from django.core.exceptions import ImproperlyConfigured

try:
    from django.contrib.auth.mixins import AccessMixin
    from django.contrib.auth.views import LoginView, LogoutView, redirect_to_login
    from django.views.generic.base import RedirectView
    improperly_configured_error = None
        
    try:
        from rest_framework.views import APIView
        with_rest_framework = True
    except ImportError:
        with_rest_framework = False
except ImproperlyConfigured as improperly_configured_error:
    # delay exception in class instantiation to avoid failure during unittest discovery
    pass


logger = logging.getLogger(__name__)

class StaffAuthorizationMiddleware:
    no_default_for = ["/", "/status"]

    def __init__(self, get_response):
        if improperly_configured_error:
            raise improperly_configured_error
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path in self.no_default_for:
            return # no default permission

        if view_func.__module__.startswith("django.contrib.admin."):
            return # no default permission

        if not hasattr(view_func, "view_class"):
            # function-based view
            if not self.is_authorized(request.user):
                logger.debug("function-based view %s: default authorization required", ".".join([view_func.__module__, view_func.__name__]))
                return self._deny_or_login(request)
            
        else:
            # class-based view
            view = view_func.view_class

            if issubclass(view, (LoginView, LogoutView, RedirectView)):
                return # no default permission

            if with_rest_framework and issubclass(view, APIView):
                # API view (Django Rest Framework)
                if not view.permission_classes:
                    if not self.is_authorized(request.user):
                        logger.debug("no permission_classes for rest_framework view %s: default authorization required required", ".".join([view.__module__, view.__name__]))
                        return HttpResponseForbidden() # do not redirect to login page (this is supposed to be accessed by javascript or as an API)

            else:
                # Standard class-based view
                if not issubclass(view, AccessMixin):
                    if not self.is_authorized(request.user):
                        logger.debug("no AccessMixin for view %s: default authorization required", ".".join([view.__module__, view.__name__]))
                        return self._deny_or_login(request)

    def is_authorized(self, user):
        return user.is_staff

    def _deny_or_login(self, request):
        if request.user.is_authenticated:
            return HttpResponseForbidden()
        else:
            return redirect_to_login(next=request.get_full_path())


class AdminAuthorizationMiddleware(StaffAuthorizationMiddleware):
    def is_authorized(self, user):
        return user.is_admin
