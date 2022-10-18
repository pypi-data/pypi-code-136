import datetime
import decimal
from types import FunctionType, MethodType, ModuleType
from google.protobuf.reflection import GeneratedProtocolMessageType
from google.protobuf.internal import api_implementation

if api_implementation.Type() == "upb":
    import google

import six

if six.PY2:
    from types import TypeType

try:
    import numpy
except ImportError:
    numpy = None

try:
    import torch
except ImportError:
    torch = None

try:
    import multidict
except ImportError:
    multidict = None

try:
    from bson import ObjectId
    from bson.raw_bson import RawBSONDocument
except ImportError:
    ObjectId = None
    RawBSONDocument = None

class NamespaceSerializerBase(object):
    BUILTIN_ATTRIBUTES_IGNORE = {
        '__dict__',
        '__module__',
        '__weakref__',
        '__name__',
        '__doc__',
        '__qualname__',
        '__spec__',
        '__defaults__',
        '__code__',
        '__globals__',
        '__closure__',
        '__annotations__',
        '__kwdefaults__',
        '__bases__'}

    try:
        BINARY_TYPES = (buffer, bytearray)
        CODE_TYPES = (FunctionType, MethodType, TypeType, ModuleType, six.MovedModule)
        PRIMITIVE_TYPES = (type(None), int, long, float, str, unicode, complex, decimal.Decimal) + BINARY_TYPES + CODE_TYPES + (datetime.datetime,)

    except NameError:
        BINARY_TYPES = (bytearray, bytes)
        CODE_TYPES = (FunctionType, MethodType, type, ModuleType, six.MovedModule)
        PRIMITIVE_TYPES = (type(None), int, float, str, complex, decimal.Decimal) + BINARY_TYPES + CODE_TYPES + (datetime.datetime,)

    def __init__(self, use_string_cache=False):
        self.use_string_cache = use_string_cache
        self.string_cache = {}

        if use_string_cache:
            # Lock the 0 index since some variant will have no originalType (container for example)
            self.string_cache[""] = 0

        self.estimated_pending_bytes = 0

    def get_string_cache(self):
        return self.string_cache

    def get_estimated_pending_bytes(self):
        return self.estimated_pending_bytes

    def _get_string_index_in_cache(self, string_to_cache):
        index = self.string_cache.get(string_to_cache, None)
        if index is None:
            index = len(self.string_cache)
            # We estimate each character is one byte in utf-8 and overhead is 5 bytes
            self.estimated_pending_bytes += len(string_to_cache) + 5
            self.string_cache[string_to_cache] = index

        return index

    @staticmethod
    def _get_object_width(obj):
        object_width = 0
        if hasattr(obj, '__dict__') and obj.__dict__:
            object_width += len(obj.__dict__)
        if hasattr(obj, '__slots__') and obj.__slots__:
            object_width += len(obj.__slots__)
        return object_width

    if six.PY2:
        @staticmethod
        def normalize_string(obj):
            if isinstance(obj, str):
                return unicode(obj, errors="replace")
            else:
                return unicode(obj)
    else:
        @staticmethod
        def normalize_string(obj):
            return obj

    @staticmethod
    def is_numpy_obj(obj):
        if not numpy:
            return False

        return not isinstance(obj, six.MovedModule) and isinstance(obj, numpy.generic)

    @staticmethod
    def is_torch_obj(obj, obj_type=None):
        if torch is None:
            return False

        if obj_type is None:
            obj_type = type(obj)

        module = getattr(obj_type, '__module__', None)
        if not module:
            return False

        return module.startswith('torch')

    @staticmethod
    def is_multidict_obj(obj):
        if not multidict:
            return False

        return isinstance(obj, (multidict.MultiDict, multidict.CIMultiDict,
                                multidict.MultiDictProxy,
                                multidict.CIMultiDictProxy))

    @staticmethod
    def is_protobuf_obj(obj):
        klass = getattr(obj, '__class__', None)
        if api_implementation.Type() == "upb":
            if klass is not None and isinstance(klass, google._upb._message.MessageMeta):
                return True
        else:
            if klass is not None and isinstance(klass, GeneratedProtocolMessageType):
                return True

        return False

    @staticmethod
    def is_bson(obj):
        if not ObjectId or not RawBSONDocument:
            return False

        klass = getattr(obj, '__class__', None)
        if klass is not None and isinstance(obj, ObjectId):
            return True

        if klass is not None and isinstance(obj, RawBSONDocument):
            return True

        return False
