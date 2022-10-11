"""
This module contains code benchmarking tools.
"""

import time
import statistics
import psutil
import os

from functools import wraps
from mandarina.file import convert_size_bytes_to_human_readable_format


class Benchmark:
    """
    This class runs a benchmark on a function passed to the
    run method. It calls the function a specified number of times
    and calculates the mean and standard deviation across all runs.
    """

    @staticmethod
    def run(function, runs, print_output=True):
        """
        The run method prints the benchmark statistics when called
        with a function as parameter. If you set print_output to False,
        the function will only return the final value without printing
        anything to the console.

        :param function: The function to benchmark
        :return: The mean running time in seconds and its standard
                 deviation.

        Example
            Benchmark.run(lambda: time.sleep(1), 100)

        """
        timings = []
        if print_output:
            print("Runs Median Mean Stddev")
        for i in range(runs):
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            timings.append(seconds)
            median = statistics.median(timings)
            mean = statistics.mean(timings)
            if print_output:
                if i < 10 or i % 10 == 9:
                    print(
                        "{0}\t{1:3.2f}\t{2:3.2f}\t{3:3.2f}".format(
                            1 + i,
                            median,
                            mean,
                            statistics.stdev(timings, mean) if i > 1 else 0,
                        )
                    )
        return (median, mean, statistics.stdev(timings, mean))


def timer(f):
    """
    Wraps a function in order to capture and print the
    execution time.

    Example
        @timer
        def f(x):
            print(x)

    """

    @wraps(f)
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function {f.__name__} with args {args, kwargs} took: {(end_time - start_time):.4f} seconds."
        )
        return result

    return wrap


def counter(func):
    """
    Wraps a function and counts the number of calls.

    Example:
        @counter
        def f(x):
            pass

        f(3)
        print(f.calls) # 1
        f(5)
        print(f.calls) # 2

    """

    @wraps(func)
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)

    helper.calls = 0
    return helper


def start_timing():
    """
    This closure function calculates the elapsed time in seconds since its initialization
    each time it is invoked.

    Example
        # Initialize
        elapsed_time = start_timing()

        time.sleep(1)

        # Get elapsed time
        et = elapsed_time()

    """
    CNT = [time.time()] * 2

    def calculate_elapsed_time():
        CNT[0] = CNT[1] - time.time()
        return abs(CNT[0])

    return calculate_elapsed_time


def get_process_memory_usage(readable=True):
    """
    Returns the memory usage of the current process the python
    script is running in.

    :param:  If readable is True the memory usage is returned
             in a human readable format.
    :return: Memory usage in bytes or human readable format.

    Example
        get_process_memory_usage()

    """
    process = psutil.Process(os.getpid())
    if readable:
        return convert_size_bytes_to_human_readable_format(
            process.memory_full_info()[0]
        )
    else:
        return process.memory_full_info()[0]
