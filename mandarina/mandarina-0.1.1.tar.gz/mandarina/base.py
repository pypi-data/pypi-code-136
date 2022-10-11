from datetime import datetime


def frange(start, stop, increment):
    """
    Custom iterator to iterate in floating point steps.
    :return: Generator of steps between start and stop

    Example:
        for n in frange(0, 4, 0.5):
        print(n)
    """
    x = start
    while x < stop:
        yield x
        x += increment


def unixtime_to_isotime(unixtime, microseconds):
    """
    Converts a unix timestamp to a readable string timestamp
    :param unixtime:
    :param microseconds: If True microseconds will be visible
    :return:
    """
    return datetime.fromtimestamp(unixtime).strftime(
        "%Y-%m-%dT%H:%M:%S" + microseconds * ".%f"
    )


def apply_async(func, args, *, callback):
    """
    Async callback
    :param func:
    :param args:
    :param callback:
    :return:
    """
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


def get_iso_timestamp():
    """
    Returns a string of an ISO 8601 timestamp without microseconds
    :return: ISO 8601 timestamp string
    """
    return datetime.now().replace(microsecond=0).isoformat()
