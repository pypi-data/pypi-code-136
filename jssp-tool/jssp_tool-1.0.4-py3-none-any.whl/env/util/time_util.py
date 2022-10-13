import time
from time import strftime, localtime


def get_standard_current_time_str():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def get_current_time_for_filename():
    return strftime("%Y-%m-%d_%H-%M-%S", localtime())
