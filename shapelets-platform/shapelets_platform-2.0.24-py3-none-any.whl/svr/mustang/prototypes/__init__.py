import sys
import types 

from functools import wraps

def built_in(**meta):
    """ Decorator factory. """

    def variable_injector(func):
        """ Decorator. """
        func.__dbname__ = meta['db_name']
        func.__aggregated__ = meta['aggregated']

        @wraps(func)
        def decorator(*args, **kwargs):
            func.__dbname__ = meta['db_name']
            func.__aggregated__ = meta['aggregated']

            func_globals = func.__globals__

            # Save copy of any global values that will be replaced.
            saved_values = {
                key: func_globals[key] 
                for key in meta
                if key in func_globals
            }
            
            func_globals.update(meta)
            try:
                result = func(*args, **kwargs)
            finally:
                func_globals.update(saved_values)  # Restore replaced globals.

            return result

        return decorator

    return variable_injector


@built_in(db_name='avg', aggregated=True)
def avg() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='favg', aggregated=True)
def favg() -> dict:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='fsum', aggregated=True)
def fsum() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='sum', aggregated=True)
def sum() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass

@built_in(db_name='count', aggregated=True)
def count() -> float:
    pass 

@built_in(db_name='ceil', aggregated=False)
def ceil() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='lgamma', aggregated=False)
def lgamma() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='radians', aggregated=False)
def radians() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='sin', aggregated=False)
def sin() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='cos', aggregated=False)
def cos() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='abs', aggregated=False)
def absolute() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='lcase', aggregated=False)
def lcase() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='upper', aggregated=False)
def upper() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='histogram', aggregated=False)
def histogram() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='pow', aggregated=False)
def power() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='round', aggregated=False)
def round() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='corr', aggregated=False)
def corr() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='stddev', aggregated=True)
def stddev() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='median', aggregated=True)
def median() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='day', aggregated=True)
def day() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='month', aggregated=False)
def month() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='year', aggregated=False)
def year() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='hour', aggregated=False)
def hour() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='minute', aggregated=False)
def minute() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='second', aggregated=False)
def second() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='getDate', aggregated=False)
def getDate() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='getTime', aggregated=False)
def getTime() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='min', aggregated=True)
def min() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='max', aggregated=True)
def max() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='left', aggregated=True)
def left() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass


@built_in(db_name='right', aggregated=True)
def right() -> float:
    """_summary_

    Returns:
        float: _description_
    """
    pass

this_module = sys.modules[__name__]

func_list = [
    getattr(this_module, a)
    for a in dir(this_module)
    if isinstance(getattr(this_module, a), types.FunctionType)
]

allowedFunctionList = [
    item.__name__ 
    for item in func_list
    if (item.__name__ != 'built_in' and item.__name__ != 'wraps')
]

realFunctionList = [
    item.__dbname__ 
    for item in func_list
    if (item.__name__ != 'built_in' and item.__name__ != 'wraps')
]

zip_iterator = zip(allowedFunctionList, realFunctionList)
function_dictionary = dict(zip_iterator)

aggregatedFunctionList = [
    (item.__dbname__, item.__aggregated__) 
    for item in func_list
    if (item.__name__ != 'built_in' and item.__name__ != 'wraps')]

aggregatedFunctionList = [f[0] for f in aggregatedFunctionList if f[1]] 


__all__ = [
    'avg','favg','count','fsum','sum','ceil','lgamma','radians','sin','cos',
    'absolute','lcase','upper','histogram','power','round','corr','stddev',
    'median','day','month','year','hour','minute','second','getDate','getTime',
    'min','max','left','right'
]