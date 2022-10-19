import functools
import logging
from numbers import Number
import os
from pandas import read_excel
import sys
from time import time
from typing import Union


logger = logging.getLogger(__name__)


def dict_insert(dict_, key, value):
    """Checks if a key already exists in dict, creates new key if not.
    Prevents overwriting of existing dictionary entries.

    Args:
        dict_ (dict): Dictionary to update.
        key (str): Key to check.
        value (str): Value to update if key doesn't exist.

    Returns:
        dict: Updated dictionary.
    """
    if key in dict_:
        pass
    else:
        dict_[key] = value
    return dict_

def get_snow_df(dashboard_folder, data_source):
    """Pulls snow data & returns a dataframe. Temporary fix for now, need to
    update path references

    Returns:
        DataFrame: Snow data
    """
    snow_file = os.path.join(dashboard_folder, 'Python_Functions', 'Snow Losses', '{}Operating-States-snowfall.xlsx'.format(data_source))
    raw_snow_df = read_excel(snow_file)

    return raw_snow_df

# Decorator function for timing the execution of functions
def func_timer(func):
    """Decorator for timing the execution of functions.

    Args:
        func (function): Function to time.
    """
    # Initiate logger
    logger = logging.getLogger('timer')

    @functools.wraps(func)
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        elapsed = time() - start

        # Build custom message for the logger so it doesn't just show that each
        # call came from the `timer()` function
        # Python 2 compatibility
        # Python 2 compatibility
        if sys.version_info.major == 3:
            file_str = 'File: {}'.format(os.path.basename(func.__code__.co_filename))
            line_str = 'Line: {}'.format(func.__code__.co_firstlineno)
        else:
            file_str = 'File: {}'.format(os.path.basename(func.func_code.co_filename))
            line_str = 'Line: {}'.format(func.func_code.co_firstlineno)

        log_msg = {
            'file': file_str,
            'module': 'Module: {}'.format(func.__module__),
            'function': 'Function: {}'.format(func.__name__),
            'line_no': line_str,
            'func_name': func.__name__,
            'elapsed': elapsed
        }
        # Check if the function call comes from a project, if so we'll add the project name to the log message
        try:
            log_msg['project_name'] = args[0].project_name
            message = '{file}\t{module}\t{function}\t{line_no}\tFunction call `{func_name}` for {project_name} complete. Total time: {elapsed:7.3f}s'.format(**log_msg)
        except AttributeError:
            message = '{file}\t{module}\t{function}\t{line_no}\tFunction call `{func_name}` complete. Total time: {elapsed:7.3f}s'.format(**log_msg)
        logger.info(message)

        return result
    return timer

def update_config(func):
    """Decorator to update the config file if necessary before running a function.

    Args:
        func (function): Function that will need an updated config file.
    """
    @functools.wraps(func)
    def check_config(self, *args, **kwargs):
        if self.last_update_config != os.path.getmtime(self.config_filepath):
            self._parse_config_file()
        return func(self, *args, **kwargs)
    return check_config
