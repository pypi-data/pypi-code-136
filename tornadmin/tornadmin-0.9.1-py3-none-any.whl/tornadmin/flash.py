from tornado import escape
from json.decoder import JSONDecodeError


class FlashMixin:
    """Mixin class for adding flash message feature to a request handler.

    This is provided as mixin so that it can be used outside of the admin as well.
    """
    def flash(self, category, message):
        """Create flash messages.

        It is important that this method must be called **before** flushing the 
        response because once the response is flushed, http headers can't be
        modified.
        """
        if not hasattr(self, '_enqueued_flash_messages'):
            setattr(self, '_enqueued_flash_messages', [])

        self._enqueued_flash_messages.append((category, message))

        messages = self.get_flashed_messages(clear=False)

        self.set_cookie('flash', flash_cookie_encoder(messages))

    def get_flashed_messages(self, clear=True):
        """Returns a list of all flashed messages including the fresh ones
        set on the current request.

        Calling this function assumes that the messages will be displayed
        to the user. Hence, the messages will also be cleared from the cookie.

        If you need to preserve the messages, pass `clear=False` argument. 

        It is important that this method must be called **before** flushing the
        response because once the response is flushed, http headers can't be
        modified. That means the cookie won't be cleared and the messages will
        persist for multiple requests.
        """
        cookie = self.get_cookie('flash', None)

        _enqueued = getattr(self, '_enqueued_flash_messages', [])

        if clear:
            if cookie or len(_enqueued):
                self.clear_cookie('flash')

        if not cookie:
            return _enqueued

        messages = flash_cookie_decoder(cookie)

        return messages + _enqueued


def flash_cookie_encoder(messages):
    for message in messages:
        message = list(message)

    return escape.url_escape(escape.json_encode(messages))


def flash_cookie_decoder(value):
    try:
        _messages = escape.json_decode(escape.url_unescape(value))
    except JSONDecodeError:
        return []

    messages = []
    for message in _messages:
        messages.append(tuple(message))
    return messages
