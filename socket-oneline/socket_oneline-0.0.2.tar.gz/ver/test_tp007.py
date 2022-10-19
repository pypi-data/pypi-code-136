import sys
import unittest

from pytest_ver import pth

sys.path.append('.')
# from ver.core.ver_server import VerServer  # noqa: E402
# from ver.core.ver_client import VerClient  # noqa: E402
# from ver.helper import Helper  # noqa: E402
from socket_oneline.lib.oneline_server import OnelineServer


# -------------------
class TestTp007(unittest.TestCase):

    # --------------------
    @classmethod
    def setUpClass(cls):
        pth.init()

    # -------------------
    def setUp(self):
        print('')

    # -------------------
    def tearDown(self):
        pass

    # --------------------
    @classmethod
    def tearDownClass(cls):
        pth.term()

    class LocalLogger:
        def info(self):
            pass

    # --------------------
    def test_tp_007(self):
        pth.proto.protocol('tp-007', 'check server and client arguments')

        pth.proto.step('initiate Server with all arguments to start()')
        server = OnelineServer()
        ok = server.start(ip_address='127.0.0.2',
                          ip_port=5002,
                          callback=self._server_callback,
                          logger=TestTp007.LocalLogger,
                          verbose=True)

        pth.ver.verify_true(ok, reqids='SRS-001')
        pth.ver.verify_equal('127.0.0.2', server.ip_address, reqids='SRS-001')
        pth.ver.verify_equal(5002, server.ip_port, reqids='SRS-001')
        pth.ver.verify_not_none(server.callback, reqids='SRS-001')
        pth.ver.verify_not_none(server.logger, reqids='SRS-001')
        pth.ver.verify_equal(True, server.verbose, reqids='SRS-001')
        server.term()

        pth.proto.step('initiate Server missing ip_address')
        server = OnelineServer()
        ok = server.start(ip_port=5003,
                          callback=self._server_callback,
                          logger=TestTp007.LocalLogger,
                          verbose=True)

        pth.ver.verify_false(ok, reqids='SRS-001')
        pth.ver.verify_is_none(server.ip_address, reqids='SRS-001')
        pth.ver.verify_equal(5003, server.ip_port, reqids='SRS-001')
        pth.ver.verify_not_none(server.callback, reqids='SRS-001')
        pth.ver.verify_not_none(server.logger, reqids='SRS-001')
        pth.ver.verify_equal(True, server.verbose, reqids='SRS-001')
        server.term()

        pth.proto.step('initiate Server missing ip_port')
        server = OnelineServer()
        ok = server.start(ip_address='127.0.0.4',
                          callback=self._server_callback,
                          logger=TestTp007.LocalLogger,
                          verbose=True)

        pth.ver.verify_false(ok, reqids='SRS-001')
        pth.ver.verify_equal('127.0.0.4', server.ip_address, reqids='SRS-001')
        pth.ver.verify_is_none(server.ip_port, reqids='SRS-001')
        pth.ver.verify_not_none(server.callback, reqids='SRS-001')
        pth.ver.verify_not_none(server.logger, reqids='SRS-001')
        pth.ver.verify_equal(True, server.verbose, reqids='SRS-001')
        server.term()

        pth.proto.step('initiate Server missing callback')
        server = OnelineServer()
        ok = server.start(ip_address='127.0.0.5',
                          ip_port=5005,
                          logger=TestTp007.LocalLogger,
                          verbose=True)

        pth.ver.verify_false(ok, reqids='SRS-001')
        pth.ver.verify_equal('127.0.0.5', server.ip_address, reqids='SRS-001')
        pth.ver.verify_equal(5005, server.ip_port, reqids='SRS-001')
        pth.ver.verify_is_none(server.callback, reqids='SRS-001')
        pth.ver.verify_not_none(server.logger, reqids='SRS-001')
        pth.ver.verify_equal(True, server.verbose, reqids='SRS-001')
        server.term()

        pth.proto.step('initiate Server missing logger')
        server = OnelineServer()
        ok = server.start(ip_address='127.0.0.6',
                          ip_port=5006,
                          callback=self._server_callback,
                          verbose=True)

        pth.ver.verify_true(ok, reqids='SRS-001')
        pth.ver.verify_equal('127.0.0.6', server.ip_address, reqids='SRS-001')
        pth.ver.verify_equal(5006, server.ip_port, reqids='SRS-001')
        pth.ver.verify_not_none(server.callback, reqids='SRS-001')
        pth.ver.verify_is_none(server.logger, reqids='SRS-001')
        pth.ver.verify_equal(True, server.verbose, reqids='SRS-001')
        server.term()

        pth.proto.step('initiate Server missing verbose (default False)')
        server = OnelineServer()
        ok = server.start(ip_address='127.0.0.7',
                          ip_port=5007,
                          callback=self._server_callback)

        pth.ver.verify_true(ok, reqids='SRS-001')
        pth.ver.verify_equal('127.0.0.7', server.ip_address, reqids='SRS-001')
        pth.ver.verify_equal(5007, server.ip_port, reqids='SRS-001')
        pth.ver.verify_not_none(server.callback, reqids='SRS-001')
        pth.ver.verify_is_none(server.logger, reqids='SRS-001')
        pth.ver.verify_equal(False, server.verbose, reqids='SRS-001')
        server.term()

    # --------------------
    def _server_callback(self, cmd, is_invalid):
        self._callback_called = True
        self._callback_cmd = cmd
        self._callback_invalid = is_invalid
