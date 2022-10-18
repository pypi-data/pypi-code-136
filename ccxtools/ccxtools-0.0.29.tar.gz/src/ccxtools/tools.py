def add_query_to_url(base_url, queries):
    url = f'{base_url}?'
    for field, value in queries.items():
        url += f'{field}={value}&'
    return url[:-1]
