from mandarina.scheduling import *
import unittest

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

class SchedulingTest(unittest.TestCase):
    def test(self):
        pass

    def test_run_function_every_n_seconds_thread(self):
        def fn(*s):
            print(s)

        run_function_every_n_seconds_thread(fn, ["tick", "tock"], 1.0)


    def test_run_function_after_n_seconds(self):
        def fn(*s):
            print(s)

        run_function_after_n_seconds_thread(fn, ["tock", "tock"], 1.0)
        time.sleep(10)
