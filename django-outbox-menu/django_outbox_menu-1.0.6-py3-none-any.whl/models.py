'''
    Recreate model base on OPD project and Outbox Project
    29th September 2022
    Grid Software, Inc.
'''
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.db import models

# User = get_user_model()

class OptMenuKinds(models.IntegerChoices):
    '''
        Jenis menu : 
            0 : Front end without user login
            1 : Front end with user login
            2 : Back end with user login (nothing for none user)

            Update 17 Sept 2021
            0 : Front End
            1 : Back End
    '''
    FRONTEND = 1
    BACKEND = 2 
    # Tidak jadi karena crash dengan unique together di model
    # BACKEND_DEFAULT = 3 # Penanda user baru login, belum ada company yg aktif, sehingga menu belum bisa di generate
                        # untuk itu generate menu default langsung   


class MenuGroup(models.Model):
    '''
        Group : Model Menu
        Simpan data group menu :
        1. Owner
        2. Manager
        3. Operator
        4. Kasir
        5. dll...

        Tidak ada interface, maintenance di halaman admin
    '''
    # Update 19 Oktober 2022
    # untuk membedakan menu project 1 dengan yg lain, dengan nama sama
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    # Tidak boleh ada data kembar di name
    name = models.CharField(max_length=100) # unique=True (Unique together with site)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)    

    # Optional Fields:
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # objects = MenuGroupManager()
    
    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['site', 'name'], name='unique_site_name')
        ]

# def company_name_validate(value):
#     if len(value) < 3:
#         raise ValidationError("Company name mush be more than 3 character")
#     else:
#         return value

class Menu(models.Model):
    '''    
        Relase :
            User --1:N-- Menu
        Deskripsi :
            # Menu di buat per user,
            # Satu company bisa mempunyai banyak user,
            # Satu User bisa punya banyak menu
            # Tetapkan satu user sebagai user master (berguna sebagai menu master), di copy ke menu user lain
    
        # ada 1 company dengan site ID = 1 sebagai master menu
        # seluruh menu di create dari site ini (berarti is_master_menu tidak di perlukan lagi)
        # Untuk menu di app blog, user tidak dalam kondisi login
        # Untuk menu di app inventory, user harus login dulu        
        # Jika user telah di create, langsung generate menu untuk user tersebut
        # dapat di visible sesuai kebutuhan
    '''       
    name = models.CharField(max_length=100)

    # menu group, relasi many to many 
    # Untuk frontend menu group kosong
    menu_group = models.ManyToManyField(MenuGroup, blank=True) # , null=True, blank=True)  not effect to m2m relation

    # Optional Fields:
    # user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)        # Menu di generate per user   
    # user harus diimport dulu

    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)    

    # link: adalah name menu yg di slugify
    # href di ubah menjadi link
    # jika ada ://www maka dianggap link luar
    # /home/dashboard is not valid URLField (change back to CharField)
    # link = models.URLField(max_length=255, null=True, blank=True)  # , verbose_name='Link'
    link = models.CharField(max_length=255, null=True, blank=True) 

    # urut menu
    order_menu = models.SmallIntegerField(default=0)

    # awesome icon
    # data berupa blok <i class="icon"></i>
    icon = models.CharField(max_length=50, null=True, blank=True)    

    #is_admin_menu = models.BooleanField(default=False)	    
    # is_admin_menu: jika true, menu untuk backend, jika false menu untuk frontend
    # jenis menu
    kind = models.SmallIntegerField(choices=OptMenuKinds.choices, default=OptMenuKinds.FRONTEND)

    # is_visibled: untuk menyembunyikan menu
    is_visibled = models.BooleanField(default=True)	    

    # is_master_menu: adalah menu yg digunakan oleh banyak user
    # tidak bisa dihapus, hanya super user yg bisa menghapus
    # is_master_menu adalah menu yg di copy oleh user lain saat pertama kali di buat

    # Update 17 Sept 2021 
    # is_master_menu tidak digunakan lagi karena seluruh menu di create sesuai dengan
    # data menu di SITE 1
    # (menu di SITE 1 sebagai menu master yg akan di copy ke site lain saat User pertama kali di create)
    # is_master_menu = models.BooleanField(default=False)	 

    # is_statis_menu: penanda halaman statis
    # semua menu yg di create oleh user adalah statis menu
    # diakses khusus melalui link tertentu di halaman statis   
    # is_statis_menu = models.BooleanField(default=False)	
    is_external = models.BooleanField(default=False)	    # Jika external menu True, maka otomatis target _BLANK

    # timestamp
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # untuk status sinkronisasi ke server
    # penanda di server lokal apakah sudah di sinkronisasi atau belum
    # yg paling penting tanggal harus valid 
    # is_already_sync = models.BooleanField(default=False)	

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)    

    # def __str__(self):
    #     return self.name

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['menu_group', 'name'], name='unique_menu_group_name')
    #     ]

    # def updated_at_(self):
    #     return get_natural_datetime(self.updated_at)

    # def created_at_(self):
    #     return get_natural_datetime(self.created_at)

    # def parent_(self):
    #     if self.parent:
    #         return self.parent.name
    #     else:
    #         return '-'

    # def updated_at_(self):
    #     return get_natural_datetime(self.updated_at)        
    
    # def updated_at_(self):
    #     return  "naturalday(self.updated_at)"
       # return serializers.serialize("json",' naturalday(self.updated_at)')
        #return serializers.serialize('json', naturalday(self.updated_at))

    def __str__(self):          
        if self.kind == OptMenuKinds.FRONTEND:
            res = '[ Front-End ]'       # halaman depan
        # elif self.kind == OptMenuKinds.BACKEND_DEFAULT:
        #     res = '[ Default ]'
        else:
            res = '[ Back-End ]'        # halaman dashboard

        if self.parent:
            par = self.parent.name      # tampilkan name parent jika ada    
        else:
            par = 'ROOT'

        return "{} {} > {}".format(res, par, self.name)  


class MenuCustom(models.Model):
    '''
        Custom menu adalah menu yg hanya muncul di site dan menu_group tertentu saja
        tidak muncul di tempat lain
    '''
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    menu_group = models.ForeignKey(MenuGroup, on_delete=models.PROTECT, blank=True, null=True)    
    menu = models.OneToOneField(Menu, on_delete=models.CASCADE) # One to One Relations to menu

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)    


    def __str__(self):  
        return "{}".format(self.menu)  
