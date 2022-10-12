import os
import json
import time
import queue
from _collections import defaultdict
import inspect
import functools
import sys


def is_Windows():
    return os.sep == '\\'

    
# is Linux System
def is_Linux():
    return os.sep == '/'


def argmax(arr):
    maxi = arr[0]
    index = 0
    for i in range(1, len(arr)):
        a = arr[i]
        if a > maxi:
            index = i
        
    return index

def argmin(arr):
    maxi = arr[0]
    index = 0
    for i in range(1, len(arr)):
        a = arr[i]
        if a < maxi:
            index = i
        
    return index

def rindex(arr, e):
    for i, _e in enumerate(reversed(arr)):
        if e == _e:
            return -i - 1
    else:
        raise ValueError(f'{e} is not in list')


def batch_map(proc, items, processes=8):
    from multiprocessing import Pool
    with Pool(processes=processes) as pool:
        return pool.map(proc, items)    
    

def eol_convert(fileName):
    with open(fileName, "rb") as f:
        data = bytearray(os.path.getsize(fileName))
        f.readinto(data)
        # print(data)
        data = data.replace(b"\r\n", b"\n")

    with open(fileName, "wb") as f:
        # print(data)
        f.write(data)    


def cstring(s):
    return bytes(s, 'utf8')


def json_encode(data, utf8=False, indent=None):
    from types import FunctionType
    if isinstance(data, FunctionType):

        def func(*args, **kwargs): 
            return json_encode(data(*args, **kwargs), utf8=utf8, indent=indent)
        
        func.__name__ = data.__name__
        return func 
    
    s = json.dumps(data, ensure_ascii=False, indent=indent, cls=JSONEncoder)
    if utf8:
        s = s.encode(encoding='utf-8')
    return s 


class Object:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value

    def __iter__(self):  # Get iterator object on iter
        return iter(self.__dict__.keys())

    def __getitem__(self, index):
        return self.__dict__.get(index, None)

    def __setitem__(self, index, rhs):
        self.__dict__[index] = rhs
    
    def __setattr__(self, index, rhs): 
        self.__dict__[index] = rhs
        
    def __getattr__(self, index): 
        return self.__dict__.get(index, None)

    def keys(self):
        return self.__dict__.keys()
    
    def items(self):
        return self.__dict__.items()
    
    def serialize(self):
        res = {}
        for k, v in self.__dict__.items():
            if isinstance(v, Object):
                v = v.serialize()
            res[k] = v
        return res
    
    # perform el in self
    def __contains__(self, el):
        return el in self.__dict__
    
    def pop(self, key):
        return self.__dict__.pop(key)
    
    def __str__(self):
        return str(self.__dict__)
    
    __repr__ = __str__
    
    # self | rhs
    # self |= rhs
    def __or__(self, rhs):
        obj = Object()
        for key, value in self.items():
            obj[key] = value

        for key, value in rhs.items():
            obj[key] = value
            
        return obj

    def __len__(self):
        return len(self.__dict__)
    
    def __eq__(self, rhs):
        if len(self) != len(rhs):
            return False
        
        for k, v in self.items():
            if v != rhs[k]:
                return False
        return True

    @staticmethod
    def from_dict(kwargs):
        obj = Object()
        for key, value in kwargs.items():
            if isinstance(value, dict):
                value = Object.from_dict(value)
                
            obj[key] = value
        return obj
      
class JSONEncoder(json.JSONEncoder):

    def default(self, obj):
      
        if isinstance(obj, (bytes, bytearray)):
            return str(obj, encoding='utf-8')
        
        if isinstance(obj, Object): 
            return obj.__dict__
        
        from inspect import isgenerator#, isgeneratorfunction
        if isgenerator(obj):
            return [*obj]
        
        return super().default(self, obj)

def binary_insert(arr, value, compareTo=None):
    index = binary_search(arr, value, compareTo)
    arr.insert(index, value)  
    
def binary_search(arr, value, compareTo=None):    
    if compareTo is None:
        compareTo = lambda x, y: -1 if x < y else 1 if x > y else 0
        
    begin = 0
    end = len(arr)
    while True:
        if begin == end:
            return begin
            
        mid = begin + end >> 1
        ret = compareTo(arr[mid], value)
        if ret < 0:
            begin = mid + 1
        elif ret > 0:
            end = mid
        else:
            return mid


def equal_range(arr, value, compareTo=None):
    if compareTo is None:
        compareTo = lambda x, y: -1 if x < y else 1 if x > y else 0
    
    begin = 0
    end = len(arr)
    while True:
        if begin == end:
            break
            
        mid = begin + end >> 1
            
        ret = compareTo(arr[mid], value)
        if ret < 0:
            begin = mid + 1
        elif ret > 0:
            end = mid
        else:
            stop = begin - 1
            begin = mid
            while True:
                pivot = -(-begin - stop >> 1)
                if pivot == begin:
                    break
                    
                if compareTo(arr[pivot], value):
                    stop = pivot
                else:
                    begin = pivot

            while True:
                pivot = mid + end >> 1
                if pivot == mid:
                    break
                    
                if compareTo(arr[pivot], value):
                    end = pivot
                else:
                    mid = pivot

            break
        
    return begin, end


def computed(prop):

    @cache
    @property
    def func(self):
        return prop(self)

    func.fget.__name__ = prop.__name__
    return func


def cache(prop):
    if isinstance(prop, property): 

        class cached(property):
                
            def __get__(self, obj, objtype=None):
                name = self.fget.__name__
                if name in obj.__dict__:
                    return obj.__dict__[name]
                value = self.fget(obj)
                obj.__dict__[name] = value
                return value

        return cached(prop.fget)
    
        
class cached_property:
    "Emulate PyProperty_Type() in Objects/descrobject.c"
 
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc
 
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        
        name = self.fget.__name__
        if name in obj.__dict__:
            return obj.__dict__[name]
        value = self.fget(obj)
        obj.__dict__[name] = value
        return value
 
    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)
 
    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)
 
    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)
 
    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)
 
    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


def indexOf(arr, value):
    for i, val in enumerate(arr):
        if val == value:
            return i
    
    return -1
    
    
class _DecoratorContextManager:
    """Allow a context manager to be used as a decorator"""

    def __call__(self, func):
        if inspect.isgeneratorfunction(func):
            return self._wrap_generator(func)

        @functools.wraps(func)
        def decorate_context(*args, **kwargs):
            with self.__class__():
                return func(*args, **kwargs)
        return decorate_context

    def _wrap_generator(self, func):
        """Wrap each generator invocation with the context manager"""
        @functools.wraps(func)
        def generator_context(*args, **kwargs):
            gen = func(*args, **kwargs)

            # Generators are suspended and unsuspended at `yield`, hence we
            # make sure the grad mode is properly set every time the execution
            # flow returns into the wrapped generator and restored when it
            # returns through our `yield` to our caller (see PR #49017).
            cls = type(self)
            try:
                # Issuing `None` to a generator fires it up
                with cls():
                    response = gen.send(None)

                while True:
                    try:
                        # Forward the response to our caller and get its next request
                        request = yield response

                    except GeneratorExit:
                        # Inform the still active generator about its imminent closure
                        with cls():
                            gen.close()
                        raise

                    except BaseException:
                        # Propagate the exception thrown at us by the caller
                        with cls():
                            response = gen.throw(*sys.exc_info())

                    else:
                        # Pass the last request to the generator and get its response
                        with cls():
                            response = gen.send(request)

            # We let the exceptions raised above by the generator's `.throw` or
            # `.send` methods bubble up to our caller, except for StopIteration
            except StopIteration as e:
                # The generator informed us that it is done: take whatever its
                # returned value (if any) was and indicate that we're done too
                # by returning it (see docs for python's return-statement).
                return e.value

        return generator_context

    
class Timer(_DecoratorContextManager):
    def __init__(self, message=None, logger=None, startHint=False):
        self.message = message
        self.logger = logger
        if startHint:
            if self.logger:
                self.logger.info(message)
            else:
                print(message)
        
    def __enter__(self):
        self.start = time.time()
        
    def __exit__(self, *_): 
        lapse = time.time() - self.start
        if self.message:
            msg = f'time cost for {self.message} is {lapse} seconds'
        else:
            msg = f'time cost is {lapse} seconds'
            
        if self.logger:
            self.logger.info(msg)
        else:
            print(msg)            

def setitem(arr, *args):
    *indices, index, value = args
    
    for i in indices:
        if i >= len(arr):
            arr += [None] * (i + 1 - len(arr))
            
        if arr[i] is None:
            arr[i] = []
            
        arr = arr[i]
        
    if index >= len(arr):
        arr += [None] * (index + 1 - len(arr))
        
    arr[index] = value
    
    
def getitem(data, *indices):
    for i in indices:
        if data is None:
            return
                
        if i >= len(data):
            return
        
        data = data[i]
    
    return data


def splice(arr, index, num, *args):
    del arr[index: index + num]
    
    for arg in args:
        arr.insert(index, arg)
        index += 1
        
    return arr

def split_filename(filename):
    extIndex = filename.rindex('.')
    return filename[:extIndex], filename[extIndex + 1:]


def json_to_array(json):
    if isinstance(json, list):
        return [json_to_array(data) for data in json]
    
    if isinstance(json, dict) and all(isinstance(index, int) or index.isdigit() for index in json):
        arr = []
        for index in json: 
            setitem(arr, int(index), json_to_array(json[index]))
    
        return arr
    
    return json


def toggleCase(s):
    return ''.join(ch.upper() if ch.islower() else ch.lower() if ch.isupper() else ch for ch in s)


def clip(this, min, max):
    if this < min:
        return min
    
    if this > max:
        return max
        
    return this

def deleteIndices(arr, fn, postprocess=None):
    indicesToDelete = []
    for i in range(len(arr)):
        if fn(arr, i):
            indicesToDelete.append(i)
            
    if indicesToDelete:
        indicesToDelete.reverse()
        for i in indicesToDelete:
            if postprocess:
                postprocess(arr, i)
            del arr[i]
            
            
def batches(listOfElement, batch_size):
    batches = [None] * ((len(listOfElement) + batch_size - 1) // batch_size)

    index = 0
    for i in range(0, len(listOfElement), batch_size):
        batches[index] = listOfElement[i: min(i + batch_size, len(listOfElement))]
        index += 1
    return batches

            
if __name__ == '__main__':
    obj = Object(a=1, b=2, c=3)
    dic = {**obj}
    print(dic)
    
