from get_auth import current_request

get_order = current_request.get_order_lines()
print(f'Orders Line: {get_order}')
