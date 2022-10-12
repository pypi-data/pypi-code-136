import itertools


def escape_string(string: str) -> str:
    return string.encode("unicode_escape").decode("utf-8")


def pairwise(iterable):
    if not iterable:
        return iterable
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)
