def return_on_failure(errors=(Exception,), default_value=None):
    def decorator(func):
        def applicator(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors:
                return default_value

        return applicator

    return decorator
