from get_auth import current_request


category = current_request.category()
print(f'Category: {category}')
