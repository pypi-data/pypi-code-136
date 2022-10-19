import sys
import unittest

from pytest_ver import pth

sys.path.append('.')
from ver.core.ver_server import VerServer
from ver.core.ver_client import VerClient  # noqa: E402
from ver.core.ver_services import VerServices  # noqa: E402


# -------------------
class TestTp002(unittest.TestCase):

    # --------------------
    @classmethod
    def setUpClass(cls):
        pth.init()

        # when logger is None and verbose is true, then logging goes to stdout
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
    def test_tp_002(self):
        pth.proto.protocol('tp-002', 'common commands')

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

        pth.proto.step('set the callback function')
        VerServices.server.ols.callback = self._server_callback

        pth.proto.step('verify user cmd with callback works')
        self._callback_called = False
        self._callback_cmd = None
        self._callback_invalid = False
        # send cmd, get rsp
        rsp = VerServices.client.cmd01()
        pth.ver.verify_equal('ut_rsp', rsp, reqids=['SRS-008', 'SRS-015'])
        pth.ver.verify_true(self._callback_called, reqids=['SRS-008', 'SRS-013'])
        pth.ver.verify_equal('cmd01', self._callback_cmd, reqids='SRS-008')
        pth.ver.verify_false(self._callback_invalid, reqids='SRS-007')

        pth.proto.step('verify invalid cmd with callback works')
        self._callback_called = False
        self._callback_cmd = None
        self._callback_invalid = False
        # send cmd, get rsp
        rsp = VerServices.client.send_recv('ab\xEDcd')
        pth.ver.verify_true(self._callback_invalid, reqids='SRS-007')
        pth.ver.verify_equal('ut_rsp', rsp, reqids='SRS-008')
        pth.ver.verify_true(self._callback_called, reqids=['SRS-007', 'SRS-013', 'SRS-015'])
        # the invalid character is skipped
        # The \xED turns into two characers 0xC3 and 0XAD
        pth.ver.verify_equal('abcd', self._callback_cmd, reqids='SRS-007')

        pth.proto.step('client requests disconnect')
        VerServices.client.disconnect()
        pth.ver.verify_false(VerServices.client.olc.connected, reqids='SRS-012')

        # server should be still running
        pth.ver.verify_true(VerServices.server.ols.is_running, reqids=['SRS-005', 'SRS-006'])

    # --------------------
    def _server_callback(self, cmd, is_invalid):
        self._callback_called = True
        self._callback_cmd = cmd
        self._callback_invalid = is_invalid
        VerServices.server.ols.send('ut_rsp')
