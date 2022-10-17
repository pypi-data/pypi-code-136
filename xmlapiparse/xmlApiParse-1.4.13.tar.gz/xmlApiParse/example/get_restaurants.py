from get_auth import current_request


restaurant_list = current_request.get_restaurants()
print(f'All restaurants: {restaurant_list}')
