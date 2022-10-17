from get_auth import current_request

order_list, last_version = current_request.get_orders()
print(f'All Orders: {order_list}')
