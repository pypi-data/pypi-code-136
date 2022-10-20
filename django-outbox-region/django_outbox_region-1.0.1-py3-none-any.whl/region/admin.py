from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *
from .resources import *


# Negara
class CountryAdmin(ImportExportModelAdmin, admin.ModelAdmin):    
    list_filter = ('name',) 
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ('name',)
    ordering = ('id', 'name',)
    resource_class = CountryResource    

admin.site.register(Country, CountryAdmin)

# Provinsi
class ProvinceAdmin(ImportExportModelAdmin, admin.ModelAdmin):    
    list_filter = ('name',) 
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ('name',)
    ordering = ('id', 'name',)
    resource_class = ProvinceResource    

admin.site.register(Province, ProvinceAdmin)

# Kabupaten / Kota
class RegencyAdmin(ImportExportModelAdmin, admin.ModelAdmin):    
    list_filter = ('province',) 
    list_display = ['province', 'name', 'created_at', 'updated_at']
    search_fields = ('name', 'province__name',)
    ordering = ('id', 'province__id', 'name',)
    resource_class = RegencyResource    

admin.site.register(Regency, RegencyAdmin)

# Kecamatan
class SubDistrictAdmin(ImportExportModelAdmin, admin.ModelAdmin):    
    list_filter = ('regency',) 
    list_display = ['regency', 'name', 'created_at', 'updated_at']
    search_fields = ('name', 'regency__name',)
    ordering = ('id', 'regency__id', 'name',)
    resource_class = SubDistrictResource    

admin.site.register(SubDistrict, SubDistrictAdmin)

# Kelurahan
class UrbanVillageAdmin(ImportExportModelAdmin, admin.ModelAdmin):    
    list_filter = ('sub_district',) 
    list_display = ['sub_district', 'name', 'created_at', 'updated_at']
    search_fields = ('name', 'sub_district__name',)
    ordering = ('id', 'sub_district__id', 'name',)
    resource_class = UrbanVillageResource    

admin.site.register(UrbanVillage, UrbanVillageAdmin)
# 80534
# kurang 2 karena di update, kemungkinan ID double di csv 2
