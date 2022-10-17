import warnings
import functools

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def warning_on_one_line(message, category, filename, lineno, file=None, line=None):
    start = ''
    end = ''
    if category == DeprecationWarning:
        start = bcolors.WARNING
        end = bcolors.ENDC

    return f'{start}[{category.__name__}] {filename}:{lineno}: {message}{end}\n'

warnings.formatwarning = warning_on_one_line

def deprecated(newFuncName):
    def decorate(func):
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            warnings.filterwarnings("always", category=DeprecationWarning)
            warnings.warn('function {} is deprecated and will be removed soon. The new API is {}'.format(func.__name__, newFuncName),
                    category=DeprecationWarning)
            warnings.filterwarnings("default", category=DeprecationWarning)
            return func(*args, **kwargs)
        return new_func
    return decorate
