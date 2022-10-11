"""Main module."""


def batchify(iterable, n=1):
    iter_len = len(iterable)
    for ndx in range(0, iter_len, n):
        yield iterable[ndx:min(ndx + n, iter_len)]


def camel_to_snake(camel_str):
    import re
    snake_str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake_str).lower()


def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for key, val in d.items():
        new_key = (parent_key + sep + key) if parent_key else key
        if isinstance(val, dict):
            items = {**items, **flatten_dict(val, parent_key=new_key, sep=sep)}
        else:
            items[new_key] = val
    return items
