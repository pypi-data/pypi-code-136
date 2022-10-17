class AutoBuiltIns:
    @staticmethod
    def _head_tail_json_path(json_path):
        components = json_path.split(".")

        head = components[0]
        tail = ".".join(components[1:]) if len(components) > 1 else None
        return head, tail

    # dict built-ins
    def __getitem__(self, __name__):
        # 1: get the item
        # 2: split path
        # 3: skip properties and get item

        def _jsonpaths_applicable():
            return self.__jsonpaths__ and "properties" in self.keys()

        def _action_01(name):
            return self.dict()[name]

        def _action_02(name):

            head, tail = self._head_tail_json_path(name)

            if tail is not None:
                return self.dict()[head][tail]
            else:
                raise KeyError("KeyError: '{n}'".format(n=head))

        def _action_03(name):
            return self.dict()["properties"][name]

        if self.__jsonpaths__:
            actions = [_action_01, _action_02, _action_03]
        else:
            actions = [_action_01]

        value = None
        no_error = False
        error = None
        for counter, action in enumerate(actions):
            try:
                value = action(__name__)
                no_error = True
                break
            except KeyError as e:
                error = e
                # dotdicts do not throw keyerrors, only the underlying dotdict.dict() do!
                continue

        if no_error:
            return value
        else:
            raise KeyError(error)

    def __setitem__(self, __name__: str, __value__):

        if self.__jsonpaths__:
            head, tail = self._head_tail_json_path(__name__)
            if tail is not None:
                __name__ = head

                __present_value__ = self.get(head, dict())
                __updated_value__ = {tail: __value__}

                assert hasattr(
                    __present_value__, "items"
                ), "Your jsonpath is leading to the expansion of an object that is not a mapping: is the path correct?"
                __value__ = {**__present_value__, **__updated_value__}
        else:
            pass

        if self.__recursive__ and isinstance(__value__, dict):
            __value__ = DotDict(
                __value__,
                name=__name__,
                recursive=self.__recursive__,
                jsonpaths=self.__jsonpaths__,
            )

        return self.dict().__setitem__(__name__, __value__)

    # attribute built-ins
    def __getattr__(self, __name__: str, default=None):
        try:
            return self.__getitem__(__name__)
        except KeyError:
            return default

    def __setattr__(self, __name__: str, __value__):
        if self.__overrride_setattr__:
            self.__setitem__(__name__, __value__)
        else:
            super().__setattr__(__name__, __value__)
            return


class DotDict(AutoBuiltIns):
    __overrride_setattr__ = False

    def __init__(
        self,
        dictionary,
        name: str = "dotdict",
        recursive: bool = True,
        jsonpaths: bool = False,
    ):
        self.__name__ = name
        self.__recursive__ = recursive
        self.__jsonpaths__ = jsonpaths
        self.__dictionary__ = dict()
        for k, v in dictionary.items():
            self.__setitem__(k, v)

        self.__overrride_setattr__ = True
        return

    # representations
    def __repr__(self):
        return "{} {}".format(self.__name__, list(self.keys()))

    # serialize (to dump to json)
    def serialize(self, flatten=("")):
        def _serialize(o):
            d = dict()
            for k, v in o.items():
                if isinstance(v, dict):
                    v = _serialize(v)
                elif isinstance(v, DotDict) and k in flatten:
                    v = v.flatten()
                elif isinstance(v, DotDict) and k not in flatten:
                    v = _serialize(v)
                else:
                    pass
                d[k] = v
            return d

        return _serialize(self)

    # mirror dict behavior
    def dict(self):
        return self.__dictionary__

    # dict-like behavior
    def keys(self):
        return self.dict().keys()

    def values(self):
        return self.dict().values()

    def items(self):
        return self.dict().items()

    def get(self, key, default=None):
        return self.dict().get(key, default)

    def pop(self, key, default=None):
        return self.dict().pop(key, default)

    # jsonpaths
    def collect_jsonpaths(self, prefix: str = ""):
        def _collect_jsonpaths(dd, prefix=""):
            keys = []
            prefix = "{p}.".format(p=prefix) if len(prefix) > 0 else ""
            for k, v in dd.items():
                key = "{p}{k}".format(p=prefix, k=k)

                if hasattr(v, "items") and len(v.items()) > 0:
                    keys.extend(_collect_jsonpaths(v, prefix=key))
                else:
                    keys.append(key)
            return keys

        return _collect_jsonpaths(self, prefix="")

    def flatten(self, prefix: str = ""):
        return {k: self[k] for k in self.collect_jsonpaths(prefix=prefix)}

    def jsonpaths(self):
        # alternative for keys() for a complete iteration
        return self.collect_jsonpaths()

    @property
    def jsonpaths_enabled(self):
        return self.__jsonpaths__
