import sys
import unittest

from pytest_ver import pth

sys.path.append('.')
from ver.core.ver_server import VerServer
from ver.core.ver_client import VerClient  # noqa: E402
from ver.core.ver_services import VerServices  # noqa: E402
from ver.helper import Helper


# -------------------
class TestTp003(unittest.TestCase):

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
        VerServices.server.term()
        VerServices.client.term()

    # --------------------
    @classmethod
    def tearDownClass(cls):
        pth.term()

    # --------------------
    def test_tp_003(self):
        pth.proto.protocol('tp-003', 'disconnect then reconnect with a new client')

        pth.proto.step('start server')
        VerServices.server.init()

        pth.proto.step('verify server is running')
        pth.ver.verify(VerServices.server.ols.is_running, reqids='SRS-001')

        pth.proto.step('start client')
        VerServices.client = VerClient()
        VerServices.client.init()
        pth.ver.verify_true(VerServices.client.olc.connected, reqids='SRS-011')

        pth.proto.step('verify ping works')
        rsp = VerServices.client.ping()
        pth.ver.verify_equal('pong', rsp, reqids=['SRS-004', 'SRS-013', 'SRS-015'])

        pth.proto.step('client requests disconnect')
        VerServices.client.disconnect()
        pth.ver.verify_false(VerServices.client.olc.connected, reqids='SRS-012')

        pth.proto.step('start new client')
        VerServices.client = VerClient()
        VerServices.client.init()
        pth.ver.verify_true(VerServices.client.olc.connected, reqids='SRS-011')

        pth.proto.step('verify ping works')
        rsp = VerServices.client.ping()
        pth.ver.verify_equal('pong', rsp, reqids=['SRS-004', 'SRS-013', 'SRS-015'])

        pth.proto.step('client requests shutdown')
        VerServices.client.shutdown()
        pth.ver.verify_false(VerServices.client.olc.connected, reqids='SRS-012')

        # server should be stopped
        Helper.wait_until_stopped(5)
        pth.ver.verify_false(VerServices.server.ols.is_running, reqids='SRS-006')
