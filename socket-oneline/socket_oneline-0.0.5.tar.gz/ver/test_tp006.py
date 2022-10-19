import sys
import unittest

from pytest_ver import pth

sys.path.append('.')
from ver.core.ver_server import VerServer  # noqa: E402
from ver.core.ver_client import VerClient  # noqa: E402
from ver.core.ver_services import VerServices  # noqa: E402
from ver.helper import Helper  # noqa: E402


# -------------------
class TestTp006(unittest.TestCase):

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
        VerServices.server.term()

    # --------------------
    @classmethod
    def tearDownClass(cls):
        pth.term()

    # --------------------
    def test_tp_006(self):
        pth.proto.protocol('tp-006', 'send 2 commands in one string')

        pth.proto.step('start server')
        ok = VerServices.server.init()
        pth.ver.verify_true(ok, reqids='SRS-001')
        VerServices.server.ols.callback = self._server_callback

        pth.proto.step('verify server is running')
        Helper.wait_until_started(5)
        pth.ver.verify(VerServices.server.ols.is_running, reqids='SRS-001')

        pth.proto.step('start client')
        VerServices.client = VerClient()
        VerServices.client.init()

        pth.proto.step('send two commands in one string')
        VerServices.client.send('ping\x0Acmd01')

        pth.proto.step('verify 1st response is for ping')
        rsp = VerServices.client.recv()
        pth.ver.verify_equal('pong', rsp, reqids=['SRS-009', 'SRS-014'])

        pth.proto.step('verify 1st response is for cmd01')
        rsp = VerServices.client.recv()
        pth.ver.verify_equal('ut_rsp', rsp, reqids=['SRS-009', 'SRS-014'])

    # --------------------
    def _server_callback(self, cmd, is_invalid):
        self._callback_called = True
        self._callback_cmd = cmd
        self._callback_invalid = is_invalid
        VerServices.server.ols.send('ut_rsp')
