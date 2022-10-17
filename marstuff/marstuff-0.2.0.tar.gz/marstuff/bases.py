import inspect
import json
from datetime import date, datetime


class ObjectBaseMeta(type):
    def __call__(cls, *args, **kwargs):
        if len(args) == 1:
            if isinstance(args[0], dict):
                kwargs = {**args[0]}
                args = ()
            elif isinstance(args[0], str) or isinstance(args[0], bytes):
                data = json.loads(args[0])
                if type(data) == list:
                    return cls.__call__(data)
                kwargs = {**data}
                args = ()
            elif isinstance(args[0], list):
                object_list = []
                for data in args[0]:
                    object_list.append(cls.__call__(**data))
                return object_list

        try:
            object_ = object.__new__(cls)
        except:
            object_ = cls.__new__(cls)
        object_.__init__(*args, **kwargs)
        object_.extended_objects = []
        return object_


class ObjectBase:
    @classmethod
    def from_json(cls, json):
        obj: cls = cls.__call__(json)
        return obj

    def to_json(self):
        return json.dumps(dict(self))

    def convert_to_raw_json(self, var):
        if isinstance(var, ObjectBase):
            return str(var)
        if isinstance(var, list):
            return [self.convert_to_raw_json(x) for x in var]
        if isinstance(var, ObjectBase):
            return dict(var)
        if isinstance(var, (date, datetime)):
            return var.isoformat()
        return var

    def __iter__(self):
        for field in list(inspect.signature(self.__init__).parameters)[:-1]:
            yield field, self.convert_to_raw_json(getattr(self, field))

    def __repr__(self):
        return f'<{self.__class__.__name__} {" ".join(x[0] + "=" + str(x[1]) for x in list(self))}>'


class Object(ObjectBase, metaclass = ObjectBaseMeta):
    pass
