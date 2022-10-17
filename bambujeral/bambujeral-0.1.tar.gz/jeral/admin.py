from django.contrib import admin
from jeral.models import *
# Register your models here.




from import_export import resources

from import_export.admin import ImportExportModelAdmin



class MunisipiuResource(resources.ModelResource):
    class Meta:
        model = Munisipiu
class MunisipiuAdmin(ImportExportModelAdmin):
    resource_class = MunisipiuResource
admin.site.register(Munisipiu, MunisipiuAdmin)


class LinguaResource(resources.ModelResource):
    class Meta:
        model = Lingua
class LinguaAdmin(ImportExportModelAdmin):
    resource_class =LinguaResource
admin.site.register(Lingua, LinguaAdmin)




class PostuResource(resources.ModelResource):
    class Meta:
        model = Postu
class PostuAdmin(ImportExportModelAdmin):
    resource_class = PostuResource
admin.site.register(Postu, PostuAdmin)



class SukuResource(resources.ModelResource):
    class Meta:
        model = Suku
class SukuAdmin(ImportExportModelAdmin):
    resource_class = SukuResource
admin.site.register(Suku, SukuAdmin)





# admin.site.register(Postu)
# admin.site.register(Suku)
# admin.site.register(Lingua)