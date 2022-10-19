'''
    Generate menus - create by ione
    Class ini untuk generate menu sesuai dengan data di database
    Date 13-02-21

    Update v2.0:
        # Sdh mengikuti update terakhir dari project OPD
        # Atur ulang tab
        # Ikuti model tabel menu yg ada di project ini atau OPD

    Update v2.1:
        # create menu berdasarkan user yg login
        # untuk front end, karena tidak login maka generate menu berdasarkan
        # user yg berada di site tersebut

    Update v2.2:
        # perbaikan bread crumb menu
        # tambah bread crumb lengkap dengan link (tidak hanya name saja)

    Update v3.0:
        # using recursive function, all result list same as old version
'''

# Tambah dictionary sesuai data di database, Algoritma :
# 1. Buat query Order by parent id dan order menu
# 2. copy data ke mDict record per pecord
# 3. Append ke mList, sehingga jadinya list of dictionary
# 4. Atur ulang mList, sehingga urutannya menjadi :
#    Menu Parent
#       |--- Menu Anak1
#       |--- Menu Anak2, dst...
# 5. Atur Ulang Level, sehingga menjadi :
#    Dictionary memiliki item baru
#       1. Level : untuk menentukan kedalaman level menu anak
#       2. HaveChild : True or False, Untuk penanda apakah menu parent mempunyai anak atau tidak
#       3. haveChildEndTag : Type Integer, Untuk penanda tag penutup menu anak di buat
#          Jika level 1, buat satu tag penutup menu anak
#          Jika level 2, buat dua tag penutup menu anak, dst...
# 6. Atur active menu
# Buat function baru untuk Atur BreadCrumb, tambahkan List of Dictionary dengan format 
#       [{'Nama','href'},{'nama2','href2'}]
#       Data ini akan di cek di template dengan cara yang sama seperti generate menu
#  --------------------------------------------------------------------------------------------------          

from django.db.models import F

from .models import Menu, MenuCustom


class Menus:    
    # mLvl_prev = -1   # catat level sebelumnya  
    mList_recursive = []
    mList_active = []
    menu_custom_list = []   # exclude this menu from default menus
    # mDict = {}     
    # mList = []      # result ada di mList
    site_id = 1

    # defailt menu_group = 0 artinya front end
    def __init__(self, menu_group = 0, kinds = 0, site_id = 1): #, pIs_master_menu = False):         # menu_group adalah filter untuk company tertentu saja
        '''
            Jika pKind = 0 maka ambil data semua, frontend dan backend
        '''
        self.site_id = site_id
        if len(self.mList_recursive) == 0:
            #if menu_group != "":
            self.create_menus(menu_group, kinds) #, pIs_master_menu)
        else:
            # self.mDict = {}  # clear dulu (karena prosedur init ini sekali dijalankan saat class di buat)
            self.mList_recursive = []
            self.mList_active = []
            self.create_menus(menu_group, kinds) #, pIs_master_menu)                    

    def get_menus(self):
        return self.mList_recursive

    def get_list_active(self):
        return self.mList_active

    def get_menu_custom_list(self, menu_group):
        # select custom menu for ignoring
        self.menu_custom_list = []
        menu_custom = list(MenuCustom.objects.filter(site_id=self.site_id). \
            exclude(menu_group_id=menu_group).values('menu_id'))
        # print(menu_custom)

        for i in menu_custom:
            self.menu_custom_list.append(i['menu_id'])

        print(self.menu_custom_list)


    def ignore_circular_parent(self):
        # 0. Sebelum proses menu, update dulu seluruh menu yg id = id parent set id parent = NULL untuk menghindari
        Menu.objects.filter(id=F('parent_id')).update(parent_id=None)    # query pengaman

    def create_menus(self, menu_group, kinds):     
        # 0. Sebelum proses menu, update dulu seluruh menu yg id = id parent set id parent = NULL untuk menghindari
        # Menu.objects.filter(id=F('parent_id')).update(parent_id=None)    # query pengaman
        # 1. Clear circular reference (ignore it, or set as None)
        self.ignore_circular_parent()
       
        # exclude custom menu tidak digunakan disini karena hanya di ambil root menu saja
        # [UPDATE] tetap digunakan untuk antisipasi root menu digunakan sebagai custom menu
        self.get_menu_custom_list(menu_group)

        # 2. Get data by user options (UPDATE only get ROOT MENU base on User OPTION)
        # Harus konversi ke integer karena tidak masuk ke kondisi        
        if int(kinds) == 0: # jika kind = 0 ambil semua data front end dan back end            
            mData = Menu.objects.filter(menu_group__id=menu_group, is_visibled=True, parent=None) \
                .exclude(id__in=self.menu_custom_list) \
                .order_by('parent_id','order_menu').values('id')     
        elif int(menu_group) == 0:   # menu group = 0 artinya menu frontend            
            mData = Menu.objects.filter(kind=kinds, is_visibled=True, parent=None) \
                .exclude(id__in=self.menu_custom_list) \
                .order_by('parent_id','order_menu').values('id')     
        else:            
            mData = Menu.objects.filter(menu_group__id=menu_group, kind=kinds, is_visibled=True, parent=None) \
                .exclude(id__in=self.menu_custom_list) \
                .order_by('parent_id','order_menu').values('id')                  

        # .exclude(id__in=menu_custom_list) \
        # 3. Get root menu
        # get menu id only
        # print(mData)
        # menu_id = []
        # for i in mData:
        #     menu_id.append(i.id)

        # Entry point from root menu
        # root_menu = self.get_root_menu(menu_id)
        root_menu = []
        for i in mData:
            root_menu.append(i['id'])

        print('root_menu', root_menu)

        # 4. begin process recursive menu
        self.create_menu_recursive(root_menu,0)

        # 5. Update End Tag
        self.update_end_tag()

        # 6. get complete data base on mData
        self.get_menus_complete()

        # 6. return result
        #return self.get_menus()

    def get_menus_complete(self):
        mCount = 0
        while mCount < len(self.mList_recursive):
            mData = Menu.objects.get(id=self.mList_recursive[mCount]['id'])
            # print(mData)
            self.mList_recursive[mCount]['name'] = mData.name
            self.mList_recursive[mCount]['link'] = mData.link
            self.mList_recursive[mCount]['icon'] = mData.icon
            self.mList_recursive[mCount]['is_external'] = mData.is_external
            self.mList_recursive[mCount]['parent_id'] = mData.parent_id

            mCount += 1

    # def get_root_menu(self, menu_id):
    #     data = Menu.objects.filter(id__in=menu_id, parent=None).values('id')        
    #     ret = []
    #     for i in data:
    #         ret.append(i['id'])

    #     return ret

    def is_have_child(self, menu_id):
        '''
            cek apakah ada menu dengan parent = menu_id?
            jika ya return True, else False
        '''
        data = Menu.objects.filter(parent_id=menu_id) \
            .exclude(id__in=self.menu_custom_list) \
            .order_by('parent_id','order_menu').values('id')        
        ret = []
        for i in data:
            ret.append(i['id'])

        return ret

    def create_menu_recursive(self, root_menu_id, lvl): # , menu_group, kinds):     
        '''
            menu_group, kinds : untuk mendapatkan kondisi where, data selalu sama
            root_menu_id : berisi ID menu root untuk level 0
                           berisi ID menu[0] (data satu index saja) untuk level 1..n
                           Hanya berisi ID dengan format ['id_1', 'id_2', 'id_n']
        '''        
        # print(root_menu_id)

        for i in root_menu_id:
            child_id = self.is_have_child(i)
            if child_id:
                self.mList_recursive.append({'id':i, 'level':lvl, 'haveChild':True})
                lvl += 1                                    
                self.create_menu_recursive(child_id, lvl)                
                lvl -= 1
            else:
                self.mList_recursive.append({'id':i, 'level':lvl, 'haveChild':False})

    def update_end_tag(self):
        '''
            parameter mList_recursive
            cari yang next level turun (misal dari 1 ke 0, atau dari 2 ke 1, 2 ke 0, semua yg menurun tandai sebagai true end_tag nya)
        '''
        mCount = 0
        while mCount < len(self.mList_recursive):
            # kondisi akhir 
            if mCount == len(self.mList_recursive)-1:
                if self.mList_recursive[mCount]['level'] == 0:  # kondisi tag akhir 0, langsung set end tag = 1
                    self.mList_recursive[mCount]['haveChildEndTag'] = [1]
                else:
                    tmp = self.mList_recursive[mCount]['level']
                    self.mList_recursive[mCount]['haveChildEndTag'] = list(range(1,tmp+1))

            # kondisi lvl skr dan next sama2 nol (root)
            elif self.mList_recursive[mCount]['level'] == 0 and self.mList_recursive[mCount+1]['level'] == 0:
                self.mList_recursive[mCount]['haveChildEndTag'] = [1]

            # kondisi lvl menurun
            else:
                selisih = self.mList_recursive[mCount]['level'] - self.mList_recursive[mCount+1]['level']
                if selisih > 0:
                    self.mList_recursive[mCount]['haveChildEndTag'] = list(range(1,selisih+1))
                else:
                    self.mList_recursive[mCount]['haveChildEndTag'] = []

            mCount += 1

    # Menu bisa diberikan dengan nama yg sama, oleh karena itu cari active menu dan breadcrumb menggunakan ID
    def get_active_menu(self, menu_id):
        '''
            Find active menu recursively
        '''        
        data = Menu.objects.filter(id=menu_id) \
                .exclude(id__in=self.menu_custom_list) 
        if data:
            for i in data:
                # print(i.parent_id)
                parent_id = i.parent_id
                self.mList_active.insert(0, {'id': i.id, 'name': i.name, 'link': i.link, 'icon': i.icon, 'is_external':i.is_external})
                self.get_active_menu(parent_id)
        

