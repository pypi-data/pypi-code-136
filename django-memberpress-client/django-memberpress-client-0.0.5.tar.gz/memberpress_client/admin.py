from django.contrib import admin
from memberpress_client.models import MemberpressEvents


class MemberpressEventsAdmin(admin.ModelAdmin):
    """
    Memberpress Webhook event log
    """

    def has_change_permission(self, request, obj=None):
        return False

    search_fields = ()
    list_display = (
        "created",
        "event",
        "event_type",
        "is_valid",
        "username",
        "json",
    )


admin.site.register(MemberpressEvents, MemberpressEventsAdmin)
