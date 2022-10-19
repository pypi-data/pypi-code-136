__all__ = [
    'ResultException', 'ResultType', 'Result', 'Ok', 'Err',
    'WrappedBase', 'UnwrappedBase', 'wrap_result', 'auto_unwrap',
]

import types
import asyncio
import inspect
from typing import Any, Callable, ForwardRef
from functools import wraps


class ResultException(Exception):
    pass


class _ResultType(type):
    pass


class ResultType(_ResultType):
    def __getitem__(cls, key: Any) -> type:
        if cls is Ok or issubclass(cls, Ok):
            T: ResultType = type(f'Ok[{key}]', (Ok,), {
                '__annotations__': {
                    'v': key
                }
            })
        elif cls is Err or issubclass(cls, Err):
            T: ResultType = type(f'Err[{key}]', (Err,), {
                '__annotations__': {
                    'e': key
                }
            })
        elif cls is Result or issubclass(cls, Result):
            T: ResultType = type(f'Result[{key}]', (Result,), {
                '__annotations__': {
                    'v': key[0],
                    'e': key[1],
                }
            })
        else:
            raise TypeError(f'Unsupported type {cls}') # pragma: no cover

        return T


    def __or__(cls: type, other: type) -> 'ResultType':
        V: type = cls.__annotations__['v']
        E: type = other.__annotations__['e']

        T: ResultType = type(f'Result[{V}, {E}]', (Result,), {
            '__annotations__': {
                'v': V,
                'e': E,
            }
        })

        return T


    def __eq__(cls: type, other: type) -> bool:
        return (
            cls.__annotations__['v'] == other.__annotations__['v'] and
            cls.__annotations__['e'] == other.__annotations__['e']
        )


    def __call__(cls, *args, **kwargs) -> Callable:
        if (
            len(args) == 1 and
            not kwargs and
            not issubclass(cls, Ok) and
            not issubclass(cls, Err) and
            (fn := args[0]) and
            (callable(fn) or asyncio.iscoroutinefunction(fn))
        ):
            V = cls.__annotations__['v']
            E = cls.__annotations__['e']
            
            if asyncio.iscoroutinefunction(fn):
                @wraps(fn)
                async def wrap(*args, **kwargs) -> cls:
                    try:
                        v = await fn(*args, **kwargs)
                        return Ok[V](v)
                    except Exception as e:
                        return Err[E](e)
            elif inspect.isfunction(fn) or inspect.ismethod(fn):
                @wraps(fn)
                def wrap(*args, **kwargs) -> cls:
                    try:
                        v = fn(*args, **kwargs)
                        return Ok[V](v)
                    except Exception as e:
                        return Err[E](e)
            elif callable(fn):
                def wrap(*args, **kwargs) -> cls:
                    try:
                        v = fn(*args, **kwargs)
                        return Ok[V](v)
                    except Exception as e:
                        return Err[E](e)

            return wrap
        else:
            return super().__call__(*args, **kwargs)


class _Result(metaclass=ResultType):
    v: type | None = None
    e: type | None = None


class Result(_Result):
    def __new__(cls, *args, **kwargs) -> None:
        raise TypeError('Cannot be instantiated')


    def __enter__(self):
        try:
            v = self.unwrap()
        except Exception as e:
            self.__exit__(type(e), e, e.__traceback__)

        return v


    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type or exc_value:
            raise exc_value

        return self


class Ok(Result):
    __match_args__ = ('v',)
    v: Any


    def __new__(cls, *args, **kwargs) -> 'Ok':
        self = _Result.__new__(cls)
        return self


    def __init__(self, v: Any):
        V: type = self.__class__.__annotations__['v']

        if not (isinstance(V, types.GenericAlias) or
                isinstance(V, str) or
                V is Any or
                isinstance(V, ForwardRef) or
                isinstance(v, V)):
            raise TypeError(f'Got {type(v)} but expected {self.__class__.__annotations__["v"]}')
        
        self.v = v


    def unwrap(self) -> Any:
        """
        This function unwrap and returns a value of Ok type of Result
        """
        return self.v


    def unwrap_or(self, v: Any) -> Any:
        """
        This function unwrap and returns a value of Ok type of Result
        """
        return self.v


    def unwrap_value(self) -> Any:
        """
        This function unwrap and returns a value of Ok type of Result
        """
        return self.v


class Err(Result):
    __match_args__ = ('e',)
    e: Any


    def __new__(cls, *args, **kwargs) -> 'Err':
        self = _Result.__new__(cls)
        return self


    def __init__(self, e: Any):
        E: type = self.__class__.__annotations__['e']

        if not (isinstance(E, types.GenericAlias) or
                isinstance(E, str) or
                E is Any or
                isinstance(E, ForwardRef) or
                isinstance(e, (E, Exception))):
            raise TypeError(f'Got {type(e)} but expected {self.__class__.__annotations__["e"]}')

        self.e = e


    def unwrap(self) -> None:
        """
        This function unwrap and raise exception of Error type of Err type of Result
        """
        if not isinstance(self.e, Exception):
            e = ResultException(self.e)
        else:
            e = self.e # pragma: no cover

        raise e


    def unwrap_or(self, v: Any) -> Any:
        """
        This function unwrap and returns a value
        """
        return v


    def unwrap_value(self) -> Any:
        """
        This function unwrap and returns a value of Err type of Result
        """
        return self.e


def wrap_result(res: Result):
    """
    This function wraps the Result type and returns a Ok or Err type of Result
    """
    def outer(f):
        @wraps(f)
        def inner(*args, **kwargs):
            if asyncio.iscoroutinefunction(f):
                async def a():
                    try:
                        v = await f(*args, **kwargs)
                        return Ok(v)
                    except Exception as e:
                        return Err(e)  
                
                return a()
            else:
                try:
                    v = f(*args, **kwargs)
                    return Ok(v)
                except Exception as e:
                    return Err(e)

        return inner

    return outer


class WrappedBase:
    def __getstate__(self) -> dict:
        state = {}

        for a in dir(self):
            if a.startswith('__') and a.endswith('__'):
                continue

            v = getattr(self, a)

            if callable(v):
                continue

            state[a] = v

        return state


class UnwrappedBase:
    def __setstate__(self, state):
        for a, v in state.items():
            setattr(self, a, v)


def _auto_unwrap_type(type_):
    new_type_dict = {}
    new_type = type(type_.__name__, (type_, UnwrappedBase), new_type_dict)

    for a in dir(type_):
        f = getattr(type_, a)

        if not callable(f):
            # print('not callable', a, f)
            continue

        if not hasattr(f, '__annotations__'):
            # print('no __annotations__', a, f)
            continue

        return_type = f.__annotations__.get('return')

        if not return_type:
            # print('no return_type', a, f)
            continue  # pragma: no cover
        
        '''
        if not (isinstance(return_type, type) or isinstance(return_type, str)):
            print('return_type is not type/str', a, f, return_type, type(return_type))
            continue

        if not (issubclass(return_type, Result) or isinstance(return_type, str)):
            print('return_type is Result/str subclass', a, f, return_type, type(return_type))
            continue
        '''

        '''
        if isinstance(return_type, type) and issubclass(return_type, Result):
            pass
        elif isinstance(return_type, str):
            pass
        else:
            print('return_type is not type Result/str', a, f, return_type, type(return_type))
            continue
        '''

        new_f = _auto_unwrap_func(f, old_type=return_type, new_type=new_type)
        setattr(new_type, a, new_f)
    
    return new_type


def _auto_unwrap_func(func, old_type=None, new_type=None):
    # print('auto_unwrap func-like', func, old_type, new_type)

    @wraps(func)
    def wrapper(*args, **kwargs):
        if asyncio.iscoroutinefunction(func):
            async def a():
                r = await func(*args, **kwargs)

                if isinstance(r, Result):
                    r = r.unwrap()
                
                if (inspect.isclass(old_type) and issubclass(old_type, WrappedBase) and isinstance(r, old_type)) or \
                   (isinstance(old_type, ForwardRef) and old_type.__forward_arg__ == r.__class__.__name__):
                    new_r = new_type.__new__(new_type)
                    state = r.__getstate__()
                    new_r.__setstate__(state)
                    r = new_r
                
                return r
            
            return a()
        elif inspect.ismethod(func):
            r = func(*args, **kwargs)

            if isinstance(r, Result):
                r = r.unwrap()
            
            if (inspect.isclass(old_type) and issubclass(old_type, WrappedBase) and isinstance(r, old_type)) or \
               (isinstance(old_type, ForwardRef) and old_type.__forward_arg__ == r.__class__.__name__):
                new_r = new_type.__new__(new_type)
                state = r.__getstate__()
                new_r.__setstate__(state)
                r = new_r

            return r
        else:
            r = func(*args, **kwargs)

            if isinstance(r, Result):
                r = r.unwrap()
            
            if (inspect.isclass(old_type) and issubclass(old_type, WrappedBase) and isinstance(r, old_type)) or \
               (isinstance(old_type, ForwardRef) and old_type.__forward_arg__ == r.__class__.__name__):
                new_r = new_type.__new__(new_type)
                state = r.__getstate__()
                new_r.__setstate__(state)
                r = new_r

            return r

    return wrapper


def auto_unwrap(obj) -> Any:
    '''
    This function auto unwraps Ok or Err type of Result
    '''
    if inspect.isclass(obj):
        r = _auto_unwrap_type(obj)
    else:
        r = _auto_unwrap_func(obj)
    
    return r
