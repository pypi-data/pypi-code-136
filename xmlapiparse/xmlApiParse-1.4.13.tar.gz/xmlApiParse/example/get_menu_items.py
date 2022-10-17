from get_auth import current_request


menu_list = current_request.get_menu_items()
filter_name = current_request.get_menu_items('Бомба брава с ромеско и щучьей икрой')
print(f'All menu by code: {menu_list}')
print(f'Filter menu: {filter_name}')
