"""Custom middlewares"""

from ipware import get_client_ip  # type: ignore


def real_ip_middleware(get_response):
    """Set REMOTE_ADDR for ip guessed by django-ipware."""

    def middleware(request):
        request.META["REMOTE_ADDR"] = get_client_ip(request)[0]
        return get_response(request)

    return middleware
