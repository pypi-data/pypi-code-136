def log(text):
    """
    Melakukan print ke console untuk menginformasikan proses yg sedang berjalan didalam program.
    """

    def inner_log(func):
        print(f">>> {text}")

        def callable_func(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return callable_func

    return inner_log
