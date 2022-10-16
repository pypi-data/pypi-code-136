#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Make sudden erros not stop your program
"""


__author__ = "phoenixR"
__version__ = "0.0.2"
__copyright__ = "Copyright (c) 2022 phoenixR"
__license__ = "MIT"


import functools as ft
import sys
import traceback as tb
import typing

class Result:
    """
    A class representing a function's result
    """
    def __init__(self, success, result):
        self.success = success
        self.result = result
    
    def __bool__(self):
        return self.success
    
    def __call__(self):
        return self.result

def makesafe(
    return_entire_result: bool = False,
    quiet: bool = False,
    title: str = "Ignoring exception in {function.__name__}",
    colored: bool = False,
    file: typing.TextIO = sys.stderr,
    *,
    raise_when: typing.Optional[typing.List[Exception]] = None,
    ignore: typing.Optional[typing.List[Exception]] = None
) -> typing.Callable:
    """
    A decorator to avoid the script from stoppig
    as soon as an error occures. You can configurate
    this command to react differently on specific
    errors, give an error message and make te
    error message printed out for a better readability.
    """
    if (raise_when is not None) and (ignore is not None):
        raise TypeError("raise_when and ignore cannot both be set")
    
    color = "\x1b[38;5;8m" if colored else ""
    
    def decorator(func: typing.Callable) -> typing.Callable:
        @ft.wraps(func)
        def safe(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
            def warn():
                if not quiet:
                    print(f"{color}{title.format(function = func)}", file = file)
                    tb.print_exc(file = file)
                    if colored:
                        print("\x1b[0m")
            
            try:
                result = func(*args, **kwargs)
            except Exception as exc:
                if ignore is None and raise_when is None:
                    warn()
                
                if ignore is not None:
                    if exc.__class__ in ignore:
                        warn()
                    else:
                        raise exc
                if raise_when is not None:
                    if exc.__class__ in raise_when:
                        raise exc
                    else:
                        warn()
                
                if return_entire_result:
                    return Result(False, exc)
                else:
                    return None
            else:
                if return_entire_result:
                    return Result(True, result)
                else:
                    return result
        return safe
        
    return decorator

if __name__ == "__main__":
    # Returns function result
    # Ignores any Error
    
    @makesafe()
    def divide(a, b):
        return a / b
    
    print("Let's calculate!")
    result = divide(1, 0)
    print(f"{result = }")
    
    print("---")
    
    # Returns function result
    # Ignores any Error
    
    @makesafe(return_entire_result = True)
    def divide(a, b):
        return a / b
    
    print("Let's calculate!")
    result = divide(1, 1)
    if result: # or result.success
        print(result()) # or result.result
    
    print("---")
    
    # Returns exception result
    # Ignores any Error
    
    @makesafe(return_entire_result = True)
    def divide(a, b):
        return a / b
    
    print("Let's calculate!")
    result = divide(1, 0)
    if result: # or result.success
        print(result()) # or result.result
    
    print("---")
    
    # Returns function result
    # Ignores ZeroDivisionError
    
    @makesafe(return_entire_result = True, ignore = [ZeroDivisionError])
    def divide(a, b):
        return a / b
    
    print("Let's calculate!")
    result = divide("Hello", 0)
    if result:
        print(result())
    
    print("---")
    
    # Raises due to ZeroDivisionError
    
    @makesafe(return_entire_result = True, raise_when = [ZeroDivisionError])
    def divide(a, b):
        return a / b
    
    print("Let's calculate!")
    result = divide("Hello", 0)
    if result:
        print(result())
