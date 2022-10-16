from __future__ import annotations

__all__ = ["makesafe"]

from functools import wraps
from typing import Any, Callable, TypeVar, Union

T = TypeVar("T")

class Some:
    def __init__(self, value: Any):
        self._value = value
    
    def get(self):
        return self._value

class Result:
    def __init__(
        self,
        value: Union[Some, None] # Using Union instead of Optional
                                 # to emphasize that None does not
                                 # indicate an "omitted" value.
    ):
        self._value = value
    
    def is_some(self) -> bool:
        return isinstance(self._value, Some)
    
    def is_some_and(self, f: Callable[[Any], bool]) -> bool:
        if self.is_some():
            return f(self.unwrap())
        
        return False
    
    def is_none(self) -> bool:
        return isinstance(self._value, type(None))
    
    def expect(self, msg: str) -> Any:
        if self.is_some():
            return self._value.get() # type: ignore
        
        raise RuntimeError(msg)
    
    def unwrap(self) -> Any:
        return self.expect(f"value is None")
    
    def unwrap_or(self, default: T) -> T:
        if self.is_some():
            return self.unwrap()
        
        return default
    
    def unwrap_or_else(self, f: Callable[[], T]) -> T:
        # Not using `unwrap_or` to avoid unnecessary
        # computing.
        if self.is_some():
            return self.unwrap()
        
        return f()
    
    def map(self, f: Callable[[Any], T]) -> Result:
        if self.is_some():
            return Result(Some(f(self.unwrap())))
        
        return self
    
    def map_or(self, default: T, f: Callable[[Any], T]) -> T:
        if self.is_some():
            return f(self.unwrap())
        
        return default
    
    def map_or_else(self, default: Callable[[], T], f: Callable[[Any], T]) -> T:
        # Not using `unwrap_or` to avoid unnecessary
        # computing.
        if self.is_some():
            return f(self.unwrap())
        
        return default()
    
    def filter(self, predicate: Callable[[Any], bool]) -> Result:
        if self.is_some():
            new = predicate(self.unwrap())
            if new:
                return self
            
            return Result(None)
        
        return self
    
    def insert(self, value: T) -> T:
        self._value = Some(value)
        return value
    
    def get_or_insert(self, value: Any[T]) -> T:
        if self.is_some():
            return self.unwrap()
        
        self._value = value
        return value

def makesafe(f: Callable[..., Any]) -> Callable[..., Result]:
    @wraps(f)
    def wrapper(*args, **kwargs) -> Result:
        try:
            res = f(*args, **kwargs)
        except Exception:
            return Result(None)
        else:
            return Result(Some(res))
    
    return wrapper


