"""
This module provides functionality for timing of methods.
"""

import time
import threading


def run_function_every_n_seconds(fn, fn_args, seconds):
    """
    Runs a function every n seconds.

    :param fn: The function to run
    :param fn_args: Arguments to pass to the function as list
    :param seconds: Timeinterval in seconds between function executions
    :return: None

    """
    start_time = time.time()
    while True:
        fn(fn_args)
        time.sleep(seconds - ((time.time() - start_time) % seconds))


def run_function_every_n_seconds_thread(fn, fn_args, seconds):
    thread = threading.Thread(
        name="run_function_every_n_seconds",
        target=run_function_every_n_seconds,
        args=[fn, fn_args, seconds],
    )


def run_function_after_n_seconds(fn, fn_args, seconds):
    """
    Runs a function after n seconds have passed
    :param fn:
    :param fn_args:
    :param seconds:
    :return:
    """
    start_time = time.time()
    time.sleep(seconds - ((time.time() - start_time) % seconds))
    fn(fn_args)


def run_function_after_n_seconds_thread(fn, fn_args, seconds):
    thread = threading.Thread(
        name="run_function_after_n_seconds",
        target=run_function_after_n_seconds,
        args=[fn, fn_args, seconds],
    )
    thread.start()
