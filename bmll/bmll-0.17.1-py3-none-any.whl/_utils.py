from functools import partial
import warnings

import pandas as pd


__all__ = ('chunk_call', 'to_pandas', 'paginate', 'to_list_of_str')


ID_COL_TYPE = 'Int64' if pd.__version__ >= '0.24.0' else 'object'


def to_pandas(table):
    """Return a pandas DataFrame from a Table response."""
    df = pd.DataFrame(data=table['data'], columns=table['columns'])

    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])

    if 'ObjectId' in df.columns:
        df['ObjectId'] = df['ObjectId'].astype(ID_COL_TYPE)

    return df


def _collect_notifications(container, response):
    """ Add notifications from the response JSON data to the given container if
        they are present in the response data.

        If present at the top-level of the response JSON data, a 'notifications'
        key is looked up. If present, that must have a 'message' key beneath if
        whose value is a string message to display to the user.
    """
    notifications = response.get('notifications')
    if notifications:
        container.add(notifications['message'])


def paginate(request):
    table = request()
    token = table.get('token')

    all_notifications = set()
    _collect_notifications(all_notifications, table)

    while token:
        page = request(token=token)
        _collect_notifications(all_notifications, page)

        if isinstance(table['data'], dict):
            table['data'].update(page['data'])
        else:
            table['data'].extend(page['data'])
        token = page.get('token')

    if all_notifications:
        notifications = "\n".join(all_notifications)
        warnings.warn(notifications, stacklevel=2)

    return table


def chunk_call(req_func, object_ids, chunk_size):
    """
    Retrieve data from `req_func` after splitting requests by `objects_ids`.

    This avoids a single request with an excessive request body size.

    Args:
        req_func: func
            Request function with kwargs `object_ids` and `token`.
        object_ids: list(int)
            IDs of objects for which to retrieve data.
        chunk_size: int
            Maximum number of object IDs in a single request.

    Returns:
        `pandas.DataFrame`:
            Data from the service.
    """
    if chunk_size < 1:
        raise ValueError('Chunk size must be greater than or equal to 1.')

    if object_ids is None:
        chunks = [None]
    else:
        chunks = [object_ids[i:i + chunk_size] for i in range(0, len(object_ids), chunk_size)]

    data = []
    for chunk_ids in chunks:
        chunk_func = partial(req_func, object_ids=chunk_ids)
        table = paginate(chunk_func)
        df = to_pandas(table)
        data.append(df)
    return pd.concat(data)


def to_list_of_str(x):
    """Converts variable to list. int -> list, str -> list, list -> list."""
    if hasattr(x, '__iter__') and not isinstance(x, str):
        return [str(y) for y in x]
    return [str(x)]
