'''
    1. ----------------------------------------------------------------------------
    Parameter menu_group [Optional]
    Jika kosong, cek Site_ID (proses berdasarkan site ID menu default)
    Jika menu_group kosong, SITE_id harus ada, jika tidak maka ditidak datap di proses

    2. ----------------------------------------------------------------------------
    Di tabel tambahkan User_ID dan Site_ID
    Jika data SITE_ID saja yg ada maka ini untuk front end
    Jika User_ID saja yg ada maka ini sebagai backend

    3. ----------------------------------------------------------------------------
    Jika dua2nya ada, maka USER_ID saja yg di cek SITE_ID tidak di gunakan

    Update 4 Oktober 2022
'''

from django import template
from ..models import Menu
from ..menus import Menus

register = template.Library()

# SET GLOBAL VARIABLE FORM MENU
 # cache nanti di template
 # variable global ini bukan untuk cache
global_menu = {} 
# format:
    # USER_ID, MENU_DATA, User_group, site_ID
    # Ada project_ID (untuk membedakan, project company_profile, acounting, etc)


# 2. Create Menu 
class MenuCreate(template.Node):
    '''
        menu_kind :
            FRONTEND = 1
            BACKEND = 2 

        menu_group :
            jika = 0 maka front end, menu group kosong (ignore untuk mode frontend)
    '''
    def __init__(self, menu_kind, menu_group = 0, var_name='menu'):       
        self.menu_group = menu_group
        self.menu_kind = menu_kind           
        self.var_name = var_name

    # 1. Cache server
    #    Cek jika sudah ada data di variable maka tidak perlu ambil lagi di database
    # def menu_cache():
    #     lanjut = False
    #     if global_menu:
    #         if global_menu[self.menu_group]:

    #     if not global_menu:
    #         if self.menu_kind == 'FRONTEND':                  
    #             my_menu = Menus(self.menu_group, 1)
    #         else:                  
    #             my_menu = Menus(self.menu_group, 2)
    #         global_menu[self.menu_group] = my_menu
    #         print('load from source')
    #     else:
    #         if not global_menu[self.menu_group]:
    #             if self.menu_kind == 'FRONTEND':                  
    #                 my_menu = Menus(self.menu_group, 1)
    #             else:                  
    #                 my_menu = Menus(self.menu_group, 2)
    #             global_menu[self.menu_group] = my_menu
    #             print('load from source')
    #         else:
    #             my_menu = global_menu[self.menu_group]
    #             print('load from cache')   

    def render(self, context):        
        # print('group = ', self.menu_group)
        # print('kinds = ', self.menu_kind)
        # print('var_name = ', self.var_name)
        
        # Parameter di template tidak perlu menggunakan tanda petik untuk menandakan string

        # if not global_menu:
        #     if self.menu_kind == 'FRONTEND':                  
        #         my_menu = Menus(self.menu_group, 1)
        #     else:                  
        #         my_menu = Menus(self.menu_group, 2)
        #     global_menu[self.menu_group] = my_menu
        #     print('load from source')
        # else:
        #     if not global_menu[self.menu_group]:
        #         if self.menu_kind == 'FRONTEND':                  
        #             my_menu = Menus(self.menu_group, 1)
        #         else:                  
        #             my_menu = Menus(self.menu_group, 2)
        #         global_menu[self.menu_group] = my_menu
        #         print('load from source')
        #     else:
        #         my_menu = global_menu[self.menu_group]
        #         print('load from cache') 

        if self.menu_kind == 'FRONTEND':    
            # print('oke')
            my_menu = Menus(self.menu_group, 1)
        else:
            my_menu = Menus(self.menu_group, 2)

        global_menu['0'] = my_menu
        context[self.var_name] = my_menu.get_menus()
        return ''

@register.tag(name='menu_create')            
def get_menu_list(parser, token):
    error = False
    try :
        tag_name, menu_kind, menu_group, _as, var_name = token.split_contents()
        if _as != 'as':
            error = True
    except:
        error = True

    if error:
        raise template.TemplateSyntaxError('menu_create must be of the form, "menu_create <menu_group> <menu_kind> as <var_name>"')
    else:
        return MenuCreate(menu_kind, menu_group, var_name)    

# ------------------------
# get active mnu

# @register.simple_tag(takes_context=True)
# def menu_active_simple_tag(context, active_menu, menu_group):    
#     my_menu = global_menu['1']
#     print('simple tag = ', my_menu.find_activeMenuList(active_menu))
#     return my_menu.get_menus()

# # OKE pakai simple tag
@register.simple_tag    #(takes_context=True) context, 
def menu_active(active_menu):    
    my_menu = global_menu['0']  # harus tipe data string    
    my_menu.get_active_menu(active_menu)
    return my_menu.get_list_active()

# @register.simple_tag # (takes_context=True) context
# def menu_breadcrumb(active_menu):    
#     # print('active_menu =' ,active_menu)
#     my_menu = global_menu['0']  # harus tipe data string  
#     # print(my_menu)  
#     return my_menu.create_breadcrumb(active_menu)


# OKE pakai simple tag untuk create bread crumb
# @register.simple_tag
# def menu_bread_crumb():
#     my_menu = global_menu['0']
#     print('bread  =', my_menu.create_breadCrumb('profile')    )
#     return my_menu.create_breadCrumb('profile')    