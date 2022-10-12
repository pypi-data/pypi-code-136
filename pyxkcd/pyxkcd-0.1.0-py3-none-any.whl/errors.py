class XkcdError(Exception):
    """
    Base class for exceptions in this module.
    """

    pass


class InvalidComicError(XkcdError):
    """
    Exception raised for errors caused by non-existent comics.
    """

    pass
