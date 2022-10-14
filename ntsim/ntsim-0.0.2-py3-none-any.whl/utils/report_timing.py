import logging
from time import time


def report_timing(func):
    def func_wrapper(args):
        logger = logging.getLogger(type(args).__name__)
        tic = time()
        func(args)
        toc = time()
        dt = toc - tic
        logger.info(f'{func.__name__}'.ljust(40)+f'{dt:6.3E}s'.rjust(30))
    return func_wrapper
