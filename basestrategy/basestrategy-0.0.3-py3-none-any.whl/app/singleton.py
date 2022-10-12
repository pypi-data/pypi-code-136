class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """if instance already exist dont create one"""
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
