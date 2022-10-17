from django.db import models
from jeral.models import *
from django.contrib.auth.models import User
from django.contrib import admin
from informasaun.models import *
# Create your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources


admin.site.register(Informasaun)

admin.site.register(KategoriaProdutu)

admin.site.register(KonteuduProdutu)

admin.site.register(ImagenProdutu)

admin.site.register(Produtu)



class PajinaResource(resources.ModelResource):
    class Meta:
        model = Pajina
class PajinaAdmin(ImportExportModelAdmin):
    resource_class = PajinaResource
admin.site.register(Pajina, PajinaAdmin)



class KonteuduPajinaResource(resources.ModelResource):
    class Meta:
        model = KonteuduPajina
class KonteuduPajinaAdmin(ImportExportModelAdmin):
    resource_class = KonteuduPajinaResource
admin.site.register(KonteuduPajina, KonteuduPajinaAdmin)

