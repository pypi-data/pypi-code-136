import abc


class APIMethod():
    """
    Base API Method
    """
    http_method: str = "GET"
    path: str