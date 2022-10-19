import sys
import unittest

from pytest_ver import pth

sys.path.append('.')
from ver.core.ver_server import VerServer
from ver.mocks.mock_logger import MockLogger  # noqa: E402
from ver.core.ver_client import VerClient  # noqa: E402
from ver.core.ver_services import VerServices  # noqa: E402


# -------------------
class TestTp004(unittest.TestCase):

    # --------------------
    @classmethod
    def setUpClass(cls):
        pth.init()

        VerServices.logger = None
        VerServices.verbose = True

    # -------------------
    def setUp(self):
        print('')
        VerServices.server = VerServer()

    # -------------------
    def tearDown(self):
        VerServices.client.term()

    # --------------------
    @classmethod
    def tearDownClass(cls):
        pth.term()

    # --------------------
    def test_tp_004(self):
        pth.proto.protocol('tp-004', 'basic client tests')

        pth.proto.step('start client')
        VerServices.client = VerClient()
        VerServices.client.init()

        pth.proto.step('verify parameters are set correctly')
        pth.ver.verify_equal(VerServices.ip_address, VerServices.client.olc.ip_address, reqids='SRS-002')
        pth.ver.verify_equal(VerServices.ip_port, VerServices.client.olc.ip_port, reqids='SRS-002')
        pth.ver.verify_equal(VerServices.logger, VerServices.client.olc.logger, reqids='SRS-002')
        pth.ver.verify_equal(VerServices.verbose, VerServices.client.olc.verbose, reqids='SRS-002')

        VerServices.client.term()
