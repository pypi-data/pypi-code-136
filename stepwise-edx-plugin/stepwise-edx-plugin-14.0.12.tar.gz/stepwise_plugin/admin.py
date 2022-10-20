# python

# django
from django.contrib import admin

# open edx

# this plugin
from .models import Configuration, Locale, MarketingSites, EcommerceConfiguration, EcommerceEOPWhitelist


class MarketingSitesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MarketingSites._meta.get_fields()]


admin.site.register(MarketingSites, MarketingSitesAdmin)


class LocaleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Locale._meta.get_fields()]


admin.site.register(Locale, LocaleAdmin)


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Configuration._meta.get_fields()]


admin.site.register(Configuration, ConfigurationAdmin)


class EcommerceConfigurationAdmin(admin.ModelAdmin):
    """
    Stepwise Math Ecommerce Configuration
    """

    search_fields = ("course_id",)
    list_display = (
        "course_id",
        "payment_deadline_date",
        "created",
        "modified",
    )
    readonly_fields = ("created", "modified")


admin.site.register(EcommerceConfiguration, EcommerceConfigurationAdmin)


class EcommerceEOPWhitelistAdmin(admin.ModelAdmin):
    """
    Stepwise Math Ecommerce Configuration for EOP Student Exemptions
    """

    search_fields = (
        "user_email",
        "type",
    )
    list_display = (
        "id",
        "user_email",
        "type",
        "created",
        "modified",
    )


admin.site.register(EcommerceEOPWhitelist, EcommerceEOPWhitelistAdmin)
