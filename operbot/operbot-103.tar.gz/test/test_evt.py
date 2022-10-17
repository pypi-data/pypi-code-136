# This file is placed in the Public Domain.


import unittest


from opm.run import Event


class TestEvent(unittest.TestCase):

    def testconstructor(self):
        evt = Event()
        self.assertEqual(type(evt), Event)
