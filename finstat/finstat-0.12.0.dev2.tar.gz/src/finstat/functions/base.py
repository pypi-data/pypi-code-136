import inspect
import functools as ft

from ..base import FinStatBaseObject
from ..elements.lineitem import LineItem

class statfunc:
    def __init__(self, func):
        ft.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        return ArrayFunction(self.func, *args, **kwargs)

class FuncMixin:
    _call_kwargs = {}

    def _shorten(self, *args, **kwargs):
        return FinStatBaseObject._shorten(self, *args, **kwargs)

    @property
    def call_kwargs(self):
        return self._call_kwargs

    def set_call_kwargs(self, **kwargs):
        if not kwargs['short_name']:
            kwargs['short_name'] = self._shorten(kwargs['name'])
        
        self._call_kwargs = kwargs
        
        for k, v in self.call_kwargs.items():
            setattr(self, k, v)

class StatFunction(FuncMixin):
    pass

class ArrayFunction(StatFunction):
    def __init__(self, func, *fargs, **fkwargs):
        ft.update_wrapper(self, func)

        funcsig = inspect.getfullargspec(func)
        if 'periods' in fkwargs and 'periods' in funcsig.args:
            self._periods = fkwargs['periods']
        elif 'periods' in inspect.getargspec(func).args:
            self._periods = fargs[funcsig.args.index('periods')]
        else:
            self._periods = fkwargs.pop('periods', None)

        self.func = func
        self.fargs = fargs
        self.fkwargs = fkwargs

    def __repr__(self):
        return f'Array Function: {self.__name__}'

    @property
    def is_multi(self):
        return False # allows StatFunction to act as a LineItem in `add_account` method

    @property
    def periods(self):
        if hasattr(self, '_periods') and self._periods is not None:
            return self._periods
        else:
            args = list(self.fargs) + list(self.fkwargs.values())
            for arg in args:
                if hasattr(arg, 'has_graph'):
                    if arg.has_graph:
                        return self.graph.graph['periods']

            raise ValueError('You must provide `periods` argument if none of the function arguments are part of a FinancialStatement')

    def __call__(self, *args, **kwargs):
        obj = self.func(*args, *self.fargs, **kwargs, **self.fkwargs)
        return LineItem(
            obj,
            index=self.periods,
            *args,
            **kwargs,
            **self.call_kwargs
        )
