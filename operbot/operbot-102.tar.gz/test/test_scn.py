# This file is placed in the Public Domain.
# pylint: disable=C0113,C0114,C0115,C0116


import unittest


from opm.run import Command
from opm import irc
from opm.irc import IRC


class TestScan(unittest.TestCase):

    def test_scan(self):
        iii = irc.IRC()
        iii.scan(irc)
        self.assertTrue("cfg" in Command.cmd)
