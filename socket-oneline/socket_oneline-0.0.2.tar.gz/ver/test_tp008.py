import sys
import unittest

from pytest_ver import pth

sys.path.append('.')
from socket_oneline.lib.oneline_client import OnelineClient


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
    def test_tp_008(self):
        pth.proto.protocol('tp-008', 'check server and client arguments')

        pth.proto.step('initiate Server with all arguments to init()')
        client = OnelineClient()
        ok = client.init(ip_address='127.0.0.2',
                         ip_port=5002,
                         logger=TestTp007.LocalLogger,
                         verbose=True)

        pth.ver.verify_true(ok, reqids='SRS-001')
        pth.ver.verify_equal('127.0.0.2', client.ip_address, reqids='SRS-001')
        pth.ver.verify_equal(5002, client.ip_port, reqids='SRS-001')
        pth.ver.verify_not_none(client.logger, reqids='SRS-001')
        pth.ver.verify_equal(True, client.verbose, reqids='SRS-001')
        client.term()

        pth.proto.step('initiate Server missing ip_address')
        client = OnelineClient()
        ok = client.init(ip_port=5003,
                         logger=TestTp007.LocalLogger,
                         verbose=True)

        pth.ver.verify_false(ok, reqids='SRS-001')
        pth.ver.verify_is_none(client.ip_address, reqids='SRS-001')
        pth.ver.verify_equal(5003, client.ip_port, reqids='SRS-001')
        pth.ver.verify_not_none(client.logger, reqids='SRS-001')
        pth.ver.verify_equal(True, client.verbose, reqids='SRS-001')
        client.term()

        pth.proto.step('initiate Server missing ip_port')
        client = OnelineClient()
        ok = client.init(ip_address='127.0.0.4',
                         logger=TestTp007.LocalLogger,
                         verbose=True)

        pth.ver.verify_false(ok, reqids='SRS-001')
        pth.ver.verify_equal('127.0.0.4', client.ip_address, reqids='SRS-001')
        pth.ver.verify_is_none(client.ip_port, reqids='SRS-001')
        pth.ver.verify_not_none(client.logger, reqids='SRS-001')
        pth.ver.verify_equal(True, client.verbose, reqids='SRS-001')
        client.term()

        pth.proto.step('initiate Server missing logger')
        client = OnelineClient()
        ok = client.init(ip_address='127.0.0.6',
                         ip_port=5006,
                         verbose=True)

        pth.ver.verify_true(ok, reqids='SRS-001')
        pth.ver.verify_equal('127.0.0.6', client.ip_address, reqids='SRS-001')
        pth.ver.verify_equal(5006, client.ip_port, reqids='SRS-001')
        pth.ver.verify_is_none(client.logger, reqids='SRS-001')
        pth.ver.verify_equal(True, client.verbose, reqids='SRS-001')
        client.term()

        pth.proto.step('initiate Server missing verbose (default False)')
        client = OnelineClient()
        ok = client.init(ip_address='127.0.0.7',
                         ip_port=5007)

        pth.ver.verify_true(ok, reqids='SRS-001')
        pth.ver.verify_equal('127.0.0.7', client.ip_address, reqids='SRS-001')
        pth.ver.verify_equal(5007, client.ip_port, reqids='SRS-001')
        pth.ver.verify_is_none(client.logger, reqids='SRS-001')
        pth.ver.verify_equal(False, client.verbose, reqids='SRS-001')
        client.term()
