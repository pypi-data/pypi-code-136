from django.contrib import admin

from .jwt_serializer import jwt_serializer
from . import models
from django.contrib import admin
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.conf import settings

MICROSERVICE_ADMIN_TITLE = getattr(settings, 'MICROSERVICE_ADMIN_TITLE', 'Microservice Admin')

class ModelsAdmin(admin.AdminSite):

    def each_context(self, request):
        context = super().each_context(request)
        if not request.user.is_authenticated:
            return context
        microservice_admin_list = []
        for app in models.AdminApps.objects.all().order_by('app_order'):
            app_url = f'{app.app_url}{app.redirect_path}'
            if app.app_name == settings.MICROSERVICE_ADMIN_APP_NAME:  
                app_url = f'{app.app_url}{reverse("admin:index")}'
                microservice_admin_list.append({'app_name': app.app_name, 'app_url': app_url, 'active': True})
            else:
                microservice_admin_list.append({'app_name': app.app_name, 'app_url': app_url, 'active': False})

        context["admin_apps"]=  microservice_admin_list
        context['microservice_header'] = settings.MICROSERVICE_ADMIN_APP_SECRET_KEY_HEADER
        jwt = jwt_serializer.get_token(request.user)
        context['microservice_secret_key'] = jwt
        context['microservice_admin_title'] = MICROSERVICE_ADMIN_TITLE
        return context

admin_site = ModelsAdmin(name=settings.MICROSERVICE_ADMIN_APP_NAME)

MICROSERVICE_ADMIN_REGISTER_SETTINGS = getattr(settings, 'MICROSERVICE_ADMIN_REGISTER_SETTINGS', False)
if MICROSERVICE_ADMIN_REGISTER_SETTINGS:
    from .models import AdminApps
    admin_site.register(User, UserAdmin)
    admin_site.register(Group, GroupAdmin)
    admin_site.register(AdminApps)
