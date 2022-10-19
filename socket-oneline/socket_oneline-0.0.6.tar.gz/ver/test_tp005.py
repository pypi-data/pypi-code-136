import sys
import time
import unittest

from pytest_ver import pth

sys.path.append('.')
from ver.core.ver_server import VerServer
from ver.mocks.mock_logger import MockLogger  # noqa: E402
from ver.core.ver_client import VerClient  # noqa: E402
from ver.core.ver_services import VerServices  # noqa: E402
from ver.helper import Helper


# -------------------
class TestTp005(unittest.TestCase):

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

    # --------------------
    @classmethod
    def tearDownClass(cls):
        pth.term()

    # --------------------
    def test_tp_005(self):
        pth.proto.protocol('tp-005', 'connect a client, attempt to connect with another client')

        pth.proto.step('start server')
        VerServices.server.init()

        pth.proto.step('verify server is running')
        pth.ver.verify(VerServices.server.ols.is_running, reqids='SRS-001')

        pth.proto.step('start client1')
        client1 = VerClient()
        client1.init()
        pth.ver.verify_true(client1.olc.connected, reqids='SRS-011')

        pth.proto.step('verify ping works on client1')
        rsp = client1.ping()
        pth.ver.verify_equal('pong', rsp, reqids='SRS-004')

        # server should be still running
        pth.ver.verify_true(VerServices.server.ols.is_running, reqids='SRS-006')

        pth.proto.step('start new client2')
        client2 = VerClient()
        client2.init()
        # time.sleep(0.5)

        pth.proto.step('verify client1 is still connected, and client2 is not')
        pth.ver.verify_false(client2.olc.connected, reqids='SRS-003')
        pth.ver.verify_true(client1.olc.connected, reqids='SRS-003')

        pth.proto.step('client1 requests shutdown')
        client1.shutdown()

        # server should be stopped
        Helper.wait_until_stopped(5)
        pth.ver.verify_false(VerServices.server.ols.is_running, reqids='SRS-006')

        client1.term()
        client2.term()
