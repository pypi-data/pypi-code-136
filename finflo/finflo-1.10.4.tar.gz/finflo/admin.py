from django.contrib import admin
from .models import Action, Flowmodel, PartyType, States, TransitionManager , workevents , workflowitems , SignList 
# Register your models here.
from django.contrib import messages
from django.utils.translation import ngettext
from django.conf import settings


class TransitionModeladmin(admin.ModelAdmin):
    list_display = ("t_id", "type", "in_progress")

    def change_to_draft(self, request, queryset):
        updated = queryset.update(in_progess = False )
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

class CustomActionAdminModel(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return obj is None or obj.pk != 1


class customadminforsign(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return obj is None or obj.pk != 0
    

admin.site.register(Flowmodel)
admin.site.register(TransitionManager,TransitionModeladmin)
admin.site.register(Action , CustomActionAdminModel )
admin.site.register(States)
admin.site.register(PartyType)
admin.site.register(SignList , customadminforsign)
admin.site.register(workflowitems)
admin.site.register(workevents)