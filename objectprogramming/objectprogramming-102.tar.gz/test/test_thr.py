# This file is placed in the Public Domain.
# pylint: disable=C0115,C0116


"thread"


import unittest


from run import Thread


def test():
    pass


class TestThread(unittest.TestCase):

    def test_thread(self):
        thr = Thread(test, "test")
        self.assertEqual(type(thr), Thread)
