from import_export import resources
from import_export.fields import Field

from .models import *  # Kabupaten, Kecamatan, Kelurahan, Provinsi


class CountryResource(resources.ModelResource):
    # name = Field(attribute='name', column_name='name')
    # user_id = Field(attribute='user_id', column_name='user_id')

    class Meta:
        model = Country
        skip_unchanged = True
        report_skipped = False

        # sertakan pk di fields ini
        # import_id_fields = ('user_id', 'name',)

        # fields yg di eksport
        fields = ( 'id', 'name',) 
        export_order = fields    

class ProvinceResource(resources.ModelResource):
    # name = Field(attribute='name', column_name='name')
    # user_id = Field(attribute='user_id', column_name='user_id')

    class Meta:
        model = Province
        skip_unchanged = True
        report_skipped = False

        # sertakan pk di fields ini
        # import_id_fields = ('user_id', 'name',)

        # fields yg di eksport
        fields = ( 'id', 'name',) 
        export_order = fields    

class RegencyResource(resources.ModelResource):
    # name = Field(attribute='name', column_name='name')
    province_id = Field(attribute='province_id', column_name='province_id')

    class Meta:
        model = Regency
        skip_unchanged = True
        report_skipped = False

        # sertakan pk di fields ini
        # import_id_fields = ('user_id', 'name',)

        # fields yg di eksport
        # field tidak bisa terima data provinsi__name
        fields = ( 'id', 'province_id', 'name',) 
        export_order = fields    

class SubDistrictResource(resources.ModelResource):
    # name = Field(attribute='name', column_name='name')
    regency_id = Field(attribute='regency_id', column_name='regency_id')

    class Meta:
        model = SubDistrict
        skip_unchanged = True
        report_skipped = False

        # sertakan pk di fields ini
        # import_id_fields = ('user_id', 'name',)

        # fields yg di eksport
        # field tidak bisa terima data provinsi__name
        fields = ( 'id', 'regency_id', 'name',) 
        export_order = fields            

class UrbanVillageResource(resources.ModelResource):
    # name = Field(attribute='name', column_name='name')
    sub_district_id = Field(attribute='sub_district_id', column_name='sub_district_id')

    class Meta:
        model = UrbanVillage
        skip_unchanged = True
        report_skipped = False

        # sertakan pk di fields ini
        # import_id_fields = ('user_id', 'name',)

        # fields yg di eksport
        # field tidak bisa terima data provinsi__name
        fields = ( 'id', 'sub_district_id', 'name',) 
        export_order = fields                    
