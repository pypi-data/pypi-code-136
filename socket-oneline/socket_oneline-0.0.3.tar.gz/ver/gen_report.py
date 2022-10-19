import unittest

from pytest_ver import pth


# -------------------
class TestReport(unittest.TestCase):

    # --------------------
    @classmethod
    def setUpClass(cls):
        pass

    # -------------------
    def setUp(self):
        print('')

    # -------------------
    def tearDown(self):
        pass

    # --------------------
    @classmethod
    def tearDownClass(cls):
        pass

    # --------------------
    def test_report(self):
        pth.init()
        pth.report()
        pth.term()
