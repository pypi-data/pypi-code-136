import numpy as np
import pandas as pd

from .base import statfunc

__all__ = ['add', 'multiply', 'divide', 'cumsum', 'compound_growth']

def derag(args):
    if any(not isinstance(arg, (pd.Series, pd.DataFrame, np.ndarray)) for arg in args):
        args = np.array(args, dtype='object')
    return args

@statfunc
def add(*args):
    return np.add.reduce(derag(args))

@statfunc
def multiply(*args):
    return np.multiply.reduce(derag(args))

@statfunc
def divide(a, b):
    a, b = derag((a, b))
    if isinstance(a, (pd.Series, np.ndarray)):
        a = a.astype('float')
    if isinstance(b, (pd.Series, np.ndarray)):
        b = b.astype('float')

    return np.divide(a, b, out=np.zeros_like(a), where=b!=0)

@statfunc
def cumsum(arr):
    return np.cumsum(arr)

@statfunc
def compound_growth(init, g, n):
    return init * np.repeat(1 + g, n).cumprod()

@statfunc
def repeat(value, n, start=0):
    arr = np.zeros(n)
    arr[start:] = np.repeat(value, n - start)
    return arr

@statfunc
def ffill(v, periods, fill_value=np.nan):
    arr = np.zeros(periods.size) * fill_value
    arr[0] = v
    return arr