import time
import unittest
from random import random

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from mandarina.benchmark import Benchmark, start_timing, counter
from mandarina.benchmark import timer
from mandarina.benchmark import get_process_memory_usage


class TestBenchmark(unittest.TestCase):
    def test(self):
        pass

    def test_benchmark(self):
        execution_time = 0.1
        result = Benchmark.run(
            lambda: time.sleep(execution_time), 10, print_output=False
        )
        self.assertAlmostEqual(result[0], execution_time, 2)
        self.assertAlmostEqual(result[1], execution_time, 2)

    def test_timer(self):
        # Call to test if function runs without errors
        @timer
        def f():
            time.sleep(0.1)

    def test_get_process_memory_usage(self):
        # Call to test if function runs without errors
        get_process_memory_usage()
        get_process_memory_usage(readable=False)

    def test_start_timing(self):
        elapsed_time = start_timing()
        time.sleep(1)

        self.assertAlmostEqual(elapsed_time(), 1, 2)
        time.sleep(0.1)
        self.assertAlmostEqual(elapsed_time(), 1.1, 2)
        time.sleep(0.3)
        self.assertAlmostEqual(elapsed_time(), 1.4, 2)
        print(elapsed_time())

    def test_counter(self):
        @counter
        def f():
            pass

        f()
        self.assertEqual(f.calls, 1)
        for i in range(88):
            f()
        self.assertEqual(f.calls, 89)
