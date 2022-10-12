from .utils import Util


class Field:

    """
    List[etype=xxx]
    Int
    Label[dom=xxx]
    """

    FIELD_MAPPING = {
        "bbox": "BBox",
        "int": "Int",
        "float": "Num",
        "str": "Str",
        "points": "Polygon",
        "list": "List",
        "media": "Image",
        "bool": "Bool",
        "category": f"Label",
        "map_path": "SegMap"
    }
    ARG_MAPPGING = {
        'BBox': None,
        "Polygon": None,
        'Int': None,
        'Num': None,
        'Str': None,
        'Image': None,
        'Bool': None,
        "Label": 'dom',
        "List": "etype",
        "SegMap": "dom",
    }

    def __init__(self, name, field_value=None, field_type=None, is_attr=None, param=None):
        """
            param: 如果当前field有参数的话，
                比如 ListField, 则需要指定其参数 List[etype={param}]
                比如 LabelField，组要指定参数 Label[dom={param}]
        """
        self._name = name
        self._is_attr = is_attr
        self._param = param
        self._arg = None
        if field_type is not None:
            self.field_type = self.FIELD_MAPPING[field_type]
        elif field_value is not None:
            self.field_type = self.FIELD_MAPPING[field_value.__class__.__name__]
            if self.field_type == "List":
                self._param = self.FIELD_MAPPING[field_value[0].__class__.__name__]
        else:
            raise RuntimeError("not supported field type")

        self._arg = self.ARG_MAPPGING[self.field_type]
        if self.arg is not None:
            assert isinstance(self.param, str)

    @property
    def is_attr(self):
        return self._is_attr

    @property
    def type(self):
        return self.field_type

    @property
    def arg(self):
        return self._arg

    @property
    def param(self):
        return self._param

    @property
    def name(self):
        return self._name

    def format(self):
        if not self._is_attr and not self.arg:
            return {self._name: self.field_type}
        elif self.is_attr and not self.arg:
            return {self._name: f"{self.field_type}[is_attr=True]"}
        elif not self.is_attr and self.arg:
            return {self._name: f"{self.field_type}[{self.arg}={self.param}]"}
        else:
            return {self._name: f"{self.field_type}[is_attr=True, {self.arg}={self.param}]"}


class Struct:
    DEF = "struct"

    def __init__(self, name, args=None):
        """
        当前struct的名字
        """
        self._name = name
        self._fields = []
        self._field_names = []
        self._optional = []
        if args is None:
            self._args = []
        elif not isinstance(args, list):
            self._args = [args]
        else:
            self._args = args

    @property
    def args(self):
        return self._args

    @property
    def fields(self):
        return self._fields

    @property
    def optional_field_names(self):
        return self._optional

    def set_arg(self, args):
        if not isinstance(args, list):
            self._args = [args]
        else:
            self._args = args

    def add_field(self, item, optional=False):
        if item.name in self._field_names:
            return
        self._fields.append(item)
        self._field_names.append(item.name)
        if optional:
            self._optional.append(item.name)

    def set_optional(self, name):
        if name in self._field_names:
            self._optional.append(name)
            return
        else:
            raise RuntimeError(f"field {name} not exists.")

    @property
    def name(self):
        return self._name

    def format(self):
        content = dict()
        content["$def"] = self.DEF
        if self._args:
            content["$params"] = Util.flist(self._args)
        content["$fields"] = {}
        for field in self._fields:
            content["$fields"].update(field.format())
        optional_lst = list(set(self._optional))
        if optional_lst:
            content["$optional"] = Util.flist(optional_lst)
        return {self.name: content}

    def as_others_param(self, other_struct):  # TODO: debug

        return f"{self._name}[{self.args[0]}=${other_struct.args[0]}]"
