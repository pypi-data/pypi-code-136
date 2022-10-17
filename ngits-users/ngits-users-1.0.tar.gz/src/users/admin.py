from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


class UserAdmin(UserAdmin):
    list_display = ("username", "email", "is_active", "account_type")
    list_filter = ("account_type", "is_active", "is_superuser", "is_staff")


admin.site.register(User, UserAdmin)
