from tornado.escape import xhtml_escape, to_unicode


class SafeString(bytes):
    """Instances of this class will not be escaped in the templates.

    This only works with ``conditional_xhtml_escape`` function as Tornado's
    built-in ``xhtml_escape`` function has not concept of safe objects.

    We're inheriting it from ``bytes`` because Tornado's template engine
    encodes ``str`` to bytestring but an already bytestring object is
    returned as-is, before it's passed on to the escape function.

    If we inherit from ``str``, the information that it's a safe object
    will be lost during conversion to bytestring.

    This is also the reason we can't re-use pre-existing implementation
    safe objects from third-party libs such as makupsafe.Markup because
    they inherit from ``str``.
    """
    pass


def conditional_xhtml_escape(value):
    if isinstance(value, SafeString):
        return to_unicode(value)
    return xhtml_escape(value)


def mark_safe(value):
    if isinstance(value, str):
        value = SafeString(value.encode('utf8'))
    elif hasattr(value, '__html__'):
        # __html__ method is implemented in many libraries
        # to denote that it returns safe html data
        value = SafeString(value.__html__().encode('utf8'))
    return value


def format_html(format_str, *args, **kwargs):
    # taken from django
    args_safe = map(conditional_xhtml_escape, args)
    kwargs_safe = {k: conditional_xhtml_escape(v) for (k, v) in kwargs.items()}
    return mark_safe(format_str.format(*args_safe, **kwargs_safe))
