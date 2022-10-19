def EMPTY_METHOD(*args, **kwargs):
    pass


class AttrMap(dict):

    def __getattr__(self, item):
        return self.get(item)


class ModuleNotExistedError(Exception):
    pass
